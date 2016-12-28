import os, glob
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror
import tkinter as tk
import shutil
from datetime import datetime,timedelta



# Import modules
import move_main
import move_gui


def center_window(self,w,h): # passing in the tkinter frame (master) reference
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to center app on user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # Closes app
        self.master.destroy()
        os._exit(0)

def load_file(self):
    fname = askdirectory()
    if fname:
        try:
            print(fname)
            self.txt_browse.delete(0.0,END)
            self.txt_browse.insert(0.0,fname)
        except:                     # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read directory\n'%s'" % fname)
        return
    
def load_file2(self):
    fname2 = askdirectory()
    if fname2:
        try:
            print(fname2)
            self.txt_browse2.delete(0.0,END)
            self.txt_browse2.insert(0.0,fname2)
        except:                     # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read directory\n'%s'" % fname2)
        return

def move_files(self):
    source = self.txt_browse.get("1.0",'end-1c')
    dest = self.txt_browse2.get("1.0",'end-1c')

    for file in glob.glob(os.path.join(source, '*.txt')):
        file_name = os.path.basename(file)
        time_info = os.path.getmtime(file)
        date = datetime.fromtimestamp(time_info)
        if date > (datetime.today() - timedelta(1)):
            shutil.move(file,dest)
            print(file_name + ' -Moved')
        else:
            print(file_name + ' -Not Moved')

if __name__ == "__main__":
    pass
