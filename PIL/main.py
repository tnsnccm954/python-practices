import os
from PyQt5.QtWidgets import QApplication, QWidget, \
    QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout

app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Easy Editor")
lbImage = QLabel("Image")
btnDir = QPushButton("Folder")
lwFile = QListWidget()

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btnDir)
col1.addWidget(lwFile)
col2.addWidget(lbImage,95)

btnLeft = QPushButton('Left')
btnRight = QPushButton('Right')
btnFlip = QPushButton('Flip')
btnSharp = QPushButton('Sharp')
btnBw = QPushButton('B/W')

rowTools = QHBoxLayout()
rowTools.addWidget(btnLeft)
rowTools.addWidget(btnRight)
rowTools.addWidget(btnFlip)
rowTools.addWidget(btnSharp)
rowTools.addWidget(btnBw)
col2.addLayout(rowTools)

row.addLayout(col1,20)
row.addLayout(col2,80)
win.setLayout(row)

win.show()

workDir = ''



def showFileList():
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    workDir = QFileDialog.getExistingDirectory()
    files = os.listdir(workDir)
    lwFile.clear()
    for file in files:
        for ext in extensions:
            if(file.endswith(ext)):
                lwFile.addItem(file)
    
btnDir.clicked.connect(showFileList)

app.exec()




