# MIT License
#
# Copyright (c) 2023 LandInsightLab 
# Author: Rui Shi
# Date: July 2023
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import threading
import numpy as np

from PySide6.QtWidgets import QWidget, QTextBrowser
from PySide6.QtCore import QThread, Signal
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from pymoo.core.problem import Problem
from libs import MUSE_API_GA

from resources.ui.POT_ui import Ui_POT

class GAThread(QThread):
    progress = Signal(str)

    def __init__(self, pool, ga_muse_parameters, pop_size, n_gen, var, xl, xu, current_algorithm, opimision_parameters):
        super().__init__()
        self.pool = pool
        self.ga_muse_parameters = ga_muse_parameters
        self.pop_size = pop_size
        self.n_gen = n_gen
        self.var = var
        self.xl = xl
        self.xu = xu
        self.current_algorithm = current_algorithm
        self.opimision_parameters = opimision_parameters

    def run(self):
        from pymoo.algorithms.soo.nonconvex.ga import GA
        from pymoo.algorithms.soo.nonconvex.de import DE
        from pymoo.algorithms.soo.nonconvex.pso import PSO
        from pymoo.algorithms.soo.nonconvex.pattern import PatternSearch
        from pymoo.algorithms.moo.nsga2 import NSGA2
        from pymoo.optimize import minimize
        try:
            muse_problem = MyProblem(pool=self.pool, ga_muse_parameters=self.ga_muse_parameters, var=self.var, xl=self.xl, 
                                     xu=self.xu, opimision_parameters=self.opimision_parameters ,show_messagge=self.show_mesg)
            n_gen = self.n_gen

            algorithms = {
                "Genetic Algorithm (GA)": GA(pop_size=self.pop_size),
                "Differential Evolution (DE)": DE(pop_size=self.pop_size),
                "Particle Swarm Optimization (PSO)": PSO(pop_size=self.pop_size),
                "Pattern Search": PatternSearch(),
                "NSGA-II": NSGA2(pop_size=self.pop_size),
            }

            selected_algorithm = algorithms.get(self.current_algorithm)

            res = minimize(
                problem=muse_problem,
                algorithm=selected_algorithm,
                termination=('n_gen', n_gen),
                seed=1,
                verbose=False
            )

            # Close and join the pool
            self.pool.close()
            self.pool.join()

            # Format the solution and objective values to 8 decimal places
            best_solution = [f"{x:.6f}" for x in res.X]
            objective_value = [f"{-f:.8f}" for f in res.F]

            # Output results
            self.show_mesg("Optimization Results")
            self.show_mesg("---------------------")
            self.show_mesg(f"Best Solution: {best_solution}")
            self.show_mesg(f"Objective Value: {objective_value}")
            self.show_mesg(f"Execution Time: {res.exec_time:.8f} seconds")

            # If multi-objective
            if hasattr(res, "CV"):
                constraint_violation = [f"{cv:.8f}" for cv in res.CV]
                self.show_mesg(f"Constraint Violation: {constraint_violation}")
            if hasattr(res, "G"):
                constraints = [f"{g:.8f}" for g in res.G]
                self.show_mesg(f"Constraints: {constraints}")

        except Exception as e:
            # Capture any exception and send it to the show_mesg method
            self.show_mesg(f"An error occurred: {str(e)}")

    def show_mesg(self, message):
        self.progress.emit(message)


class MyProblem(Problem):
    def __init__(self, pool, ga_muse_parameters, var, xl, xu, opimision_parameters, show_messagge=None, **kwargs):
        super().__init__(n_var=var, n_obj=1, n_ieq_constr=0, xl=xl, xu=xu, **kwargs)
        self.pool = pool
        self.ga_muse_parameters = ga_muse_parameters
        self.show_message = show_messagge
        self.opimision_parameters = opimision_parameters

    def _evaluate(self, X, out, *args, **kwargs):
        params = [[X[k]] for k in range(len(X))]
        F = self.pool.starmap(self.my_eval, params)
        out["F"] = np.array(F)

    def my_eval(self, x):
        thread_id = threading.get_ident()
        params = MUSE_API_GA.MUSE_API_GA_Parameters()

        params.mode = self.ga_muse_parameters['mode']
        params.expansionControl = self.ga_muse_parameters['expansionControl']
        params.cityCenter = self.ga_muse_parameters['cityCenter']
        params.correctionParameters = self.ga_muse_parameters['correctionParameters']
        params.cityCenterWeight = self.ga_muse_parameters['cityCenterWeight']
        params.initialUrbanLand = self.ga_muse_parameters['initialUrbanLand']
        params.developmentConstraints = self.ga_muse_parameters['developmentConstraints']
        params.finalUrbanLand = self.ga_muse_parameters['finalUrbanLand']
        params.urbanSuitability = self.ga_muse_parameters['urbanSuitability']
        params.additionalUrbanLandArea = self.ga_muse_parameters['additionalUrbanLandArea']
        params.initialNode = self.ga_muse_parameters['initialNode']
        params.finalNode = self.ga_muse_parameters['finalNode']
        params.uncertainty = self.ga_muse_parameters['uncertainty']
        params.neighborhoodType = self.ga_muse_parameters['neighborhoodType']
        params.additionalUrbanLandOrganic = self.ga_muse_parameters['additionalUrbanLandOrganic']
        params.controllerType = self.ga_muse_parameters['controllerType']
        params.lognormalMean = self.ga_muse_parameters['lognormalMean']
        params.lognormalStdDev = self.ga_muse_parameters['lognormalStdDev']
        params.powerLawConstant = self.ga_muse_parameters['powerLawConstant']
        params.powerLawExponent = self.ga_muse_parameters['powerLawExponent']
        params.historicalBlockSizes = self.ga_muse_parameters['historicalBlockSizes']
        params.blockEngineType = self.ga_muse_parameters['blockEngineType']
        params.neighborhoodControlParam = self.ga_muse_parameters['neighborhoodControlParam']
        params.distanceControlParam = self.ga_muse_parameters['distanceControlParam']
        params.pruningCoefficient = x[0]
        params.additionalUrbanLandOrganic = x[1]
        idex = 2
        if params.expansionControl == 1:
            params.cityCenterWeight = x[idex]
            idex += 1
        if params.blockEngineType == 1:
            params.neighborhoodControlParam = x[idex]
        elif params.blockEngineType == 2:
            params.distanceControlParam = x[idex]

        result = MUSE_API_GA.ga_muse(params)



        message = f"{thread_id}\t"
        if self.opimision_parameters[0]:
            message += f"{params.pruningCoefficient:.6f}\t"
        if self.opimision_parameters[1]:
            message += f"{params.additionalUrbanLandOrganic:.6f}\t"
        if self.opimision_parameters[2]:
            message += f"{params.cityCenterWeight:.3f}\t"
        if self.opimision_parameters[3]:
            message += f"{params.neighborhoodControlParam:.4f}\t"
        elif self.opimision_parameters[4]:
            message += f"{params.distanceControlParam:.4f}\t"
        message += f"{result[2]:.8f}"

        self.show_message(message)
        
        if result[0] == 1:
            return -result[2]
        else:
            print(f"Thread ID: {thread_id}\tResult: 0")


class POT_Widget(QWidget, Ui_POT):
    def __init__(self):
        super().__init__()
        self.ui = Ui_POT()
        self.ui.setupUi(self)  # Set up the UI

        # load_modules()

        self.setWindowTitle("Parameter Optimization Tool (POT) module")  # Set window title
        self.ga_thread = None
        self.pool = None
        self.mgot_algorithms_init()
        self.set_default_parameters()
        self.ui.textBrowser.setLineWrapMode(QTextBrowser.NoWrap)
        self.ui.comboBox_00_algorithms.currentIndexChanged.connect(self.on_algorithm_changed)

        self.ui.textBrowser.setPlaceholderText("Run Information Output...")
        
    def on_algorithm_changed(self, index):
        if index == 3:
            self.ui.spinBox_01_pop_size.hide()
            self.ui.label.hide()
        else:
            self.ui.spinBox_01_pop_size.show()
            self.ui.label.show()

    def mgot_algorithms_init(self):
        algorithms = [
            "Genetic Algorithm (GA)",
            "Differential Evolution (DE)",
            "Particle Swarm Optimization (PSO)",
            "Pattern Search",
            "NSGA-II",
        ]
        for name in algorithms:
            self.ui.comboBox_00_algorithms.addItem(f"{name}")

    def set_default_parameters(self):
        num_cores = cpu_count()
        self.ui.spinBox_01_thread_count.setMaximum(num_cores)

    def set_weight_for_gauss(self, is_sliped):
        self.ui.checkBox_02_weight_of_gauss.setVisible(is_sliped)
    
    def set_engine_checkBox(self, engine_id):
        if engine_id == 0:
            self.ui.checkBox_02_beta.setVisible(False)
            self.ui.checkBox_02_delta.setVisible(False)
        elif engine_id == 1:
            self.ui.checkBox_02_beta.setVisible(True)
            self.ui.checkBox_02_delta.setVisible(False)
        elif engine_id == 2:
            self.ui.checkBox_02_beta.setVisible(False)
            self.ui.checkBox_02_delta.setVisible(True)

    def run(self, ga_muse_parameters):

        thread_num = self.ui.spinBox_01_thread_count.value()
        self.pool = ThreadPool(thread_num)

        pop_size = self.ui.spinBox_01_pop_size.value()
        n_gen = self.ui.spinBox__01_n_gen.value()

        xl = np.array([])
        xu = np.array([])
        var = 0
        header = "Thread-ID\t"

        if self.ui.checkBox_02_pruning_par.isChecked():
            xl = np.append(xl, [0.000001])
            xu = np.append(xu, [0.7])
            var += 1
            header += "Pruning-par\t"
        if self.ui.checkBox__02_organic.isChecked():
            xl = np.append(xl, [0.2])
            xu = np.append(xu, [0.99])
            var += 1
            header += "Organic-ratio\t"
        if self.ui.checkBox_02_weight_of_gauss.isChecked():
            xl = np.append(xl, [0])
            xu = np.append(xu, [1])
            var += 1
            header += "Gaussian-weight\t"
        if self.ui.checkBox_02_beta.isChecked():
            xl = np.append(xl, [0.001])
            xu = np.append(xu, [4])
            var += 1
            header += "Beta\t"
        elif self.ui.checkBox_02_delta.isChecked():
            xl = np.append(xl, [-2])
            xu = np.append(xu, [2])
            var += 1
            header += "Delta\t"

        self.ui.textBrowser.append(header+"FoM")

        opimision_parameters = [self.ui.checkBox_02_pruning_par.isChecked(),
                                self.ui.checkBox__02_organic.isChecked(),
                                self.ui.checkBox_02_weight_of_gauss.isChecked(),
                                self.ui.checkBox_02_beta.isChecked(),
                                self.ui.checkBox_02_delta.isChecked()]

        current_algorithm = self.ui.comboBox_00_algorithms.currentText()

        self.ga_thread = GAThread(self.pool, ga_muse_parameters, pop_size, n_gen, var, xl, xu, current_algorithm, opimision_parameters)
        self.ga_thread.start()
        self.ga_thread.progress.connect(lambda message: self.ui.textBrowser.append(message))

    def closeEvent(self, event):
        if self.ga_thread and self.ga_thread.isRunning():
            self.ga_thread.terminate()
            self.ga_thread.wait()
        self.close()
        event.accept()