# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/HelpInterfacePage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpInterfacePage(object):
    def setupUi(self, HelpInterfacePage):
        HelpInterfacePage.setObjectName("HelpInterfacePage")
        HelpInterfacePage.resize(557, 152)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpInterfacePage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(HelpInterfacePage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line9 = QtWidgets.QFrame(HelpInterfacePage)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line9.setObjectName("line9")
        self.verticalLayout.addWidget(self.line9)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.label_2 = QtWidgets.QLabel(HelpInterfacePage)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.styleComboBox = QtWidgets.QComboBox(HelpInterfacePage)
        self.styleComboBox.setObjectName("styleComboBox")
        self.gridlayout.addWidget(self.styleComboBox, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(HelpInterfacePage)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.styleSheetEdit = QtWidgets.QLineEdit(HelpInterfacePage)
        self.styleSheetEdit.setObjectName("styleSheetEdit")
        self.gridlayout.addWidget(self.styleSheetEdit, 1, 1, 1, 1)
        self.styleSheetButton = QtWidgets.QToolButton(HelpInterfacePage)
        self.styleSheetButton.setObjectName("styleSheetButton")
        self.gridlayout.addWidget(self.styleSheetButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        spacerItem = QtWidgets.QSpacerItem(537, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(HelpInterfacePage)
        QtCore.QMetaObject.connectSlotsByName(HelpInterfacePage)
        HelpInterfacePage.setTabOrder(self.styleComboBox, self.styleSheetEdit)
        HelpInterfacePage.setTabOrder(self.styleSheetEdit, self.styleSheetButton)

    def retranslateUi(self, HelpInterfacePage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("HelpInterfacePage", "<b>Configure User Interface</b>"))
        self.label_2.setText(_translate("HelpInterfacePage", "Style:"))
        self.styleComboBox.setToolTip(_translate("HelpInterfacePage", "Select the interface style"))
        self.label_3.setText(_translate("HelpInterfacePage", "Style Sheet:"))
        self.styleSheetEdit.setToolTip(_translate("HelpInterfacePage", "Enter the name of the style sheet file"))
        self.styleSheetButton.setToolTip(_translate("HelpInterfacePage", "Select the style sheet file via a file selection dialog"))

