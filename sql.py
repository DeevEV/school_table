import sqlite3


class SQLighter:
    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # КОМАНДЫ ДЛЯ УРОКОВ
    def group_exists(self, id_group):
        """Проверяем, есть ли уже группа в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `group` WHERE `id_group` = ?', (id_group,)).fetchall()
            return bool(len(result))

    def add_group(self, domain, id_group, name, last_post, type):
        """Добавляем новую группу в таблицу"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `group` (`domain`, `id_group`, `name`, `last_post`, `type`) "
                                       "VALUES(?,?,?,?,?)", (domain, id_group, name, last_post, type))

    def update_last_post(self, domain, last_post):
        """Обновляем статус группы"""
        with self.connection:
            return self.cursor.execute("UPDATE `group` SET `last_post` = ? WHERE `domain` = ?", (last_post, domain))

    def id_group_lst(self):
        """Список всех айди групп"""
        with self.connection:
            dt = self.cursor.execute(f'SELECT id_group FROM `group`').fetchall()
            return [i[0] for i in dt]

    def get_last_post(self, idg):
        """Получение последнего поста"""
        with self.connection:
            return self.cursor.execute("SELECT last_post FROM `group` WHERE `id` = ?", (idg,)).fetchone()

    def domain_by_id(self, idg):
        """Получение домена по айди"""
        with self.connection:
            return self.cursor.execute("SELECT domain FROM `group` WHERE `id` = ?", (idg,)).fetchone()

    def get_group_id(self, id_group):
        """Получение айди группы в базе данных"""
        with self.connection:
            return self.cursor.execute("SELECT id FROM `group` WHERE `id_group` = ?", (id_group,)).fetchone()[0]

    # СВЯЗКА ПОЛЬЗОВАТЕЛЯ
    def user_exists(self, id_user):
        """Проверяем, есть ли уже пользователь в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `id_user` = ?', (id_user,)).fetchall()
            return bool(len(result))

    def add_user(self, id_user):
        """Добавляем нового пользователя"""
        with self.connection:
            return self.cursor.execute(f"INSERT INTO `user` (`id_user`, `groups`) VALUES(?,?)", (id_user, ""))

    def add_group_user(self, num, id_user, group):
        """Обновляем группы пользователя"""
        with self.connection:
            if num:
                groups = str(self.cursor.execute("SELECT groups FROM `user` WHERE `id_user` = ?",
                                                 (id_user,)).fetchone()[0]) + str(group) + " "
                return self.cursor.execute(f"UPDATE `user` SET `groups` = ? WHERE `id_user` = ?", (groups, id_user))
            else:
                lst = self.cursor.execute("SELECT groups FROM `user` WHERE `id_user` = ?", (id_user,)).fetchone()
                groups = [i for i in lst[0].split()]
                del groups[groups.index(str(group))]
                groups = " ".join(groups) + " "
                return self.cursor.execute(f"UPDATE `user` SET `groups` = ? WHERE `id_user` = ?", (groups, id_user))

    def get_user_groups(self, id_user):
        """Получаем все группы пользователя"""
        with self.connection:
            lst = self.cursor.execute("SELECT groups FROM `user` WHERE `id_user` = ?", (id_user,)).fetchone()
            return [int(i) for i in lst[0].split()]

    def id_user_lst(self):
        """Список айди"""
        with self.connection:
            dt = self.cursor.execute(f'SELECT id_user, groups FROM `user` WHERE `status` = 1').fetchall()
            return [list(i) for i in dt]

    def upd_user_status(self, id_user):
        """Обновление статуса подписки"""
        with self.connection:
            st = self.cursor.execute("SELECT status FROM `user` WHERE `id_user` = ?", (id_user,)).fetchone()[0]
            if st:
                self.cursor.execute("UPDATE `user` SET `status` = ? WHERE `id_user` = ?", (0, id_user))
                return 0
            else:
                self.cursor.execute("UPDATE `user` SET `status` = ? WHERE `id_user` = ?", (1, id_user))
                return 1

    def get_groups_user(self, id_user):
        """Получение полных данных на все группы на которые подписан пользователь"""
        with self.connection:
            lst = self.cursor.execute("SELECT groups FROM `user` WHERE `id_user` = ?", (id_user,)).fetchone()
            lst = [int(i) for i in lst[0].split()]
            data = []
            for i in lst:
                grp = self.cursor.execute('SELECT * FROM `group` WHERE `id` = ?', (i,)).fetchone()
                data.append(list(grp))
            return data

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
