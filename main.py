import datetime as dt
import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyWidget(QMainWindow):  # Ui_MainWindow
    def __init__(self):
        super().__init__()
        uic.loadUi('rasp.ui', self)  # self.setupUi(self)
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
        self.complete.clicked.connect(self.add_notes)  # ДОБАВЛЕНИЕ

        # ДАННЫЕ ТАБЛИЦЫ
        self.table()

    def table(self):
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

            # ЗАПОЛНЕНИЕ ВЫПАДАЮЩИХ СПИСКОВ CHOOSE 1 / 2
            try:
                with self.connection:
                    notes = self.cursor.execute('SELECT `note` FROM `notes`').fetchall()
                notes = [i[0] for i in notes]
                for choose_obj in [self.choose, self.choose_2]:
                    choose_obj.clear()
                    if self.choose == choose_obj:
                        choose_obj.insertItem(0, "Все за этот день!")
                        choose_obj.insertItems(1, notes)
                    else:
                        choose_obj.insertItems(0, notes)
            except Exception:
                pass

            # НАСТРОЙКА ДИСПЛЕЕВ ДАТ
            now = QtCore.QDateTime.currentDateTime()
            for date in [self.date_1, self.date_2, self.date_3]:
                date.setDateTime(now)
                date.setDateRange(QtCore.QDate.currentDate().addDays(-365), QtCore.QDate.currentDate().addDays(365))
                if self.date_1 == date:
                    date.setDisplayFormat("dd.MM.yyyy")

            # ВСЕ ЗАМЕТКИ
            with self.connection:
                note = self.cursor.execute("SELECT `date`, `note` FROM notes").fetchall()
            maintable = self.maintable
            maintable.setColumnCount(2)
            maintable.setRowCount(0)
            maintable.setHorizontalHeaderLabels(["Дата", "Заметка"])

            for i, row in enumerate(note):
                maintable.setRowCount(maintable.rowCount() + 1)
                for j, elem in enumerate(row):
                    maintable.setItem(i, j, QTableWidgetItem(str(elem)))
            maintable.horizontalHeader().setStretchLastSection(True)

            # ЗАМЕТКИ ПОД РАСПИСАНИЕМ
            with self.connection:
                note = self.cursor.execute("SELECT `date`, `note` FROM notes").fetchall()
            notes = [self.Mon_note, self.Tue_note, self.Wed_note, self.Thu_note, self.Fri_note, self.Sat_note]

            week = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
            for i in note:
                weekday = dt.datetime.weekday(i[0])
                if weekday != 6:
                    week[weekday].append(i)

            for write in notes:
                write.setColumnCount(2)
                write.setRowCount(0)
                write.setHorizontalHeaderLabels(["Дата", "Заметка"])

                for i, row in enumerate(week[notes.index(write)]):
                    write.setRowCount(write.rowCount() + 1)
                    for j, elem in enumerate(row):
                        write.setItem(i, j, QTableWidgetItem(str(elem)))
                write.horizontalHeader().setStretchLastSection(True)

        except Exception:
            QMessageBox.about(self, 'Ошибка!', "Таблица данных не найдена!")

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
                self.table()
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
            self.table()
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
        self.table()

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
        self.table()

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
                            self.table()

    # ЗАМЕТКИ
    def add_notes(self):
        ind = self.choose.currentIndex()
        if ind:
            pass

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
