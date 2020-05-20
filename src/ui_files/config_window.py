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
        Form.resize(905, 571)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_move_top = QPushButton(self.tab)
        self.pushButton_move_top.setObjectName(u"pushButton_move_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_move_top.sizePolicy().hasHeightForWidth())
        self.pushButton_move_top.setSizePolicy(sizePolicy1)
        self.pushButton_move_top.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.pushButton_move_top)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_move_higer = QPushButton(self.tab)
        self.pushButton_move_higer.setObjectName(u"pushButton_move_higer")

        self.verticalLayout_4.addWidget(self.pushButton_move_higer)

        self.pushButton_move_lower = QPushButton(self.tab)
        self.pushButton_move_lower.setObjectName(u"pushButton_move_lower")

        self.verticalLayout_4.addWidget(self.pushButton_move_lower)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.pushButton_move_bottom = QPushButton(self.tab)
        self.pushButton_move_bottom.setObjectName(u"pushButton_move_bottom")

        self.verticalLayout_4.addWidget(self.pushButton_move_bottom)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_append = QPushButton(self.tab)
        self.pushButton_append.setObjectName(u"pushButton_append")

        self.horizontalLayout.addWidget(self.pushButton_append)

        self.pushButton_remove = QPushButton(self.tab)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.horizontalLayout.addWidget(self.pushButton_remove)

        self.pushButton_clear = QPushButton(self.tab)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout.addWidget(self.pushButton_clear)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_pos_on_first_comb = QCheckBox(self.tab_2)
        self.checkBox_pos_on_first_comb.setObjectName(u"checkBox_pos_on_first_comb")

        self.verticalLayout_3.addWidget(self.checkBox_pos_on_first_comb)

        self.checkBox_restore_clipboard = QCheckBox(self.tab_2)
        self.checkBox_restore_clipboard.setObjectName(u"checkBox_restore_clipboard")

        self.verticalLayout_3.addWidget(self.checkBox_restore_clipboard)

        self.checkBox_w_hidden_win_start = QCheckBox(self.tab_2)
        self.checkBox_w_hidden_win_start.setObjectName(u"checkBox_w_hidden_win_start")

        self.verticalLayout_3.addWidget(self.checkBox_w_hidden_win_start)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.pushButton_hide = QPushButton(Form)
        self.pushButton_hide.setObjectName(u"pushButton_hide")

        self.verticalLayout_2.addWidget(self.pushButton_hide)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"py_quick_paste", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Pos", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442", None));
        self.pushButton_move_top.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.pushButton_move_higer.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0448\u0435", None))
        self.pushButton_move_lower.setText(QCoreApplication.translate("Form", u"\u041d\u0438\u0436\u0435", None))
        self.pushButton_move_bottom.setText(QCoreApplication.translate("Form", u"\u0412\u043d\u0438\u0437", None))
        self.pushButton_append.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_remove.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438", None))
        self.checkBox_pos_on_first_comb.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u0438\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438 \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u0438\u0442\u044c \u043d\u0430 \u043f\u0435\u0440\u0432\u0443\u044e \u0432 \u0441\u043f\u0438\u0441\u043a\u0435", None))
        self.checkBox_restore_clipboard.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0442\u044c \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430 \u043f\u043e\u0441\u043b\u0435 \u0432\u0441\u0442\u0430\u0432\u043a\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438", None))
        self.checkBox_w_hidden_win_start.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u0441\u043a\u0440\u044b\u0442\u043e\u0439 \u0432 \u0442\u0440\u0435\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0414\u043e\u043f. \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pushButton_hide.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

