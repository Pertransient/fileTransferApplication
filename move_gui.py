from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import tkinter as tk

# Importing other modules
import move_main
import move_func
        
def load_gui(self):

    self.lbl_source = tk.Label(self.master,text='Source File:')
    self.lbl_source.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_dest = tk.Label(self.master,text='Destination File:')
    self.lbl_dest.grid(row=3,column=0,padx=(27,0),pady=(10,0),sticky =N+W)
    self.lbl_move = tk.Label(self.master,text='Move Files:')
    self.lbl_move.grid(row=5,column=0,padx=(27,0),pady=(10,0),sticky =N+W)

    self.txt_browse = Text(self.master, width = 40, height =1)
    self.txt_browse.grid(row=1,column=2,pady=(5,0), sticky=W+E)
    self.txt_browse2 = Text(self.master, width = 40, height =1)
    self.txt_browse2.grid(row=4,column=2,pady=(5,0), sticky=W+E)

    self.btn_browse = tk.Button(self.master,width=10,height=1,text='Browse',command=lambda: move_func.load_file(self))
    self.btn_browse.grid(row=1, column=0, padx=(25,0),pady=(5,0), sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=10,height=1,text='Browse',command=lambda: move_func.load_file2(self))
    self.btn_browse2.grid(row=4, column=0, padx=(25,0),pady=(5,0), sticky=W)
    self.btn_execute = tk.Button(self.master,width=40,height=6,text='Move Files',command=lambda: move_func.move_files(self))
    self.btn_execute.grid(row=6,column=0, columnspan=3,padx=(40,0),pady=(15,0),sticky=N)


if __name__=="__main__":
    pass
