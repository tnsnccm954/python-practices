from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from random import randint
app = QApplication([])
# main window:
my_win = QWidget()
my_win.setWindowTitle('Lottery')
my_win.move(100, 100)
my_win.resize(400, 200)

btn = QPushButton('Get your lucky number')
label = QLabel('Clcik the button to get your lucky number')
winners = QLabel('?')
layout = QVBoxLayout()
layout.addWidget(label, alignment=Qt.AlignCenter)
layout.addWidget(winners, alignment=Qt.AlignCenter)
layout.addWidget(btn, alignment=Qt.AlignCenter)

def showWinnerNumber():
    number = randint(1, 100)
    winners.setText(str(number))
    # QMessageBox.information(my_win, 'Information', 'You are the winner')

btn.clicked.connect(showWinnerNumber)

my_win.setLayout(layout)
my_win.show()
app.exec_()
