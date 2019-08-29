# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autopasteUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 324)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 341, 271))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 67, 21))
        self.label.setObjectName("label")
        self.lineEditPath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPath.setEnabled(True)
        self.lineEditPath.setGeometry(QtCore.QRect(50, 30, 251, 25))
        self.lineEditPath.setObjectName("lineEditPath")
        self.listWidgetView = QtWidgets.QListWidget(self.groupBox)
        self.listWidgetView.setGeometry(QtCore.QRect(10, 60, 321, 161))
        self.listWidgetView.setObjectName("listWidgetView")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 67, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditFile = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditFile.setGeometry(QtCore.QRect(50, 230, 281, 25))
        self.lineEditFile.setObjectName("lineEditFile")
        self.toolButtonSelectPath = QtWidgets.QToolButton(self.groupBox)
        self.toolButtonSelectPath.setGeometry(QtCore.QRect(310, 30, 21, 24))
        self.toolButtonSelectPath.setObjectName("toolButtonSelectPath")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(185, 290, 171, 25))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelError = QtWidgets.QLabel(Dialog)
        self.labelError.setGeometry(QtCore.QRect(10, 280, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelError.setFont(font)
        self.labelError.setText("")
        self.labelError.setWordWrap(True)
        self.labelError.setObjectName("labelError")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Auto Paste "))
        self.label.setText(_translate("Dialog", "Path:"))
        self.label_2.setText(_translate("Dialog", "File:"))
        self.toolButtonSelectPath.setText(_translate("Dialog", "..."))
        self.labelError.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))

