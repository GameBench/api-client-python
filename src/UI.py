import os
import sys
import json
from datetime import datetime
from PyQt5 import QtGui, QtCore, QtWidgets

class ChecklistDialog(QtWidgets.QDialog):

    def __init__(
        self,
        name,
        stringlist=None,
        checked=False,
        icon=None,
        parent=None,
        ):
        super(ChecklistDialog, self).__init__(parent)

        self.name = name
        self.icon = icon
        self.model = QtGui.QStandardItemModel()
        self.listView = QtWidgets.QListView()

        for string in stringlist:
            item = QtGui.QStandardItem(string)
            item.setCheckable(True)
            check = \
                (QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            item.setCheckState(check)
            self.model.appendRow(item)

        self.listView.setModel(self.model)

        self.okButton = QtWidgets.QPushButton('OK')
        self.cancelButton = QtWidgets.QPushButton('Cancel')
        self.selectButton = QtWidgets.QPushButton('Select All')
        self.unselectButton = QtWidgets.QPushButton('Unselect All')

        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        hbox.addWidget(self.selectButton)
        hbox.addWidget(self.unselectButton)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.listView)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setWindowTitle(self.name)
        if self.icon:
            self.setWindowIcon(self.icon)

        self.okButton.clicked.connect(self.onAccepted)
        self.cancelButton.clicked.connect(self.reject)
        self.selectButton.clicked.connect(self.select)
        self.unselectButton.clicked.connect(self.unselect)

    def onAccepted(self):
        self.choices = [self.model.item(i).text() for i in
                        range(self.model.rowCount())
                        if self.model.item(i).checkState()
                        == QtCore.Qt.Checked]
        self.accept()

    def select(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Checked)

    def unselect(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)

# Convert Unix to datetime object on Windows
def unix_to_datetime(x):   
    try:
        date = datetime.fromtimestamp(int(x)/1000).strftime('%Y-%m-%d')
    except:
        date = x
    return date

if __name__ == '__main__':
    
    with open("all_tags.json", "r") as read_file:
        all_tags = json.load(read_file)
    
    with open("all_sessions.json", "r") as read_file:
        all_sessions = json.load(read_file)

    all_tags_formatted = []
    for key in all_tags.keys():
        for val in all_tags[key]:
            all_tags_formatted.append(f"{key}: {val}")
    
    app = QtWidgets.QApplication(sys.argv)
    form = ChecklistDialog('Session Tags', all_tags_formatted, checked=True)
    session_list = []

    if form.exec_() == QtWidgets.QDialog.Accepted:
        keys = [str(s).split(":")[0] for s in form.choices]
        vals = [str(s).split(":")[1].replace(" ","") for s in form.choices]
        
        for session_id in all_sessions:
            match = True
            cur_session = all_sessions[session_id]
            if set(keys).issubset(cur_session["tags"].keys()):
                for i, key in enumerate(keys):
                    if cur_session["tags"][key] != vals[i]:
                        match = False
                if match:
                    session_list.append(str(session_id) + f" ({cur_session['user']['userPlayAccount']}) [{unix_to_datetime(cur_session['sessionDate'])}]")
                    #print(f"Session {session_id} by {cur_session['user']['userPlayAccount']} on {unix_to_datetime(cur_session['sessionDate'])} has tags: {cur_session['tags']}.")
        
    app_2 = QtWidgets.QApplication(sys.argv)
    form2 = ChecklistDialog('Sessions', session_list, checked=True)
    if form2.exec_() == QtWidgets.QDialog.Accepted:
        session_IDs = [str(s).split(" ")[0] for s in form2.choices]
        
        with open("output_session_IDs.txt", "w+") as file:
            for session in session_IDs:
                file.write(session + "\n")
        