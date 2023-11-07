# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(652, 778)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(360, 100))
        font = QFont()
        font.setFamilies([u"\uad74\ub9bc"])
        font.setPointSize(24)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_C = QPushButton(self.centralwidget)
        self.pushButton_C.setObjectName(u"pushButton_C")
        self.pushButton_C.setMinimumSize(QSize(70, 60))
        font1 = QFont()
        font1.setFamilies([u"\uad74\ub9bc"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_C.setFont(font1)
        self.pushButton_C.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_C, 0, 2, 1, 1)

        self.pushButton_DEL = QPushButton(self.centralwidget)
        self.pushButton_DEL.setObjectName(u"pushButton_DEL")
        self.pushButton_DEL.setMinimumSize(QSize(70, 60))
        self.pushButton_DEL.setFont(font1)
        self.pushButton_DEL.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_DEL, 0, 3, 1, 1)

        self.pushButton_fraction = QPushButton(self.centralwidget)
        self.pushButton_fraction.setObjectName(u"pushButton_fraction")
        self.pushButton_fraction.setMinimumSize(QSize(70, 60))
        self.pushButton_fraction.setFont(font1)
        self.pushButton_fraction.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_fraction, 1, 0, 1, 1)

        self.pushButton_percent = QPushButton(self.centralwidget)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        self.pushButton_percent.setMinimumSize(QSize(70, 60))
        self.pushButton_percent.setFont(font1)
        self.pushButton_percent.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_percent, 0, 0, 1, 1)

        self.pushButton_CE = QPushButton(self.centralwidget)
        self.pushButton_CE.setObjectName(u"pushButton_CE")
        self.pushButton_CE.setMinimumSize(QSize(70, 60))
        self.pushButton_CE.setFont(font1)
        self.pushButton_CE.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_CE, 0, 1, 1, 1)

        self.pushButton_square = QPushButton(self.centralwidget)
        self.pushButton_square.setObjectName(u"pushButton_square")
        self.pushButton_square.setMinimumSize(QSize(70, 60))
        self.pushButton_square.setFont(font1)
        self.pushButton_square.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_square, 1, 1, 1, 1)

        self.pushButton_root = QPushButton(self.centralwidget)
        self.pushButton_root.setObjectName(u"pushButton_root")
        self.pushButton_root.setMinimumSize(QSize(70, 60))
        self.pushButton_root.setFont(font1)
        self.pushButton_root.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_root, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(70, 60))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(70, 60))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(70, 60))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_divide = QPushButton(self.centralwidget)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setMinimumSize(QSize(70, 60))
        self.pushButton_divide.setFont(font1)
        self.pushButton_divide.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_divide, 1, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(70, 60))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_mult = QPushButton(self.centralwidget)
        self.pushButton_mult.setObjectName(u"pushButton_mult")
        self.pushButton_mult.setMinimumSize(QSize(70, 60))
        self.pushButton_mult.setFont(font1)
        self.pushButton_mult.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_mult, 2, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(70, 60))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(70, 60))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_minus = QPushButton(self.centralwidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setMinimumSize(QSize(70, 60))
        self.pushButton_minus.setFont(font1)
        self.pushButton_minus.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_minus, 3, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(70, 60))
        font2 = QFont()
        font2.setFamilies([u"\uad74\ub9bc"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setKerning(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(70, 60))
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)

        self.pushButton_dot = QPushButton(self.centralwidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setMinimumSize(QSize(70, 60))
        self.pushButton_dot.setFont(font1)
        self.pushButton_dot.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_dot, 5, 2, 1, 1)

        self.pushButton_negative_positive = QPushButton(self.centralwidget)
        self.pushButton_negative_positive.setObjectName(u"pushButton_negative_positive")
        self.pushButton_negative_positive.setMinimumSize(QSize(70, 60))
        self.pushButton_negative_positive.setFont(font1)
        self.pushButton_negative_positive.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_negative_positive, 5, 0, 1, 1)

        self.pushButton_plus = QPushButton(self.centralwidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setMinimumSize(QSize(70, 60))
        self.pushButton_plus.setFont(font1)
        self.pushButton_plus.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)

        self.pushButton_equal = QPushButton(self.centralwidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setMinimumSize(QSize(70, 60))
        self.pushButton_equal.setFont(font1)
        self.pushButton_equal.setStyleSheet(u"background-color: rgb(160, 235, 255);")

        self.gridLayout.addWidget(self.pushButton_equal, 5, 3, 1, 1)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(70, 60))
        self.pushButton_0.setFont(font1)
        self.pushButton_0.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_0, 5, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(70, 60))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(194, 194, 194);")

        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_DEL.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.pushButton_fraction.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.pushButton_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pushButton_square.setText(QCoreApplication.translate("MainWindow", u"x^2", None))
        self.pushButton_root.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_mult.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_negative_positive.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
    # retranslateUi

