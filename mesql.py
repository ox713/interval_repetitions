# -*- coding: utf-8 -*-
import sqlite3
import hashlib

class SQLighter1:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        # connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()


    def select_all(self, table):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute(f'SELECT * FROM {table}').fetchall()

    def select_single(self, table, rownum):
        """ Получаем одну строку с номером rownum """
        #with self.connection:
        print(self.cursor)
        return self.cursor.execute(f'SELECT * FROM {table} WHERE hash = ?', (rownum,)).fetchall()[0]

    def count_rows(self, table):
        """ Считаем количество строк """
        with self.connection:

            result = self.cursor.execute(f'SELECT * FROM {table}').fetchall()
            return len(result)

    def writing_line(self, table, tuple_str):
        #добавляем хеш
        tuple_str = self.hash_answer(tuple_str)
        print(11111111111, tuple_str)
        tuple_str = tuple(tuple_str)

        with self.connection:
            self.cursor.execute(f"""INSERT INTO {table} VALUES {tuple_str}""")
            self.connection.commit()

    def update_line(self, table, tuple_str):
        old_line = self.select_single("python", tuple_str[13])
        tuple_str = list(tuple_str)

        # ищем новые ячейки
        temp_mass = []
        for i in range(len(tuple_str)):
            if tuple_str[i] != old_line[i]:
                temp_mass.append(i)



        #with self.connection:
        # названия столбцев
        colum_name = []
        self.cursor = self.connection.execute(f'select * from {table}')
        colnames = self.cursor.description
        for row in colnames:
            colum_name.append(row[0])
        # обновляем только те ячейки которые новые
        for i in temp_mass:
            self.cursor.execute(f"""UPDATE {table} SET {colum_name[i]} = {str(tuple_str[i])} WHERE hash = {tuple_str[13]}""")
        self.connection.commit()




    def hash_answer(self, tuple_str):
        tuple_str = list(tuple_str)
        print(tuple_str)
        temp = hashlib.md5(str(tuple_str[1]).encode())

        print(1, tuple_str[13])
        tuple_str[13] = temp.hexdigest()
        return tuple_str

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()

