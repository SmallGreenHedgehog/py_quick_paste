import sys
from PySide2 import QtWidgets, QtCore, QtGui
from ui_files.config_window import Ui_Form as ConfWindow
from ui_files.edit_comb_window import Ui_Form as EditWindow
from quick_keyboard import KeyMonitor
from quick_base import BaseManager


class ConfigWindowForm(QtWidgets.QWidget):
    def __init__(self):
        super(ConfigWindowForm, self).__init__()

        self.ui = ConfWindow()
        self.ui.setupUi(self)

        # Присоединяем слоты
        self.ui.pushButton_append.clicked.connect(self.append_rule)
        self.ui.pushButton_remove.clicked.connect(self.remove_rule)
        self.ui.pushButton_remove.clicked.connect(self.clear_rule)
        self.ui.pushButton_hide.clicked.connect(self.hide_window)

    def append_rule(self):
        edit_window.set_is_edit(False)
        self.hide()
        edit_window.show()

    def remove_rule(self):
        print('Удаляем правило из БД')

    def clear_rule(self):
        print('Очищаем записи БД')

    def hide_window(self):
        self.hide()
        tray_icon_window.main_window_action.setChecked(False)


class EditWindowForm(QtWidgets.QWidget):
    def __init__(self):
        super(EditWindowForm, self).__init__()

        self.ui = EditWindow()
        self.ui.setupUi(self)

        self.act_comb = ''

        # Присоединяем слоты
        self.ui.pushButton_set_comb.clicked.connect(self.set_comb)
        self.ui.pushButton_save.clicked.connect(self.save_rule)
        self.ui.pushButton_cancel.clicked.connect(self.cancel_rule)

        self.__is_edit = False
        self.__edit_id = None

    def __rule_is_correct(self):
        # TODO реализовать функционал корректности заполнения всех полей
        return False

    def set_comb(self):
        self.act_comb = tray_icon_window.keys.get_combination()
        self.ui.label_comb.setText(str(self.act_comb))

    def save_rule(self):
        print('Пытаемся сохранить правило')
        if self.__rule_is_correct():
            print('Сохраняем правило')
            # TODO реализовать функционал сохранения или обновления правила в БД

            self.hide()
            tray_icon_window.main_window_action.setChecked(True)
            conf_window.show()
        else:
            print('Правило заполнено не корректно')

    def cancel_rule(self):
        print('Отменяем сохранение правила')
        self.hide()
        tray_icon_window.main_window_action.setChecked(True)
        conf_window.show()

    def set_is_edit(self, is_edit=False, edit_id=None):
        self.__is_edit = is_edit
        if is_edit:
            self.__edit_id = edit_id

    @property
    def get_is_edit(self):
        return self.__is_edit


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, parent=None):
        icon = QtGui.QIcon(r"ui_files/Icon.png")
        super(SystemTrayIcon, self).__init__(icon, parent)
        self.menu = QtWidgets.QMenu(parent)
        self.main_window_action = self.menu.addAction('Главное меню')
        self.main_window_action.setCheckable(True)
        self.exit_action = self.menu.addAction("Выход")
        self.setContextMenu(self.menu)

        # Присоединяем слоты
        self.main_window_action.triggered.connect(self.main_window_show)
        self.main_window_action.triggered.connect(self.main_window_show)
        self.exit_action.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.keys = KeyMonitor()
        self.base = BaseManager()

    def main_window_show(self):
        if self.main_window_action.isChecked():
            conf_window.show()
        else:
            conf_window.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    conf_window = ConfigWindowForm()
    edit_window = EditWindowForm()
    tray_icon_window = SystemTrayIcon()

    tray_icon_window.show()
    sys.exit(app.exec_())
