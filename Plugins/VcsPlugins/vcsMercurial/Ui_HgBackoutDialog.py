# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/HgBackoutDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgBackoutDialog(object):
    def setupUi(self, HgBackoutDialog):
        HgBackoutDialog.setObjectName("HgBackoutDialog")
        HgBackoutDialog.resize(372, 515)
        HgBackoutDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(HgBackoutDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.revisionGroup = QtWidgets.QGroupBox(HgBackoutDialog)
        self.revisionGroup.setObjectName("revisionGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.revisionGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.numberButton = QtWidgets.QRadioButton(self.revisionGroup)
        self.numberButton.setObjectName("numberButton")
        self.gridLayout.addWidget(self.numberButton, 0, 0, 1, 1)
        self.numberSpinBox = QtWidgets.QSpinBox(self.revisionGroup)
        self.numberSpinBox.setEnabled(False)
        self.numberSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.numberSpinBox.setMaximum(999999999)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.gridLayout.addWidget(self.numberSpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.idButton = QtWidgets.QRadioButton(self.revisionGroup)
        self.idButton.setObjectName("idButton")
        self.gridLayout.addWidget(self.idButton, 1, 0, 1, 1)
        self.idEdit = QtWidgets.QLineEdit(self.revisionGroup)
        self.idEdit.setEnabled(False)
        self.idEdit.setObjectName("idEdit")
        self.gridLayout.addWidget(self.idEdit, 1, 1, 1, 2)
        self.tagButton = QtWidgets.QRadioButton(self.revisionGroup)
        self.tagButton.setObjectName("tagButton")
        self.gridLayout.addWidget(self.tagButton, 2, 0, 1, 1)
        self.tagCombo = QtWidgets.QComboBox(self.revisionGroup)
        self.tagCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagCombo.sizePolicy().hasHeightForWidth())
        self.tagCombo.setSizePolicy(sizePolicy)
        self.tagCombo.setEditable(True)
        self.tagCombo.setObjectName("tagCombo")
        self.gridLayout.addWidget(self.tagCombo, 2, 1, 1, 2)
        self.branchButton = QtWidgets.QRadioButton(self.revisionGroup)
        self.branchButton.setObjectName("branchButton")
        self.gridLayout.addWidget(self.branchButton, 3, 0, 1, 1)
        self.branchCombo = QtWidgets.QComboBox(self.revisionGroup)
        self.branchCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.branchCombo.sizePolicy().hasHeightForWidth())
        self.branchCombo.setSizePolicy(sizePolicy)
        self.branchCombo.setEditable(True)
        self.branchCombo.setObjectName("branchCombo")
        self.gridLayout.addWidget(self.branchCombo, 3, 1, 1, 2)
        self.bookmarkButton = QtWidgets.QRadioButton(self.revisionGroup)
        self.bookmarkButton.setObjectName("bookmarkButton")
        self.gridLayout.addWidget(self.bookmarkButton, 4, 0, 1, 1)
        self.bookmarkCombo = QtWidgets.QComboBox(self.revisionGroup)
        self.bookmarkCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmarkCombo.sizePolicy().hasHeightForWidth())
        self.bookmarkCombo.setSizePolicy(sizePolicy)
        self.bookmarkCombo.setEditable(True)
        self.bookmarkCombo.setObjectName("bookmarkCombo")
        self.gridLayout.addWidget(self.bookmarkCombo, 4, 1, 1, 2)
        self.noneButton = QtWidgets.QRadioButton(self.revisionGroup)
        self.noneButton.setChecked(True)
        self.noneButton.setObjectName("noneButton")
        self.gridLayout.addWidget(self.noneButton, 5, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.revisionGroup)
        self.groupBox_2 = QtWidgets.QGroupBox(HgBackoutDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.messageEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.messageEdit.setTabChangesFocus(True)
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout.addWidget(self.messageEdit)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.userEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.userEdit.setObjectName("userEdit")
        self.gridLayout_2.addWidget(self.userEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.mergeCheckBox = QtWidgets.QCheckBox(HgBackoutDialog)
        self.mergeCheckBox.setObjectName("mergeCheckBox")
        self.verticalLayout_2.addWidget(self.mergeCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgBackoutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(HgBackoutDialog)
        self.buttonBox.accepted.connect(HgBackoutDialog.accept)
        self.buttonBox.rejected.connect(HgBackoutDialog.reject)
        self.numberButton.toggled['bool'].connect(self.numberSpinBox.setEnabled)
        self.idButton.toggled['bool'].connect(self.idEdit.setEnabled)
        self.tagButton.toggled['bool'].connect(self.tagCombo.setEnabled)
        self.branchButton.toggled['bool'].connect(self.branchCombo.setEnabled)
        self.bookmarkButton.toggled['bool'].connect(self.bookmarkCombo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(HgBackoutDialog)
        HgBackoutDialog.setTabOrder(self.numberButton, self.numberSpinBox)
        HgBackoutDialog.setTabOrder(self.numberSpinBox, self.idButton)
        HgBackoutDialog.setTabOrder(self.idButton, self.idEdit)
        HgBackoutDialog.setTabOrder(self.idEdit, self.tagButton)
        HgBackoutDialog.setTabOrder(self.tagButton, self.tagCombo)
        HgBackoutDialog.setTabOrder(self.tagCombo, self.branchButton)
        HgBackoutDialog.setTabOrder(self.branchButton, self.branchCombo)
        HgBackoutDialog.setTabOrder(self.branchCombo, self.bookmarkButton)
        HgBackoutDialog.setTabOrder(self.bookmarkButton, self.bookmarkCombo)
        HgBackoutDialog.setTabOrder(self.bookmarkCombo, self.noneButton)
        HgBackoutDialog.setTabOrder(self.noneButton, self.messageEdit)
        HgBackoutDialog.setTabOrder(self.messageEdit, self.dateEdit)
        HgBackoutDialog.setTabOrder(self.dateEdit, self.userEdit)
        HgBackoutDialog.setTabOrder(self.userEdit, self.mergeCheckBox)
        HgBackoutDialog.setTabOrder(self.mergeCheckBox, self.buttonBox)

    def retranslateUi(self, HgBackoutDialog):
        _translate = QtCore.QCoreApplication.translate
        HgBackoutDialog.setWindowTitle(_translate("HgBackoutDialog", "Mercurial Revision"))
        self.revisionGroup.setTitle(_translate("HgBackoutDialog", "Revision"))
        self.numberButton.setToolTip(_translate("HgBackoutDialog", "Select to specify a revision by number"))
        self.numberButton.setText(_translate("HgBackoutDialog", "Number"))
        self.numberSpinBox.setToolTip(_translate("HgBackoutDialog", "Enter a revision number"))
        self.idButton.setToolTip(_translate("HgBackoutDialog", "Select to specify a revision by changeset id"))
        self.idButton.setText(_translate("HgBackoutDialog", "Id:"))
        self.idEdit.setToolTip(_translate("HgBackoutDialog", "Enter a changeset id"))
        self.tagButton.setToolTip(_translate("HgBackoutDialog", "Select to specify a revision by a tag"))
        self.tagButton.setText(_translate("HgBackoutDialog", "Tag:"))
        self.tagCombo.setToolTip(_translate("HgBackoutDialog", "Enter a tag name"))
        self.branchButton.setToolTip(_translate("HgBackoutDialog", "Select to specify a revision by a branch"))
        self.branchButton.setText(_translate("HgBackoutDialog", "Branch:"))
        self.branchCombo.setToolTip(_translate("HgBackoutDialog", "Enter a branch name"))
        self.bookmarkButton.setToolTip(_translate("HgBackoutDialog", "Select to specify a revision by a bookmark"))
        self.bookmarkButton.setText(_translate("HgBackoutDialog", "Bookmark:"))
        self.bookmarkCombo.setToolTip(_translate("HgBackoutDialog", "Enter a bookmark name"))
        self.noneButton.setToolTip(_translate("HgBackoutDialog", "Select to not specify a specific revision"))
        self.noneButton.setText(_translate("HgBackoutDialog", "Parent"))
        self.groupBox_2.setTitle(_translate("HgBackoutDialog", "Commit data"))
        self.label_3.setText(_translate("HgBackoutDialog", "Commit message:"))
        self.messageEdit.setToolTip(_translate("HgBackoutDialog", "Enter the commit message or leave empty to use the default one"))
        self.label.setText(_translate("HgBackoutDialog", "Commit Date:"))
        self.dateEdit.setToolTip(_translate("HgBackoutDialog", "Enter optional date for the commit"))
        self.label_2.setText(_translate("HgBackoutDialog", "Commit User:"))
        self.userEdit.setToolTip(_translate("HgBackoutDialog", "Enter optional user for the commit"))
        self.mergeCheckBox.setToolTip(_translate("HgBackoutDialog", "Select to merge with parent of the project directory"))
        self.mergeCheckBox.setText(_translate("HgBackoutDialog", "Merge with current parent"))
