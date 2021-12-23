# -*- coding: utf-8 -*-
import datetime as dt
import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets, QtGui  # uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Школьное Расписание")
        MainWindow.resize(1000, 840)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.rasp = QtWidgets.QWidget()
        self.rasp.setObjectName("rasp")
        self.gridLayout = QtWidgets.QGridLayout(self.rasp)
        self.gridLayout.setObjectName("gridLayout")
        self.Tuesday = QtWidgets.QWidget(self.rasp)
        self.Tuesday.setMinimumSize(QtCore.QSize(240, 370))
        self.Tuesday.setObjectName("Tuesday")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Tuesday)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Tue = QtWidgets.QLabel(self.Tuesday)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Tue.setFont(font)
        self.Tue.setStyleSheet("QLable { font-size: 14px; }")
        self.Tue.setAlignment(QtCore.Qt.AlignCenter)
        self.Tue.setObjectName("Tue")
        self.verticalLayout_8.addWidget(self.Tue)
        self.Tue_school = QtWidgets.QTableWidget(self.Tuesday)
        self.Tue_school.setMinimumSize(QtCore.QSize(0, 242))
        self.Tue_school.setMaximumSize(QtCore.QSize(16777215, 242))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tue_school.setFont(font)
        self.Tue_school.setObjectName("Tue_school")
        self.Tue_school.setColumnCount(0)
        self.Tue_school.setRowCount(0)
        self.verticalLayout_8.addWidget(self.Tue_school)
        self.Tue_note = QtWidgets.QTableWidget(self.Tuesday)
        self.Tue_note.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Tue_note.setObjectName("Tue_note")
        self.Tue_note.setColumnCount(0)
        self.Tue_note.setRowCount(0)
        self.verticalLayout_8.addWidget(self.Tue_note)
        self.gridLayout.addWidget(self.Tuesday, 0, 1, 1, 1)
        self.Wednesday = QtWidgets.QWidget(self.rasp)
        self.Wednesday.setMinimumSize(QtCore.QSize(240, 370))
        self.Wednesday.setObjectName("Wednesday")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Wednesday)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Wed = QtWidgets.QLabel(self.Wednesday)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Wed.setFont(font)
        self.Wed.setStyleSheet("QLable { font-size: 14px; }")
        self.Wed.setAlignment(QtCore.Qt.AlignCenter)
        self.Wed.setObjectName("Wed")
        self.verticalLayout_9.addWidget(self.Wed)
        self.Wed_school = QtWidgets.QTableWidget(self.Wednesday)
        self.Wed_school.setMinimumSize(QtCore.QSize(0, 242))
        self.Wed_school.setMaximumSize(QtCore.QSize(16777215, 242))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Wed_school.setFont(font)
        self.Wed_school.setObjectName("Wed_school")
        self.Wed_school.setColumnCount(0)
        self.Wed_school.setRowCount(0)
        self.verticalLayout_9.addWidget(self.Wed_school)
        self.Wed_note = QtWidgets.QTableWidget(self.Wednesday)
        self.Wed_note.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Wed_note.setObjectName("Wed_note")
        self.Wed_note.setColumnCount(0)
        self.Wed_note.setRowCount(0)
        self.verticalLayout_9.addWidget(self.Wed_note)
        self.gridLayout.addWidget(self.Wednesday, 0, 2, 1, 1)
        self.Thursday = QtWidgets.QWidget(self.rasp)
        self.Thursday.setMinimumSize(QtCore.QSize(240, 370))
        self.Thursday.setObjectName("Thursday")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Thursday)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Thu = QtWidgets.QLabel(self.Thursday)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Thu.setFont(font)
        self.Thu.setStyleSheet("QLable { font-size: 14px; }")
        self.Thu.setAlignment(QtCore.Qt.AlignCenter)
        self.Thu.setObjectName("Thu")
        self.verticalLayout_10.addWidget(self.Thu)
        self.Thu_school = QtWidgets.QTableWidget(self.Thursday)
        self.Thu_school.setMinimumSize(QtCore.QSize(0, 242))
        self.Thu_school.setMaximumSize(QtCore.QSize(16777215, 242))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Thu_school.setFont(font)
        self.Thu_school.setObjectName("Thu_school")
        self.Thu_school.setColumnCount(0)
        self.Thu_school.setRowCount(0)
        self.verticalLayout_10.addWidget(self.Thu_school)
        self.Thu_note = QtWidgets.QTableWidget(self.Thursday)
        self.Thu_note.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Thu_note.setObjectName("Thu_note")
        self.Thu_note.setColumnCount(0)
        self.Thu_note.setRowCount(0)
        self.verticalLayout_10.addWidget(self.Thu_note)
        self.gridLayout.addWidget(self.Thursday, 2, 0, 1, 1)
        self.Saturday = QtWidgets.QWidget(self.rasp)
        self.Saturday.setMinimumSize(QtCore.QSize(240, 370))
        self.Saturday.setObjectName("Saturday")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Saturday)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Sat = QtWidgets.QLabel(self.Saturday)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Sat.setFont(font)
        self.Sat.setStyleSheet("QLable { font-size: 14px; }")
        self.Sat.setAlignment(QtCore.Qt.AlignCenter)
        self.Sat.setObjectName("Sat")
        self.verticalLayout_12.addWidget(self.Sat)
        self.Sat_school = QtWidgets.QTableWidget(self.Saturday)
        self.Sat_school.setMinimumSize(QtCore.QSize(0, 242))
        self.Sat_school.setMaximumSize(QtCore.QSize(16777215, 242))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sat_school.setFont(font)
        self.Sat_school.setObjectName("Sat_school")
        self.Sat_school.setColumnCount(0)
        self.Sat_school.setRowCount(0)
        self.verticalLayout_12.addWidget(self.Sat_school)
        self.Sat_note = QtWidgets.QTableWidget(self.Saturday)
        self.Sat_note.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Sat_note.setObjectName("Sat_note")
        self.Sat_note.setColumnCount(0)
        self.Sat_note.setRowCount(0)
        self.verticalLayout_12.addWidget(self.Sat_note)
        self.gridLayout.addWidget(self.Saturday, 2, 2, 1, 1)
        self.Monday = QtWidgets.QWidget(self.rasp)
        self.Monday.setMinimumSize(QtCore.QSize(240, 370))
        self.Monday.setObjectName("Monday")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Monday)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Mon = QtWidgets.QLabel(self.Monday)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Mon.setFont(font)
        self.Mon.setStyleSheet("QLable { font-size: 14px; }")
        self.Mon.setAlignment(QtCore.Qt.AlignCenter)
        self.Mon.setObjectName("Mon")
        self.verticalLayout_7.addWidget(self.Mon)
        self.Mon_school = QtWidgets.QTableWidget(self.Monday)
        self.Mon_school.setMinimumSize(QtCore.QSize(0, 242))
        self.Mon_school.setMaximumSize(QtCore.QSize(16777215, 242))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Mon_school.setFont(font)
        self.Mon_school.setShowGrid(True)
        self.Mon_school.setGridStyle(QtCore.Qt.SolidLine)
        self.Mon_school.setWordWrap(True)
        self.Mon_school.setCornerButtonEnabled(True)
        self.Mon_school.setObjectName("Mon_school")
        self.Mon_school.setColumnCount(0)
        self.Mon_school.setRowCount(0)
        self.verticalLayout_7.addWidget(self.Mon_school)
        self.Mon_note = QtWidgets.QTableWidget(self.Monday)
        self.Mon_note.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Mon_note.setBaseSize(QtCore.QSize(0, 0))
        self.Mon_note.setObjectName("Mon_note")
        self.Mon_note.setColumnCount(0)
        self.Mon_note.setRowCount(0)
        self.verticalLayout_7.addWidget(self.Mon_note)
        self.gridLayout.addWidget(self.Monday, 0, 0, 1, 1)
        self.Check_Obj = QtWidgets.QWidget(self.rasp)
        self.Check_Obj.setMinimumSize(QtCore.QSize(190, 0))
        self.Check_Obj.setObjectName("Check_Obj")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Check_Obj)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fake2 = QtWidgets.QWidget(self.Check_Obj)
        self.fake2.setObjectName("fake2")
        self.verticalLayout.addWidget(self.fake2)
        self.Check = QtWidgets.QGroupBox(self.Check_Obj)
        self.Check.setMinimumSize(QtCore.QSize(0, 0))
        self.Check.setMaximumSize(QtCore.QSize(16777215, 210))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Check.setFont(font)
        self.Check.setAlignment(QtCore.Qt.AlignCenter)
        self.Check.setObjectName("Check")
        self.Check.setTitle("Предмет")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Check)
        self.verticalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.choose_obj4 = QtWidgets.QComboBox(self.Check)
        self.choose_obj4.setMinimumSize(QtCore.QSize(0, 32))
        self.choose_obj4.setObjectName("choose_obj4")
        self.verticalLayout_18.addWidget(self.choose_obj4)
        self.check_but1 = QtWidgets.QPushButton(self.Check)
        self.check_but1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.check_but1.setFont(font)
        self.check_but1.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.check_but1.setObjectName("check_but1")
        self.verticalLayout_18.addWidget(self.check_but1)
        self.check_but2 = QtWidgets.QPushButton(self.Check)
        self.check_but2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.check_but2.setFont(font)
        self.check_but2.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.check_but2.setObjectName("check_but2")
        self.verticalLayout_18.addWidget(self.check_but2)
        self.check_but3 = QtWidgets.QPushButton(self.Check)
        self.check_but3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.check_but3.setFont(font)
        self.check_but3.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.check_but3.setObjectName("check_but3")
        self.verticalLayout_18.addWidget(self.check_but3)
        self.verticalLayout.addWidget(self.Check)
        self.gridLayout.addWidget(self.Check_Obj, 2, 3, 1, 1)
        self.Friday = QtWidgets.QWidget(self.rasp)
        self.Friday.setMinimumSize(QtCore.QSize(240, 370))
        self.Friday.setObjectName("Friday")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Friday)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Fri = QtWidgets.QLabel(self.Friday)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Fri.setFont(font)
        self.Fri.setStyleSheet("QLable { font-size: 14px; }")
        self.Fri.setAlignment(QtCore.Qt.AlignCenter)
        self.Fri.setObjectName("Fri")
        self.verticalLayout_11.addWidget(self.Fri)
        self.Fri_school = QtWidgets.QTableWidget(self.Friday)
        self.Fri_school.setMinimumSize(QtCore.QSize(0, 242))
        self.Fri_school.setMaximumSize(QtCore.QSize(16777215, 242))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fri_school.setFont(font)
        self.Fri_school.setObjectName("Fri_school")
        self.Fri_school.setColumnCount(0)
        self.Fri_school.setRowCount(0)
        self.verticalLayout_11.addWidget(self.Fri_school)
        self.Fri_note = QtWidgets.QTableWidget(self.Friday)
        self.Fri_note.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Fri_note.setObjectName("Fri_note")
        self.Fri_note.setColumnCount(0)
        self.Fri_note.setRowCount(0)
        self.verticalLayout_11.addWidget(self.Fri_note)
        self.gridLayout.addWidget(self.Friday, 2, 1, 1, 1)
        self.AToolBars = QtWidgets.QWidget(self.rasp)
        self.AToolBars.setMinimumSize(QtCore.QSize(190, 0))
        self.AToolBars.setMaximumSize(QtCore.QSize(190, 16777215))
        self.AToolBars.setObjectName("AToolBars")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.AToolBars)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Toolbar1 = QtWidgets.QTabWidget(self.AToolBars)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Toolbar1.setFont(font)
        self.Toolbar1.setObjectName("Toolbar1")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Add)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.combo1 = QtWidgets.QWidget(self.Add)
        self.combo1.setMinimumSize(QtCore.QSize(148, 30))
        self.combo1.setObjectName("combo1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.combo1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.weekday1 = QtWidgets.QComboBox(self.combo1)
        self.weekday1.setMinimumSize(QtCore.QSize(69, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weekday1.setFont(font)
        self.weekday1.setObjectName("weekday1")
        for i in ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб"]:
            self.weekday1.addItem(i)
        self.horizontalLayout.addWidget(self.weekday1)
        self.object1 = QtWidgets.QComboBox(self.combo1)
        self.object1.setMinimumSize(QtCore.QSize(69, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.object1.setFont(font)
        self.object1.setObjectName("object1")
        for i in range(9):
            if i:
                self.object1.addItem(str(i))
            else:
                self.object1.addItem("След.")
        self.horizontalLayout.addWidget(self.object1)
        self.verticalLayout_5.addWidget(self.combo1)
        self.add_line = QtWidgets.QLineEdit(self.Add)
        self.add_line.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_line.setFont(font)
        self.add_line.setObjectName("add_line")
        self.verticalLayout_5.addWidget(self.add_line)
        self.choose_obj1 = QtWidgets.QComboBox(self.Add)
        self.choose_obj1.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choose_obj1.setFont(font)
        self.choose_obj1.setObjectName("choose_obj1")
        self.verticalLayout_5.addWidget(self.choose_obj1)
        self.add_but = QtWidgets.QPushButton(self.Add)
        self.add_but.setMinimumSize(QtCore.QSize(0, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.add_but.setFont(font)
        self.add_but.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white;\n"
"    box-shadow: 0 0 10px rgb(0, 0, 0);\\n\n"
"    transition: all 1s;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.add_but.setObjectName("add_but")
        self.verticalLayout_5.addWidget(self.add_but)
        self.Toolbar1.addTab(self.Add, "")
        self.Del = QtWidgets.QWidget()
        self.Del.setObjectName("Del")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Del)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.choose_obj3 = QtWidgets.QComboBox(self.Del)
        self.choose_obj3.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choose_obj3.setFont(font)
        self.choose_obj3.setObjectName("choose_obj3")
        self.verticalLayout_14.addWidget(self.choose_obj3)
        self.fake1 = QtWidgets.QWidget(self.Del)
        self.fake1.setObjectName("fake1")
        self.verticalLayout_14.addWidget(self.fake1)
        self.del_but = QtWidgets.QPushButton(self.Del)
        self.del_but.setMinimumSize(QtCore.QSize(0, 37))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.del_but.setFont(font)
        self.del_but.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.del_but.setObjectName("del_but")
        self.verticalLayout_14.addWidget(self.del_but)
        self.Toolbar1.addTab(self.Del, "")
        self.verticalLayout_4.addWidget(self.Toolbar1)
        self.Toolbar2 = QtWidgets.QTabWidget(self.AToolBars)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Toolbar2.setFont(font)
        self.Toolbar2.setObjectName("Toolbar2")
        self.Upd = QtWidgets.QWidget()
        self.Upd.setObjectName("Upd")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.Upd)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.choose_obj2 = QtWidgets.QComboBox(self.Upd)
        self.choose_obj2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choose_obj2.setFont(font)
        self.choose_obj2.setObjectName("choose_obj2")
        self.verticalLayout_15.addWidget(self.choose_obj2)
        self.upd_line = QtWidgets.QLineEdit(self.Upd)
        self.upd_line.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.upd_line.setFont(font)
        self.upd_line.setObjectName("upd_line")
        self.verticalLayout_15.addWidget(self.upd_line)
        self.upd_but = QtWidgets.QPushButton(self.Upd)
        self.upd_but.setMinimumSize(QtCore.QSize(0, 40))
        self.upd_but.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.upd_but.setFont(font)
        self.upd_but.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.upd_but.setObjectName("upd_but")
        self.verticalLayout_15.addWidget(self.upd_but)
        self.Toolbar2.addTab(self.Upd, "")
        self.Clear = QtWidgets.QWidget()
        self.Clear.setObjectName("Clear")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.Clear)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.weekday3 = QtWidgets.QComboBox(self.Clear)
        self.weekday3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.weekday3.setFont(font)
        self.weekday3.setObjectName("weekday3")
        for i in ["Везде", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"]:
            self.weekday3.addItem(i)
        self.verticalLayout_16.addWidget(self.weekday3)
        self.object3 = QtWidgets.QComboBox(self.Clear)
        self.object3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.object3.setFont(font)
        self.object3.setObjectName("object3")
        for i in range(9):
            if i:
                self.object3.addItem(str(i))
            else:
                self.object3.addItem("Все")
        self.verticalLayout_16.addWidget(self.object3)
        self.clear_but = QtWidgets.QPushButton(self.Clear)
        self.clear_but.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.clear_but.setFont(font)
        self.clear_but.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.clear_but.setObjectName("clear_but")
        self.verticalLayout_16.addWidget(self.clear_but)
        self.Toolbar2.addTab(self.Clear, "")
        self.verticalLayout_4.addWidget(self.Toolbar2)
        self.gridLayout.addWidget(self.AToolBars, 0, 3, 1, 1)
        self.Saturday.raise_()
        self.Friday.raise_()
        self.Thursday.raise_()
        self.Wednesday.raise_()
        self.Tuesday.raise_()
        self.Monday.raise_()
        self.Check_Obj.raise_()
        self.AToolBars.raise_()
        self.tabWidget.addTab(self.rasp, "")
        self.note = QtWidgets.QWidget()
        self.note.setObjectName("note")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.note)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.note)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 260))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(16777215, 260))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Show = QtWidgets.QWidget()
        self.Show.setObjectName("Show")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Show)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_3 = QtWidgets.QWidget(self.Show)
        self.widget_3.setMinimumSize(QtCore.QSize(231, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(231, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.showing = QtWidgets.QPushButton(self.widget_3)
        self.showing.setMinimumSize(QtCore.QSize(211, 51))
        self.showing.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.showing.setFont(font)
        self.showing.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.showing.setObjectName("showing")
        self.verticalLayout_20.addWidget(self.showing)
        self.fake9 = QtWidgets.QWidget(self.widget_3)
        self.fake9.setObjectName("fake9")
        self.verticalLayout_20.addWidget(self.fake9)
        self.horizontalLayout_6.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.Show)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.choosedate = QtWidgets.QComboBox(self.widget_5)
        self.choosedate.setMinimumSize(QtCore.QSize(0, 51))
        self.choosedate.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.choosedate.setFont(font)
        self.choosedate.setObjectName("choosedate")
        for i in ["За всё время", "На месяц", "На неделю"]:
            self.choosedate.addItem(i)
        self.verticalLayout_21.addWidget(self.choosedate)
        self.fake10 = QtWidgets.QWidget(self.widget_5)
        self.fake10.setObjectName("fake10")
        self.verticalLayout_21.addWidget(self.fake10)
        self.horizontalLayout_6.addWidget(self.widget_5)
        self.tabWidget_2.addTab(self.Show, "")
        self.Doing = QtWidgets.QWidget()
        self.Doing.setObjectName("Doing")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Doing)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.Doing)
        self.widget_2.setMinimumSize(QtCore.QSize(231, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(231, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.complete = QtWidgets.QPushButton(self.widget_2)
        self.complete.setMinimumSize(QtCore.QSize(211, 51))
        self.complete.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.complete.setFont(font)
        self.complete.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.complete.setObjectName("complete")
        self.verticalLayout_13.addWidget(self.complete)
        self.fake4 = QtWidgets.QWidget(self.widget_2)
        self.fake4.setObjectName("fake4")
        self.verticalLayout_13.addWidget(self.fake4)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.Doing)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.choose = QtWidgets.QComboBox(self.widget_4)
        self.choose.setMinimumSize(QtCore.QSize(0, 51))
        self.choose.setMaximumSize(QtCore.QSize(16777215, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose.setFont(font)
        self.choose.setObjectName("choose")
        self.verticalLayout_17.addWidget(self.choose)
        self.fake6 = QtWidgets.QWidget(self.widget_4)
        self.fake6.setObjectName("fake6")
        self.verticalLayout_17.addWidget(self.fake6)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.tabWidget_2.addTab(self.Doing, "")
        self.Adding = QtWidgets.QWidget()
        self.Adding.setObjectName("Adding")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Adding)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.default2 = QtWidgets.QWidget(self.Adding)
        self.default2.setMinimumSize(QtCore.QSize(231, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.default2.setFont(font)
        self.default2.setObjectName("default2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.default2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.added = QtWidgets.QPushButton(self.default2)
        self.added.setMinimumSize(QtCore.QSize(211, 51))
        self.added.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.added.setFont(font)
        self.added.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.added.setObjectName("added")
        self.verticalLayout_3.addWidget(self.added)
        self.date_1 = QtWidgets.QDateTimeEdit(self.default2)
        self.date_1.setMinimumSize(QtCore.QSize(211, 51))
        self.date_1.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.date_1.setFont(font)
        self.date_1.setAlignment(QtCore.Qt.AlignCenter)
        self.date_1.setObjectName("date_1")
        self.verticalLayout_3.addWidget(self.date_1)
        self.fake7 = QtWidgets.QWidget(self.default2)
        self.fake7.setObjectName("fake7")
        self.verticalLayout_3.addWidget(self.fake7)
        self.horizontalLayout_5.addWidget(self.default2)
        self.write = QtWidgets.QPlainTextEdit(self.Adding)
        self.write.setObjectName("write")
        self.horizontalLayout_5.addWidget(self.write)
        self.tabWidget_2.addTab(self.Adding, "")
        self.Upating = QtWidgets.QWidget()
        self.Upating.setObjectName("Upating")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Upating)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.default3 = QtWidgets.QWidget(self.Upating)
        self.default3.setMinimumSize(QtCore.QSize(231, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.default3.setFont(font)
        self.default3.setObjectName("default3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.default3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.demonstr = QtWidgets.QPushButton(self.default3)
        self.demonstr.setMinimumSize(QtCore.QSize(211, 51))
        self.demonstr.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.demonstr.setFont(font)
        self.demonstr.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.demonstr.setObjectName("demonstr")
        self.verticalLayout_19.addWidget(self.demonstr)
        self.choose_2 = QtWidgets.QComboBox(self.default3)
        self.choose_2.setMinimumSize(QtCore.QSize(211, 51))
        self.choose_2.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.choose_2.setFont(font)
        self.choose_2.setObjectName("choose_2")
        self.verticalLayout_19.addWidget(self.choose_2)
        self.date_2 = QtWidgets.QDateTimeEdit(self.default3)
        self.date_2.setMinimumSize(QtCore.QSize(211, 51))
        self.date_2.setMaximumSize(QtCore.QSize(211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.date_2.setFont(font)
        self.date_2.setAlignment(QtCore.Qt.AlignCenter)
        self.date_2.setObjectName("date_2")
        self.verticalLayout_19.addWidget(self.date_2)
        self.fake8 = QtWidgets.QWidget(self.default3)
        self.fake8.setObjectName("fake8")
        self.verticalLayout_19.addWidget(self.fake8)
        self.horizontalLayout_4.addWidget(self.default3)
        self.write_2 = QtWidgets.QPlainTextEdit(self.Upating)
        self.write_2.setObjectName("write_2")
        self.horizontalLayout_4.addWidget(self.write_2)
        self.default4 = QtWidgets.QWidget(self.Upating)
        self.default4.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.default4.setFont(font)
        self.default4.setObjectName("default4")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.default4)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.fake11 = QtWidgets.QWidget(self.default4)
        self.fake11.setObjectName("fake11")
        self.verticalLayout_22.addWidget(self.fake11)
        self.updat = QtWidgets.QPushButton(self.default4)
        self.updat.setMinimumSize(QtCore.QSize(140, 51))
        self.updat.setMaximumSize(QtCore.QSize(140, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.updat.setFont(font)
        self.updat.setStyleSheet("QPushButton {\n"
"    padding:10px;\n"
"    color: #fffff;\n"
"    font-size: 18px;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #3873d9;\n"
"    background-color: white; }\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(171, 211, 247);\n"
"    effect = QtWidgets.QGraphicsDropShadowEffect(QPushButton)\n"
"    effect.setOffset(0, 0)\n"
"    effect.setBlurRadius(20)\n"
"    effect.setColor(QColor(57, 219, 255))\n"
"    QPushButton.setGraphicsEffect(effect)\n"
"}")
        self.updat.setObjectName("updat")
        self.verticalLayout_22.addWidget(self.updat)
        self.horizontalLayout_4.addWidget(self.default4)
        self.tabWidget_2.addTab(self.Upating, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        self.maintable = QtWidgets.QTableWidget(self.note)
        self.maintable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.maintable.setFont(font)
        self.maintable.setObjectName("maintable")
        self.maintable.setColumnCount(0)
        self.maintable.setRowCount(0)
        self.gridLayout_2.addWidget(self.maintable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.note, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_Sig_in = QtWidgets.QAction(MainWindow)
        self.action_Sig_in.setObjectName("action_Sig_in")
        self.action_Sign_in = QtWidgets.QAction(MainWindow)
        self.action_Sign_in.setObjectName("action_Sign_in")
        self.file = QtWidgets.QAction(MainWindow)
        self.file.setObjectName("file")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Toolbar1.setCurrentIndex(0)
        self.Toolbar2.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Дневник"))
        MainWindow.setWindowIcon(QtGui.QIcon('image.ico'))
        data = [[self.Tue, "Вторник"], [self.Wed, "Среда"], [self.Thu, "Четверг"], [self.Sat, "Суббота"],
                [self.Mon, "Понедельник"], [self.check_but1, "Выделить"], [self.check_but2, "Отменить"],
                [self.check_but3, "Очистить"], [self.Fri, "Пятница"], [self.add_but, "Обновить"],
                [self.del_but, "Удалить"], [self.upd_but, "Изменить"], [self.clear_but, "Убрать"],
                [self.showing, "Показать"], [self.complete, "Выполнить"], [self.added, "Добавить"],
                [self.demonstr, "Показать"], [self.updat, "Обновить"]]

        for x, tx in data:
            x.setText(_translate("MainWindow", tx))

        self.Toolbar1.setTabText(self.Toolbar1.indexOf(self.Add), _translate("MainWindow", "Добавить"))
        self.Toolbar1.setTabText(self.Toolbar1.indexOf(self.Del), _translate("MainWindow", "Удалить"))
        self.Toolbar2.setTabText(self.Toolbar2.indexOf(self.Upd), _translate("MainWindow", "Изменить"))
        self.Toolbar2.setTabText(self.Toolbar2.indexOf(self.Clear), _translate("MainWindow", "Убрать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rasp), _translate("MainWindow", "Расписание"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Show), _translate("MainWindow", "Показать"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Doing), _translate("MainWindow", "Сделать"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Adding), _translate("MainWindow", "Добавить"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Upating), _translate("MainWindow", "Редактрировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.note), _translate("MainWindow", "Заметки"))


# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # uic.loadUi('rasp.ui', self)
        self.connection = sqlite3.connect("table.db")
        self.cursor = self.connection.cursor()

        # РАСПИСАНИЕ
        self.add_but.clicked.connect(self.add)  # ДОБАВЛЕНИЕ
        self.upd_but.clicked.connect(self.upd)  # ИЗМЕНЕНИЕ
        self.clear_but.clicked.connect(self.clear)  # УБИРАНИЕ
        self.del_but.clicked.connect(self.delete)  # УДАЛЕНИЕ

        self.check_but1.clicked.connect(self.check)  # ВЫДЕЛЕНИЕ
        self.check_but2.clicked.connect(self.check)
        self.check_but3.clicked.connect(self.check)

        # ЗАМЕТКИ
        self.showing.clicked.connect(self.show_note)  # ПОКАЗАТЬ
        self.complete.clicked.connect(self.check_note)  # ВЫПОЛНИТЬ
        self.added.clicked.connect(self.add_note)  # ДОБАВЛЕНИЕ
        self.demonstr.clicked.connect(self.update_note)  # РЕДАКТИРОВАТЬ
        self.updat.clicked.connect(self.update_note)

        # ДАННЫЕ ТАБЛИЦЫ
        self.table_rasp()
        self.table_note()
        self.table_note_date()

    def table_rasp(self):
        try:
            # РАСПИСАНИЕ
            with self.connection:
                all_day = self.cursor.execute("SELECT * FROM timetable").fetchall()
            tables = [self.Mon_school, self.Tue_school, self.Wed_school,
                      self.Thu_school, self.Fri_school, self.Sat_school]

            for day in tables:
                weekday, subjects = all_day[tables.index(day)], []
                for i in range(10):
                    if i > 1:
                        if weekday[i]:
                            obj = self.cursor.execute(f"SELECT name FROM "
                                                      f"lessons WHERE `id` = {weekday[i]}").fetchone()[0]
                        else:
                            obj = ""
                        subjects.append((obj, ))
                day.setColumnCount(1)
                day.horizontalHeader().setVisible(False)
                day.setRowCount(0)

                for i, row in enumerate(subjects):
                    day.setRowCount(day.rowCount() + 1)
                    for j, elem in enumerate(row):
                        day.setItem(i, j, QTableWidgetItem(elem))
                day.horizontalHeader().setStretchLastSection(True)

            # ЗАПОЛНЕНИЕ ВЫПАДАЮЩИХ СПИСКОВ ADD / UPD / DEL / CHECK
            try:
                with self.connection:
                    lessons = self.cursor.execute('SELECT `name` FROM `lessons`').fetchall()
                lessons = [i[0] for i in lessons]
                for choose_obj in [self.choose_obj1, self.choose_obj2, self.choose_obj3, self.choose_obj4]:
                    choose_obj.clear()
                    if choose_obj == self.choose_obj1:
                        choose_obj.insertItem(0, "Новый предмет")
                        choose_obj.insertItems(1, lessons)
                    else:
                        choose_obj.insertItems(0, lessons)
            except Exception:
                pass

            # ЗАМЕТКИ ПОД РАСПИСАНИЕМ
            with self.connection:
                note = self.cursor.execute("SELECT `date`, `day`, `note` FROM notes").fetchall()
            notes = [self.Mon_note, self.Tue_note, self.Wed_note, self.Thu_note, self.Fri_note, self.Sat_note]

            # СОРТИРОВКА ДАТ
            note = [[dt.datetime.strptime(dat, "%H:%M %d.%m.%Y"), d, nt] for dat, d, nt in note]
            note.sort()
            note = [[dt.datetime.strftime(dat, "%d.%m %H:%M "), d, nt] for dat, d, nt in note]

            week = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
            for i in note:
                if i[1] != 6:
                    week[i[1]].append((i[0], i[2]))

            for write in notes:
                write.setColumnCount(2)
                write.setRowCount(0)
                write.setHorizontalHeaderLabels(["Дата", "Заметка"])
                header = write.horizontalHeader()
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

                for i, row in enumerate(week[notes.index(write)]):
                    write.setRowCount(write.rowCount() + 1)
                    for j, elem in enumerate(row):
                        write.setItem(i, j, QTableWidgetItem(str(elem)))
                write.horizontalHeader().setStretchLastSection(True)

        except Exception:
            QMessageBox.about(self, 'Ошибка!', "Таблица данных не найдена!")

    def table_note(self):
        try:
            # ЗАПОЛНЕНИЕ ВЫПАДАЮЩИХ СПИСКОВ CHOOSE 1 / 2
            try:
                with self.connection:
                    notes = self.cursor.execute('SELECT `date`, `note` FROM `notes`').fetchall()

                # СОРТИРОВКА ДАТ
                notes = [[dt.datetime.strptime(dat, "%H:%M %d.%m.%Y"), nt] for dat, nt in notes]
                notes.sort()
                notes = [nt for dat, nt in notes]

                notes = [f"{i + 1}. {nt}" for i, nt in enumerate(notes)]
                for choose_obj in [self.choose, self.choose_2]:
                    choose_obj.clear()
                    choose_obj.insertItems(0, notes)
            except Exception:
                pass

            # ВСЕ ЗАМЕТКИ
            with self.connection:
                note = self.cursor.execute("SELECT `date`, `note` FROM notes").fetchall()

            # СОРТИРОВКА ДАТ
            note = [[dt.datetime.strptime(dat, "%H:%M %d.%m.%Y"), nt] for dat, nt in note]
            note.sort()
            note = [[dt.datetime.strftime(dat, "%d.%m.%Y %H:%M "), nt] for dat, nt in note]

            maintable = self.maintable
            maintable.setColumnCount(2)
            maintable.setRowCount(0)
            maintable.setHorizontalHeaderLabels(["Дата", "Заметка"])
            header = maintable.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            for i, row in enumerate(note):
                maintable.setRowCount(maintable.rowCount() + 1)
                for j, elem in enumerate(row):
                    maintable.setItem(i, j, QTableWidgetItem(str(elem)))
            maintable.horizontalHeader().setStretchLastSection(True)
        except Exception:
            QMessageBox.about(self, 'Ошибка!', "Таблица данных не найдена!")

    def table_note_date(self):
        try:
            # НАСТРОЙКА ДИСПЛЕЕВ ДАТ
            now = QtCore.QDateTime.currentDateTime()
            for date in [self.date_1, self.date_2]:
                date.setDateTime(now)
                date.setDateRange(QtCore.QDate.currentDate().addDays(-365), QtCore.QDate.currentDate().addDays(365))
                date.setDisplayFormat("HH:mm dd.MM.yyyy")
        except Exception:
            QMessageBox.about(self, 'Ошибка!', "Неудалось вывести указанное время!")

    # РАСПИСАНИЕ
    def add(self):
        day = self.weekday1.currentIndex()
        obj = self.object1.currentIndex()
        txt1 = self.add_line.text()
        txt2 = self.choose_obj1.currentText()
        if txt1 or txt2 != "Новый предмет":
            with self.connection:
                lessons = self.cursor.execute('SELECT `name` FROM `lessons`').fetchall()
            lessons = [i[0] for i in lessons]
            if txt1:
                if txt1 not in lessons:
                    with self.connection:
                        self.cursor.execute(f"INSERT INTO `lessons` (`name`) VALUES(?)", (txt1,))
                        lessons = self.cursor.execute('SELECT `name` FROM `lessons`').fetchall()
                    lessons = [i[0] for i in lessons]
                with self.connection:
                    index = self.cursor.execute("SELECT `id` FROM `lessons` WHERE `name` = ?", (txt1,)).fetchone()[0]
            else:
                with self.connection:
                    index = self.cursor.execute("SELECT `id` FROM `lessons` WHERE `name` = ?", (txt2,)).fetchone()[0]
            with self.connection:
                less = self.cursor.execute("SELECT * FROM `timetable` WHERE `id` = ?", (day + 1,)).fetchone()
            less = list(less)[2:]
            if None in less:
                if obj == 0:
                    k = 0
                    for les in reversed(less):
                        if les is not None:
                            obj = len(less) - k + 1
                            break
                        else:
                            k += 1
                    if k == len(less):
                        obj = 1
                with self.connection:
                    self.cursor.execute(f"UPDATE `timetable` SET `less_{obj}` = ? WHERE `id` = ?", (index, day + 1))
                for choose_obj in [self.choose_obj1, self.choose_obj2]:
                    choose_obj.clear()
                    choose_obj.insertItem(0, "Новый предмет")
                self.add_line.clear()
                self.table_rasp()
            else:
                for choose_obj in [self.choose_obj1, self.choose_obj2]:
                    choose_obj.clear()
                    choose_obj.insertItem(0, "Новый предмет")
                    choose_obj.insertItems(1, lessons)
                QMessageBox.about(self, 'Ошибка!', "В этом дне уже расписание всё занято!")
        else:
            QMessageBox.about(self, 'Ошибка!', "Введите предмет, который желаете добавить!")

    def upd(self):
        obj = self.choose_obj2.currentText()
        txt = self.upd_line.text()
        if txt != "":
            with self.connection:
                self.cursor.execute(f"UPDATE `lessons` SET `name` = ? WHERE `name` = ?", (txt, obj))
            self.upd_line.clear()
            self.table_rasp()
        else:
            QMessageBox.about(self, 'Ошибка!', "Вы не ввели новое название!")

    def clear(self):
        day = self.weekday3.currentIndex()
        obj = self.object3.currentIndex()

        for wkd in range(1, 7):
            if day == 0 or day == wkd:
                for less in range(1, 9):
                    if obj == 0 or obj == less:
                        with self.connection:
                            self.cursor.execute(f"UPDATE `timetable` SET `less_{less}` = ? WHERE `id` = ?", (None, wkd))
        self.table_rasp()

    def delete(self):
        index = self.choose_obj3.currentText()
        with self.connection:
            ids = self.cursor.execute("SELECT `id` FROM `lessons` WHERE `name` = ?", (index, )).fetchone()[0]
            self.cursor.execute("DELETE FROM `lessons` WHERE `id` = ?", (ids, ))

        for day in range(1, 7):
            with self.connection:
                lessons = self.cursor.execute("SELECT * FROM `timetable` WHERE `id` = ?", (day,)).fetchone()
            lessons = list(lessons)[2:]
            if ids in lessons:
                for less in range(1, 9):
                    if ids == lessons[less - 1]:
                        with self.connection:
                            self.cursor.execute(f"UPDATE `timetable` SET `less_{less}` = ? WHERE `id` = ?", (None, day))
        self.table_rasp()

    def check(self):
        index, sender = self.choose_obj4.currentText(), self.sender().text()
        with self.connection:
            ids = self.cursor.execute("SELECT `id` FROM `lessons` WHERE `name` = ?", (index,)).fetchone()[0]

        tables = [self.Mon_school, self.Tue_school, self.Wed_school,
                  self.Thu_school, self.Fri_school, self.Sat_school]

        for day in range(1, 7):
            with self.connection:
                lessons = self.cursor.execute("SELECT * FROM `timetable` WHERE `id` = ?", (day,)).fetchone()
            lessons = list(lessons)[2:]
            if ids in lessons:
                for less in range(1, 9):
                    if ids == lessons[less - 1]:
                        if sender == "Выделить":
                            tables[day - 1].item(less - 1, 0).setBackground(QtGui.QColor(0, 150, 100))
                        elif sender == "Отменить":
                            tables[day - 1].item(less - 1, 0).setBackground(QtGui.QColor(255, 255, 255))
                        else:
                            self.table_rasp()

    # ЗАМЕТКИ
    def show_note(self):
        tp = self.choosedate.currentIndex()
        if tp == 0:
            self.table_note()
        elif tp == 1 or tp == 2:
            with self.connection:
                note = self.cursor.execute("SELECT `date`, `note` FROM notes").fetchall()

            # СОРТИРОВКА ДАТ
            note = [[dt.datetime.strptime(dat, "%H:%M %d.%m.%Y"), nt] for dat, nt in note]
            note.sort()

            maintable = self.maintable
            maintable.setColumnCount(2)
            maintable.setRowCount(0)
            maintable.setHorizontalHeaderLabels(["Дата", "Заметка"])

            if tp == 1:
                dates = [dt.date.today() + dt.timedelta(days=i) for i in range(30)]
            else:
                dates = [dt.date.today() + dt.timedelta(days=i) for i in range(7)]

            notes = [[dt.datetime.strftime(dat, "%d.%m.%Y %H:%M "), nt] for dat, nt in note if dat.date() in dates]

            if notes:
                for i, row in enumerate(notes):
                    maintable.setRowCount(maintable.rowCount() + 1)
                    for j, elem in enumerate(row):
                        maintable.setItem(i, j, QTableWidgetItem(str(elem)))
                maintable.horizontalHeader().setStretchLastSection(True)
            else:
                QMessageBox.about(self, 'Нет Заметок!', "На данные даты заметки отсутствуют!")

    def check_note(self):
        note = self.choose.currentText()
        if note:
            ids = note.split(".")[0]

            with self.connection:
                notes = self.cursor.execute("SELECT `id`, `date` FROM `notes`").fetchall()

            notes = [[dt.datetime.strptime(dat, "%H:%M %d.%m.%Y"), ids] for ids, dat in notes]
            notes.sort()
            notes = [idp for dat, idp in notes]

            ids = notes[int(ids) - 1]

            with self.connection:
                self.cursor.execute("DELETE FROM `notes` WHERE `id` = ?", (ids, ))
            self.table_rasp()  # после вёрстки удалить !!!
            self.table_note()
        else:
            QMessageBox.about(self, 'Нет заметки!', "Чтобы выполнить заметку, необходимо её хотя бы иметь!")

    def add_note(self):
        date = self.date_1.dateTime().toString("HH:mm dd.MM.yyyy")
        txt = self.write.toPlainText()
        day = self.date_1.dateTime().toString()[:2]

        if txt:
            for i, elem in enumerate(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]):
                if day == elem:
                    day = i
                    break
            with self.connection:
                self.cursor.execute("INSERT INTO `notes` (`date`, `day`, `note`) VALUES(?,?,?)", (date, day, txt))
            self.table_rasp()
            self.table_note()
        else:
            QMessageBox.about(self, 'Отсутствует информация!',
                              "Для добавления заметки вы должны заполнить текстовое поле!")

    def update_note(self):
        sender = self.sender().text()
        z = self.choose_2.currentText()
        if z:
            ids = z.split(".")[0]

            with self.connection:
                notes = self.cursor.execute("SELECT `id`, `date` FROM `notes`").fetchall()

            notes = [[dt.datetime.strptime(dat, "%H:%M %d.%m.%Y"), ids] for ids, dat in notes]
            notes.sort()
            notes = [idp for dat, idp in notes]

            ids = notes[int(ids) - 1]

            if sender == "Показать":
                with self.connection:
                    note = self.cursor.execute(f"SELECT `date`, `note` FROM notes WHERE `id` = {ids}").fetchone()

                # ОТОБРАЖЕНИЕ ДАТЫ ИЗ БАЗЫ
                datetime = note[0].split()
                time = datetime[0].split(":")
                date = datetime[1].split('.')
                now = QtCore.QDateTime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]))
                self.date_2.setDateTime(now)

                self.write_2.setPlainText(note[1])
            elif sender == "Обновить":
                date = self.date_2.dateTime().toString("HH:mm dd.MM.yyyy")
                txt = self.write_2.toPlainText()

                with self.connection:
                    self.cursor.execute(f"UPDATE `notes` SET `date` = ?, `note` = ? WHERE `id` = ?", (date, txt, ids))

                self.write_2.clear()
                self.table_rasp()
                self.table_note()
                self.table_note_date()
        else:
            QMessageBox.about(self, 'Нет заметки!', "Чтобы изменить заметку, необходимо её хотя бы иметь!")

    # ЗАКРЫТИЕ ОКНА
    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())