# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsPySvn/SvnOptionsDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnOptionsDialog(object):
    def setupUi(self, SvnOptionsDialog):
        SvnOptionsDialog.setObjectName("SvnOptionsDialog")
        SvnOptionsDialog.resize(565, 169)
        SvnOptionsDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnOptionsDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.TextLabel5 = QtWidgets.QLabel(SvnOptionsDialog)
        self.TextLabel5.setObjectName("TextLabel5")
        self.gridlayout.addWidget(self.TextLabel5, 2, 0, 1, 1)
        self.layoutCheckBox = QtWidgets.QCheckBox(SvnOptionsDialog)
        self.layoutCheckBox.setChecked(True)
        self.layoutCheckBox.setObjectName("layoutCheckBox")
        self.gridlayout.addWidget(self.layoutCheckBox, 3, 0, 1, 2)
        self.protocolCombo = QtWidgets.QComboBox(SvnOptionsDialog)
        self.protocolCombo.setObjectName("protocolCombo")
        self.gridlayout.addWidget(self.protocolCombo, 0, 1, 1, 1)
        self.vcsUrlLabel = QtWidgets.QLabel(SvnOptionsDialog)
        self.vcsUrlLabel.setObjectName("vcsUrlLabel")
        self.gridlayout.addWidget(self.vcsUrlLabel, 1, 0, 1, 1)
        self.vcsLogEdit = QtWidgets.QLineEdit(SvnOptionsDialog)
        self.vcsLogEdit.setObjectName("vcsLogEdit")
        self.gridlayout.addWidget(self.vcsLogEdit, 2, 1, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(SvnOptionsDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.vcsUrlEdit = QtWidgets.QLineEdit(SvnOptionsDialog)
        self.vcsUrlEdit.setObjectName("vcsUrlEdit")
        self.gridlayout.addWidget(self.vcsUrlEdit, 1, 1, 1, 1)
        self.vcsUrlButton = QtWidgets.QToolButton(SvnOptionsDialog)
        self.vcsUrlButton.setObjectName("vcsUrlButton")
        self.gridlayout.addWidget(self.vcsUrlButton, 1, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.TextLabel5.setBuddy(self.vcsLogEdit)
        self.vcsUrlLabel.setBuddy(self.vcsUrlEdit)
        self.textLabel1.setBuddy(self.protocolCombo)

        self.retranslateUi(SvnOptionsDialog)
        self.buttonBox.accepted.connect(SvnOptionsDialog.accept)
        self.buttonBox.rejected.connect(SvnOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnOptionsDialog)
        SvnOptionsDialog.setTabOrder(self.protocolCombo, self.vcsUrlEdit)
        SvnOptionsDialog.setTabOrder(self.vcsUrlEdit, self.vcsUrlButton)
        SvnOptionsDialog.setTabOrder(self.vcsUrlButton, self.vcsLogEdit)
        SvnOptionsDialog.setTabOrder(self.vcsLogEdit, self.layoutCheckBox)

    def retranslateUi(self, SvnOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnOptionsDialog.setWindowTitle(_translate("SvnOptionsDialog", "Repository Infos"))
        SvnOptionsDialog.setWhatsThis(_translate("SvnOptionsDialog", "<b>Repository Infos Dialog</b>\n"
"<p>Enter the various infos into the entry fields. These values are used to generate a new project in the repository. If the checkbox is selected, the URL must end in the project name. A directory tree with project/tags, project/branches and project/trunk will be generated in the repository. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>"))
        self.TextLabel5.setText(_translate("SvnOptionsDialog", "Log &Message:"))
        self.layoutCheckBox.setToolTip(_translate("SvnOptionsDialog", "Select, if the standard repository layout (projectdir/trunk, projectdir/tags, projectdir/branches) should be generated"))
        self.layoutCheckBox.setText(_translate("SvnOptionsDialog", "Create standard repository &layout"))
        self.layoutCheckBox.setShortcut(_translate("SvnOptionsDialog", "Alt+L"))
        self.protocolCombo.setToolTip(_translate("SvnOptionsDialog", "Select the protocol to access the repository"))
        self.vcsUrlLabel.setText(_translate("SvnOptionsDialog", "&URL:"))
        self.vcsLogEdit.setToolTip(_translate("SvnOptionsDialog", "Enter the log message for the new project."))
        self.vcsLogEdit.setWhatsThis(_translate("SvnOptionsDialog", "<b>Log Message</b>\n"
"<p>Enter the log message to be used for the new project.</p>"))
        self.vcsLogEdit.setText(_translate("SvnOptionsDialog", "new project started"))
        self.textLabel1.setText(_translate("SvnOptionsDialog", "&Protocol:"))
        self.vcsUrlEdit.setToolTip(_translate("SvnOptionsDialog", "Enter the url path of the module in the repository (without protocol part)"))
        self.vcsUrlEdit.setWhatsThis(_translate("SvnOptionsDialog", "<b>URL</b><p>Enter the URL to the module. For a repository with standard layout, this must not contain the trunk, tags or branches part.</p>"))
        self.vcsUrlButton.setToolTip(_translate("SvnOptionsDialog", "Select the repository url via a directory selection dialog or the repository browser"))

