# MIT License
#
# Copyright (c) 2023 LandInsightLab 
# Author: Rui Shi
# Date: October 2024
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

import sys
import os
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Add libs and resources directories
    libs_dir = os.path.join(current_dir, 'libs')
    resources_dir = os.path.join(current_dir, 'resources')
    src_dir = os.path.join(current_dir, 'src')  # Add src directory

    sys.path.append(libs_dir)
    sys.path.append(resources_dir)
    sys.path.append(src_dir)  # Add src directory

    from src.mainwindow import MainWindow  # Import MainWindow from src

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
