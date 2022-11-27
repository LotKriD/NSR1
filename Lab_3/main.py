import sys
import os
import numpy as np
import random
from PyQt5 import QtWidgets
from form import Ui_MainWindow
from BubbleSort import bubbleSort
from QuickSort import quickSort
from SelectionSort import selectionSort
import time

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.buttonLoad.clicked.connect(self.btnLoadClicked)
        self.ui.buttonGenerate.clicked.connect(self.btnGenerateClicked)
        self.ui.buttonSort.clicked.connect(self.btnSortClicked)

    def btnLoadClicked(self):
        global array
        global array1
        self.ui.textBrowser.append("Массив:")

        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, 'array.txt')
        array = np.genfromtxt(path, delimiter=' ', dtype=np.int64)

        array1 = array.copy()
        
        self.showArray()

    def btnGenerateClicked(self):
        global array
        global array1
        array = []
        self.ui.textBrowser.append("Массив:")

        n = self.ui.spinBox.value()

        for i in range(0, n):
            array.append(random.randint(-100, 100))

        array1 = array.copy()
        
        self.showArray()

    def btnSortClicked(self):
        global array
        global array1
        global sort_types

        self.ui.textBrowser.append("Отсортированный массив:")

        n = sort_types[self.ui.comboBox.currentText()]

        array1 = array.copy()
        
        if n == 1:
            start = time.time()
            bubbleSort(array1)
            end = time.time() - start
        elif n == 2:
            start = time.time()
            array = quickSort(array1)
            end = time.time() - start
        elif n == 3:
            start = time.time()
            selectionSort(array1)
            end = time.time() - start

        self.ui.textBrowser_Time.append(str(end))

        self.showArray()

    def showArray(self):
        st = ""
        for i in array1:
            if i > 100:
                break
            st = "{} {}".format(st, i)
        
        self.ui.textBrowser.append(st)

sort_types = {'Пузырьковая' : 1, 'Быстрая': 2, 'Выбором': 3}

array = []
array1 = []

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MainWindow()
    sys.exit(app.exec_())
