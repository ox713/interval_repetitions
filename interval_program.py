"""
Консольная программа анки, должна быть яркой, возможно с графическим интерефейсом
Программа должна вести записи в базу данных на основе которой потом будет создаваться статистика
В неё должны отмечать все что повторенно, желательно с отображением статистики
Несколько методов повторения


"""

import sqlite3
import datetime

import config
import mesql




class Console_anki():
    def __init__(self):
        self.database = mesql.SQLighter1("main_base.db")

    def find_reiteration_base(self):
        quantity = len(self.database.select_all("python"))
        print(self.database.select_all("python"))

        #for i in self.database.select_all("python"):
            #i[2] =
        # находим нужные строки по дате
        reiteration = []
        today = datetime.date.today()
        today = datetime.datetime.strptime(str(today), '%Y-%m-%d')
        for i in self.database.select_all("python"):
            for g in config.DATES_PLUS:
                print(i[2])
                d = datetime.datetime.strptime(i[2][0:10], '%Y-%m-%d')
                d = d + datetime.timedelta(days=g)
                if d == today:
                    reiteration.append(i[13])
                    print("yes")
        return reiteration

                    #if datetime.date(int(str(temp)[0:4]), int(str(temp)[5:7]), int(str(temp)[8:10])) == date:
                       # reiteration.append(i)
        #print(reiteration, 6)
        #return reiteration

        #for i in range(quantity):
            #self.database.select_single("python", i)

    def console_output(self, reapeat):
        for i in reapeat:
            temp = self.database.select_single('python', i)
            print(1, type(temp))
            print("Вопрос\n", temp[0])
            assesment = input()
            today = str(datetime.datetime.today())[0:10]
            print(type(temp[10]))
            temp = list(temp)

            #temp[10] = ["" if temp[10] == None  else temp[10]][0]+ " " + str(today)
            if temp[10] == None:
                temp[10] = str(today)
            else: temp[10] += str(today)

            temp[11] += assesment
            print(temp)
            self.database.update_line("python", temp)


test = Console_anki()
test.console_output(test.find_reiteration_base())