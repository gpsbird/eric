# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/DebuggerPropertiesDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DebuggerPropertiesDialog(object):
    def setupUi(self, DebuggerPropertiesDialog):
        DebuggerPropertiesDialog.setObjectName("DebuggerPropertiesDialog")
        DebuggerPropertiesDialog.resize(592, 656)
        DebuggerPropertiesDialog.setSizeGripEnabled(True)
        self._2 = QtWidgets.QVBoxLayout(DebuggerPropertiesDialog)
        self._2.setObjectName("_2")
        self.groupBox = QtWidgets.QGroupBox(DebuggerPropertiesDialog)
        self.groupBox.setObjectName("groupBox")
        self._4 = QtWidgets.QHBoxLayout(self.groupBox)
        self._4.setObjectName("_4")
        self.debugClientEdit = QtWidgets.QLineEdit(self.groupBox)
        self.debugClientEdit.setObjectName("debugClientEdit")
        self._4.addWidget(self.debugClientEdit)
        self.debugClientButton = QtWidgets.QToolButton(self.groupBox)
        self.debugClientButton.setObjectName("debugClientButton")
        self._4.addWidget(self.debugClientButton)
        self._2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(DebuggerPropertiesDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self._5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self._5.setObjectName("_5")
        self.interpreterEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.interpreterEdit.setObjectName("interpreterEdit")
        self._5.addWidget(self.interpreterEdit)
        self.interpreterButton = QtWidgets.QToolButton(self.groupBox_2)
        self.interpreterButton.setObjectName("interpreterButton")
        self._5.addWidget(self.interpreterButton)
        self._2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(DebuggerPropertiesDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self._6 = QtWidgets.QGridLayout(self.groupBox_3)
        self._6.setObjectName("_6")
        self.debugEnvironmentOverrideCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.debugEnvironmentOverrideCheckBox.setObjectName("debugEnvironmentOverrideCheckBox")
        self._6.addWidget(self.debugEnvironmentOverrideCheckBox, 0, 0, 1, 2)
        self.debugEnvironmentEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.debugEnvironmentEdit.setObjectName("debugEnvironmentEdit")
        self._6.addWidget(self.debugEnvironmentEdit, 1, 1, 1, 1)
        self.textLabel1_16 = QtWidgets.QLabel(self.groupBox_3)
        self.textLabel1_16.setObjectName("textLabel1_16")
        self._6.addWidget(self.textLabel1_16, 1, 0, 1, 1)
        self._2.addWidget(self.groupBox_3)
        self.remoteDebuggerGroup = QtWidgets.QGroupBox(DebuggerPropertiesDialog)
        self.remoteDebuggerGroup.setCheckable(True)
        self.remoteDebuggerGroup.setObjectName("remoteDebuggerGroup")
        self._7 = QtWidgets.QGridLayout(self.remoteDebuggerGroup)
        self._7.setObjectName("_7")
        self.pathTranslationGroup = QtWidgets.QGroupBox(self.remoteDebuggerGroup)
        self.pathTranslationGroup.setCheckable(True)
        self.pathTranslationGroup.setObjectName("pathTranslationGroup")
        self.gridlayout = QtWidgets.QGridLayout(self.pathTranslationGroup)
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel2_9 = QtWidgets.QLabel(self.pathTranslationGroup)
        self.textLabel2_9.setObjectName("textLabel2_9")
        self.gridlayout.addWidget(self.textLabel2_9, 1, 0, 1, 1)
        self.translationLocalEdit = QtWidgets.QLineEdit(self.pathTranslationGroup)
        self.translationLocalEdit.setObjectName("translationLocalEdit")
        self.gridlayout.addWidget(self.translationLocalEdit, 1, 1, 1, 1)
        self.translationRemoteEdit = QtWidgets.QLineEdit(self.pathTranslationGroup)
        self.translationRemoteEdit.setObjectName("translationRemoteEdit")
        self.gridlayout.addWidget(self.translationRemoteEdit, 0, 1, 1, 1)
        self.textLabel1_18 = QtWidgets.QLabel(self.pathTranslationGroup)
        self.textLabel1_18.setObjectName("textLabel1_18")
        self.gridlayout.addWidget(self.textLabel1_18, 0, 0, 1, 1)
        self._7.addWidget(self.pathTranslationGroup, 2, 0, 1, 2)
        self.hostLabel = QtWidgets.QLabel(self.remoteDebuggerGroup)
        self.hostLabel.setObjectName("hostLabel")
        self._7.addWidget(self.hostLabel, 0, 0, 1, 1)
        self.remoteCommandEdit = QtWidgets.QLineEdit(self.remoteDebuggerGroup)
        self.remoteCommandEdit.setObjectName("remoteCommandEdit")
        self._7.addWidget(self.remoteCommandEdit, 1, 1, 1, 1)
        self.execLabel = QtWidgets.QLabel(self.remoteDebuggerGroup)
        self.execLabel.setObjectName("execLabel")
        self._7.addWidget(self.execLabel, 1, 0, 1, 1)
        self.remoteHostEdit = QtWidgets.QLineEdit(self.remoteDebuggerGroup)
        self.remoteHostEdit.setObjectName("remoteHostEdit")
        self._7.addWidget(self.remoteHostEdit, 0, 1, 1, 1)
        self._2.addWidget(self.remoteDebuggerGroup)
        self.consoleDebuggerGroup = QtWidgets.QGroupBox(DebuggerPropertiesDialog)
        self.consoleDebuggerGroup.setCheckable(True)
        self.consoleDebuggerGroup.setObjectName("consoleDebuggerGroup")
        self._3 = QtWidgets.QHBoxLayout(self.consoleDebuggerGroup)
        self._3.setObjectName("_3")
        self.textLabel1_17 = QtWidgets.QLabel(self.consoleDebuggerGroup)
        self.textLabel1_17.setObjectName("textLabel1_17")
        self._3.addWidget(self.textLabel1_17)
        self.consoleCommandEdit = QtWidgets.QLineEdit(self.consoleDebuggerGroup)
        self.consoleCommandEdit.setObjectName("consoleCommandEdit")
        self._3.addWidget(self.consoleCommandEdit)
        self._2.addWidget(self.consoleDebuggerGroup)
        self.redirectCheckBox = QtWidgets.QCheckBox(DebuggerPropertiesDialog)
        self.redirectCheckBox.setObjectName("redirectCheckBox")
        self._2.addWidget(self.redirectCheckBox)
        self.noEncodingCheckBox = QtWidgets.QCheckBox(DebuggerPropertiesDialog)
        self.noEncodingCheckBox.setObjectName("noEncodingCheckBox")
        self._2.addWidget(self.noEncodingCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(DebuggerPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self._2.addWidget(self.buttonBox)

        self.retranslateUi(DebuggerPropertiesDialog)
        self.buttonBox.accepted.connect(DebuggerPropertiesDialog.accept)
        self.buttonBox.rejected.connect(DebuggerPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DebuggerPropertiesDialog)
        DebuggerPropertiesDialog.setTabOrder(self.debugClientEdit, self.debugClientButton)
        DebuggerPropertiesDialog.setTabOrder(self.debugClientButton, self.interpreterEdit)
        DebuggerPropertiesDialog.setTabOrder(self.interpreterEdit, self.interpreterButton)
        DebuggerPropertiesDialog.setTabOrder(self.interpreterButton, self.debugEnvironmentOverrideCheckBox)
        DebuggerPropertiesDialog.setTabOrder(self.debugEnvironmentOverrideCheckBox, self.debugEnvironmentEdit)
        DebuggerPropertiesDialog.setTabOrder(self.debugEnvironmentEdit, self.remoteDebuggerGroup)
        DebuggerPropertiesDialog.setTabOrder(self.remoteDebuggerGroup, self.remoteHostEdit)
        DebuggerPropertiesDialog.setTabOrder(self.remoteHostEdit, self.remoteCommandEdit)
        DebuggerPropertiesDialog.setTabOrder(self.remoteCommandEdit, self.pathTranslationGroup)
        DebuggerPropertiesDialog.setTabOrder(self.pathTranslationGroup, self.translationRemoteEdit)
        DebuggerPropertiesDialog.setTabOrder(self.translationRemoteEdit, self.translationLocalEdit)
        DebuggerPropertiesDialog.setTabOrder(self.translationLocalEdit, self.consoleDebuggerGroup)
        DebuggerPropertiesDialog.setTabOrder(self.consoleDebuggerGroup, self.consoleCommandEdit)
        DebuggerPropertiesDialog.setTabOrder(self.consoleCommandEdit, self.redirectCheckBox)

    def retranslateUi(self, DebuggerPropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        DebuggerPropertiesDialog.setWindowTitle(_translate("DebuggerPropertiesDialog", "Debugger Properties"))
        self.groupBox.setTitle(_translate("DebuggerPropertiesDialog", "Debug Client"))
        self.debugClientEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the path of the Debug Client to be used.  Leave empty to use the default."))
        self.debugClientButton.setToolTip(_translate("DebuggerPropertiesDialog", "Press to select the Debug Client via a file selection dialog"))
        self.groupBox_2.setTitle(_translate("DebuggerPropertiesDialog", "Interpreter for Debug Client"))
        self.interpreterEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the path of the interpreter to be used by the debug client."))
        self.interpreterButton.setToolTip(_translate("DebuggerPropertiesDialog", "Press to select the interpreter via a file selection dialog"))
        self.groupBox_3.setTitle(_translate("DebuggerPropertiesDialog", "Environment for Debug Client"))
        self.debugEnvironmentOverrideCheckBox.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if the environment of the debug client should be replaced"))
        self.debugEnvironmentOverrideCheckBox.setText(_translate("DebuggerPropertiesDialog", "Replace Environment"))
        self.debugEnvironmentEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the environment variables to be set."))
        self.debugEnvironmentEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Environment</b>\n"
"<p>Enter the environment variables to be set for the debugger. The individual settings must be separate by whitespace and be given in the form \'var=value\'.</p>\n"
"<p>Example: var1=1 var2=\"hello world\"</p>"))
        self.textLabel1_16.setText(_translate("DebuggerPropertiesDialog", "Environment:"))
        self.remoteDebuggerGroup.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if the debugger should be run remotely"))
        self.remoteDebuggerGroup.setTitle(_translate("DebuggerPropertiesDialog", "Remote Debugger"))
        self.pathTranslationGroup.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if path translation for remote debugging should be done"))
        self.pathTranslationGroup.setTitle(_translate("DebuggerPropertiesDialog", "Perform Path Translation"))
        self.textLabel2_9.setText(_translate("DebuggerPropertiesDialog", "Local Path:"))
        self.translationLocalEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the local path"))
        self.translationRemoteEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the remote path"))
        self.textLabel1_18.setText(_translate("DebuggerPropertiesDialog", "Remote Path:"))
        self.hostLabel.setText(_translate("DebuggerPropertiesDialog", "Remote Host:"))
        self.remoteCommandEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the remote execution command."))
        self.remoteCommandEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Remote Execution</b>\n"
"<p>Enter the remote execution command (e.g. ssh). This command is used to log into the remote host and execute the remote debugger.</p>"))
        self.execLabel.setText(_translate("DebuggerPropertiesDialog", "Remote Execution:"))
        self.remoteHostEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the hostname of the remote machine."))
        self.remoteHostEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Remote Host</b>\n"
"<p>Enter the hostname of the remote machine.</p>"))
        self.consoleDebuggerGroup.setToolTip(_translate("DebuggerPropertiesDialog", "Select, if the debugger should be executed in a console window"))
        self.consoleDebuggerGroup.setTitle(_translate("DebuggerPropertiesDialog", "Console Debugger"))
        self.textLabel1_17.setText(_translate("DebuggerPropertiesDialog", "Console Command:"))
        self.consoleCommandEdit.setToolTip(_translate("DebuggerPropertiesDialog", "Enter the console command (e.g. xterm -e)"))
        self.consoleCommandEdit.setWhatsThis(_translate("DebuggerPropertiesDialog", "<b>Console Command</b>\n"
"<p>Enter the console command (e.g. xterm -e). This command is used to open a command window for the debugger.</p>"))
        self.redirectCheckBox.setToolTip(_translate("DebuggerPropertiesDialog", "Select to redirect stdin, stdout and stderr of the program being debugged to the eric6 IDE"))
        self.redirectCheckBox.setText(_translate("DebuggerPropertiesDialog", "Redirect stdin/stdout/stderr"))
        self.noEncodingCheckBox.setToolTip(_translate("DebuggerPropertiesDialog", "Select to not set the debug client encoding"))
        self.noEncodingCheckBox.setText(_translate("DebuggerPropertiesDialog", "Don\'t set the encoding of the debug client"))

