import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

# 전역 변수 선언
temp_operator = None
temp_val1 = 0
temp_val2 = 0

form_main = uic.loadUiType("calculator2.ui")[0]  # ui 파일 불러오기


class MainWindow(QMainWindow, form_main):
    def __init__(self):
        super().__init__()
        self.initUI(),
        self.show()

    def initUI(self):
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.button_1)  # 버튼 클릭시 연결 되는 함수
        self.pushButton_2.clicked.connect(self.button_2)
        self.pushButton_3.clicked.connect(self.button_3)
        self.pushButton_4.clicked.connect(self.button_4)
        self.pushButton_5.clicked.connect(self.button_5)
        self.pushButton_6.clicked.connect(self.button_6)
        self.pushButton_7.clicked.connect(self.button_7)
        self.pushButton_8.clicked.connect(self.button_8)
        self.pushButton_9.clicked.connect(self.button_9)
        self.pushButton_0.clicked.connect(self.button_0)
        self.pushButton_negative_positive.clicked.connect(self.negative_positive)
        self.pushButton_dot.clicked.connect(self.button_dot)
        self.pushButton_DEL.clicked.connect(self.del_num)
        self.pushButton_C.clicked.connect(self.clr_num)
        self.pushButton_CE.clicked.connect(self.clr_num)
        self.pushButton_plus.clicked.connect(self.plus)
        self.pushButton_minus.clicked.connect(self.minus)
        self.pushButton_mult.clicked.connect(self.multiple)
        self.pushButton_divide.clicked.connect(self.divide)
        self.pushButton_equal.clicked.connect(self.equal)
        self.pushButton_percent.clicked.connect(self.percent)
        self.pushButton_fraction.clicked.connect(self.fraction)
        self.pushButton_square.clicked.connect(self.square)
        self.pushButton_root.clicked.connect(self.root)


    def button_1(self):
        self.number("1")

    def button_2(self):
        self.number("2")

    def button_3(self):
        self.number("3")

    def button_4(self):
        self.number("4")

    def button_5(self):
        self.number("5")

    def button_6(self):
        self.number("6")

    def button_7(self):
        self.number("7")

    def button_8(self):
        self.number("8")

    def button_9(self):
        self.number("9")

    def button_0(self):
        self.number("0")

    def negative_positive(self):
        exist_text = self.lineEdit.text()
        ans = float(exist_text) * (-1)
        self.lineEdit.setText(str(ans))

    def button_dot(self):
        if "." not in self.lineEdit.text()[:]:
            self.number(".")

    def number(self, num):
        try:
            # if(exist_text[-1].isnull==False):
            if temp_operator is not None:
                # print("현재 라인에디트 안의 원소",self.lineEdit.text()[:])
                if (temp_operator == "+") | (temp_operator == "-") | (temp_operator == "*") | (temp_operator == "/"):
                    if self.lineEdit.text()[:] == temp_operator:
                        self.lineEdit.setText("")

        except IndexError as e:
            print("for Index Error Handling")
            # self.lineEdit.setText(str(e))

        exist_text = self.lineEdit.text()  # lineEdit값을 가져와서 exist_text에 저장
        self.lineEdit.setText(exist_text + num)  # 기존값 + 새로 입력된 값

    def del_num(self):
        exist_text = self.lineEdit.text()
        self.lineEdit.setText(exist_text[:-1])

    def clr_num(self):
        self.lineEdit.setText("")

    def plus(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력 되면 그 중 맨 마지막으로 입력 받은 기호만이 수행 된다.
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        global temp_val1
        temp_val1 = exist_text[:]
        self.lineEdit.setText("")  # 부호를 입력 받은 순간 기존에 입력 받아 뒀던 숫자는 가린다
        global temp_operator
        temp_operator = "+"
        self.lineEdit.setText(temp_operator)

    def minus(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력되면 그 중 맨 마지막으로 입력 받은 기호만이 수행된다.
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        global temp_val1
        temp_val1 = exist_text[:]
        self.lineEdit.setText("")  # 부호를 입력 받은 순간 기존에 입력 받아 뒀던 숫자는 가린다
        global temp_operator
        temp_operator = "-"
        self.lineEdit.setText(temp_operator)

    def multiple(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력되면 그 중 맨 마지막으로 입력 받은 기호만이 수행된다.
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        global temp_val1
        temp_val1 = exist_text[:]
        self.lineEdit.setText("")  # 부호를 입력 받은 순간 기존에 입력 받아 뒀던 숫자는 가린다
        global temp_operator
        temp_operator = "*"
        self.lineEdit.setText(temp_operator)

    def divide(self):
        exist_text = self.lineEdit.text()
        # 연산 기호가 여러개 입력되면 그 중 맨 마지막으로 입력 받은 기호만이 수행된다.
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        global temp_val1
        temp_val1 = exist_text[:]
        self.lineEdit.setText("")  # 부호를 입력 받은 순간 기존에 입력 받아 뒀던 숫자는 가린다
        global temp_operator
        temp_operator = "/"
        self.lineEdit.setText(temp_operator)

    def percent(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        ans = float(exist_text) * 0.01
        self.lineEdit.setText(str(ans))

    def fraction(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        value = float(exist_text)
        ans = np.power(value, -1)
        self.lineEdit.setText(str(ans))

    def square(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        value = float(exist_text)
        ans = np.power(value, 2)
        self.lineEdit.setText(str(ans))

    def root(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])
        value = float(exist_text)
        ans = np.power(value, 0.5)
        self.lineEdit.setText(str(ans))

    def equal(self):
        exist_text = self.lineEdit.text()
        if ((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (
                exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1])

        global temp_val2
        temp_val2 = exist_text[:]
        if temp_operator == "+":
            result = float(temp_val1) + float(temp_val2)
            self.lineEdit.setText(str(result))
        elif temp_operator == "-":
            result = float(temp_val1) - float(temp_val2)
            self.lineEdit.setText(str(result))
        elif temp_operator == "*":
            result = float(temp_val1) * float(temp_val2)
            self.lineEdit.setText(str(result))
        elif temp_operator == "/":
            result = float(temp_val1) / float(temp_val2)
            self.lineEdit.setText(str(result))
        # self.number("=")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
