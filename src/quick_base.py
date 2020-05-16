# -*- coding: utf-8 -*-
import os, sys
import sqlite3
import traceback
from time import sleep


class BaseManager():
    def __new__(cls):  # Singleton
        if not hasattr(cls, 'instance'):
            cls.instance = super(BaseManager, cls).__new__(cls)
            cls.instance.__initialized = False
        return cls.instance

    def __init__(self):
        if not self.__initialized:
            self.__conf_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'config.db')
            # self.__conf_file_name = 'config.db'
            self.__init_base()
            self.__first_start = False
            self.__initialized = True

    def get_parameter(self, name):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        result = None

        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute('SELECT Val FROM PARAMS WHERE Name="%s" LIMIT 1' % name)
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            list_query = cursor.fetchone()
            if not list_query == None:
                if len(list_query) > 0:
                    result = list_query[0]
        cursor = ''
        sqlite_base.close()
        sqlite_base = ''
        return result

    def set_parameter(self, name, val):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute('INSERT OR REPLACE INTO PARAMS (Name, Val) Values("%s", "%s")' % (name, val))
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            ok = False
            attempts_q = 5
            attempts_num = 0;

            while (attempts_num < attempts_q) and (not ok):
                attempts_num += 1
                ok = True
                try:
                    sqlite_base.commit()
                except:
                    ok = False
                    print(traceback.print_exc())
                    sleep(1)
        cursor = ''
        sqlite_base.close()
        sqlite_base = ''
        return ok

    def set_rule(self, rule_comb, rule_name, rule_text, rule_id=None):
        if rule_id != None:  # обновляем правило
            req_text = 'UPDATE RULES SET Combination=?, Name=?, TXT=? WHERE Id=%s' % rule_id
        else:  # добавляем новое правило
            req_text = 'INSERT INTO RULES (Combination, Name, TXT) VALUES (?, ?, ?)'

        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        # Создаем таблицу параметров
        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute(req_text, (rule_comb, rule_name, rule_text))
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            ok = False
            attempts_q = 5
            attempts_num = 0;

            while (attempts_num < attempts_q) and (not ok):
                attempts_num += 1
                ok = True
                try:
                    sqlite_base.commit()
                except:
                    ok = False
                    print(traceback.print_exc())
                    sleep(1)

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''

        return ok

    def get_all_rules(self):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        result = None

        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute('SELECT * FROM RULES')
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            result = cursor.fetchall()

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''
        return result

    def get_rule_by_id(self, rule_id):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        result = None

        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute('SELECT * FROM RULES WHERE id=%s LIMIT 1' % rule_id)
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            result = cursor.fetchone()

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''
        return result

    def get_list_rules_by_comb(self, comb):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        list_of_combs = []
        cond_text = ''
        for c in comb:
            cond_text += ' and (instr(Combination, ?)>0)'
            list_of_combs.append(c.replace('\'', '') if c.find('Key') < 0 else c)
        cond_text = cond_text[5:]

        req_text = 'SELECT Id, Name FROM RULES' + (' WHERE ' + cond_text if cond_text else '')

        result = None

        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute(req_text, list_of_combs)
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            result = cursor.fetchall()

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''
        return result

    def remove_rule(self, rule_id):
        if rule_id != None:
            sqlite_base = sqlite3.connect(self.__conf_file_name)
            cursor = sqlite_base.cursor()

            # Создаем таблицу параметров
            ok = False
            attempts_q = 5
            attempts_num = 0;

            while (attempts_num < attempts_q) and (not ok):
                attempts_num += 1
                ok = True
                try:
                    cursor.execute('DELETE FROM RULES WHERE Id=%s' % rule_id)
                except:
                    ok = False
                    print(traceback.print_exc())
                    sleep(1)
            if ok:
                ok = False
                attempts_q = 5
                attempts_num = 0;

                while (attempts_num < attempts_q) and (not ok):
                    attempts_num += 1
                    ok = True
                    try:
                        sqlite_base.commit()
                    except:
                        ok = False
                        print(traceback.print_exc())
                        sleep(1)

            cursor = ''
            sqlite_base.close()
            sqlite_base = ''

            return ok

    def remove_all_rules(self):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        # Создаем таблицу параметров
        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute('DELETE FROM RULES')
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            ok = False
            attempts_q = 5
            attempts_num = 0;

            while (attempts_num < attempts_q) and (not ok):
                attempts_num += 1
                ok = True
                try:
                    sqlite_base.commit()
                except:
                    ok = False
                    print(traceback.print_exc())
                    sleep(1)

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''

        return ok

    def __init_base(self):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        # Создаем таблицу параметров
        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.execute('CREATE TABLE IF NOT EXISTS PARAMS ('
                               'Id INTEGER  PRIMARY KEY NOT NULL'
                               ',Name CHAR(100)'
                               ',Val CHAR(100));'
                               )
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            # Создаем таблицу правил
            ok = False
            attempts_q = 5
            attempts_num = 0;

            while (attempts_num < attempts_q) and (not ok):
                attempts_num += 1
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

        if ok:
            self.__first_start = not bool(self.get_parameter('not_firts_start'))

            if self.__first_start:  # Это первый запуск программы, заполним дефолтными значениями
                def_comb = set()
                def_comb.add('Key.ctrl')
                def_comb.add('17')
                if self.set_rule(str(def_comb), 'Тестовая комбинация', 'Текст тестовой комбинации'):
                    self.set_parameter('not_firts_start', 'True')

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''

        return ok
