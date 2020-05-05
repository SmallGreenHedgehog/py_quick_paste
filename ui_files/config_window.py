# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(596, 510)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_append = QPushButton(Form)
        self.pushButton_append.setObjectName(u"pushButton_append")

        self.horizontalLayout.addWidget(self.pushButton_append)

        self.pushButton_remove = QPushButton(Form)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.horizontalLayout.addWidget(self.pushButton_remove)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout.addWidget(self.pushButton_clear)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_hide = QPushButton(Form)
        self.pushButton_hide.setObjectName(u"pushButton_hide")

        self.verticalLayout.addWidget(self.pushButton_hide)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"py_quick_paste", None))
        self.pushButton_append.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_remove.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_hide.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

