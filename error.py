# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 275)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_text = QtWidgets.QLabel(self.centralwidget)
        self.label_text.setGeometry(QtCore.QRect(120, 60, 531, 71))
        self.label_text.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_text.setObjectName("label_text")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(250, 180, 131, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy)
        self.btn_ok.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.btn_ok.setObjectName("btn_ok")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 91))
        self.label.setStyleSheet("\n"
"font: 72pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Error"))
        self.label_text.setText(_translate("MainWindow", "The operation was not completed successfully. \n"
"Read the rules carefully and try again."))
        self.btn_ok.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "⊗"))
