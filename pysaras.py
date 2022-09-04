from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import math


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 420)
        Form.setStyleSheet("background-color:#fffaef")

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(Form)
        font = QtGui.QFont()
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -595, 527, 1983))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        #pySARAS heading
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(21)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        #Target label
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #3d3d3d")
        self.label_10.setObjectName("label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        #Targetcpu radio button
        self.targetcpu = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetcpu.sizePolicy().hasHeightForWidth())
        self.targetcpu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.targetcpu.setFont(font)
        self.targetcpu.setAutoFillBackground(False)
        self.targetcpu.setStyleSheet("color: #3d3d3d")
        self.targetcpu.setObjectName("targetcpu")

        self.gridLayout_2.addWidget(self.targetcpu, 0, 1, 1, 1)

        #targetgpu radio button
        self.targetgpu = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetgpu.sizePolicy().hasHeightForWidth())
        self.targetgpu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.targetgpu.setFont(font)
        self.targetgpu.setStyleSheet("color: #3d3d3d")
        self.targetgpu.setObjectName("targetgpu")

        self.gridLayout_2.addWidget(self.targetgpu, 0, 2, 1, 1)

        #Device label
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #3d3d3d")
        self.label_8.setObjectName("label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)

        #cupyfuse label
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #3d3d3d")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2.addLayout(self.verticalLayout_2, 5, 0, 1, 1)

        #cupytrue radio button
        self.cupytrue = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cupytrue.sizePolicy().hasHeightForWidth())
        self.cupytrue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.cupytrue.setFont(font)
        self.cupytrue.setStyleSheet("color: #3d3d3d")
        self.cupytrue.setObjectName("cupytrue")

        self.gridLayout_2.addWidget(self.cupytrue, 2, 1, 1, 1)

        #cupyfalse radiobutton
        self.cupyfalse = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cupyfalse.sizePolicy().hasHeightForWidth())
        self.cupyfalse.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.cupyfalse.setFont(font)
        self.cupyfalse.setStyleSheet("color: #3d3d3d")
        self.cupyfalse.setObjectName("cupyfalse")

        self.gridLayout_2.addWidget(self.cupyfalse, 2, 2, 1, 1)

        #Probtype label
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #3d3d3d")
        self.label_9.setObjectName("label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        #probRBC radio button
        self.probRBC = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probRBC.sizePolicy().hasHeightForWidth())
        self.probRBC.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.probRBC.setFont(font)
        self.probRBC.setStyleSheet("color: #3d3d3d")
        self.probRBC.setObjectName("probRBC")

        self.gridLayout_2.addWidget(self.probRBC, 3, 1, 1, 1)

        #probHydro radio button
        self.probHydro = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probHydro.sizePolicy().hasHeightForWidth())
        self.probHydro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.probHydro.setFont(font)
        self.probHydro.setStyleSheet("color: #3d3d3d")
        self.probHydro.setObjectName("probHydro")

        self.gridLayout_2.addWidget(self.probHydro, 3, 2, 1, 1)

        #lineEdit for device
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(17)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:#fff5e3")
        self.lineEdit.setObjectName("lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.lineEdit.setDisabled(not self.targetgpu.isChecked())           #to disable lineEdit
        self.targetgpu.toggled.connect(self.lineEdit.setEnabled)            #to enable lineEdit when targetgpu is checked

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        #flow parameters heading - RBC
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")

        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 2)

        #flow parameters heading - Hydro
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 3, 1, 2)

        #Ra label
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #3d3d3d")
        self.label_11.setObjectName("label_11")

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        #Pr label
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: #3d3d3d")
        self.label_15.setObjectName("label_15")

        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)

        #Ro label
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #3d3d3d")
        self.label_14.setObjectName("label_14")

        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)

        #Ta label
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #3d3d3d")
        self.label_16.setObjectName("label_16")

        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)

        #lineEdit for Ra
        self.rbcRa = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbcRa.sizePolicy().hasHeightForWidth())
        self.rbcRa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.rbcRa.setFont(font)
        self.rbcRa.setStyleSheet("background-color:#fff5e3")
        self.rbcRa.setText("")
        self.rbcRa.setObjectName("rbcRa")

        self.gridLayout_3.addWidget(self.rbcRa, 1, 1, 1, 1)

        #lineEdit for Pr
        self.rbcPr = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbcPr.sizePolicy().hasHeightForWidth())
        self.rbcPr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.rbcPr.setFont(font)
        self.rbcPr.setStyleSheet("background-color:#fff5e3")
        self.rbcPr.setText("")
        self.rbcPr.setObjectName("rbcPr")

        self.gridLayout_3.addWidget(self.rbcPr, 2, 1, 1, 1)

        #lineEdit for Ro
        self.rbcRo = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbcRo.sizePolicy().hasHeightForWidth())
        self.rbcRo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.rbcRo.setFont(font)
        self.rbcRo.setStyleSheet("background-color:#fff5e3")
        self.rbcRo.setText("")
        self.rbcRo.setObjectName("rbcRo")

        self.gridLayout_3.addWidget(self.rbcRo, 3, 1, 1, 1)

        #lineEdit for Ta
        self.rbcTa = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbcTa.sizePolicy().hasHeightForWidth())
        self.rbcTa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.rbcTa.setFont(font)
        self.rbcTa.setStyleSheet("background-color:#fff5e3")
        self.rbcTa.setText("")
        self.rbcTa.setObjectName("rbcTa")

        self.gridLayout_3.addWidget(self.rbcTa, 4, 1, 1, 1)

        #nu label
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #3d3d3d")
        self.label_12.setObjectName("label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 3, 1, 1)

        #omega label
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: #3d3d3d")
        self.label_18.setObjectName("label_18")

        self.gridLayout_3.addWidget(self.label_18, 2, 3, 1, 1)

        #lineEdit for nu
        self.nuHydro = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nuHydro.sizePolicy().hasHeightForWidth())
        self.nuHydro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.nuHydro.setFont(font)
        self.nuHydro.setStyleSheet("background-color:#fff5e3")
        self.nuHydro.setObjectName("nuHydro")

        self.gridLayout_3.addWidget(self.nuHydro, 1, 4, 1, 1)

        #lineEdit for omega
        self.omegaHydro = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.omegaHydro.sizePolicy().hasHeightForWidth())
        self.omegaHydro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.omegaHydro.setFont(font)
        self.omegaHydro.setStyleSheet("background-color:#fff5e3")
        self.omegaHydro.setObjectName("omegaHydro")

        self.gridLayout_3.addWidget(self.omegaHydro, 2, 4, 1, 1)

        #to disable the flow parameters and to enable them when the respective probtype is selected
        self.rbcPr.setDisabled(not self.probRBC.isChecked())
        self.probRBC.toggled.connect(self.rbcPr.setEnabled)
        self.rbcRo.setDisabled(not self.probRBC.isChecked())
        self.probRBC.toggled.connect(self.rbcRo.setEnabled)
        self.rbcRa.setDisabled(not self.probRBC.isChecked())
        self.probRBC.toggled.connect(self.rbcRa.setEnabled)
        self.rbcTa.setDisabled(not self.probRBC.isChecked())
        self.probRBC.toggled.connect(self.rbcTa.setEnabled)
        self.nuHydro.setDisabled(not self.probHydro.isChecked())
        self.probHydro.toggled.connect(self.nuHydro.setEnabled)
        self.omegaHydro.setDisabled(not self.probHydro.isChecked())
        self.probHydro.toggled.connect(self.omegaHydro.setEnabled)
        self.verticalLayout.addLayout(self.gridLayout_3)
        #---------------------------------------------------------------

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem2)

        #Domain Size heading
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_22.setObjectName("label_22")

        self.verticalLayout.addWidget(self.label_22)

        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")

        #Lx label
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: #3d3d3d")
        self.label_25.setObjectName("label_25")

        self.gridLayout_6.addWidget(self.label_25, 0, 0, 1, 1)

        #Ly label
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: #3d3d3d")
        self.label_23.setObjectName("label_23")

        self.gridLayout_6.addWidget(self.label_23, 0, 1, 1, 1)

        #Lz label
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: #3d3d3d")
        self.label_24.setObjectName("label_24")

        self.gridLayout_6.addWidget(self.label_24, 0, 2, 1, 1)

        #lineEdit for Lx
        self.xDomain = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xDomain.sizePolicy().hasHeightForWidth())
        self.xDomain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.xDomain.setFont(font)
        self.xDomain.setStyleSheet("background-color:#fff5e3")
        self.xDomain.setObjectName("xDomain")

        self.gridLayout_6.addWidget(self.xDomain, 1, 0, 1, 1)

        #lineEdit for Ly
        self.yDomain = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yDomain.sizePolicy().hasHeightForWidth())
        self.yDomain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.yDomain.setFont(font)
        self.yDomain.setStyleSheet("background-color:#fff5e3")
        self.yDomain.setObjectName("yDomain")

        self.gridLayout_6.addWidget(self.yDomain, 1, 1, 1, 1)

        #lineEdit for Lz
        self.zDomain = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zDomain.sizePolicy().hasHeightForWidth())
        self.zDomain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.zDomain.setFont(font)
        self.zDomain.setStyleSheet("background-color:#fff5e3")
        self.zDomain.setObjectName("zDomain")

        self.gridLayout_6.addWidget(self.zDomain, 1, 2, 1, 1)

        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid value")
        msg.setDetailedText("The value of Nx, Ny and Nz should be of the form 2^n")
        msg.buttonClicked.connect(QtCore.QCoreApplication.instance().quit)

        #Nx label
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.gridLayout_6.addWidget(self.label, 2, 0, 1, 1)

        #Ny label
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.gridLayout_6.addWidget(self.label_2, 2, 1, 1, 1)

        #Nz label
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.gridLayout_6.addWidget(self.label_3, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)

        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")

        #lineEdit for Nx
        self.xDomain_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xDomain_2.sizePolicy().hasHeightForWidth())
        self.xDomain_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.xDomain_2.setFont(font)
        self.xDomain_2.setStyleSheet("background-color:#fff5e3")
        self.xDomain_2.setObjectName("xDomain_2")

        self.gridLayout_6.addWidget(self.xDomain_2, 3, 0, 1, 1)
        print(self.xDomain_2.text())

        #lineEdit for Ny
        self.xDomain_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xDomain_3.sizePolicy().hasHeightForWidth())
        self.xDomain_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.xDomain_3.setFont(font)
        self.xDomain_3.setStyleSheet("background-color:#fff5e3")
        self.xDomain_3.setObjectName("xDomain_3")

        self.gridLayout_6.addWidget(self.xDomain_3, 3, 1, 1, 1)

        #lineEdit for Nz
        self.xDomain_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xDomain_4.sizePolicy().hasHeightForWidth())
        self.xDomain_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.xDomain_4.setFont(font)
        self.xDomain_4.setStyleSheet("background-color:#fff5e3")
        self.xDomain_4.setObjectName("xDomain_4")

        self.gridLayout_6.addWidget(self.xDomain_4, 3, 2, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 1, 1, 1)

        #Grid Type heading
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_9.addWidget(self.label_30, 1, 1, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()

        self.gridLayout_10.setObjectName("gridLayout_10")

        #uuu radio button
        self.uuu_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uuu_2.sizePolicy().hasHeightForWidth())
        self.uuu_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.uuu_2.setFont(font)
        self.uuu_2.setAutoFillBackground(False)
        self.uuu_2.setStyleSheet("color: #3d3d3d")
        self.uuu_2.setObjectName("uuu_2")

        self.gridLayout_9.addWidget(self.uuu_2, 2, 0, 1, 1)

        #uud radio button
        self.uud_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uud_2.sizePolicy().hasHeightForWidth())
        self.uud_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.uud_2.setFont(font)
        self.uud_2.setStyleSheet("color: #3d3d3d")
        self.uud_2.setObjectName("uud_2")

        self.gridLayout_9.addWidget(self.uud_2, 2, 1, 1, 1)

        #ddd radio button
        self.ddd_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ddd_2.sizePolicy().hasHeightForWidth())
        self.ddd_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.ddd_2.setFont(font)
        self.ddd_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ddd_2.setStyleSheet("color: #3d3d3d")
        self.ddd_2.setObjectName("ddd_2")

        self.gridLayout_9.addWidget(self.ddd_2, 2, 2, 1, 1)

        #betax label
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: #3d3d3d")
        self.label_31.setObjectName("label_31")

        self.gridLayout_10.addWidget(self.label_31, 0, 0, 1, 1)

        #lineEdit for betax
        self.betax_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.betax_2.sizePolicy().hasHeightForWidth())
        self.betax_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.betax_2.setFont(font)
        self.betax_2.setStyleSheet("background-color:#fff5e3")
        self.betax_2.setObjectName("betax_2")

        self.gridLayout_10.addWidget(self.betax_2, 0, 1, 1, 1)

        #betay label
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: #3d3d3d")
        self.label_32.setObjectName("label_32")

        self.gridLayout_10.addWidget(self.label_32, 1, 0, 1, 1)

        #lineEdit for betay
        self.betay_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.betay_2.sizePolicy().hasHeightForWidth())
        self.betay_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.betay_2.setFont(font)
        self.betay_2.setStyleSheet("background-color:#fff5e3")
        self.betay_2.setObjectName("betay_2")

        self.gridLayout_10.addWidget(self.betay_2, 1, 1, 1, 1)

        #betaz label
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: #3d3d3d")
        self.label_33.setObjectName("label_33")

        self.gridLayout_10.addWidget(self.label_33, 2, 0, 1, 1)

        #lineEdit for betaz
        self.betaz_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.betaz_2.sizePolicy().hasHeightForWidth())
        self.betaz_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.betaz_2.setFont(font)
        self.betaz_2.setStyleSheet("background-color:#fff5e3")
        self.betaz_2.setObjectName("betaz_2")
        self.gridLayout_10.addWidget(self.betaz_2, 2, 1, 1, 1)

        #to disable beta parameters and to enable them when respective grid types are selected
        self.betax_2.setDisabled(not self.ddd_2.isChecked())
        self.ddd_2.toggled.connect(self.betax_2.setEnabled)
        self.betay_2.setDisabled(not self.ddd_2.isChecked())
        self.ddd_2.toggled.connect(self.betay_2.setEnabled)
        self.betaz_2.setDisabled(not self.ddd_2.isChecked())
        self.ddd_2.toggled.connect(self.betaz_2.setEnabled)
        self.uud_2.toggled.connect(self.betaz_2.setEnabled)
        #-----------------------------------------------------------------

        self.gridLayout_9.addLayout(self.gridLayout_10, 3, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_9)

        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")

        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_11.addItem(spacerItem4, 1, 0, 1, 1)

        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")

        #Initial Conditions heading
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_34.setObjectName("label_34")

        self.gridLayout_13.addWidget(self.label_34, 1, 0, 1, 2)

        #lineEdit for ICType
        self.ICType = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ICType.sizePolicy().hasHeightForWidth())
        self.ICType.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.ICType.setFont(font)
        self.ICType.setStyleSheet("background-color:#fff5e3")
        self.ICType.setObjectName("ICType")

        self.gridLayout_13.addWidget(self.ICType, 2, 1, 1, 1)

        #ICType label
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: #3d3d3d")
        self.label_35.setObjectName("label_35")

        self.gridLayout_13.addWidget(self.label_35, 2, 0, 1, 1)

        self.gridLayout_11.addLayout(self.gridLayout_13, 2, 0, 1, 1)

        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")

        self.gridLayout_11.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")

        #Boundary conditions heading
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_20.setObjectName("label_20")

        self.gridLayout_15.addWidget(self.label_20, 1, 0, 1, 3)

        #BCType label
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: #3d3d3d")
        self.label_21.setObjectName("label_21")

        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)

        #BCType radio buttons
        self.BCTypeNNN_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BCTypeNNN_2.sizePolicy().hasHeightForWidth())
        self.BCTypeNNN_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.BCTypeNNN_2.setFont(font)
        self.BCTypeNNN_2.setStyleSheet("color: #3d3d3d")
        self.BCTypeNNN_2.setObjectName("BCTypeNNN_2")

        self.gridLayout_5.addWidget(self.BCTypeNNN_2, 0, 1, 1, 1)


        self.BCTypePPN_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BCTypePPN_2.sizePolicy().hasHeightForWidth())
        self.BCTypePPN_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.BCTypePPN_2.setFont(font)
        self.BCTypePPN_2.setStyleSheet("color: #3d3d3d")
        self.BCTypePPN_2.setObjectName("BCTypePPN_2")

        self.gridLayout_5.addWidget(self.BCTypePPN_2, 0, 2, 1, 1)


        self.BCTypePPP_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BCTypePPP_2.sizePolicy().hasHeightForWidth())
        self.BCTypePPP_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.BCTypePPP_2.setFont(font)
        self.BCTypePPP_2.setStyleSheet("color: #3d3d3d")
        self.BCTypePPP_2.setObjectName("BCTypePPP_2")

        self.gridLayout_5.addWidget(self.BCTypePPP_2, 1, 2, 1, 1)


        self.BCTypeLDC_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BCTypeLDC_2.sizePolicy().hasHeightForWidth())
        self.BCTypeLDC_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.BCTypeLDC_2.setFont(font)
        self.BCTypeLDC_2.setStyleSheet("color: #3d3d3d")
        self.BCTypeLDC_2.setObjectName("BCTypeLDC_2")

        self.gridLayout_5.addWidget(self.BCTypeLDC_2, 2, 1, 1, 1)


        self.BCTypePPS_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BCTypePPS_2.sizePolicy().hasHeightForWidth())
        self.BCTypePPS_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.BCTypePPS_2.setFont(font)
        self.BCTypePPS_2.setStyleSheet("color: #3d3d3d")
        self.BCTypePPS_2.setObjectName("BCTypePPS_2")

        self.gridLayout_5.addWidget(self.BCTypePPS_2, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 3, 0, 1, 3)

        self.gridLayout_15.addLayout(self.gridLayout_5, 2, 0, 1, 3)

        #simulation parameters heading
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_36.setObjectName("label_36")

        self.gridLayout_15.addWidget(self.label_36, 3, 0, 1, 3)

        #restart label
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: #3d3d3d")
        self.label_37.setObjectName("label_37")

        self.gridLayout_15.addWidget(self.label_37, 4, 0, 1, 1)

        #restarttrue radio button
        self.restarttrue = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restarttrue.sizePolicy().hasHeightForWidth())
        self.restarttrue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.restarttrue.setFont(font)
        self.restarttrue.setStyleSheet("color: #3d3d3d")
        self.restarttrue.setObjectName("restarttrue")

        self.gridLayout_15.addWidget(self.restarttrue, 4, 1, 1, 1)

        #restartfalse radio button
        self.restartfalse = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restartfalse.sizePolicy().hasHeightForWidth())
        self.restartfalse.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.restartfalse.setFont(font)
        self.restartfalse.setStyleSheet("color: #3d3d3d")
        self.restartfalse.setObjectName("restartfalse")

        self.gridLayout_15.addWidget(self.restartfalse, 4, 2, 1, 1)

        #restart filename label
        self.label_51 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: #3d3d3d")
        self.label_51.setObjectName("label_51")

        self.gridLayout_15.addWidget(self.label_51, 5, 0, 1, 2)

        #lineEdit for restart filename
        self.time_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_4.sizePolicy().hasHeightForWidth())
        self.time_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.time_4.setFont(font)
        self.time_4.setStyleSheet("background-color:#fff5e3")
        self.time_4.setObjectName("time_4")

        self.gridLayout_15.addWidget(self.time_4, 5, 2, 1, 1)


        self.time_4.setDisabled(not self.restarttrue.isChecked())       #to disable restart filename
        self.restarttrue.toggled.connect(self.time_4.setEnabled) #to enable restart filename when restarttrue is checked

        #time label
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: #3d3d3d")
        self.label_38.setObjectName("label_38")

        self.gridLayout_15.addWidget(self.label_38, 6, 0, 1, 1)

        #lineEdit for time
        self.time = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.time.setFont(font)
        self.time.setStyleSheet("background-color:#fff5e3")
        self.time.setObjectName("time")

        self.gridLayout_15.addWidget(self.time, 6, 2, 1, 1)

        #dt label
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: #3d3d3d")
        self.label_39.setObjectName("label_39")

        self.gridLayout_15.addWidget(self.label_39, 7, 0, 1, 1)

        #lineEdit for dt
        self.dt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dt.sizePolicy().hasHeightForWidth())
        self.dt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.dt.setFont(font)
        self.dt.setStyleSheet("background-color:#fff5e3")
        self.dt.setObjectName("dt")

        self.gridLayout_15.addWidget(self.dt, 7, 2, 1, 1)

        #tMax label
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: #3d3d3d")
        self.label_40.setObjectName("label_40")

        self.gridLayout_15.addWidget(self.label_40, 8, 0, 1, 1)

        #lineEdit for tMax
        self.tMax = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tMax.sizePolicy().hasHeightForWidth())
        self.tMax.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.tMax.setFont(font)
        self.tMax.setStyleSheet("background-color:#fff5e3")
        self.tMax.setObjectName("tMax")

        self.gridLayout_15.addWidget(self.tMax, 8, 2, 1, 1)

        #Cn label
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: #3d3d3d")
        self.label_41.setObjectName("label_41")

        self.gridLayout_15.addWidget(self.label_41, 9, 0, 1, 1)

        #lineEdit for Cn
        self.Cn = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cn.sizePolicy().hasHeightForWidth())
        self.Cn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.Cn.setFont(font)
        self.Cn.setStyleSheet("background-color:#fff5e3")
        self.Cn.setObjectName("Cn")

        self.gridLayout_15.addWidget(self.Cn, 9, 2, 1, 1)

        #opInt label
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: #3d3d3d")
        self.label_42.setObjectName("label_42")

        self.gridLayout_15.addWidget(self.label_42, 10, 0, 1, 1)

        #lineEdit for opInt
        self.opInt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opInt.sizePolicy().hasHeightForWidth())
        self.opInt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.opInt.setFont(font)
        self.opInt.setStyleSheet("background-color:#fff5e3")
        self.opInt.setObjectName("opInt")

        self.gridLayout_15.addWidget(self.opInt, 10, 2, 1, 1)

        #fwInt label
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: #3d3d3d")
        self.label_43.setObjectName("label_43")

        self.gridLayout_15.addWidget(self.label_43, 11, 0, 1, 1)

        #lineEdit for fwInt
        self.fwInt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fwInt.sizePolicy().hasHeightForWidth())
        self.fwInt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.fwInt.setFont(font)
        self.fwInt.setStyleSheet("background-color:#fff5e3")
        self.fwInt.setObjectName("fwInt")

        self.gridLayout_15.addWidget(self.fwInt, 11, 2, 1, 1)

        #rwInt label
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: #3d3d3d")
        self.label_44.setObjectName("label_44")
        self.gridLayout_15.addWidget(self.label_44, 12, 0, 1, 1)

        #lineEdit for rwInt
        self.rwInt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rwInt.sizePolicy().hasHeightForWidth())
        self.rwInt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.rwInt.setFont(font)
        self.rwInt.setStyleSheet("background-color:#fff5e3")
        self.rwInt.setObjectName("rwInt")
        self.gridLayout_15.addWidget(self.rwInt, 12, 2, 1, 1)

        #FpTolerance label
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: #3d3d3d")
        self.label_45.setObjectName("label_45")

        self.gridLayout_15.addWidget(self.label_45, 13, 0, 1, 2)

        #lineEdit for FpTolerance
        self.FpTolerance = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FpTolerance.sizePolicy().hasHeightForWidth())
        self.FpTolerance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.FpTolerance.setFont(font)
        self.FpTolerance.setStyleSheet("background-color:#fff5e3")
        self.FpTolerance.setObjectName("FpTolerance")

        self.gridLayout_15.addWidget(self.FpTolerance, 13, 2, 1, 1)

        #PoissonTolerance label
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: #3d3d3d")
        self.label_46.setObjectName("label_46")

        self.gridLayout_15.addWidget(self.label_46, 14, 0, 1, 2)

        #lineEdit for PoissonTolerance
        self.PoissonTolerance = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PoissonTolerance.sizePolicy().hasHeightForWidth())
        self.PoissonTolerance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.PoissonTolerance.setFont(font)
        self.PoissonTolerance.setStyleSheet("background-color:#fff5e3")
        self.PoissonTolerance.setObjectName("PoissonTolerance")

        self.gridLayout_15.addWidget(self.PoissonTolerance, 14, 2, 1, 1)

        #gssorMG label
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: #3d3d3d")
        self.label_47.setObjectName("label_47")

        self.gridLayout_15.addWidget(self.label_47, 15, 0, 1, 1)

        #lineEdit for gssorMG
        self.gssorMG = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gssorMG.sizePolicy().hasHeightForWidth())
        self.gssorMG.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.gssorMG.setFont(font)
        self.gssorMG.setStyleSheet("background-color:#fff5e3")
        self.gssorMG.setObjectName("gssorMG")

        self.gridLayout_15.addWidget(self.gssorMG, 15, 2, 1, 1)

        #gssorWp label
        self.label_48 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: #3d3d3d")
        self.label_48.setObjectName("label_48")

        self.gridLayout_15.addWidget(self.label_48, 16, 0, 1, 1)

        #lineEdit for gssorWp
        self.gssorWp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gssorWp.sizePolicy().hasHeightForWidth())
        self.gssorWp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.gssorWp.setFont(font)
        self.gssorWp.setStyleSheet("background-color:#fff5e3")
        self.gssorWp.setObjectName("gssorWp")

        self.gridLayout_15.addWidget(self.gssorWp, 16, 2, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_15.addItem(spacerItem5, 0, 0, 1, 1)

        #gssorPP label
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: #3d3d3d")
        self.label_49.setObjectName("label_49")

        self.gridLayout_15.addWidget(self.label_49, 17, 0, 1, 1)

        #lineEdit for gssorPP
        self.gssorPP = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gssorPP.sizePolicy().hasHeightForWidth())
        self.gssorPP.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.gssorPP.setFont(font)
        self.gssorPP.setStyleSheet("background-color:#fff5e3")
        self.gssorPP.setObjectName("gssorPP")
        self.gridLayout_15.addWidget(self.gssorPP, 17, 2, 1, 1)

        #maxiteration label
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: #3d3d3d")
        self.label_50.setObjectName("label_50")

        self.gridLayout_15.addWidget(self.label_50, 18, 0, 1, 2)

        #lineEdit for maxiteration
        self.maxiteration = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxiteration.sizePolicy().hasHeightForWidth())
        self.maxiteration.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.maxiteration.setFont(font)
        self.maxiteration.setStyleSheet("background-color:#fff5e3")
        self.maxiteration.setObjectName("maxiteration")

        self.gridLayout_15.addWidget(self.maxiteration, 18, 2, 1, 1)

        self.gridLayout_12.addLayout(self.gridLayout_15, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_12)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem7)

        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")

        #MultiGrid Parameters heading
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Georgia")
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_55.setObjectName("label_55")

        self.gridLayout_17.addWidget(self.label_55, 0, 0, 1, 2)

        #preSm label
        self.label_56 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("color: #3d3d3d")
        self.label_56.setObjectName("label_56")

        self.gridLayout_17.addWidget(self.label_56, 1, 0, 1, 1)

        #lineEdit for prreSm
        self.deviceNumber_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceNumber_5.sizePolicy().hasHeightForWidth())
        self.deviceNumber_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.deviceNumber_5.setFont(font)
        self.deviceNumber_5.setStyleSheet("background-color:#fff5e3")
        self.deviceNumber_5.setObjectName("deviceNumber_5")

        self.gridLayout_17.addWidget(self.deviceNumber_5, 1, 1, 1, 1)

        #pstSm label
        self.label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: #3d3d3d")
        self.label_57.setObjectName("label_57")

        self.gridLayout_17.addWidget(self.label_57, 2, 0, 1, 1)

        #lineEdit for pstSm
        self.deviceNumber_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceNumber_6.sizePolicy().hasHeightForWidth())
        self.deviceNumber_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.deviceNumber_6.setFont(font)
        self.deviceNumber_6.setStyleSheet("background-color:#fff5e3")
        self.deviceNumber_6.setObjectName("deviceNumber_6")

        self.gridLayout_17.addWidget(self.deviceNumber_6, 2, 1, 1, 1)

        #vcCnt label
        self.label_58 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: #3d3d3d")
        self.label_58.setObjectName("label_58")

        self.gridLayout_17.addWidget(self.label_58, 3, 0, 1, 1)

        #lineEdit for vcCnt
        self.deviceNumber_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceNumber_7.sizePolicy().hasHeightForWidth())
        self.deviceNumber_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.deviceNumber_7.setFont(font)
        self.deviceNumber_7.setStyleSheet("background-color:#fff5e3")
        self.deviceNumber_7.setObjectName("deviceNumber_7")

        self.gridLayout_17.addWidget(self.deviceNumber_7, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_17)

        #push button for submitting the form
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setFamily("Prestige Elite Std")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: #903909; color: #fff5e3")
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.click_btn)   #function that defines what happens on clicking pushButton_5

        #self.pushButton_5.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        #making different groups of radio buttons wrt each parameter
        self.target_group=QtWidgets.QButtonGroup()
        self.target_group.addButton(self.targetgpu)
        self.target_group.addButton(self.targetcpu)
        self.cupyfuse_group=QtWidgets.QButtonGroup()
        self.cupyfuse_group.addButton(self.cupyfalse)
        self.cupyfuse_group.addButton(self.cupytrue)
        self.probtype_group=QtWidgets.QButtonGroup()
        self.probtype_group.addButton(self.probRBC)
        self.probtype_group.addButton(self.probHydro)
        self.BCType_group=QtWidgets.QButtonGroup()
        self.BCType_group.addButton(self.BCTypePPN_2)
        self.BCType_group.addButton(self.BCTypePPS_2)
        self.BCType_group.addButton(self.BCTypeLDC_2)
        self.BCType_group.addButton(self.BCTypeNNN_2)
        self.BCType_group.addButton(self.BCTypePPP_2)
        self.GridType_group=QtWidgets.QButtonGroup()
        self.GridType_group.addButton(self.uuu_2)
        self.GridType_group.addButton(self.ddd_2)
        self.GridType_group.addButton(self.uud_2)
        self.restart_group=QtWidgets.QButtonGroup()
        self.restart_group.addButton(self.restartfalse)
        self.restart_group.addButton(self.restarttrue)
        #---------------------------------------------------------

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def click_btn(self):  #function to create/overwrite para.py when submit button is clicked
        fname = 'para.py'
        with open(fname, 'w') as f:

            if self.targetcpu.isChecked():
                Target = "CPU"
            else:
                Target = "GPU"
            f.write('Target="{}"'.format(Target))

            if Target == "GPU":
                device = self.lineEdit.text()
                f.write('\ndevice={}'.format(device))

            if self.cupytrue.isChecked():
                cupyfuse = True
            else:
                cupyfuse = False
            f.write('\ncupyfuse={}'.format(cupyfuse))

            if self.probRBC.isChecked():
                ProbType = "RBC"
            else:
                ProbType = "Hydro"
            f.write('\nProbType="{}"'.format(ProbType))

            if ProbType == "RBC":
                Ra = self.rbcRa.text()
                Pr = self.rbcPr.text()
                Ro = self.rbcRo.text()
                Ta = self.rbcTa.text()
                f.write('\nRa={}'.format(Ra))
                f.write('\nPr={}'.format(Pr))
                f.write('\nRo={}'.format(Ro))
                f.write('\nTa={}'.format(Ta))

            if ProbType == "Hydro":
                nu = self.nuHydro.text()
                Omega = self.omegaHydro.text()
                f.write('\nnu={}'.format(nu))
                f.write('\nOmega={}'.format(Omega))

            Lx = self.xDomain.text()
            Ly = self.yDomain.text()
            Lz = self.zDomain.text()
            f.write('\nLx,Ly,Lz={}'.format(Lx))
            f.write(',{}'.format(Ly))
            f.write(',{}'.format(Lz))

            Nx = int(self.xDomain_2.text())
            Ny = self.xDomain_3.text()
            Nz = self.xDomain_4.text()

            if (math.log2(Nx).is_integer() and (math.log2(Ny).is_integer()) and math.log2(Nz).is_integer()):
                pass

            else:
                #QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Invalid value")
                msg.setDetailedText("The value of Nx, Ny and Nz should be of the form 2^n")
                #msg.buttonClicked.connect(QtCore.QCoreApplication.instance().quit)
                x=msg.exec()
                pass

            '''Nx = self.xDomain_2.text()
            Ny = self.xDomain_3.text()
            Nz = self.xDomain_4.text()

            try :
                math.log2(int(Nx)).is_integer() #and (math.log2(Ny).is_integer()) and math.log2(Nz).is_integer()

            except Exception:
                QtGui.QMessageBox.about(self, 'Error','Input can only be a number')
                pass'''

            f.write('\nNx,Ny,Nz={}'.format(Nx))
            f.write(',{}'.format(Ny))
            f.write(',{}'.format(Nz))

            '''else:
                x = msg.exec()'''

            if self.uud_2.isChecked():
                GridType = "UUD"
            elif self.ddd_2.isChecked():
                GridType = "DDD"
            else:
                GridType = "UUU"
            f.write('\nGridType="{}"'.format(GridType))

            if GridType == "DDD":
                betax = self.betax_2.text()
                betay = self.betay_2.text()
                betaz = self.betaz_2.text()
                f.write('\nbetax={}'.format(betax))
                f.write('\nbetay={}'.format(betay))
                f.write('\nbetaz={}'.format(betaz))

            if GridType == "UUD":
                betaz = self.betaz_2.text()
                f.write('\nbetaz={}'.format(betaz))

            ICtype = self.ICType.text()
            f.write('\nICtype={}'.format(ICtype))

            if self.BCTypeLDC_2.isChecked():
                BCtype="LDC"
            elif self.BCTypeNNN_2.isChecked():
                BCtype = "NNN"
            elif self.BCTypePPN_2.isChecked():
                BCtype = "PPN"
            elif self.BCTypePPP_2.isChecked():
                BCtype = "PPP"
            else:
                BCtype = "PPS"
            f.write('\nBCtype="{}"'.format(BCtype))

            if self.restarttrue.isChecked():
                restart = True
            else:
                restart = False
            f.write('\nrestart={}'.format(restart))
            if restart==True:
                restart_filename=self.time_4.text()
                f.write('\nrestart_filename="{}"'.format(restart_filename))

            time = self.time.text()
            f.write('\ntime={}'.format(time))
            dt = self.dt.text()
            f.write('\ndt={}'.format(dt))
            tMax = self.tMax.text()
            f.write('\ntMax={}'.format(tMax))
            Cn = self.Cn.text()
            f.write('\nCn={}'.format(Cn))
            opInt = self.opInt.text()
            f.write('\nopInt={}'.format(opInt))
            fwInt = self.fwInt.text()
            f.write('\nfwInt={}'.format(fwInt))
            rwInt = self.rwInt.text()
            f.write('\nrwInt={}'.format(rwInt))
            FpTolerance = self.FpTolerance.text()
            f.write('\nFpTolerance={}'.format(FpTolerance))
            PoissonTolerance = self.PoissonTolerance.text()
            f.write('\nPoissonTolerance={}'.format(PoissonTolerance))
            gssorMG = self.gssorMG.text()
            f.write('\ngssorMG={}'.format(gssorMG))
            gssorWp = self.gssorWp.text()
            f.write('\ngssorWp={}'.format(gssorWp))
            gssorPp = self.gssorPP.text()
            f.write('\ngssorPp={}'.format(gssorPp))
            maxiteration = self.maxiteration.text()
            f.write('\nmaxiteration={}'.format(maxiteration))

            preSm = self.deviceNumber_5.text()
            f.write('\npreSm={}'.format(preSm))
            pstSm = self.deviceNumber_6.text()
            f.write('\npstSm={}'.format(pstSm))
            vcCnt = self.deviceNumber_7.text()
            f.write('\nvcCnt={}'.format(vcCnt))

    def retranslateUi(self, Form):                  #function to set text to elements that will be visible to user
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "parameters"))
        self.label_6.setText(_translate("Form", "pySARAS"))
        self.cupyfalse.setText(_translate("Form", "False"))
        self.label_7.setText(_translate("Form", "cupyfuse"))
        self.label_8.setText(_translate("Form", "Device"))
        self.targetgpu.setText(_translate("Form", "GPU"))
        self.probHydro.setText(_translate("Form", "Hydro"))
        self.cupytrue.setText(_translate("Form", "True"))
        self.label_9.setText(_translate("Form", "Probtype"))
        self.targetcpu.setText(_translate("Form", "CPU"))
        self.probRBC.setText(_translate("Form", "RBC"))
        self.label_10.setText(_translate("Form", "Target"))
        self.label_13.setText(_translate("Form", "flow parameters-Hydro"))
        self.label_18.setText(_translate("Form", "omega"))
        self.label_15.setText(_translate("Form", "Pr"))
        self.label_17.setText(_translate("Form", "flow parameters-RBC"))
        self.label_12.setText(_translate("Form", "nu"))
        self.label_14.setText(_translate("Form", "Ro"))
        self.label_11.setText(_translate("Form", "Ra"))
        self.label_16.setText(_translate("Form", "Ta"))
        self.label_22.setText(_translate("Form", "Domain Size"))
        self.label_2.setText(_translate("Form", "Ny"))
        self.label_24.setText(_translate("Form", "Lz"))
        self.label.setText(_translate("Form", "Nx"))
        self.label_23.setText(_translate("Form", "Ly"))
        self.label_25.setText(_translate("Form", "Lx"))
        self.label_3.setText(_translate("Form", "Nz"))
        self.ddd_2.setText(_translate("Form", "DDD"))
        self.uuu_2.setText(_translate("Form", "UUU"))
        self.uud_2.setText(_translate("Form", "UUD"))
        self.label_30.setText(_translate("Form", "Grid Type"))
        self.label_31.setText(_translate("Form", "betax"))
        self.label_32.setText(_translate("Form", "betay"))
        self.label_33.setText(_translate("Form", "betaz"))
        self.label_34.setText(_translate("Form", "Initial Conditions"))
        self.label_35.setText(_translate("Form", "ICtype"))
        self.label_46.setText(_translate("Form", "PoissonTolerance"))
        self.label_20.setText(_translate("Form", "Boundary Conditions"))
        self.label_45.setText(_translate("Form", "FpTolerance"))
        self.label_43.setText(_translate("Form", "fwInt"))
        self.restarttrue.setText(_translate("Form", "True"))
        self.label_47.setText(_translate("Form", "gssorMG"))
        self.label_38.setText(_translate("Form", "time"))
        self.label_39.setText(_translate("Form", "dt"))
        self.restartfalse.setText(_translate("Form", "False"))
        self.label_40.setText(_translate("Form", "tMax"))
        self.label_49.setText(_translate("Form", "gssorPP"))
        self.label_37.setText(_translate("Form", "restart"))
        self.label_41.setText(_translate("Form", "Cn"))
        self.label_48.setText(_translate("Form", "gssorWP"))
        self.label_44.setText(_translate("Form", "rwInt"))
        self.BCTypeNNN_2.setText(_translate("Form", "NNN"))
        self.BCTypePPN_2.setText(_translate("Form", "PPN"))
        self.BCTypePPP_2.setText(_translate("Form", "PPP"))
        self.label_21.setText(_translate("Form", "BCType"))
        self.BCTypeLDC_2.setText(_translate("Form", "LDC"))
        self.BCTypePPS_2.setText(_translate("Form", "PPS"))
        self.label_51.setText(_translate("Form", "restart_filename"))
        self.label_50.setText(_translate("Form", "maxiteration"))
        self.label_42.setText(_translate("Form", "opInt"))
        self.label_36.setText(_translate("Form", "Simulation Parameters"))
        self.label_55.setText(_translate("Form", "Multigrid Parameters"))
        self.label_56.setText(_translate("Form", "preSm"))
        self.label_57.setText(_translate("Form", "pstSm"))
        self.label_58.setText(_translate("Form", "vcCnt"))
        self.pushButton_5.setText(_translate("Form", "submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
