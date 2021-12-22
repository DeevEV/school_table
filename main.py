import datetime as dt
import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# ВСТАВИТЬ В ИНТЕРФЕЙС ПОСЛЕ ФОРМАТИРОВАНИЯ
# self.setWindowTitle('Icon')
# self.setWindowIcon(QtGui.QIcon('web.png'))


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
            maintable = self.maintable
            maintable.setColumnCount(2)
            maintable.setRowCount(0)
            maintable.setHorizontalHeaderLabels(["Дата", "Заметка"])

            if tp == 1:
                dates = ['.'.join(reversed(str(dt.date.today() + dt.timedelta(days=i)).split('-'))) for i in range(30)]
            else:
                dates = ['.'.join(reversed(str(dt.date.today() + dt.timedelta(days=i)).split('-'))) for i in range(7)]

            notes = [i for i in note if i[0][-10:] in dates]

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
                notes = self.cursor.execute("SELECT `id` FROM `notes`").fetchall()
            ids = notes[int(ids) - 1][0]

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
            self.table_rasp()  # после вёрстки удалить !!!
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
                notes = self.cursor.execute("SELECT `id` FROM `notes`").fetchall()
            ids = notes[int(ids) - 1][0]

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
                self.table_rasp()  # после вёрстки удалить !!!
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
