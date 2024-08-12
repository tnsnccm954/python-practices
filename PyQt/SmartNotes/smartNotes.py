from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,\
      QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout,\
         QFormLayout
# CTRL + / 
# import json

app = QApplication([])
notes = []


notesWin = QWidget()
notesWin.setWindowTitle("Smart Notes")
notesWin.resize(900,600)


layoutNote = QHBoxLayout()

col1 = QVBoxLayout()
textField = QTextEdit()
col1.addWidget(textField)

col2 = QVBoxLayout()
lineNotes = QListWidget()
lineNotesLabel = QLabel('List of notes')
col2.addWidget(lineNotesLabel)
col2.addWidget(lineNotes)
row1 = QHBoxLayout()
btnNotesCreate = QPushButton("Create")
btnNotesDel = QPushButton("Delete")
btnNotesSave = QPushButton("Save")
row1.addWidget(btnNotesCreate)
row1.addWidget(btnNotesDel)
row2 = QHBoxLayout()
row2.addWidget(btnNotesSave)

col2.addLayout(row1)
col2.addLayout(row2)

lineTagsLabel = QLabel('List of Tags:')
lineTags = QListWidget()
col2.addWidget(lineTagsLabel)
col2.addWidget(lineTags)
fieldTags = QLineEdit('')
fieldTags.setPlaceholderText('Enter Tag ...')
col2.addWidget(fieldTags)
row3 = QHBoxLayout()
tagBtnAdd = QPushButton('Add Tag to Note')
tagBtnDelete = QPushButton('Untag from Note')
row3.addWidget(tagBtnAdd)
row3.addWidget(tagBtnDelete)
row4 = QHBoxLayout()
tagBtnSearch = QPushButton('Search Notes by Tags')
row4.addWidget(tagBtnSearch)

col2.addLayout(row3)
col2.addLayout(row4)


layoutNote.addLayout(col1)
layoutNote.addLayout(col2)
notesWin.setLayout(layoutNote)

'''
CRUD
C : Create
R : Read
U : Update
D : delete
'''
def showNotes(): # Read
    key = lineNotes.selectedItems()[0].text()
    print(key)
    # textField.setText(notes[key]["text"])
    # lineTags.clear()
    # lineTags.addItems(notes[key]["tags"])
    for note in notes:
        if note[0] == key:
            textField.setText(note[1])
            lineTags.clear()
            lineTags.addItems(note[2])

# Create Note
def createNote():
    noteName, status = QInputDialog.getText(notesWin,"Add note","Note name:") 
    if status and noteName != "" :
        # notes[noteName] = {"text":"","tags":[]}
        # lineNotes.addItem(noteName)
        # lineTags.addItems(notes[noteName]["tags"])
        note = list()
        note = [noteName, '', []]
        notes.append(note)
        lineNotes.addItems(note[0])
        lineTags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+".txt","w") as file:
            file.write(note[0]+'\n')

# Update
def storeNote(): 
    if lineNotes.selectedItems():
        key = lineNotes.selectedItems()[0].text()
        # notes[key]["text"] = textField.toPlainText()
        # with open ('C:/Users/tnsnc/OneDrive/Desktop/Alg/WF/notes.json','w') as file:
        #     json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        idx = 0
        for note[0] in notes:
            if note[0] == key:
                note[1] = textField.toPlainText()
                with open(str(idx)+".txt","w") as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    file.write(note[2]+'\n')
                    file.write
            idx+=1
        print(notes)
    else:
        print('Note to save')


# Delete
def deleteNote():
    if lineNotes.selectedItems():
        key = lineNotes.selectedItems()[0].text()
        del notes[key]
        lineNotes.clear()
        lineTags.clear()
        textField.clear()
        lineNotes.addItems(notes)
      #   with open ('notes.json','w') as file:
        with open ('C:/Users/tnsnc/OneDrive/Desktop/Alg/WF/notes.json','w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def addTag():
      if(lineNotes.selectedItems()):
            tagName, status = QInputDialog.getText(notesWin,"Add Tag to Note","Tag name:")
            if(status and tagName != ""):
                  key = lineNotes.selectedItems()[0].text()
                  notes[key]["tags"].append(tagName)
                  lineTags.clear()
                  lineTags.addItems(notes[key]["tags"])

def delTag():
    if(lineNotes.selectedItems() and lineTags.selectedItems()):
      key = lineNotes.selectedItems()[0].text()
      tag = lineTags.selectedItems()[0].text()
      notes[key]["tags"].remove(tag)
      lineTags.clear()
      lineTags.addItems(notes[key]["tags"])

def searchTag():
    print(tagBtnSearch.text())
    tag = fieldTags.text()
    if tagBtnSearch.text() ==  'Search Notes by Tags' and tag:
        notesFiltered = {}
        for note in notes:
            if tag in notes[note]["tags"]:
                notesFiltered[note] = notes[note]
        tagBtnSearch.setText('Reset Search')
        lineNotes.clear()
        lineTags.clear()
        print(notesFiltered)
        lineNotes.addItems(notesFiltered)
    elif tagBtnSearch.text() ==  "Reset Search" :
        fieldTags.clear()
        lineTags.clear()
        lineNotes.clear()
        lineNotes.addItems(notes)
        tagBtnSearch.setText('Search Notes by Tags')
    else:
        pass

tagBtnSearch.clicked.connect(searchTag)
btnNotesCreate.clicked.connect(createNote)
btnNotesSave.clicked.connect(storeNote)
btnNotesDel.clicked.connect(deleteNote)
tagBtnAdd.clicked.connect(addTag)
tagBtnDelete.clicked.connect(delTag)
lineNotes.itemClicked.connect(showNotes)

notesWin.show()

# with open('C:/Users/tnsnc/OneDrive/Desktop/Alg/WF/notes.json','r') as file:
#     notes = json.load(file)
# lineNotes.addItems(notes)
name = 0
note = []
while True :
    filename = str(name) + ".text"
    try:
        with open(filename,'r',encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n','')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags
        notes.append(note)
        note = []
        name+=1
    except IOError:
        break

print(notes)
for note in notes:
    lineNotes.addItem(note[0])

app.exec_()