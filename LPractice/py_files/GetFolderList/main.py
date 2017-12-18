#coding=utf8

import os
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter.filedialog import askdirectory

outTxt = "FolderList.txt"

if(os.path.exists(outTxt)):
    os.remove(outTxt)

class Application(tk.Frame):
    
    _path = ""
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.flab = tk.Label(self,text = "目标路径:")
        self.flab.pack()
        #self.finput = Entry(self, textvariable = self._path)
        #self.finput.pack()
        self.fsel = tk.Button(self, text = "路径选择", command = self.selectPath)
        self.fsel.pack()
        '''
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        '''
    '''
    def hello(self):
        name = self.nameInput.get() or 'world'
        msgbox.showinfo('message', 'Hello, %s' % name )
    '''

    def selectPath(self):
        self._path = askdirectory()
        self.flab.config(text = "目标路径: " + self._path)
        #msgbox.showinfo('filePath', '%s' % self._path)

root = tk.Tk()

app = Application(root)

app.master.title('Hello world')

app.mainloop()
