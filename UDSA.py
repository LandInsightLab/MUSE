import sys, os
import numpy as np

from libs.CheckTifDimensions import CheckTifDimensions, CountDistinctIntegers
from libs.CreateData import SampleDataGenerator, TestDataGenerator, DataToTif

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QSettings, QTimer, Signal, QThread
from UDSA_ui import Ui_UDSA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import xgboost as xgb

# Predefined model classes and parameter grids
model_classes = {
    'Logistic Regression': (LogisticRegression(), {
        'penalty': ['l1', 'l2', 'elasticnet', 'none'],
        'C': [0.1, 1.0, 10.0],
        'solver': ['lbfgs', 'liblinear', 'sag', 'saga']
    }),
    'SVM': (SVC(probability=True), {
        'C': [0.1, 1.0, 10.0],
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'degree': [3, 4, 5],
        'gamma': ['scale', 'auto']
    }),
    'XGBoost': (xgb.XGBClassifier(), {
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.02, 0.1, 0.2],
        'max_depth': [3, 6, 9],
        'subsample': [0.7, 1.0],
        'colsample_bytree': [0.7, 1.0]
    }),
    'Naive Bayes': (GaussianNB(), {}),
    'MLP': (MLPClassifier(), {
        'hidden_layer_sizes': [(50,), (100,), (100, 100)],
        'activation': ['relu', 'tanh', 'logistic'],
        'solver': ['adam', 'sgd', 'lbfgs'],
        'alpha': [0.0001, 0.001],
        'learning_rate': ['constant', 'invscaling', 'adaptive']
    }),
    'Random Forest': (RandomForestClassifier(), {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'max_features': ['sqrt', 'log2', 'None']
    }),
}


class SampleFetcher(QThread):
    finished = Signal(list)
    progress = Signal(str)

    def __init__(self, file_paths, sample_size, input_file_path, csv_path=None):
        super().__init__()
        self.file_paths = file_paths
        self.sample_size = sample_size
        self.input_file_path = input_file_path
        self.csv_path = csv_path

    def run(self):
        self.progress.emit("Starting to train samples...")
        # Collect file paths
        paths = self.file_paths + [self.input_file_path]

        # Generate samples
        samples_generator = SampleDataGenerator()
        self.progress.emit("Generating random samples...")

        samples = samples_generator.readRandomSamples(paths, self.sample_size)
        self.progress.emit("Finished fetching random samples.")

        # If save path is specified, determine file type and save samples
        if self.csv_path:
            file_extension = os.path.splitext(self.csv_path)[1].lower()
            
            samples_generator.saveToCSV(self.file_paths, self.csv_path)
            self.progress.emit(f"Samples saved to {file_extension} at {self.csv_path}.")
        
        self.finished.emit(samples)


class AutoFetcherAndTrainer(QThread):
    progress = Signal(str)
    finished = Signal(dict)

    def __init__(self, model, param_grid, X_train, X_test, y_train, y_test, cross_validation, cv_num, mutithread, n_jobs):
        super().__init__()
        self.model = model
        self.param_grid = param_grid
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.cross_validation = cross_validation
        self.cv_num = cv_num
        self.mutithread = mutithread
        self.n_jobs = n_jobs
        # self.n_jobs = 3
        self.is_running = True

    def run(self):
        try:
            self.progress.emit("Starting GridSearchCV...")
            #  if self.mutithread else None
            grid_search = GridSearchCV(
                estimator=self.model,
                param_grid=self.param_grid,
                cv=self.cv_num if self.cross_validation else None,
                n_jobs=self.n_jobs if self.mutithread else None,
                verbose=2,
            )
            self.progress.emit("Fitting the model...")
            grid_search.fit(self.X_train, self.y_train)

            self.progress.emit("Grid search completed.")
            best_model = grid_search.best_estimator_
            best_params = grid_search.best_params_
            self.progress.emit(f"Best parameters found: {best_params}")

            # Calculate training and test accuracy
            train_accuracy = best_model.score(self.X_train, self.y_train)
            test_accuracy = best_model.score(self.X_test, self.y_test)

            self.progress.emit(f"Training accuracy: {train_accuracy:.4f}")
            self.progress.emit(f"Test accuracy: {test_accuracy:.4f}")

            y_test_pred = best_model.predict(self.X_test)
            class_report = classification_report(self.y_test, y_test_pred)
            conf_matrix = confusion_matrix(self.y_test, y_test_pred)

            self.progress.emit("Classification Report:\n" + class_report)
            self.progress.emit("Confusion Matrix:\n" + str(conf_matrix))

            # Emit the results as a dictionary
            self.finished.emit({
                'best_params': best_params,
                'best_model': best_model
            })

        except Exception as e:
            self.progress.emit(f"Error during optimization: {str(e)}")
    
    def stop(self):
        self.is_running = False


class ModelTrainer(QThread):
    finished = Signal(dict)
    progress = Signal(str)

    def __init__(self, model, model_params, X_train, X_test, y_train, y_test, cross_validation, cv_num, multithread, n_jobs):
        super().__init__()
        self.model = model
        self.model_params = model_params
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.cross_validation = cross_validation
        self.cv_num = cv_num
        self.multithread = multithread
        self.n_jobs = n_jobs

    def run(self):
        try:
            self.progress.emit("Setting model parameters...")
            if self.multithread and isinstance(self.model, (LogisticRegression, xgb.XGBClassifier, RandomForestClassifier)):
                self.model.set_params(**self.model_params, n_jobs=self.n_jobs)
            else:
                self.model.set_params(**self.model_params)

            if self.cross_validation:
                self.progress.emit("Training the model...")
                self.model.fit(self.X_train, self.y_train)
                self.progress.emit("Model training completed.")

                self.progress.emit("Starting cross-validation...")
                
                # Perform cross-validation
                scores = cross_val_score(self.model, self.X_train, self.y_train, cv=self.cv_num)
                
                # Calculate mean accuracy
                mean_score = scores.mean()
                
                self.progress.emit(f"Cross-validation completed with mean accuracy: {mean_score:.2f}")
                results = {'cross_val_accuracy': mean_score}
            else:
                self.progress.emit("Training the model...")
                self.model.fit(self.X_train, self.y_train)
                y_pred = self.model.predict(self.X_test)
                test_accuracy = accuracy_score(self.y_test, y_pred)
                self.progress.emit(f"Model trained and evaluated with test accuracy: {test_accuracy:.2f}")
                results = {'test_accuracy': test_accuracy}

            results['model'] = self.model
            self.finished.emit(results)

        except Exception as e:
            error_msg = f"Error occurred during model training: {str(e)}"
            self.progress.emit(error_msg)
            self.finished.emit({'error': error_msg})


class ModelPredictor(QThread):
    finished = Signal(dict)
    progress = Signal(str)
    
    def __init__(self, model, test_paths, save_path):
        super().__init__()
        self.model = model
        self.test_paths = test_paths
        self.save_path = save_path
        
    def run(self):
        try:
            self.progress.emit("Starting to fetch test data...")
            test_generator = TestDataGenerator()
            X_new = test_generator.readTestData(self.test_paths)
            coor = test_generator.getCoor()
            self.progress.emit("Test data fetching completed.")
            self.progress.emit("Starting prediction...")
            
            probabilities = self.model.predict_proba(X_new)[:, 1]
            
            # 标准化 probabilities
            min_prob = np.min(probabilities)
            max_prob = np.max(probabilities)
            probabilities = (probabilities - min_prob) / (max_prob - min_prob)
            
            combined_data = np.hstack((coor, probabilities.reshape(-1, 1)))
            message = DataToTif(combined_data, self.save_path, self.test_paths[0])
            self.progress.emit(message)
        except Exception as e:
            error_msg = f"Error occurred during data prediction: {str(e)}"
            self.progress.emit(error_msg)
            self.finished.emit({'error': error_msg})


class UDSA_Dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UDSA()
        self.ui.setupUi(self)
        self.setWindowTitle("Urban Development Suitability Assessment (UDSA) module")  # Set window title
        
        # Initialize QSettings
        self.settings = QSettings("MyCompany", "MLSuitabilityAssessment")
        self.samples = None
        self.sample_size = None
        self.is_auto_fetch_flag = False
        self.trained_model = None
        self.test_paths = None

        self.sample_fetcher_thread = None
        self.optimizer_thread = None
        self.model_trainer_thread = None
        self.model_predictor_thread = None

        # Set up table
        self.ui.table_01.setColumnCount(1)
        self.ui.table_01.setHorizontalHeaderLabels(["Path"])

        # Connect signals to slots
        self.ui.button_01_add.clicked.connect(self.add_raster_files)
        self.ui.button_01_del.clicked.connect(self.remove_selected_rows)
        self.ui.button_02_input.clicked.connect(self.select_input_file)
        self.ui.checkBox_03_cv.stateChanged.connect(self.toggle_cv)
        self.ui.checkBox_03_thread.stateChanged.connect(self.toggle_mutithreading)
        self.ui.comboBox_03.currentIndexChanged.connect(self.model_parameters_setting)
        self.ui.button_05_save.clicked.connect(self.save_file_as)
        self.ui.toolButton_03_save.clicked.connect(self.select_save_directory)
        self.ui.button_04_fetch.clicked.connect(self.btn_auto_fetch_on_clicked)
        self.ui.button_04_train.clicked.connect(self.btn_train_on_clicked)
        self.ui.button_05_predict.clicked.connect(self.bun_predict_on_clicked)

        self.resizeEvent = self.customResizeEvent

        # Set up comboBox_03
        self.ui.comboBox_03.addItems(['XGBoost', 'Random Forest', 'SVM','MLP','Naive Bayes','Logistic Regression',  ])
        self.ui.comboBox_03.setCurrentText('XGBoost')

        # Set lineEdit_03_sample_ratio default value
        self.ui.lineEdit_03_sample_ratio.setText('0.2')

        # Set checkBox_03_cv and lineEdit_03_cv default states
        max_threads = os.cpu_count()
        self.ui.spinBox_03_thread.setMaximum(max_threads)
        self.ui.spinBox_03_thread.setValue(max_threads)  # Optionally set the current value to the max threads
        self.ui.spinBox_03_cv.setVisible(False)
        self.ui.spinBox_03_thread.setVisible(False)
        self.ui.frame_8.setVisible(False)
        self.ui.lineEdit_03_save.setVisible(False)
        self.ui.toolButton_03_save.setVisible(False)
        # Set checkBox_03_save and frame_03_save default states
        self.ui.checkBox_03_save.setChecked(False)
        self.ui.checkBox_03_save.stateChanged.connect(self.toggle_save)

        self.model_parameters_setting()
        self.set_prompt()

    def set_prompt(self):
        self.ui.lineEdit_03_random_samples.setPlaceholderText("Number of random samples")
        self.ui.lineEdit_03_sample_ratio.setPlaceholderText("Train = 1 - Test ratio")
        self.ui.lineEdit_03_save.setPlaceholderText("Enter save path for training data (csv or txt)")
        self.ui.lineEdit_05_save_path.setPlaceholderText("Enter save path for prediction results (tif or tiff)")
        self.ui.textBrowser_06_output.setPlaceholderText("Run Information Output...")

    def set_initial_column_widths(self):
        column_width = self.ui.table_01.width()
        self.ui.table_01.setColumnWidth(0, column_width)

    def customResizeEvent(self, event):
        self.set_initial_column_widths()
        super().resizeEvent(event)

    def add_raster_files(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Raster files (*.tif *.tiff)")
        last_dir_add = self.settings.value("last_dir_add", "")
        if last_dir_add:
            file_dialog.setDirectory(last_dir_add)
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            for file_path in file_paths:
                if self.is_path_in_table(file_path):
                    continue
                row_position = self.ui.table_01.rowCount()
                self.ui.table_01.insertRow(row_position)
                self.ui.table_01.setItem(row_position, 0, QTableWidgetItem(file_path))
            self.settings.setValue("last_dir_add", file_dialog.directory().absolutePath())

    def is_path_in_table(self, file_path):
        for row in range(self.ui.table_01.rowCount()):
            path_item = self.ui.table_01.item(row, 0)
            if path_item and path_item.text() == file_path:
                return True
        return False

    def remove_selected_rows(self):
        for item in self.ui.table_01.selectedItems():
            self.ui.table_01.removeRow(item.row())

    def select_input_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Raster files (*.tif *.tiff)")
        last_dir_input = self.settings.value("last_dir_input", "")
        if last_dir_input:
            file_dialog.setDirectory(last_dir_input)
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.ui.lineEdit_02_input.setText(file_path)
            self.settings.setValue("last_dir_input", file_dialog.directory().absolutePath())

    def toggle_cv(self):
        if self.ui.checkBox_03_cv.isChecked():
            self.ui.spinBox_03_cv.show()
        else:
            self.ui.spinBox_03_cv.hide()

    def toggle_mutithreading(self):
        if self.ui.checkBox_03_thread.isChecked():
            self.ui.spinBox_03_thread.show()
        else:
            self.ui.spinBox_03_thread.hide()

    def toggle_save(self):
        if self.ui.checkBox_03_save.isChecked():
            self.ui.lineEdit_03_save.show()
            self.ui.toolButton_03_save.show()
        else:
            self.ui.lineEdit_03_save.hide()
            self.ui.toolButton_03_save.hide()

    def select_save_directory(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Text files (*.csv)")
        file_dialog.setDefaultSuffix("csv")
        last_txt_save = self.settings.value("last_txt_save", "")
        if last_txt_save:
            file_dialog.setDirectory(last_txt_save)
        if file_dialog.exec():
            directory = file_dialog.selectedFiles()[0]
            self.ui.lineEdit_03_save.setText(directory)
            self.settings.setValue("last_txt_save", file_dialog.directory().absolutePath())

    def model_parameters_setting(self):
        current_text = self.ui.comboBox_03.currentText()
        line_edits = [self.ui.lineEdit_041, self.ui.lineEdit_042, self.ui.lineEdit_043, self.ui.lineEdit_044, self.ui.lineEdit_045]
        labels = [self.ui.label_041, self.ui.label_042, self.ui.label_043, self.ui.label_044, self.ui.label_045]
        
        if current_text == 'Logistic Regression':
            params = ['penalty', 'C', 'solver', '', '']
            default_values = ['l2', '1.0', 'lbfgs', '', '']
            self.ui.button_04_fetch.setVisible(True)
        elif current_text == 'SVM':
            params = ['C', 'kernel', 'degree', 'gamma', '']
            default_values = ['1.0', 'rbf', '3', 'scale', '']
            self.ui.button_04_fetch.setVisible(True)
        elif current_text == 'XGBoost':
            params = ['n_estimators', 'learning rate', 'max depth', 'subsample', 'colsample bytree']
            default_values = ['100', '0.1', '3', '1.0', '1.0']
            self.ui.button_04_fetch.setVisible(True)
        elif current_text == 'Naive Bayes':
            params = ['', '', '', '', '']
            default_values = ['', '', '', '', '']
            self.ui.button_04_fetch.setVisible(False)
        elif current_text == 'MLP':
            params = ['hidden layer sizes', 'activation', 'solver', 'alpha', 'learning rate']
            default_values = ['(100,)', 'relu', 'adam', '0.0001', 'constant']
            self.ui.button_04_fetch.setVisible(True)
        elif current_text == 'Random Forest':
            params = ['n_estimators', 'max depth', 'min samples split', 'min samples leaf', 'max features']
            default_values = ['100', 'None', '2', '1', 'sqrt']
            self.ui.button_04_fetch.setVisible(True)
        else:
            params = ['', '', '', '', '']
            default_values = ['', '', '', '', '']

        for label, line_edit, param, default_value in zip(labels, line_edits, params, default_values):
            if param:
                label.setText(param)
                label.show()
                line_edit.setText(default_value)
                line_edit.show()
            else:
                label.hide()
                line_edit.hide()

    def save_file_as(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Raster files (*.tif *.tiff)")
        file_dialog.setDefaultSuffix("tif")
        file_dialog.setDirectory(self.settings.value("last_dir_save", ""))

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            if not file_path.endswith(('.tif', '.tiff')):
                file_path += '.tif'
            self.ui.lineEdit_05_save_path.setText(file_path)
            self.settings.setValue("last_dir_save", file_dialog.directory().absolutePath())
        
    def show_message(self, message, msg_type="error"):
        msg_box = QMessageBox()
        if msg_type == "error":
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
        elif msg_type == "info":
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Information")
        elif msg_type == "warning":
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Warning")
        else:
            msg_box.setIcon(QMessageBox.NoIcon)
            msg_box.setWindowTitle("Message")

        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def files_and_parameters_detection(self):
        file_paths = []
        # Check files in table_01
        for row in range(self.ui.table_01.rowCount()):
            item = self.ui.table_01.item(row, 0)
            if item:
                file_path = item.text()
                if not file_path.endswith('.tif'):
                    self.show_message(f"Invalid file format: {file_path}. All files must be in .tif format.", "error")
                    return False
                if not os.path.exists(file_path):
                    self.show_message(f"Feature file not found: {file_path}. Please ensure all files are in .tif format.", "error")
                    return False
                file_paths.append(file_path)
            else:
                self.show_message("Please enter feature data in the table (all files must be .tif format).", "error")
                return False

        input_file_path = self.ui.lineEdit_02_input.text()
        if not input_file_path:
            self.show_message("Please enter label data (file must be in .tif format).", "error")
            return False
        if not input_file_path.endswith('.tif'):
            self.show_message(f"Invalid file format: {input_file_path}. The file must be in .tif format.", "error")
            return False
        if not os.path.exists(input_file_path):
            self.show_message(f"Label file not found: {input_file_path}. Please ensure the file is in .tif format.", "error")
            return False
        file_paths.append(input_file_path)

        if not CheckTifDimensions(file_paths):
            self.show_message("All TIF files must have the same shape (rows and columns).", "error")
            return False

        count_distinct_integers = CountDistinctIntegers(input_file_path)
        if count_distinct_integers == 0:
            self.show_message("The label file must be of discrete type with exactly two distinct values: 0 and 1.", "error")
            return False
        elif count_distinct_integers == 1 or count_distinct_integers > 2:
            self.show_message("The label file must contain exactly two distinct values: 0 and 1.", "error")
            return False
        
        # Check and set default values for lineEdit_03_random_samples and lineEdit_03_sample_ratio
        random_samples_value = self.ui.lineEdit_03_random_samples.text()
        sample_ratio_value = self.ui.lineEdit_03_sample_ratio.text()

        if not random_samples_value:
            self.show_message("Random samples value not set. Setting default value: 1000", "info")
            self.ui.lineEdit_03_random_samples.setText("1000")
            random_samples_value = "1000"
        if not sample_ratio_value:
            self.show_message("Sample ratio value not set. Setting default value: 0.2", "info")
            self.ui.lineEdit_03_sample_ratio.setText("0.2")
            sample_ratio_value = "0.2"
        # If both values were not set, provide a combined message
        if not random_samples_value and not sample_ratio_value:
            self.show_message("Random samples and sample ratio values not set. Setting default values: 0.1 and 0.2", "info")
            self.ui.lineEdit_03_random_samples.setText("0.1")
            self.ui.lineEdit_03_sample_ratio.setText("0.2")
            random_samples_value = "0.1"
            sample_ratio_value = "0.2"
        
        if self.ui.checkBox_03_save.isChecked():
            save_path = self.ui.lineEdit_03_save.text().strip()
            if not save_path:
                self.show_message('Save path is required when the "Save Training Data" option is checked.', "error")
                return False
            
            # Check if directory exists
            directory = os.path.dirname(save_path)
            if not os.path.exists(directory):
                self.show_message(f"Directory does not exist: {directory}. Please provide a valid save path.", "error")
                return False
        
        self.test_paths = file_paths[:-1]
        return True

    def genrate_samples(self):
        file_paths = [self.ui.table_01.item(row, 0).text() for row in range(self.ui.table_01.rowCount())]
        sample_size = int(self.ui.lineEdit_03_random_samples.text())
        input_file_path = self.ui.lineEdit_02_input.text()
        save_path = self.ui.lineEdit_03_save.text()

        self.sample_fetcher_thread = SampleFetcher(file_paths, sample_size, input_file_path, save_path)
        self.sample_fetcher_thread.finished.connect(self.on_generate_samples_finished)
        self.sample_fetcher_thread.progress.connect(self.ui.textBrowser_06_output.append)
        self.sample_fetcher_thread.start()

    def on_generate_samples_finished(self, samples):
        self.samples = samples

        test_size = float(self.ui.lineEdit_03_sample_ratio.text())
        random_state = 42
        cross_validation = self.ui.checkBox_03_cv.isChecked()
        cv_num = int(self.ui.spinBox_03_cv.text()) if cross_validation else None
        mutithread = self.ui.checkBox_03_thread.isChecked()
        n_jobs = int(self.ui.spinBox_03_thread.text()) if mutithread else None
        current_text = self.ui.comboBox_03.currentText()
        model, param_grid = model_classes.get(current_text, (None, None))

        X = np.array([row[:-1] for row in self.samples])
        y = np.array([row[-1] for row in self.samples])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        if self.is_auto_fetch_flag:
            self.on_auto_fetch(model, param_grid, X_train, X_test, y_train, y_test, cross_validation, cv_num, mutithread, n_jobs)
            self.is_auto_fetch_flag = False  # Reset the flag after use
        else:
            model_params = self.get_model_parameters()
            self.on_train(model, model_params, X_train, X_test, y_train, y_test, cross_validation, cv_num, mutithread, n_jobs)

    def validate_model_parameters(self, params):
        """
        Validate the model parameters to ensure they conform to the expected types and values.
        
        :param model_name: The name of the model (e.g., 'Logistic Regression', 'SVM', 'XGBoost', 'MLP', 'Random Forest')
        :param params: A dictionary of parameters to validate
        :return: A tuple (is_valid, message). is_valid is a boolean indicating if parameters are valid. 
                message is a string describing any issues found.
        """
        model_name = self.ui.comboBox_03.currentText()

        if model_name == 'Logistic Regression':
            if params.get('penalty') not in ['l1', 'l2', 'elasticnet', None]:
                return False, "penalty must be one of {'l1', 'l2', 'elasticnet', None}."
            if not isinstance(params.get('C'), (int, float)) or params.get('C') <= 0:
                return False, "C must be a positive number."
            if params.get('solver') not in ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']:
                return False, "solver must be one of {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}."
        
        elif model_name == 'SVM':
            if not isinstance(params.get('C'), (int, float)) or params.get('C') <= 0:
                return False, "C must be a positive number."
            if params.get('kernel') not in ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'] and not callable(params.get('kernel')):
                return False, "kernel must be one of {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'} or a callable."
            if not isinstance(params.get('degree'), int) or params.get('degree') < 0:
                return False, "degree must be a non-negative integer."
            if not (params.get('gamma') in ['scale', 'auto'] or isinstance(params.get('gamma'), (int, float)) and params.get('gamma') >= 0):
                return False, "gamma must be 'scale', 'auto', or a non-negative float."

        elif model_name == 'XGBoost':
            if not isinstance(params.get('n_estimators'), int) or params.get('n_estimators') <= 0:
                return False, "n_estimators must be a positive integer."
            if not isinstance(params.get('learning_rate'), (int, float)) or not (0 < params.get('learning_rate') <= 1):
                return False, "learning_rate must be a number between 0 and 1."
            if not isinstance(params.get('max_depth'), int) or params.get('max_depth') <= 0:
                return False, "max_depth must be a positive integer."
            if not isinstance(params.get('subsample'), (int, float)) or not (0 < params.get('subsample') <= 1):
                return False, "subsample must be a number between 0 and 1."
            if not isinstance(params.get('colsample_bytree'), (int, float)) or not (0 < params.get('colsample_bytree') <= 1):
                return False, "colsample_bytree must be a number between 0 and 1."
        
        elif model_name == 'MLP':
            if not isinstance(params.get('hidden_layer_sizes'), tuple) or not all(isinstance(x, int) and x > 0 for x in params.get('hidden_layer_sizes')):
                return False, "hidden_layer_sizes must be a tuple of positive integers."
            if params.get('activation') not in ['identity', 'logistic', 'tanh', 'relu']:
                return False, "activation must be one of {'identity', 'logistic', 'tanh', 'relu'}."
            if params.get('solver') not in ['lbfgs', 'sgd', 'adam']:
                return False, "solver must be one of {'lbfgs', 'sgd', 'adam'}."
            if not isinstance(params.get('alpha'), (int, float)) or params.get('alpha') < 0:
                return False, "alpha must be a non-negative number."
            if params.get('learning_rate') not in ['constant', 'invscaling', 'adaptive']:
                return False, "learning_rate must be one of {'constant', 'invscaling', 'adaptive'}."
        
        elif model_name == 'Random Forest':
            if not isinstance(params.get('n_estimators'), int) or params.get('n_estimators') <= 0:
                return False, "n_estimators must be a positive integer."
            if not (params.get('max_depth') is None or isinstance(params.get('max_depth'), int) and (params.get('max_depth') > 0)):
                return False, "max_depth must be None or a positive integer."
            if not isinstance(params.get('min_samples_split'), (int, float)) or params.get('min_samples_split') <= 0:
                return False, "min_samples_split must be a positive integer or float."
            if not isinstance(params.get('min_samples_leaf'), (int, float)) or params.get('min_samples_leaf') <= 0:
                return False, "min_samples_leaf must be a positive integer or float."
            if params.get('max_features') not in ["sqrt", "log2", None] and not isinstance(params.get('max_features'), (int, float)):
                return False, "max_features must be one of {'sqrt', 'log2', None'}, or an integer or float."
        
        return True, "Parameters are valid."

    def get_model_parameters(self):
        # Extract model parameters from the UI fields
        params = {}
        current_text = self.ui.comboBox_03.currentText()

        if current_text == 'Logistic Regression':
            params = {
                'penalty': self.ui.lineEdit_041.text(),
                'C': float(self.ui.lineEdit_042.text()),
                'solver': self.ui.lineEdit_043.text()
            }
        elif current_text == 'SVM':
            params = {
                'C': float(self.ui.lineEdit_041.text()),
                'kernel': self.ui.lineEdit_042.text(),
                'degree': int(self.ui.lineEdit_043.text()),
                'gamma': self.ui.lineEdit_044.text()
            }
        elif current_text == 'XGBoost':
            params = {
                'n_estimators': int(self.ui.lineEdit_041.text()),
                'learning_rate': float(self.ui.lineEdit_042.text()),
                'max_depth': int(self.ui.lineEdit_043.text()),
                'subsample': float(self.ui.lineEdit_044.text()),
                'colsample_bytree': float(self.ui.lineEdit_045.text())
            }
        elif current_text == 'MLP':
            params = {
                'hidden_layer_sizes': eval(self.ui.lineEdit_041.text()),  # Ensure valid tuple input
                'activation': self.ui.lineEdit_042.text(),
                'solver': self.ui.lineEdit_043.text(),
                'alpha': float(self.ui.lineEdit_044.text()),
                'learning_rate': self.ui.lineEdit_045.text()
            }
        elif current_text == 'Random Forest':
            params = {
                'n_estimators': int(self.ui.lineEdit_041.text()),
                'max_depth': None if self.ui.lineEdit_042.text() == 'None' else int(self.ui.lineEdit_042.text()),
                'min_samples_split': int(self.ui.lineEdit_043.text()),
                'min_samples_leaf': int(self.ui.lineEdit_044.text()),
                'max_features': self.ui.lineEdit_045.text()
            }

        return params

    def btn_auto_fetch_on_clicked(self):
        # Call files and parameters detection function
        fetch = self.files_and_parameters_detection()
        if not fetch:
            return
        # Show confirmation dialog with additional messages
        reply = QMessageBox.question(self, 'Confirmation', 
            'Input data and training parameters have passed the checks and are valid. '
            'Are you sure you want to start automatic parameter fetching? '
            'This process may take some time. Please be patient.',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.is_auto_fetch_flag = True
        
        if self.sample_size == int(self.ui.lineEdit_03_random_samples.text()) and self.samples:
            reply = QMessageBox.question(self, 'Confirmation', 
                f'Training samples ({self.sample_size}) already exist. Do you want to regenerate them?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                self.on_generate_samples_finished(self.samples)
                return
        # Proceed with automatic parameter fetching
        self.genrate_samples()
    
    def on_auto_fetch(self, model, param_grid, X_train, X_test, y_train, y_test, cross_validation, cv_num, mutithread, n_jobs):
        self.optimizer_thread = AutoFetcherAndTrainer(model, param_grid, X_train, X_test, y_train, y_test, cross_validation, cv_num, mutithread, n_jobs)
        self.optimizer_thread.finished.connect(self.set_best_parameters)
        self.optimizer_thread.progress.connect(lambda msg: self.ui.textBrowser_06_output.append(str(msg)))
        self.optimizer_thread.start()

    def set_best_parameters(self, best):
        self.trained_model = best['best_model']

        current_text = self.ui.comboBox_03.currentText()
        line_edits = [self.ui.lineEdit_041, self.ui.lineEdit_042, self.ui.lineEdit_043, self.ui.lineEdit_044, self.ui.lineEdit_045]

        param_keys = {
            'Logistic Regression': ['penalty', 'C', 'solver'],
            'SVM': ['C', 'kernel', 'degree', 'gamma'],
            'XGBoost': ['n_estimators', 'learning_rate', 'max_depth', 'subsample', 'colsample_bytree'],
            'MLP': ['hidden_layer_sizes', 'activation', 'solver', 'alpha', 'learning_rate'],
            'Random Forest': ['n_estimators', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'max_features']
        }

        params = param_keys.get(current_text, [])
        for i, param in enumerate(params):
            value = best['best_params'].get(param, '')
            if isinstance(value, (list, tuple)):
                value = str(value)
            line_edits[i].setText(str(value))  

    def btn_train_on_clicked(self):
        base_parameters_is_correct = self.files_and_parameters_detection()
        if not base_parameters_is_correct:
            return

        model_params = self.get_model_parameters()
        is_valid, message = self.validate_model_parameters(model_params)
        if not is_valid:
            self.show_message(message, "error")
            return

        reply = QMessageBox.question(self, 'Confirmation', 
            'Input data, training parameters, and model parameters have all passed checks and are valid. '
            'Are you sure you want to start the training? '
            'This process may take some time. Please be patient.',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        
        if self.sample_size == int(self.ui.lineEdit_03_random_samples.text()) and self.samples:
            reply = QMessageBox.question(self, 'Confirmation', 
                f'Training samples ({self.sample_size}) already exist. Do you want to regenerate them?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                self.on_generate_samples_finished(self.samples)
                return

        # Proceed with automatic parameter fetching
        self.genrate_samples()

    def on_train(self, model, model_parameters, X_train, X_test, y_train, y_test, cross_validation, cv_num, mutithread, n_jobs):
        self.model_trainer_thread = ModelTrainer(model, model_parameters, X_train, X_test, y_train, y_test, cross_validation, cv_num, mutithread, n_jobs)
        self.model_trainer_thread.finished.connect(self.on_training_finished)
        self.model_trainer_thread.progress.connect(lambda msg: self.ui.textBrowser_06_output.append(str(msg)))
        self.model_trainer_thread.start()
        # self.model_trainer_thread.run()  # when debug

    def on_training_finished(self, result):
        self.trained_model =  result['model']

    def bun_predict_on_clicked(self):
        if not self.trained_model:
            self.show_message("Please train the model first.", "error")
            return
        save_path = self.ui.lineEdit_05_save_path.text().strip()
        if not save_path:
            self.show_message('Please enter the save path for the prediction data.', "error")
            return False
        
        # Check if directory exists
        directory = os.path.dirname(save_path)
        if not os.path.exists(directory):
            self.show_message(f"Directory does not exist: {directory}. Please provide a valid save path.", "error")
            return False
        self.model_predictor_thread = ModelPredictor(self.trained_model, self.test_paths, save_path)
        self.model_predictor_thread.progress.connect(lambda msg: self.ui.textBrowser_06_output.append(str(msg)))
        self.model_predictor_thread.start()
    
    def closeEvent(self, event):
        threads = [
            self.sample_fetcher_thread,
            self.optimizer_thread,
            self.model_trainer_thread,
            self.model_predictor_thread
        ]
        for thread in threads:
            if thread and thread.isRunning():
                thread.terminate()
                thread.wait()

        event.accept()
   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UDSA_Dialog()
    window.show()
    sys.exit(app.exec())
