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
    def __init__(self, EXCELS ):
        self.excels = EXCELS


    # def import_excel_files(self):
    #     for excel in self.excels:
    #         wb = load_workbook(filename=excel)
    #         self.all_reiteration.append(self.operations.value_operations(wb[wb.sheetnames[0]]))

    def load_excel_file(self, excel):
        #names_of_sheets = []
        excel_file = load_workbook(filename=excel) # объект загружаеться в память, так что надо работать
        #names_of_sheets.append({excel: wb.sheetnames})

        return excel_file

    def return_data_from_names_of_sheets(self, excel, sheet):

        pass


    def test_print(self, reiteration, sheet):
        for i in reiteration:
            # Вопрос\ответ
            print(sheet.cell(row=i, column=3))
            print(sheet.cell(row=i, column=2))

class Operations_with_parsed_excel(object):

    def __init__(self):
        self.export_data = Export_done_file()
        pass
        #self.excels = excels
        #self.all_reiteration = all_reiteration

    #
    # def call_import_excel(self, import_class):
    #
    #     pass

    def value_operations(self, sheet):
        # пока так потом может добавить выбор
        if config.TYPE_OF_SELECT == "today":
            #self.export_data.to_txt(, sheet)
            return self.find_reiteration(sheet, 0)


        elif config.TYPE_OF_SELECT == "tomorrow":
            return self.find_reiteration(sheet, 1)

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

    def find_reiteration(self, sheet, needed_date):
        reiteration = []
        end = self.end_of_file(sheet)
        today = datetime.date.today()
        if isinstance(needed_date, datetime.date):
            date = needed_date

        else: # Если смещение
            date = today + timedelta(days=needed_date)


        for i in range(1, end):
            print(sheet.cell(row=i, column=6).value)

            if not isinstance(sheet.cell(row=i, column=6).value, datetime.datetime): # sheet.cell(row=i, column=6).value == None or sheet.cell(row=i, column=6).value =="":
                continue

            else:
                for g in config.DATES_PLUS:
                    temp = sheet.cell(row=i, column=6).value + timedelta(days=g)

                    if datetime.date(int(str(temp)[0:4]), int(str(temp)[5:7]), int(str(temp)[8:10])) == date:
                        reiteration.append(i)
        print(reiteration)
        return reiteration


class Export_done_file(object):
    def __init__(self):
        pass

    def to_txt(self, sheet, repeat):
        config.TYPE_OF_SELECT + ".txt"

        with open(config.TYPE_OF_SELECT + ".txt", 'a+', encoding="UTF-8") as f:
            counter = 1
            for i in repeat:

                print(sheet.cell(row=i, column=3).value)
                f.write(f"Вопрос {counter}\n")
                f.write(str(sheet.cell(row=i, column=3).value)+"\n")

                print(sheet.cell(row=i, column=2).value)
                f.write(f"Ответ {counter}\n")
                f.write(str(sheet.cell(row=i, column=2).value)+"\n")
                f.write("-----\n\n")
                counter += 1








# лучше вынесу все объеты в маин, чтобы логика не путалась, чтобы стал главной базой
def main():

    all_reiteration = []
    operations = Operations_with_parsed_excel()
    loader = ParserExcel(config.EXCELS)
    export_list = Export_done_file()

    k = 1

    for excel in config.EXCELS:
        excel_file = loader.load_excel_file(excel)
        for sheet in excel_file.sheetnames:
            if excel_file[sheet].cell(row=1, column=1).value == "NO":
                continue
            export_list.to_txt(excel_file[sheet], operations.value_operations(excel_file[sheet]))
            print("done", k)
            k+= 1









main()