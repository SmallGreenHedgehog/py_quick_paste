# -*- coding: utf-8 -*-
from threading import Timer
from pynput import keyboard, mouse
from PySide2.QtCore import QObject, Signal
from time import sleep
import os


class KeyMonitor(QObject):
    comb_found = Signal(enumerate)

    def __clear_released(self):
        self.__col_pressed = 0
        self.__pressed.clear()
        # print('released combs was cleared')

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
        self.__timer_clear_released = Timer(0.5, self.__clear_released)
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
        # print('pressed = %s' % self.__pressed)
        # print('col pressed = %s' % self.__col_pressed)

        if not self.__timer_clear_released.is_alive():
            self.__timer_clear_released = Timer(0.5, self.__clear_released)
            self.__timer_clear_released.start()

        if self.__is_get_comb:  # Начинаем получать комбинацию
            if self.__col_pressed > self.__max_key_count_comb:
                self._max_combination = self.__pressed.copy()
                self.__max_key_count_comb += 1
        else:
            if self.__col_pressed > 1:
                for search_comb in self.__search_combs:
                    if all(p in search_comb for p in self.__pressed) and all(s in self.__pressed for s in search_comb):
                        print('Combination %s was found' % search_comb)
                        self.__last_comb_found = search_comb.copy()
                        self.comb_found.emit(self.__last_comb_found)
                        break

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

    def get_keyboard_layout(self):
        return os.popen(
            "defaults read ~/Library/Preferences/com.apple.HIToolbox.plist AppleSelectedInputSources | "
            "egrep -w 'KeyboardLayout Name' | "
            "sed -E 's/^.+ = \"?([^\"]+)\"?;$/\\1/'").read()[:-1]

    def change_keyboard_layout(self, layout_name='ABC', layout_num=-1):
        script_text = '\n' \
                      'tell application "System Events" to tell process "SystemUIServer"\n' \
                      ' tell (1st menu bar item of menu bar 1 whose description is "text input") to {click, click (menu item %s of menu 1)}\n' \
                      'end tell\n' \
                      'delay 0.25\n' % (layout_name if layout_num < 0 else f'"{layout_name}"')
        # print("""osascript -e '%s'""" % script_text)
        os.system("""osascript -e '%s'""" % script_text)

    def cmd_v(self):
        layout_name = self.get_keyboard_layout()
        need_replace = (layout_name != 'ABC')
        print('neneed_replace = %s' % str(need_replace))
        if need_replace:
            self.change_keyboard_layout(1)
        os.system("""osascript -e 'tell application "System Events" to keystroke "v" using command down'""")
        if need_replace:
            self.change_keyboard_layout(2)

    def cmd_tab(self):
        cont = keyboard.Controller()
        cont.press(keyboard.Key.cmd)
        cont.press(keyboard.Key.tab)
        cont.release(keyboard.Key.tab)
        cont.release(keyboard.Key.cmd)
        cont = ''

    def pos_mouse_on_tray_icon_menu(self, tray_icon_x_pos):
        cont = mouse.Controller()
        current_pos = cont.position
        cont.move(tray_icon_x_pos - current_pos[0], 0 - current_pos[1])
        sleep(0.25)
        cont.click(mouse.Button.left, 1)
        cont.move(0, 55)
        cont = ''

    def pos_mouse(self, x_pos, y_pos):
        cont = mouse.Controller()
        current_pos = cont.position
        cont.move(x_pos - current_pos[0], y_pos - current_pos[1])
        cont = ''

    def get_combination(self):
        self.start_get_comb()
        while self.__is_get_comb:
            pass
        return self._max_combination
