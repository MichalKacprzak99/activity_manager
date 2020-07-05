# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activity_adder.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from datetime import datetime
from pymongo import MongoClient
from PyQt5 import QtCore, QtWidgets
root = MongoClient("localhost", 27017)
activity_adder_db = root['activity_adder_db']
user_activities = activity_adder_db['user_activities']
settings = activity_adder_db['settings']
class Ui_ActivityAdder(object):
    def setupUi(self, ActivityAdder, MainWindow):
        self.activity_adder = ActivityAdder
        self.main_window = MainWindow

        ActivityAdder.setObjectName("ActivityAdder")
        ActivityAdder.resize(800, 800)

        self.centralwidget = QtWidgets.QWidget(ActivityAdder)
        self.centralwidget.setObjectName("centralwidget")

        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(20, 680, 93, 28))
        self.cancel_button.setObjectName("cancel")

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(640, 680, 93, 28))
        self.save_button.setObjectName("save_button")

        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(200, 0, 392, 236))
        self.calendar.setObjectName("calendar")

        self.summary_text_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.summary_text_input.setGeometry(QtCore.QRect(220, 520, 351, 91))
        self.summary_text_input.setObjectName("summary_text_input")

        self.duration_setter = QtWidgets.QSpinBox(self.centralwidget)
        self.duration_setter.setGeometry(QtCore.QRect(490, 350, 48, 22))
        self.duration_setter.setMaximum(300)
        self.duration_setter.setObjectName("duration_setter")

        self.activity_grade = QtWidgets.QSpinBox(self.centralwidget)
        self.activity_grade.setGeometry(QtCore.QRect(490, 390, 48, 22))
        self.activity_grade.setMaximum(10)
        self.activity_grade.setObjectName("duration_setter")

        self.distance_setter = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.distance_setter.setGeometry(QtCore.QRect(490, 440, 48, 22))
        self.distance_setter.setMaximum(300)
        self.distance_setter.setObjectName("duration_setter")

        self.activity_box = QtWidgets.QComboBox(self.centralwidget)
        self.activity_box.setGeometry(QtCore.QRect(470, 300, 73, 22))
        self.activity_box.setObjectName("activity_box")
        self.activity_box.addItems([new_set['activity'] for new_set in settings.find({})])
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 300, 171, 20))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 350, 171, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 480, 171, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 440, 171, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 390, 171, 20))
        self.label_5.setObjectName("label_4")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        ActivityAdder.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(ActivityAdder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ActivityAdder.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(ActivityAdder)
        self.statusbar.setObjectName("statusbar")
        ActivityAdder.setStatusBar(self.statusbar)

        self.retranslateUi(ActivityAdder)
        QtCore.QMetaObject.connectSlotsByName(ActivityAdder)

        self.cancel_button.clicked.connect(self.to_main_menu)
        self.save_button.clicked.connect(self.save)

    def retranslateUi(self, ActivityAdder):
        _translate = QtCore.QCoreApplication.translate
        ActivityAdder.setWindowTitle(_translate("ActivityAdder", "MainWindow"))
        self.cancel_button.setText(_translate("ActivityAdder", "Cancel"))
        self.save_button.setText(_translate("ActivityAdder", "Save"))
        self.label.setText(_translate("ActivityAdder", "What was your daily activity?"))
        self.label_2.setText(_translate("ActivityAdder", "What was a duration?[min]"))
        self.label_4.setText(_translate("ActivityAdder", "What was a distance?[km]"))
        self.label_3.setText(_translate("ActivityAdder", "Summary"))
        self.label_5.setText(_translate("ActivityAdder", "Grade(0-10)"))

    def to_main_menu(self):
        self.activity_adder.close()
        self.main_window.show()

    def save(self):
        time = self.calendar.selectedDate().toPyDate()
        activity = {
            "time": datetime(time.year, time.month, time.day),
            "activity": self.activity_box.currentText(),
            "duration": self.duration_setter.value(),
            "grade": self.activity_grade.value(),
            "distance": self.distance_setter.value(),
            "summary": self.summary_text_input.toPlainText()
        }
        user_activities.insert_one(activity)
        self.to_main_menu()