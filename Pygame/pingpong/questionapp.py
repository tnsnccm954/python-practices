from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
def show_win():
  victory_win = QMessageBox()
  victory_win.setText('Correct!\nYou won!')
  victory_win.exec_()
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Quiz')
main_win.resize(400, 200)

question = QLabel("what's ...")
# 4 answers
btnAnswer1 = QRadioButton('choices-1')
btnAnswer2 = QRadioButton('choices-2')

mainLayout = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question,alignment = Qt.AlignCenter)
line2.addWidget(btnAnswer1,alignment = Qt.AlignCenter)
line2.addWidget(btnAnswer2,alignment = Qt.AlignCenter)
line3.addWidget(btnAnswer2,alignment = Qt.AlignCenter)

mainLayout.addLayout(line1)
mainLayout.addLayout(line2)
mainLayout.addLayout(line3)

main_win.setLayout(mainLayout)
btnAnswer1.clicked.connect(show_win)

main_win.show()
app.exec()


