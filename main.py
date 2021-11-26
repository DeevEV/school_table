import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
from PyQt5 import QtCore, QtWidgets, QtGui, uic

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
        # По умолчанию будем выводить все данные из таблицы
        self.table()

    def table(self):
        try:
            # РАСПИСАНИЕ
            print(1)
            with self.connection:
                all_day = self.cursor.execute("SELECT * FROM timetable").fetchall()
            # Заполним размеры таблицы
            tables = [self.Mon_school, self.Tue_school, self.Wed_school,
                      self.Thu_school, self.Fri_school, self.Sat_school]
            print(2)
            for day in tables:
                day = day.QTableWidget.QTableView
                day.setSpan(8, 1)
                print(3)
                # Заполняем таблицу элементами
                i, row = enumerate(all_day[tables.index(day)])
                print(i, row)
                for j, elem in enumerate(row):
                    self.tableWidget_2.setItem(
                        i, j, QTableWidgetItem(str(elem)))

            """
            # ВСЕ ФИЛЬМЫ
            with self.connection:
                res = self.cursor.execute("SELECT * FROM films").fetchall()
            # Заполним размеры таблицы
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(0)
            # Заполняем таблицу элементами
            self.tableWidget.setHorizontalHeaderLabels(["ИД", "Название фильм", "Год выпуска",
                                                        "Жанр", "Продолжительность"])
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    if j == 3:
                        for n, name in gnr:
                            if n == elem:
                                self.tableWidget.setItem(
                                    i, j, QTableWidgetItem(str(name)))
                                break
                    else:
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(str(elem)))
            """
        except Exception:
            QMessageBox.about(self, 'Ошибка!', "Таблица данных не найдена!")

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение с базой данных
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())