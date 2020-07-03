# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from activity_adder import Ui_ActivityAdder

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.add_activity = QtWidgets.QPushButton(self.centralwidget)
        self.add_activity.setGeometry(QtCore.QRect(360, 220, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.add_activity.setFont(font)
        self.add_activity.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_activity.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/trophy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_activity.setIcon(icon)
        self.add_activity.setIconSize(QtCore.QSize(50, 50))
        self.add_activity.setCheckable(True)
        self.add_activity.setChecked(False)
        self.add_activity.setAutoDefault(False)
        self.add_activity.setDefault(False)
        self.add_activity.setFlat(False)
        self.add_activity.setObjectName("add_activity")
        self.stats = QtWidgets.QPushButton(self.centralwidget)
        self.stats.setGeometry(QtCore.QRect(220, 370, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.stats.setFont(font)
        self.stats.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/stats.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stats.setIcon(icon1)
        self.stats.setIconSize(QtCore.QSize(40, 40))
        self.stats.setObjectName("stats")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(490, 370, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.settings.setFont(font)
        self.settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon2)
        self.settings.setIconSize(QtCore.QSize(40, 40))
        self.settings.setObjectName("settings")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 921, 791))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/theme1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.add_activity.raise_()
        self.stats.raise_()
        self.settings.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_activity.clicked.connect(self.open_activity_adder)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ActivityManager"))
        self.add_activity.setText(_translate("MainWindow", "ADD "))
        self.stats.setText(_translate("MainWindow", "STATISTICS"))
        self.settings.setText(_translate("MainWindow", "SETTINGS"))

    def open_activity_adder(self):
        self.ActivityAdder = QtWidgets.QMainWindow()
        self.ui = Ui_ActivityAdder()
        self.ui.setupUi(self.ActivityAdder)
        self.ActivityAdder.show()
        # self.main_window.hide()
