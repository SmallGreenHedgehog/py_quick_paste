import sqlite3
import traceback
from time import sleep


class BaseManager():
    def __new__(cls): # Singleton
        if not hasattr(cls,'instance'):
            cls.instance = super(BaseManager, cls).__new__(cls)

    def __init__(self):
        self.__conf_file_name = 'config.db'
        self.__init_base()

        # TODO реализовать фукционал проверки базы на отсутствие комбинаций и заполнения тестовыми значениями

    def __init_base(self):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        # Создаем таблицу параметров
        # TODO реализовать функционал создания таблицы параметров

        # Создаем таблицу правил
        ok = False
        attempts_q = 5
        attemps_num = 0;

        while (attemps_num < attempts_q) and (not ok):
            attemps_num += 1
            ok = True
            try:
                cursor.execute('CREATE TABLE IF NOT EXISTS RULES ('
                               'Id INTEGER  PRIMARY KEY NOT NULL'
                               ',Combination CHAR(50)'
                               ',Name CHAR(100)'
                               ',TXT TEXT);'
                               )
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''

        return ok
