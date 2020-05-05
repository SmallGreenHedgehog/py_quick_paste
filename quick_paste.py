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

        self.ui.tableWidget.hideColumn(0)
        self.ui.tableWidget.setColumnWidth(1, 171)
        self.ui.tableWidget.setColumnWidth(2, 228)
        self.ui.tableWidget.setColumnWidth(3, 253)
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Присоединяем слоты
        self.ui.pushButton_append.clicked.connect(self.append_rule)
        self.ui.pushButton_remove.clicked.connect(self.remove_rule)
        self.ui.pushButton_clear.clicked.connect(self.clear_rule)
        self.ui.pushButton_hide.clicked.connect(self.hide_window)
        self.ui.tableWidget.cellDoubleClicked.connect(self.edit_rule)

        self.update_table()

    def update_table(self):
        self.ui.tableWidget.setRowCount(0)
        rules_list = tray_icon_window.base.get_all_rules()

        # Обновим так же списко искомых комбинаций, чтобы не дергать лишний раз базу
        tray_icon_window.keys.update_search_combs(rules_list)

        row_pos = 0
        for rule in rules_list:
            self.ui.tableWidget.insertRow(row_pos)

            col_pos = 0
            for rule_item in rule:
                item = QtWidgets.QTableWidgetItem(str(rule_item))
                self.ui.tableWidget.setItem(row_pos, col_pos, item)
                col_pos += 1
            row_pos += 1

    def append_rule(self):
        edit_window.set_edit_id()
        self.hide()
        edit_window.show()

    def edit_rule(self):
        edit_row_num = self.ui.tableWidget.currentRow()
        edit_id = int(self.ui.tableWidget.item(edit_row_num, 0).text())
        edit_window.set_edit_id(edit_id)
        self.hide()
        edit_window.show()

    def remove_rule(self):
        sel_row_num = self.ui.tableWidget.currentRow()
        if not sel_row_num < 0:
            sel_rule_id = int(self.ui.tableWidget.item(sel_row_num, 0).text())
            if tray_icon_window.base.remove_rule(sel_rule_id):
                self.update_table()

    def clear_rule(self):
        if tray_icon_window.base.remove_all_rules():
            self.update_table()

    def hide_window(self):
        self.hide()
        tray_icon_window.main_window_action.setChecked(False)


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
        self.__act_comb = tray_icon_window.keys.get_combination()
        self.ui.label_comb.setText(str(self.__act_comb))

    def save_rule(self):
        if self.__rule_is_correct():
            ok = tray_icon_window.base.set_rule(
                self.ui.label_comb.text().strip()
                , self.ui.lineEdit.text().strip()
                , self.ui.plainTextEdit.toPlainText()
                , self.__edit_id
            )

            if ok:
                conf_window.update_table()

            self.hide()
            tray_icon_window.main_window_action.setChecked(True)
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
        tray_icon_window.main_window_action.setChecked(True)
        conf_window.show()

    def showEvent(self, event):
        if self.__edit_id != None:
            act_rule = tray_icon_window.base.get_rule_by_id(self.__edit_id)
            self.__act_comb = act_rule[1]
            self.ui.lineEdit.setText(act_rule[2])
            self.ui.plainTextEdit.setPlainText(act_rule[3])
            self.ui.label_comb.setText(self.__act_comb)
        else:
            self.__act_comb = ''
            self.ui.label_comb.setText(self.__act_comb)
            self.ui.lineEdit.clear()
            self.ui.plainTextEdit.clear()


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

        self.base = BaseManager()
        self.keys = KeyMonitor()

    def main_window_show(self):
        if self.main_window_action.isChecked():
            conf_window.show()
        else:
            conf_window.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    tray_icon_window = SystemTrayIcon()
    conf_window = ConfigWindowForm()
    edit_window = EditWindowForm()

    tray_icon_window.show()
    sys.exit(app.exec_())
