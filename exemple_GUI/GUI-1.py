# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI-1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 70, 211, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_a = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_a.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_a.sizePolicy().hasHeightForWidth())
        self.lineEdit_a.setSizePolicy(sizePolicy)
        self.lineEdit_a.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_a)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_b = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_b.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_b)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.plotWidget = QtWidgets.QWidget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(330, 80, 1200, 900))
        self.plotWidget.setObjectName("plotWidget")
        self.label_rezultat = QtWidgets.QLabel(self.centralwidget)
        self.label_rezultat.setGeometry(QtCore.QRect(500, 600, 331, 16))
        self.label_rezultat.setText("")
        self.label_rezultat.setObjectName("label_rezultat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "FUNCȚIE"))
        self.label_5.setText(_translate("MainWindow", "METODĂ ESTIMARE"))
        self.label.setText(_translate("MainWindow", "INTERVAL"))
        self.label_2.setText(_translate("MainWindow", "a = "))
        self.label_3.setText(_translate("MainWindow", "b ="))
        self.label_6.setText(_translate("MainWindow", "NUMĂR ITERAȚII"))
        self.label_7.setText(_translate("MainWindow", "TOLERANȚĂ (eroarea dorită)"))
        self.pushButton.setText(_translate("MainWindow", "Iterează!"))



from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
class ExempluPlot(FigureCanvas):
    def __init__(self, x, y, title="titlu grafic", parent=None):
        self.title = title
        self.x = x
        self.y = y

        fig = Figure(figsize=(9, 5), dpi=100, frameon=False)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.figure.subplots()
        self.plot()

    def plot(self):
        self.ax.plot(self.x, self.y, label=self.title)
        self.ax.set_xlabel('Label X')
        self.ax.set_ylabel('Label Y')
        self.ax.set_title(self.title, color='blue', fontsize=24)
        self.ax.legend()
        self.draw()

class OurMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(OurMainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_plot)

    def show_plot(self):
        x = np.linspace(0, 10, 100)
        y = np.exp(x)
        # cream plotul specificand titlul si widget-ul parinte
        plot = ExempluPlot(x, y, title="functia exponentiala", parent=self.plotWidget)
        plot.show()
        self.label_rezultat.setText("Am afisat plot-ul")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # definim window-ul nostru
    window = OurMainWindow()
    ui = Ui_MainWindow()
    # aplicam design-ul pt window-ul nostru
    window.show()
    # aratam plot-ul nostru

    sys.exit(app.exec_())

