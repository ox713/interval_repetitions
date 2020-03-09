"""
Программа которая должна заменить моё экселевское повторение.
Задачи:

Новая база данных:
    Перевод всего в нужную базу и тогда будет просто импорт
    Обновление базы по мере необходимости
Программа которая бы выводила мои данные в виде html + работа с базой данных:


Чтение:
    Имортировать все нужные файлы которые я добавлю через модуль values
    Анализировать ячейки по дате + смещению, которые тоже будут в отдельном файле
    Выдача нужных ячеек в формате вопрос ответ
    Выдача ячеек на несколько дней
    !Коректное закрытие

Запись
    Запись даты повторений с потверждением(будущим)


Модули
    Проверка везде ли установленна дата
    Проверка везде ли установлен вопрос

    Подгтовка к экспорту в балаболку или скармливание голосовому движку

    Реалзиация систем оценки с помощью андроид приложения и пульта:
    1. Проигрывание и замирание до оценки

Функционал:
    Типы повторений: по дате, по темам, по тегам, по источнику, по языку источника, по качеству усвоения,
    по сложности, по типу ячеек(например код не нужно в аудио), по листам


Поля:
1.
"""
import datetime

import config
from openpyxl import load_workbook
from datetime import timedelta


class ParserExcel(object):
    def __init__(self, EXCELS):
        self.excels = EXCELS
        self.all_reiteration = []
        self.operations = Operations_with_parsed_excel()

    def import_excel_files(self):
        for excel in self.excels:
            wb = load_workbook(filename=excel)
            self.all_reiteration.append(self.operations.value_operations(wb[wb.sheetnames[0]]))




    def test_print(self, reiteration, sheet):
        for i in reiteration:
            # Вопрос\ответ
            print(sheet.cell(row=i, column=3))
            print(sheet.cell(row=i, column=2))

class Operations_with_parsed_excel(object):

    def __init__(self):
        pass
        #self.excels = excels
        #self.all_reiteration = all_reiteration

    def value_operations(self, sheet):
        # пока так потом может добавить выбор
        if config.TYPE_OF_SELECT == "today":
            return self.today_reiteration(sheet, 0)

        elif config.TYPE_OF_SELECT == "tomorrow":
            return self.today_reiteration(sheet, 1)

        elif config.TYPE_OF_SELECT == "tag":
            pass

        elif config.TYPE_OF_SELECT == "source":
            pass

        elif config.TYPE_OF_SELECT == "category":
            pass

        elif config.TYPE_OF_SELECT == "language":
            pass

        elif config.TYPE_OF_SELECT == "quality of understand":
            pass

        elif config.TYPE_OF_SELECT == "special code":
            pass

        elif config.TYPE_OF_SELECT == "quality of remembering":
            pass

        elif config.TYPE_OF_SELECT == "list":
            pass





    def end_of_file(self, sheet):
        for i in range(1, 100000):
            if sheet.cell(row=i, column=1).value == "end_of_end":
                print(i)
                return i

    def today_reiteration(self, sheet, needed_date):
        reiteration = []
        end = self.end_of_file(sheet)
        today = datetime.date.today()
        if isinstance(needed_date, datetime.date):
            date = needed_date

        else: # Если смещение
            date = today + timedelta(days=needed_date)


        for i in range(1, end):
            print(sheet.cell(row=i, column=6).value)

            if not isinstance(sheet.cell(row=i, column=6).value, datetime.datetime) :#sheet.cell(row=i, column=6).value == None or sheet.cell(row=i, column=6).value =="":
                continue

            else:
                for g in config.DATES_PLUS:
                    temp = sheet.cell(row=i, column=6).value + timedelta(days=g)

                    if datetime.date(int(str(temp)[0:4]), int(str(temp)[5:7]), int(str(temp)[8:10])) == date:
                        reiteration.append(i)
        print(reiteration)
        return reiteration




test = ParserExcel(config.EXCELS)
test.import_excel_files()
print(11, test.all_reiteration)

