import os, glob
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror
import tkinter as tk
import shutil
from datetime import datetime,timedelta
import sqlite3



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

#=====================================================

def create_db(self):
    conn = sqlite3.connect('lastRun.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_lastRun( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_source TEXT, \
            col_dest TEXT, \
            col_datetime TEXT \
            );")
        # commit to save changes & close the db connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    data = ('DummyEntry', 'DummyEntry', datetime.today())
    conn = sqlite3.connect('lastRun.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_lastRun (col_source, col_dest, col_datetime) VALUES (?,?,?)""", data)
            conn.commit()
    conn.close()

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.txt_time.config(state='normal')
    self.txt_time.delete(0.0,END)
    conn = sqlite3.connect('lastRun.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_datetime FROM tbl_lastRun ORDER BY id DESC LIMIT 1;""")
        varList = cursor.fetchone()
        self.txt_time.insert(0.0,varList)

    conn.close()
    self.txt_time.config(state=DISABLED)

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_lastRun""")
    count = cur.fetchone() [0]
    return cur,count

def addToList(self):
    global source
    global dest
    var_firstField = str(self.txt_browse.get("1.0",'end-1c'))
    var_secondField = str(self.txt_browse2.get("1.0",'end-1c'))
    if(len(var_firstField)>0) and (len(var_secondField)>0):
        conn = sqlite3.connect('lastRun.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO tbl_lastRun (col_source,col_dest,col_datetime) VALUES (?,?,?)""", [source, dest, datetime.today()])
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all fields.")
        


#=====================================================

    
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
    global source
    global dest
    source = self.txt_browse.get("1.0",'end-1c')
    dest = self.txt_browse2.get("1.0",'end-1c')

    conn = sqlite3.connect('lastRun.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_datetime FROM tbl_lastRun ORDER BY id DESC LIMIT 1;""")
        count = cursor.fetchone()
        last_backup = datetime.strptime(count[0], "%Y-%m-%d %H:%M:%S.%f")
        current_time = datetime.strptime(str(datetime.today()), "%Y-%m-%d %H:%M:%S.%f")
        difference = current_time - last_backup

    for file in glob.glob(os.path.join(source, '*.txt')):
        file_name = os.path.basename(file)
        time_info = os.path.getmtime(file)
        date = datetime.fromtimestamp(time_info)
        print(date)
        if (current_time - date) < (current_time - last_backup):
            shutil.move(file,dest)
            print(file_name + ' -Moved')
        else:
            print(file_name + ' -Not Moved')
    addToList(self)
    self.txt_time.config(state='normal')
    self.txt_time.delete(0.0,END)
    self.txt_time.insert(0.0,'{' + str(datetime.today()) + '}')
    self.txt_time.config(state=DISABLED)

if __name__ == "__main__":
    pass
