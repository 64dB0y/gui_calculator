import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

temp_operator = None
temp_val1 = 0
temp_val2 = 0

form_main = uic.loadUiType("calculator2.ui")[0]  # load ui file


class MainWindow(QMainWindow, form_main):
    def __init__(self):
        super().__init__()
        self.initUI()
        # A flag indicating whether the calculator is currently in an error state. It is set to True if an error occurs.
        self.is_error = False   
        # A flag indicating whether a new input has started. It is set to True when the next input begins after pressing an operator button.
        self.new_input_started = False  
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.lineEdit.setText('0')

        self.pushButton_1.clicked.connect(self.button_1)  # functions triggered by a button click
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
        if self.is_error:
            return
        exist_text = self.lineEdit.text()
        if exist_text:  # Execute only when exist_text is not empty
            # Handle as int or str instead of converting to decimal form when calculating ans
            if '.' in exist_text or '-' in exist_text:
                ans = float(exist_text) * (-1)
                # Remove the decimal point for display when ans is an integer
                self.lineEdit.setText(str(int(ans)) if ans.is_integer() else str(ans))
            else:
                ans = int(exist_text) * (-1)
                self.lineEdit.setText(str(ans))
        else:  # If exist_text is empty, set to '0'
            self.lineEdit.setText('0')

    def button_dot(self):
        if self.is_error:
            return

        if self.new_input_started:
            self.lineEdit.setText('0.')
            self.new_input_started = False
        else:
            if "." not in self.lineEdit.text():
                self.lineEdit.setText(self.lineEdit.text() + ".")

    def number(self, num):
        if self.check_for_error():  # Check if it is an error state
            self.lineEdit.setText(num)  # If it is an error state, display the currently entered number
            self.is_error = False  # Release error state
            return

        if self.new_input_started:
            self.lineEdit.setText('')
            self.new_input_started = False

        exist_text = self.lineEdit.text()
        if exist_text == '0':  # If only '0' is currently displayed, replace it with the new number
            self.lineEdit.setText(num)
        else:
            self.lineEdit.setText(exist_text + num)  # if not, add num

    def del_num(self):
        if self.is_error:
            self.lineEdit.setText("0")
            self.is_error = False
            return

        exist_text = self.lineEdit.text()
        if exist_text and len(exist_text) > 1:  # Delete only when the length is greater than 1
            self.lineEdit.setText(exist_text[:-1])
        else:  # If only one character remains, set to '0'
            self.lineEdit.setText('0')

    def clr_num(self):
        self.lineEdit.setText("0")
        self.is_error = False

    def plus(self):
        if self.is_error:
            return
        global temp_val1, temp_operator
        self.new_input_started = True
        exist_text = self.lineEdit.text()
        # If exist_text is empty or contains only an operator, set it to '0'
        if not exist_text or exist_text in "+-*/%":
            exist_text = '0'
        # If multiple operation symbols are entered, only the last entered symbol is executed.
        elif exist_text[-1] in "+-*/%":
            exist_text = exist_text[:-1]

        temp_val1 = exist_text
        temp_operator = "+"


    def minus(self):
        if self.is_error:
            return
        global temp_val1, temp_operator
        self.new_input_started = True
        exist_text = self.lineEdit.text()
        # If exist_text is empty or contains only an operator, set it to '0'
        if not exist_text or exist_text in "+-*/%":
            exist_text = '0'
        # If multiple operation symbols are entered, only the last entered symbol is executed.
        elif exist_text[-1] in "+-*/%":
            exist_text = exist_text[:-1]

        temp_val1 = exist_text
        temp_operator = "-"


    def multiple(self):
        if self.is_error:
            return
        global temp_val1, temp_operator
        self.new_input_started = True
        exist_text = self.lineEdit.text()
        # If exist_text is empty or contains only an operator, set it to '0'
        if not exist_text or exist_text in "+-*/%":
            exist_text = '0'
        # If multiple operation symbols are entered, only the last entered symbol is executed.
        elif exist_text[-1] in "+-*/%":
            exist_text = exist_text[:-1]

        temp_val1 = exist_text
        temp_operator = "*"

    def divide(self):
        if self.is_error:
            return
        global temp_val1, temp_operator
        self.new_input_started = True
        exist_text = self.lineEdit.text()
        # If exist_text is empty or contains only an operator, set it to '0'
        if not exist_text or exist_text in "+-*/%":
            exist_text = '0'
        # If multiple operation symbols are entered, only the last entered symbol is executed.
        elif exist_text[-1] in "+-*/%":
            exist_text = exist_text[:-1]

        temp_val1 = exist_text
        temp_operator = "/"


    def percent(self):
        if self.is_error:
            return
        exist_text = self.lineEdit.text()
        try:
            ans = float(exist_text) * 0.01
            self.lineEdit.setText(str(ans))
        except ValueError:
            self.lineEdit.setText("Error")
            self.is_error = True
            return

    def fraction(self):
        if self.is_error:
            return
        exist_text = self.lineEdit.text()
        try:
            if exist_text == '0':  # Direct error handling for division by zero when '0' is entered
                raise ValueError("Cannot divide by zero")  # Raise a ValueError to display an error message
            if not exist_text or exist_text in "+-*/%":
                self.lineEdit.setText("Error")
                self.is_error = True
                return
            value = float(exist_text)
            ans = 1 / value
            self.lineEdit.setText(str(ans))
        except (ValueError, ZeroDivisionError):  # Exception handling for ValueError and ZeroDivisionError
            self.lineEdit.setText("Error, cannot divide by zero")
            self.is_error = True

    def square(self):
        if self.is_error:
            return
        exist_text = self.lineEdit.text()
        if not exist_text or exist_text in "+-*/%":
            self.lineEdit.setText("Error")
            self.is_error = True
            return
        value = float(exist_text)
        ans = value * value
        self.lineEdit.setText(str(ans))

    def root(self):
        if self.is_error:
            return
        exist_text = self.lineEdit.text()
        if not exist_text or exist_text in "+-*/%":
            self.lineEdit.setText("Error")
            self.is_error = True
            return
        value = float(exist_text)
        if value < 0:
            self.lineEdit.setText("Error")
            self.is_error = True
            return
        ans = np.sqrt(value)
        self.lineEdit.setText(str(ans))

    def equal(self):
        if self.is_error:
            return

        global temp_val1, temp_val2, temp_operator

        exist_text = self.lineEdit.text()

        if not exist_text or exist_text[-1] in "+-*/%":  # Ignore the input when an operator is the last character.
            exist_text = temp_val1

        if not temp_val1 or not exist_text:  # Do not perform calculation if temp_val1 is not set or there is no current text.
            return

        try:
            if temp_operator == "+":
                result = float(temp_val1) + float(exist_text)
            elif temp_operator == "-":
                result = float(temp_val1) - float(exist_text)
            elif temp_operator == "*":
                result = float(temp_val1) * float(exist_text)
            elif temp_operator == "/":
                if float(exist_text) == 0:
                    self.lineEdit.setText("Error, cannot divide by zero")
                    self.is_error = True
                    return
                result = float(temp_val1) / float(exist_text)

            temp_val1 = str(result)  # Store the result in temp_val1.
            self.lineEdit.setText(str(result))
            temp_operator = None
        except ValueError:
            self.lineEdit.setText("Error")
            self.is_error = True

    def check_for_error(self):
        if self.lineEdit.text() == "Error" or self.lineEdit.text() == "Error, cannot divide by zero":
            return True
        return False
    
    def handle_key(self, key: int) -> None:
        match key:
            # Numbers
            case Qt.Key_0: self.pushButton_0.clicked.emit()
            case Qt.Key_1: self.pushButton_1.clicked.emit()
            case Qt.Key_2: self.pushButton_2.clicked.emit()
            case Qt.Key_3: self.pushButton_3.clicked.emit()
            case Qt.Key_4: self.pushButton_4.clicked.emit()
            case Qt.Key_5: self.pushButton_5.clicked.emit()
            case Qt.Key_6: self.pushButton_6.clicked.emit()
            case Qt.Key_7: self.pushButton_7.clicked.emit()
            case Qt.Key_8: self.pushButton_8.clicked.emit()
            case Qt.Key_9: self.pushButton_9.clicked.emit()

            # Operators
            case Qt.Key_plusminus: \
                self.pushButton_negative_positive.clicked.emit()
            case Qt.Key_Period: self.pushButton_dot.clicked.emit()
            case Qt.Key_Backspace: self.pushButton_DEL.clicked.emit()
            case Qt.Key_Plus: self.pushButton_plus.clicked.emit()
            case Qt.Key_Minus: self.pushButton_minus.clicked.emit()
            case Qt.Key_Asterisk: self.pushButton_mult.clicked.emit()
            case Qt.Key_Slash: self.pushButton_divide.clicked.emit()
            case Qt.Key_Equal: self.pushButton_equal.clicked.emit()
            case Qt.Key_Enter: self.pushButton_equal.clicked.emit()
            case Qt.Key_Percent: self.pushButton_percent.clicked.emit()
            ## I'm interpreting Esc key as clear_everything
            case Qt.Key_Escape: self.pushButton_CE.clicked.emit()

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        self.handle_key(event.key())
        return super().keyReleaseEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()