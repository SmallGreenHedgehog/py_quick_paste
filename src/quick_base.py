# -*- coding: utf-8 -*-
import os, shutil
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
            # self.__conf_file_name = os.path.join(os.path.dirname(sys.argv[0]), 'config.db')
            self.__conf_base_path = os.path.expanduser('~/.com.company.py_quick_paste/data/Documents')
            os.system('mkdir -p %s' % self.__conf_base_path)
            self.__conf_file_name = self.__conf_base_path + '/config.db'

            self.__init_base()
            self.__first_start = False
            self.__initialized = True

    def get_version_from_txt(self):
        result = ''
        try:
            with open('./src/version', 'r') as version_file:
                result = version_file.read()
        except:
            print(traceback.print_exc())
        return result

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
            req_text = 'INSERT INTO RULES (Num, Combination, Name, TXT) VALUES ((SELECT MAX(Num) + 1 FROM RULES), ?, ?, ?)'

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
            # list_of_combs.append(c.replace('\'', '') if c.find('Key') < 0 else c)
            list_of_combs.append('\'%s\'' % c)
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

    def __update_database_version_lower_0_22(self):
        sqlite_base = sqlite3.connect(self.__conf_file_name)
        cursor = sqlite_base.cursor()

        update_req_text = 'PRAGMA foreign_keys = 0;\n' \
                          'DROP TABLE IF EXISTS sqlitestudio_temp_table;\n' \
                          'CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM RULES;\n' \
                          'DROP TABLE RULES;\n' \
                          'CREATE TABLE RULES (\n' \
                          '    Id INTEGER PRIMARY KEY NOT NULL UNIQUE,\n' \
                          '    Num INTEGER NOT NULL,\n' \
                          '    Combination CHAR (50),\n' \
                          '    Name CHAR (100),\n' \
                          '    TXT TEXT\n' \
                          ');\n' \
                          'INSERT INTO RULES (\n' \
                          '    Id,\n' \
                          '    Num,\n' \
                          '    Combination,\n' \
                          '    Name,\n' \
                          '    TXT\n' \
                          ')\n' \
                          'SELECT \n' \
                          '    Id,\n' \
                          '    Id,\n' \
                          '    Combination,\n' \
                          '    Name,\n' \
                          '    TXT\n' \
                          'FROM sqlitestudio_temp_table;\n' \
                          'DROP TABLE sqlitestudio_temp_table;\n' \
                          'PRAGMA foreign_keys = 1;'

        # print(update_req_text)

        ok = False
        attempts_q = 5
        attempts_num = 0;

        while (attempts_num < attempts_q) and (not ok):
            attempts_num += 1
            ok = True
            try:
                cursor.executescript(update_req_text)
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)

        if ok:
            update_req_text = 'PRAGMA foreign_keys = 0;\n' \
                              'CREATE TABLE sqlitestudio_temp_table AS SELECT * FROM PARAMS;\n' \
                              'DROP TABLE PARAMS;\n' \
                              'CREATE TABLE PARAMS (\n' \
                              '    Id   INTEGER    PRIMARY KEY\n' \
                              '    NOT NULL,\n' \
                              '    Name CHAR (100) UNIQUE ON CONFLICT REPLACE,\n' \
                              '    Val  CHAR (100)\n' \
                              ');\n' \
                              'INSERT INTO PARAMS (\n' \
                              '    Id,\n' \
                              '    Name,\n' \
                              '    Val\n' \
                              ')\n' \
                              'SELECT Id,\n' \
                              '    Name,\n' \
                              '    Val\n' \
                              'FROM sqlitestudio_temp_table;\n' \
                              'DROP TABLE sqlitestudio_temp_table;\n' \
                              'PRAGMA foreign_keys = 1;'

            # print(update_req_text)

            ok = False
            attempts_q = 5
            attempts_num = 0;

            while (attempts_num < attempts_q) and (not ok):
                attempts_num += 1
                ok = True
                try:
                    cursor.executescript(update_req_text)
                except:
                    ok = False
                    print(traceback.print_exc())
                    sleep(1)

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''

        self.set_parameter('w_hidden_win_start', True)

        return ok

    def __backup_database_file(self):
        database_name = self.__conf_file_name.rsplit('/', 1)[1].rsplit('.', 1)[0]
        database_path = self.__conf_file_name.rsplit('/', 1)[0]

        new_max_bak_num = 0
        for conf_file in os.listdir(database_path):
            if not conf_file.find('config_') < 0:
                conf_file_name = conf_file.rsplit('.', 1)[0]
                num_backup = 0
                try:
                    num_backup = int(conf_file_name.rsplit('_', 1)[1])
                except:
                    pass
                if num_backup > new_max_bak_num:
                    new_max_bak_num = num_backup
        new_max_bak_num += 1
        backup_path = database_path + '/' + database_name + '_' + '{:03}'.format(new_max_bak_num) + '.db'

        # print('database_path = %s' % self.__conf_file_name)
        # print('database_name = %s' % database_name)
        # print('backup_path = %s' % backup_path)

        ok = True
        try:
            shutil.copyfile(self.__conf_file_name, backup_path)
        except:
            ok = False
            print(traceback.print_exc())

        if ok:
            ok = os.path.exists(backup_path)
        return ok

    def __update_database_on_new_version(self):
        act_version = self.get_parameter('version')
        new_version = self.get_version_from_txt()
        float_act_version = 0.21 if act_version is None else float(act_version)
        float_new_version = float(new_version)

        ok = True
        if float_act_version < float_new_version:
            ok = self.__backup_database_file()
            if ok:
                if float_act_version < 0.22:
                    ok = self.__update_database_version_lower_0_22()
            if ok:
                self.set_parameter('version', new_version)

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
                cursor.execute('CREATE TABLE IF NOT EXISTS PARAMS (\n'
                               'Id INTEGER  PRIMARY KEY NOT NULL\n'
                               ',Name CHAR (100) UNIQUE ON CONFLICT REPLACE\n'
                               ',Val CHAR(100)\n'
                               ');'
                               )
            except:
                ok = False
                print(traceback.print_exc())
                sleep(1)
        if ok:
            # Создаем таблицу правил
            req_text = 'CREATE TABLE IF NOT EXISTS RULES (\n' \
                       '    Id INTEGER PRIMARY KEY NOT NULL UNIQUE\n' \
                       '    ,Num INTEGER NOT NULL\n' \
                       '    ,Combination CHAR(50)\n' \
                       '    ,Name CHAR(100)\n' \
                       '    ,TXT TEXT\n' \
                       ');'

            ok = False
            attempts_q = 5
            attempts_num = 0;

            while (attempts_num < attempts_q) and (not ok):
                attempts_num += 1
                ok = True
                try:
                    cursor.execute(req_text)
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
                ok = self.set_rule(str(def_comb), 'Тестовая комбинация', 'Текст тестовой комбинации')
                if ok:
                    ok = self.set_parameter('version', str(self.get_version_from_txt()))
                if ok:
                    self.set_parameter('not_firts_start', 'True')
            else:
                self.__update_database_on_new_version()
                # pass

        cursor = ''
        sqlite_base.close()
        sqlite_base = ''

        return ok
