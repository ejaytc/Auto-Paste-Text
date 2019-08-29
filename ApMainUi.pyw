#!/usr/bin/env python3
#Automate the pasting of copied text.

from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5 import QtCore
from ApUi import *
from docx import Document
import os, sys, re, shelve, time


class MainUI(QDialog):

    def __init__(self):
        super().__init__()
        self.selected_file  = ''
        self.folder         = ''
        self.ui             = Ui_Dialog()
        self.ui.setupUi(self)
        self.initUI()
        self.show()

    def initUI(self):
        self.start_up_select_path()
        self.ui.toolButtonSelectPath.clicked.connect(self.open_path)
        self.ui.listWidgetView.clicked.connect(self.doc_select)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    

    def open_path(self):
        self.folder = QFileDialog.getExistingDirectory(None, 'Select folder', '~/', QFileDialog.ShowDirsOnly)
        
        if self.folder == '':
            self.folder    = path
        else: 
            data["path_"]  = self.folder 

        self.ui.lineEditPath.clear()
        self.ui.listWidgetView.clear()
        self.filepath = os.path.basename(self.folder)
        self.ui.lineEditPath.insert(self.filepath)

        for item in os.listdir(self.folder):
            if fformat.search(item):
                self.ui.listWidgetView.addItem(item)

    def start_up_select_path(self):
        basedir = os.path.basename(path)
        self.notif()
        self.ui.lineEditPath.insert(basedir)
        self.ui.listWidgetView.clear()
        for item in os.listdir(path):
            if fformat.search(item):
                self.ui.listWidgetView.addItem(item)

    def doc_select(self):
        self.selected      = self.ui.listWidgetView.currentItem()
        self.selected_file = self.selected.text()
        self.ui.lineEditFile.clear()
        self.ui.lineEditFile.insert(self.selected_file)
    


    def accept(self):
        self.selected_file = self.ui.lineEditFile.text()

        if self.selected_file == '':
            self.notif()
            time.sleep(1)
            self.close()
        elif not fformat.search(self.selected_file) and not self.selected_file == '':
            self.ui.labelError.setText("Invalid file format.")
        else:
            self.create_doc()
            self.close()
            
    def create_doc(self):
        data["file_"] = self.selected_file
        document = Document()
        document.save(self.selected_file)

    def notif(self):
        self.ui.labelError.setText("No selected file. \"" + file +"\" will be use.")


if __name__ == "__main__":
    fformat              = re.compile(r'\D*.docx')
    data                 = shelve.open("AutopasteData")
    path                 = data["path_"]
    file                 = data["file_"]
    app                  = QApplication([])
    main                 = MainUI()
    main.show()
    app.exit(app.exec_())
    data.close()