# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RankingParty_FlexSize.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 913)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainVert = QtWidgets.QVBoxLayout()
        self.mainVert.setSpacing(15)
        self.mainVert.setObjectName("mainVert")
        self.teamButtons = QtWidgets.QHBoxLayout()
        self.teamButtons.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.teamButtons.setObjectName("teamButtons")
        self.pb_Yellow = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Yellow.sizePolicy().hasHeightForWidth())
        self.pb_Yellow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_Yellow.setFont(font)
        self.pb_Yellow.setStyleSheet("background-color: rgb(241, 250, 55);")
        self.pb_Yellow.setCheckable(True)
        self.pb_Yellow.setChecked(True)
        self.pb_Yellow.setObjectName("pb_Yellow")
        self.teamButtons.addWidget(self.pb_Yellow)
        self.pb_Green = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Green.sizePolicy().hasHeightForWidth())
        self.pb_Green.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_Green.setFont(font)
        self.pb_Green.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.pb_Green.setCheckable(True)
        self.pb_Green.setChecked(True)
        self.pb_Green.setObjectName("pb_Green")
        self.teamButtons.addWidget(self.pb_Green)
        self.pb_Red = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Red.sizePolicy().hasHeightForWidth())
        self.pb_Red.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_Red.setFont(font)
        self.pb_Red.setStyleSheet("background-color: rgb(255, 56, 17);")
        self.pb_Red.setCheckable(True)
        self.pb_Red.setChecked(True)
        self.pb_Red.setObjectName("pb_Red")
        self.teamButtons.addWidget(self.pb_Red)
        self.pb_Blue = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Blue.sizePolicy().hasHeightForWidth())
        self.pb_Blue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_Blue.setFont(font)
        self.pb_Blue.setAutoFillBackground(False)
        self.pb_Blue.setStyleSheet("background-color: rgb(60, 70, 255);")
        self.pb_Blue.setCheckable(True)
        self.pb_Blue.setChecked(True)
        self.pb_Blue.setObjectName("pb_Blue")
        self.teamButtons.addWidget(self.pb_Blue)
        self.mainVert.addLayout(self.teamButtons)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.mainVert.addWidget(self.line)
        self.lowerLevel = QtWidgets.QHBoxLayout()
        self.lowerLevel.setObjectName("lowerLevel")
        self.amountPanel = QtWidgets.QVBoxLayout()
        self.amountPanel.setSpacing(5)
        self.amountPanel.setObjectName("amountPanel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.amountPanel.addWidget(self.label)
        self.amntBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amntBox.sizePolicy().hasHeightForWidth())
        self.amntBox.setSizePolicy(sizePolicy)
        self.amntBox.setProperty("value", 1)
        self.amntBox.setObjectName("amntBox")
        self.amountPanel.addWidget(self.amntBox)
        self.pbClearAmnt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbClearAmnt.sizePolicy().hasHeightForWidth())
        self.pbClearAmnt.setSizePolicy(sizePolicy)
        self.pbClearAmnt.setObjectName("pbClearAmnt")
        self.amountPanel.addWidget(self.pbClearAmnt)
        self.amountPanel.setStretch(0, 1)
        self.amountPanel.setStretch(1, 15)
        self.amountPanel.setStretch(2, 15)
        self.lowerLevel.addLayout(self.amountPanel)
        self.allDrinkLists = QtWidgets.QVBoxLayout()
        self.allDrinkLists.setObjectName("allDrinkLists")
        self.upperLevelDrinks = QtWidgets.QHBoxLayout()
        self.upperLevelDrinks.setSpacing(10)
        self.upperLevelDrinks.setObjectName("upperLevelDrinks")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.ginList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ginList.sizePolicy().hasHeightForWidth())
        self.ginList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.ginList.setFont(font)
        self.ginList.setObjectName("ginList")
        item = QtWidgets.QListWidgetItem()
        self.ginList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ginList.addItem(item)
        self.verticalLayout_7.addWidget(self.ginList)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 10)
        self.upperLevelDrinks.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.shotList = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.shotList.setFont(font)
        self.shotList.setObjectName("shotList")
        item = QtWidgets.QListWidgetItem()
        self.shotList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.shotList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.shotList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.shotList.addItem(item)
        self.verticalLayout_6.addWidget(self.shotList)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 10)
        self.upperLevelDrinks.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.wodkaList = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.wodkaList.setFont(font)
        self.wodkaList.setObjectName("wodkaList")
        item = QtWidgets.QListWidgetItem()
        self.wodkaList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wodkaList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wodkaList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wodkaList.addItem(item)
        self.verticalLayout_3.addWidget(self.wodkaList)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)
        self.upperLevelDrinks.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.bacardiList = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.bacardiList.setFont(font)
        self.bacardiList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.bacardiList.setObjectName("bacardiList")
        item = QtWidgets.QListWidgetItem()
        self.bacardiList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.bacardiList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.bacardiList.addItem(item)
        self.verticalLayout_4.addWidget(self.bacardiList)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.upperLevelDrinks.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.beerList = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.beerList.setFont(font)
        self.beerList.setObjectName("beerList")
        item = QtWidgets.QListWidgetItem()
        self.beerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.beerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.beerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.beerList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.beerList.addItem(item)
        self.verticalLayout_5.addWidget(self.beerList)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 10)
        self.upperLevelDrinks.addLayout(self.verticalLayout_5)
        self.allDrinkLists.addLayout(self.upperLevelDrinks)
        self.lowerLevelDrinks = QtWidgets.QHBoxLayout()
        self.lowerLevelDrinks.setSpacing(10)
        self.lowerLevelDrinks.setObjectName("lowerLevelDrinks")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_5.sizePolicy().hasHeightForWidth())
        self.listWidget_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.listWidget_5.setFont(font)
        self.listWidget_5.setObjectName("listWidget_5")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_5.addItem(item)
        self.verticalLayout_8.addWidget(self.listWidget_5)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 10)
        self.lowerLevelDrinks.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.listWidget_4.setFont(font)
        self.listWidget_4.setObjectName("listWidget_4")
        self.verticalLayout_9.addWidget(self.listWidget_4)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 10)
        self.lowerLevelDrinks.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.listWidget_3.setFont(font)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_10.addWidget(self.listWidget_3)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 10)
        self.lowerLevelDrinks.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_11.addWidget(self.listWidget_2)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 10)
        self.lowerLevelDrinks.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(17)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_12.addWidget(self.listWidget)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 10)
        self.lowerLevelDrinks.addLayout(self.verticalLayout_12)
        self.allDrinkLists.addLayout(self.lowerLevelDrinks)
        self.lowerLevel.addLayout(self.allDrinkLists)
        self.lowerLevel.setStretch(0, 5)
        self.lowerLevel.setStretch(1, 20)
        self.mainVert.addLayout(self.lowerLevel)
        self.mainVert.setStretch(0, 3)
        self.mainVert.setStretch(1, 1)
        self.mainVert.setStretch(2, 10)
        self.verticalLayout.addLayout(self.mainVert)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_Yellow.setText(_translate("MainWindow", "Yellow"))
        self.pb_Green.setText(_translate("MainWindow", "Green"))
        self.pb_Red.setText(_translate("MainWindow", "Red"))
        self.pb_Blue.setText(_translate("MainWindow", "Blue"))
        self.label.setText(_translate("MainWindow", "Amount:"))
        self.pbClearAmnt.setText(_translate("MainWindow", "Clear Amount"))
        self.label_6.setText(_translate("MainWindow", "Gin:"))
        __sortingEnabled = self.ginList.isSortingEnabled()
        self.ginList.setSortingEnabled(False)
        item = self.ginList.item(0)
        item.setText(_translate("MainWindow", "Tonic"))
        self.ginList.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "Shots:"))
        __sortingEnabled = self.shotList.isSortingEnabled()
        self.shotList.setSortingEnabled(False)
        item = self.shotList.item(0)
        item.setText(_translate("MainWindow", "Ficken"))
        item = self.shotList.item(1)
        item.setText(_translate("MainWindow", "Berliner Luft"))
        item = self.shotList.item(2)
        item.setText(_translate("MainWindow", "Pfeffi"))
        item = self.shotList.item(3)
        item.setText(_translate("MainWindow", "Klopfer"))
        self.shotList.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Wodka:"))
        __sortingEnabled = self.wodkaList.isSortingEnabled()
        self.wodkaList.setSortingEnabled(False)
        item = self.wodkaList.item(0)
        item.setText(_translate("MainWindow", "Bull"))
        item = self.wodkaList.item(1)
        item.setText(_translate("MainWindow", "Orange"))
        item = self.wodkaList.item(2)
        item.setText(_translate("MainWindow", "Brause"))
        item = self.wodkaList.item(3)
        item.setText(_translate("MainWindow", "Pur"))
        self.wodkaList.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Bacardi"))
        __sortingEnabled = self.bacardiList.isSortingEnabled()
        self.bacardiList.setSortingEnabled(False)
        item = self.bacardiList.item(0)
        item.setText(_translate("MainWindow", "Cola"))
        item = self.bacardiList.item(1)
        item.setText(_translate("MainWindow", "Orange"))
        item = self.bacardiList.item(2)
        item.setText(_translate("MainWindow", "Pur"))
        self.bacardiList.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "Beer:"))
        __sortingEnabled = self.beerList.isSortingEnabled()
        self.beerList.setSortingEnabled(False)
        item = self.beerList.item(0)
        item.setText(_translate("MainWindow", "Halbe"))
        item = self.beerList.item(1)
        item.setText(_translate("MainWindow", "Weizen"))
        item = self.beerList.item(2)
        item.setText(_translate("MainWindow", "Radler"))
        item = self.beerList.item(3)
        item.setText(_translate("MainWindow", "Stiefel"))
        item = self.beerList.item(4)
        item.setText(_translate("MainWindow", "Maß"))
        self.beerList.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Empty:"))
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        self.listWidget_5.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Empty:"))
        self.label_9.setText(_translate("MainWindow", "Empty:"))
        self.label_10.setText(_translate("MainWindow", "Empty:"))
        self.label_11.setText(_translate("MainWindow", "Empty:"))