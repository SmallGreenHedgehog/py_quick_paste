from pynput import keyboard


class KeyMonitor():
    def start_listen(self):
        self.__listener.start()

    def stop_listen(self):
        self.__listener.stop()

    def __init__(self, parent=None):
        self.__listener = ''
        self.__search_combs = set()
        self.__pressed = set()
        self.__col_pressed = 0
        self.__is_get_comb = False
        self.__max_get_comb = 0
        self.__comb_timer_started = False
        self._max_combination = set()
        self.__listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release
        )
        self.start_listen()

    def start_get_comb(self):
        self._max_combination = set()
        self.__max_get_comb = 0
        self.__is_get_comb = True

    def stop_get_comb(self):
        self.__is_get_comb = False
        self.__comb_timer_started = False

    def __on_press(self, key):
        self.__col_pressed += 1
        self.__pressed.add(key)
        print('pressed = %s' % self.__pressed)

        if self.__col_pressed > 1:
            found = False
            for search_comb in self.__search_combs:
                if all(c in self.__pressed for c in search_comb):
                    print('СОВПАЛО')
        # TODO реализовать функционал проверки совпадения комбинации со списком из БД

        # TODO реализовать функционал вывода списка наименований правил для выбора
        # TODO реализовать функционал вставки текста из БД в активное окно

        if self.__is_get_comb:  # Начинаем получать комбинацию
            if self.__col_pressed > self.__max_get_comb:
                self._max_combination = self.__pressed.copy()
                self.__max_get_comb += 1

    def __on_release(self, key):
        if self.__is_get_comb and self.__col_pressed > 1:  # Отпустили хоть одну клавишу и получение комбинации включено - вернем макс. комб. клавиш
            self.stop_get_comb()

        self.__col_pressed -= 1
        if key in self.__pressed:
            self.__pressed.remove(key)

        if self.__col_pressed == 0:
            self.__pressed.clear()

    def update_search_combs(self, rules_list):
        self.__search_combs.clear()
        for rule in rules_list:
            self.__search_combs.add(rule[1])
        print(self.__search_combs)


    def get_combination(self):
        self.start_get_comb()
        while self.__is_get_comb:
            pass
        return self._max_combination
