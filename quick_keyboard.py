# -*- coding: utf-8 -*-
from threading import Timer
from pynput import keyboard
from PySide2.QtCore import QObject, Signal


class KeyMonitor(QObject):
    comb_found = Signal(enumerate)

    def __clear_released(self):
        self.__col_pressed = 0
        self.__pressed.clear()
        print('released combs was cleared')

    def start_listen(self):
        self.__listener.start()

    def stop_listen(self):
        self.__listener.stop()

    def __init__(self, parent=None):
        super(KeyMonitor, self).__init__()

        self.__listener = ''
        self.__search_combs = []
        self.__pressed = set()
        self.__col_pressed = 0
        self.__is_get_comb = False
        self.__max_key_count_comb = 0
        self._max_combination = set()
        self.__last_comb_found = set()
        self.__timer_clear_released = Timer(3, self.__clear_released)
        self.__listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release
        )
        self.start_listen()

    def start_get_comb(self):
        self._max_combination = set()
        self.__max_key_count_comb = 0
        self.__is_get_comb = True

    def stop_get_comb(self):
        self.__is_get_comb = False

    def __on_press(self, key):
        self.__col_pressed += 1
        self.__pressed.add(str(key))
        print('pressed = %s' % self.__pressed)
        print('col pressed = %s' % self.__col_pressed)

        if not self.__timer_clear_released.is_alive():
            self.__timer_clear_released = Timer(3, self.__clear_released)
            self.__timer_clear_released.start()

        if self.__col_pressed > 1:
            for search_comb in self.__search_combs:
                if all(p in search_comb for p in self.__pressed) and all(s in self.__pressed for s in search_comb):
                    print('Combination %s was found' % search_comb)
                    self.__last_comb_found = search_comb.copy()
                    self.comb_found.emit(self.__last_comb_found)

        if self.__is_get_comb:  # Начинаем получать комбинацию
            if self.__col_pressed > self.__max_key_count_comb:
                self._max_combination = self.__pressed.copy()
                self.__max_key_count_comb += 1

    def __on_release(self, key):
        if self.__is_get_comb and self.__col_pressed > 1:  # Отпустили хоть одну клавишу и получение комбинации включено - вернем макс. комб. клавиш
            self.stop_get_comb()

        self.__col_pressed -= 1
        if key in self.__pressed:
            self.__pressed.remove(key)

        if self.__col_pressed == 0:
            self.__pressed.clear()

    def get_set_comb_from_str(self, src_str=''):
        result = set()
        result = eval(src_str)
        return result

    def update_search_combs(self, rules_list):
        self.__search_combs.clear()
        for rule in rules_list:
            search_comb = self.get_set_comb_from_str(rule[1])
            self.__search_combs.append(search_comb)

    def ctrl_v(self):
        cont = keyboard.Controller()
        cont.press(keyboard.Key.cmd_l)
        cont.press('v')
        cont.release('v')
        cont.release(keyboard.Key.cmd_l)
        cont = ''

    def get_combination(self):
        self.start_get_comb()
        while self.__is_get_comb:
            pass
        return self._max_combination
