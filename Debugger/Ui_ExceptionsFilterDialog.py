# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Debugger/ExceptionsFilterDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExceptionsFilterDialog(object):
    def setupUi(self, ExceptionsFilterDialog):
        ExceptionsFilterDialog.setObjectName("ExceptionsFilterDialog")
        ExceptionsFilterDialog.resize(464, 385)
        ExceptionsFilterDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExceptionsFilterDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exceptionList = QtWidgets.QListWidget(ExceptionsFilterDialog)
        self.exceptionList.setAlternatingRowColors(True)
        self.exceptionList.setObjectName("exceptionList")
        self.verticalLayout.addWidget(self.exceptionList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(ExceptionsFilterDialog)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.exceptionEdit = QtWidgets.QLineEdit(ExceptionsFilterDialog)
        self.exceptionEdit.setObjectName("exceptionEdit")
        self.horizontalLayout.addWidget(self.exceptionEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteButton = QtWidgets.QPushButton(ExceptionsFilterDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.deleteAllButton = QtWidgets.QPushButton(ExceptionsFilterDialog)
        self.deleteAllButton.setObjectName("deleteAllButton")
        self.horizontalLayout_2.addWidget(self.deleteAllButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ExceptionsFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ExceptionsFilterDialog)
        self.buttonBox.accepted.connect(ExceptionsFilterDialog.accept)
        self.buttonBox.rejected.connect(ExceptionsFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExceptionsFilterDialog)
        ExceptionsFilterDialog.setTabOrder(self.exceptionList, self.exceptionEdit)
        ExceptionsFilterDialog.setTabOrder(self.exceptionEdit, self.addButton)
        ExceptionsFilterDialog.setTabOrder(self.addButton, self.deleteButton)
        ExceptionsFilterDialog.setTabOrder(self.deleteButton, self.deleteAllButton)
        ExceptionsFilterDialog.setTabOrder(self.deleteAllButton, self.buttonBox)

    def retranslateUi(self, ExceptionsFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        ExceptionsFilterDialog.setWindowTitle(_translate("ExceptionsFilterDialog", "Exceptions Filter"))
        ExceptionsFilterDialog.setWhatsThis(_translate("ExceptionsFilterDialog", "<b>Exception Filter</b>\n"
"<p>This dialog is used to enter the exception types, that shall be highlighted during a debugging session. If this list is empty, all exception types will be highlighted. If the exception reporting flag in the \"Start Debugging\" dialog is unchecked, no exception will be reported at all.</p>\n"
"<p>Please note, that unhandled exceptions are always highlighted independent of these settings.</p>"))
        self.exceptionList.setToolTip(_translate("ExceptionsFilterDialog", "List of exceptions that shall be highlighted"))
        self.addButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to add the entered exception to the list"))
        self.addButton.setText(_translate("ExceptionsFilterDialog", "Add"))
        self.exceptionEdit.setToolTip(_translate("ExceptionsFilterDialog", "Enter an exception type that shall be highlighted"))
        self.deleteButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to delete the selected exception from the list"))
        self.deleteButton.setText(_translate("ExceptionsFilterDialog", "Delete"))
        self.deleteAllButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to delete all exceptions from the list"))
        self.deleteAllButton.setText(_translate("ExceptionsFilterDialog", "Delete All"))

