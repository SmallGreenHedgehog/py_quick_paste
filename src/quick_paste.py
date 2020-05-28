# -*- coding: utf-8 -*-

import os, sys
import pyperclip
from PySide2 import QtWidgets, QtCore, QtGui
from ui_files.config_window import Ui_Form as ConfWindow
from ui_files.edit_comb_window import Ui_Form as EditWindow
from quick_keyboard import KeyMonitor
from quick_base import BaseManager
from time import sleep


class ConfigWindowForm(QtWidgets.QWidget):
    def __init__(self):
        super(ConfigWindowForm, self).__init__()

        self.ui = ConfWindow()
        self.ui.setupUi(self)

        # Список доп настроек
        self.ui.checkBox_w_hidden_win_start.setChecked(manager_w_icon_window.get_w_hidden_win_start())
        self.ui.checkBox_pos_on_first_comb.setChecked(manager_w_icon_window.get_pos_on_first_comb())
        self.ui.checkBox_restore_clipboard.setChecked(manager_w_icon_window.get_restore_clipboard())

        # Таблица шаблонов
        self.ui.tableWidget.hideColumn(0)
        self.ui.tableWidget.hideColumn(1)
        self.ui.tableWidget.setColumnWidth(2, 171)
        self.ui.tableWidget.setColumnWidth(3, 228)
        self.ui.tableWidget.setColumnWidth(4, 253)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Присоединяем слоты
        self.ui.pushButton_append.clicked.connect(self.append_rule)
        self.ui.tableWidget.cellDoubleClicked.connect(self.__on_double_click_table)
        self.ui.pushButton_remove.clicked.connect(self.__remove_rule)
        self.ui.pushButton_clear.clicked.connect(self.__clear_rule)

        self.ui.pushButton_move_top.clicked.connect(self.__move_top)
        self.ui.pushButton_move_higer.clicked.connect(self.__move_higer)
        self.ui.pushButton_move_lower.clicked.connect(self.__move_lower)
        self.ui.pushButton_move_lower.clicked.connect(self.__move_bottom)

        self.ui.pushButton_hide.clicked.connect(self.hide_window)

        self.ui.checkBox_w_hidden_win_start.stateChanged.connect(self.set_w_hidden_win_start)
        self.ui.checkBox_pos_on_first_comb.stateChanged.connect(self.set_pos_on_first_comb)
        self.ui.checkBox_restore_clipboard.stateChanged.connect(self.set_restore_clipboard)

        self.update_table()

    def append_rule(self):
        edit_window.set_edit_id()
        self.hide()
        edit_window.show()

    def edit_rule(self, edit_id):
        edit_window.set_edit_id(edit_id)
        self.hide()
        edit_window.show()

    def __on_double_click_table(self):
        edit_row_num = self.ui.tableWidget.currentRow()
        edit_id = int(self.ui.tableWidget.item(edit_row_num, 0).text())
        self.edit_rule(edit_id)

    def __remove_rule(self):
        sel_row_num = self.ui.tableWidget.currentRow()
        if not sel_row_num < 0:
            sel_rule_id = int(self.ui.tableWidget.item(sel_row_num, 0).text())
            if manager_w_icon_window.__base.remove_rule(sel_rule_id):
                self.update_table()

    def __clear_rule(self):
        if manager_w_icon_window.__base.remove_all_rules():
            self.update_table()

    def __move_top(self):
        # TODO реализовать функционал перемещения комбинации в начало списка
        print('Смотри TODO')

    def __move_bottom(self):
        # TODO реализовать функционал перемещения комбинации в конец списка
        print('Смотри TODO')

    def __move_higer(self):
        # TODO реализовать функционал перемещения комбинации в списке на позицию выше
        print('Смотри TODO')

    def __move_lower(self):
        # TODO реализовать функционал перемещения комбинации в списке на позицию ниже
        print('Смотри TODO')

    def set_w_hidden_win_start(self):
        manager_w_icon_window.set_w_hidden_win_start(self.ui.checkBox_w_hidden_win_start.isChecked())

    def set_pos_on_first_comb(self):
        manager_w_icon_window.set_pos_on_first_comb(self.ui.checkBox_pos_on_first_comb.isChecked())

    def set_restore_clipboard(self):
        manager_w_icon_window.set_restore_clipboard(self.ui.checkBox_restore_clipboard.isChecked())

    def update_table(self):
        self.ui.tableWidget.setRowCount(0)
        rules_list = manager_w_icon_window.get_all_rules_from_base()

        # Обновим так же список искомых комбинаций, чтобы не дергать лишний раз базу
        # print('rules_list = %s' % rules_list)
        manager_w_icon_window.update_search_combs_list_in_keys(rules_list)

        row_pos = 0
        for rule in rules_list:
            self.ui.tableWidget.insertRow(row_pos)

            col_pos = 0
            for rule_item in rule:
                item = QtWidgets.QTableWidgetItem(str(rule_item))
                self.ui.tableWidget.setItem(row_pos, col_pos, item)
                col_pos += 1
            row_pos += 1

    def hide_window(self):
        self.hide()
        manager_w_icon_window.main_window_action.setChecked(False)


class EditWindowForm(QtWidgets.QWidget):
    def __init__(self):
        super(EditWindowForm, self).__init__()

        self.ui = EditWindow()
        self.ui.setupUi(self)

        self.__act_comb = ''
        self.__edit_id = None

        # Присоединяем слоты
        self.ui.pushButton_set_comb.clicked.connect(self.set_comb)
        self.ui.pushButton_save.clicked.connect(self.save_rule)
        self.ui.pushButton_cancel.clicked.connect(self.cancel_rule)

    @property
    def edit_id(self):
        return self.__edit_id

    def set_edit_id(self, edit_id=None):
        self.__edit_id = edit_id

    def __rule_is_correct(self):
        comb_str_is_empty = not self.ui.label_comb.text().strip()
        name_str_is_empty = not self.ui.lineEdit.text().strip()
        txt_str_is_empty = not self.ui.plainTextEdit.toPlainText().strip()
        result = not (comb_str_is_empty or name_str_is_empty or txt_str_is_empty)
        return result

    def set_comb(self):
        self.__act_comb = manager_w_icon_window.__keys.get_combination()
        if self.__act_comb is not None:
            self.ui.label_comb.setText(str(self.__act_comb))
            self.ui.label_comb.repaint()

    def save_rule(self):
        if self.__rule_is_correct():
            ok = manager_w_icon_window.__base.set_rule(
                self.ui.label_comb.text().strip()
                , self.ui.lineEdit.text().strip()
                , self.ui.plainTextEdit.toPlainText()
                , self.__edit_id
            )

            if ok:
                conf_window.update_table()

            self.hide()
            manager_w_icon_window.main_window_action.setChecked(True)
            conf_window.show()
        else:
            msg_box = QtWidgets.QMessageBox(self)
            msg_text = 'Не все поля правила заполнены корректно.' \
                       '<br>Исправьте ошибки и попробуйте сохранить повторно.'
            msg_box.setText(msg_text)
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.show()

    def cancel_rule(self):
        self.hide()
        manager_w_icon_window.main_window_action.setChecked(True)
        conf_window.show()

    def showEvent(self, event):
        if self.__edit_id != None:
            act_rule = manager_w_icon_window.__base.get_rule_by_id(self.__edit_id)
            self.__act_comb = act_rule[2]
            self.ui.lineEdit.setText(act_rule[3])
            self.ui.plainTextEdit.setPlainText(act_rule[4])
            self.ui.label_comb.setText(self.__act_comb)
        else:
            self.__act_comb = ''
            self.ui.label_comb.setText(self.__act_comb)
            self.ui.lineEdit.clear()
            self.ui.plainTextEdit.clear()


class SystemMangerWithIcon(QtWidgets.QSystemTrayIcon):
    def find_tray_icon_pos(self):
        x_pos = self.geometry().x()
        if x_pos < 0:
            max_x_pos = QtWidgets.QDesktopWidget().geometry().getCoords()[2]
            x_pos = max_x_pos + x_pos + 1
        self.__tray_icon_x_pos = x_pos + 15
        # print('self.__tray_icon_x_pos = %s' % self.__tray_icon_x_pos)

    def __init__(self, parent=None):
        icon_path = os.path.join(os.path.dirname(sys.argv[0]), 'ui_files/icon.png')
        # print('icon_path = %s' % icon_path)
        icon = QtGui.QIcon(icon_path)
        super(SystemMangerWithIcon, self).__init__(icon, parent)

        self.main_menu = QtWidgets.QMenu()
        self.main_window_action = self.main_menu.addAction('Настройки')
        self.main_window_action.setCheckable(True)
        self.exit_action = self.main_menu.addAction("Выход")
        self.setContextMenu(self.main_menu)

        self.templates_menu = QtWidgets.QMenu()

        # Присоединяем слоты
        self.activated.connect(self.find_tray_icon_pos)
        self.main_window_action.triggered.connect(self.__main_window_show)
        self.exit_action.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.__base = BaseManager()
        self.__keys = KeyMonitor()
        self.__keys.comb_found.connect(self.select_template_event)

        # Свойства
        self.__pos_on_first_comb = (self.__base.get_parameter('pos_on_first_comb') == 'True')
        self.__restore_clipboard = (self.__base.get_parameter('restore_clipboard') == 'True')

        # Получаем координаты иконки для клика
        self.__last_cursor_pos = QtGui.QCursor().pos()

        self.find_timer = QtCore.QTimer()
        self.find_timer.singleShot(500, self.find_tray_icon_pos)

        # TODO реализовать функционал проверки включенного универсального доступа и вывода запроса
        test_text_script = '\n' \
                           'tell application "System Preferences"\n' \
                           '    set securityPane to pane id "com.apple.preference.security"\n' \
                           '    tell securityPane to reveal anchor "Privacy_Accessibility"\n' \
                           '    activate\n' \
                           'end tell\n' \
                           ''

    def get_all_rules_from_base(self):
        return self.__base.get_all_rules()

    def update_search_combs_list_in_keys(self, rules_list):
        self.__keys.update_search_combs(rules_list)

    def get_w_hidden_win_start(self):
        return self.__base.get_parameter('w_hidden_win_start') == 'True'

    def set_w_hidden_win_start(self, new_state=True):
        self.__base.set_parameter('w_hidden_win_start', new_state)

    def get_pos_on_first_comb(self):
        return self.__pos_on_first_comb

    def set_pos_on_first_comb(self, new_state=True):
        self.__pos_on_first_comb = new_state
        self.__base.set_parameter('pos_on_first_comb', new_state)

    def set_restore_clipboard(self, new_state=True):
        self.__restore_clipboard = new_state
        self.__base.set_parameter('restore_clipboard', new_state)

    def get_restore_clipboard(self):
        return self.__restore_clipboard

    def return_back_main_menu(self):
        self.setContextMenu(self.main_menu)

    def paste_selected_template(self):
        need_save_restore_clipboard = manager_w_icon_window.get_restore_clipboard()
        if need_save_restore_clipboard:
            tmp_clipboard = pyperclip.paste()

        rule_id = self.sender().property('rule_id')
        rule_txt = self.__base.get_rule_by_id(rule_id)[3]
        pyperclip.copy(rule_txt)  # Помещаем текст выбранного шаблона в буффер
        sleep(0.2)
        self.__keys.cmd_paste()  # Вызываем комбинацию встаки из буфера обмена
        self.return_back_main_menu()  # Восстанавливаем главное меню
        self.__keys.pos_mouse(self.__last_cursor_pos.x(), self.__last_cursor_pos.y())  # Возвращаем курсор на место

        if need_save_restore_clipboard:
            pyperclip.copy(tmp_clipboard)

    def fill_templates_menu(self, templates_list):
        self.templates_menu.clear()
        action_temp = []
        num_temp = 0
        for temp in templates_list:
            temp_id = temp[0]
            temp_name = temp[1]
            action_temp.append(self.templates_menu.addAction(temp_name))
            action_temp[num_temp].setProperty('rule_id', temp_id)
            action_temp[num_temp].triggered.connect(self.paste_selected_template)
            num_temp += 1

        self.templates_menu.addSeparator()
        main_menu_action = self.templates_menu.addAction('Главное меню')
        main_menu_action.triggered.connect(self.return_back_main_menu)

    def select_template_event(self, last_comb_found):
        # print('COMBINATION SLOT FUNC')

        templates_list = self.__base.get_list_rules_by_comb(last_comb_found)
        if len(templates_list) == 1:
            self.templates_menu.clear()

            single_temp_act = self.templates_menu.addAction(templates_list[0][1])
            single_temp_act.setProperty('rule_id', templates_list[0][0])
            single_temp_act.triggered.connect(self.paste_selected_template)

            single_temp_act.triggered.emit()
        else:
            self.fill_templates_menu(templates_list)
            self.setContextMenu(self.templates_menu)
            self.__last_cursor_pos = QtGui.QCursor().pos()
            self.__keys.click_mouse_on_tray_icon_menu(self.__tray_icon_x_pos, self.get_pos_on_first_comb())

    def __main_window_show(self):
        if self.main_window_action.isChecked():
            conf_window.show()
            getattr(conf_window, "raise")()
            conf_window.activateWindow()
        else:
            conf_window.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('py_quick_paste')

    manager_w_icon_window = SystemMangerWithIcon()
    conf_window = ConfigWindowForm()
    edit_window = EditWindowForm()

    manager_w_icon_window.show()
    if not manager_w_icon_window.get_w_hidden_win_start():
        manager_w_icon_window.main_window_action.trigger()

    sys.exit(app.exec_())
