# Python Ver:   3.5.2
#
# Author:       William Paulk
#
# Purpose:      Python Course, Item 65
#
# Tested OS:    This code was written and tested to work with Windows 10

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import tkinter as tk


# Importing other modules
import  move_gui
import move_func

# Frame is the Tkinter frame class our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Defining master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        move_func.center_window(self,500,300)
        self.master.title("File Transfer Application")
        self.master.configure(bg='#F0F0F0')
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, 'X' on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: move_func.ask_quit(self))
        arg = self.master

        # Loading in the GUI widgets
        move_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
    
    
