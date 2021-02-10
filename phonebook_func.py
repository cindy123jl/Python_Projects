import os
from tkinter import *
import tkinter as tk
import sqlite3

#be sure to import our other modules
#so we can have access to them
import phonebook_main
import phonebook_gui

def center_window(self, w, h): #pass in the tkinter frame (master) reference and the w and h
    #get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #calculate x and y coordinates to pain the app centered on the users screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}*{}+{}+{}'.format(w, h, x, y))
    return centerGEO

#catch if the users clicks on the windows upper-right 'x' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit application?"):
        #this closes app
        self.master.destroy()
        os._exit(0)

#=======================================================

def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE id not exists tbl_phonebook(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT,\
            col_lname TEXT,\
            col_fullname TEXT,\
            col_phone TEXT,\
            col_email Text\
            ):")
        #You must commit() to save changes& close the db connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    date = ('John','Doe','John Doe','111-111-1111','jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES(?,?,?,?,?)""",(data
            conn.commit()
        conn.close()
                                                                                                                                      
def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

#Select item in ListBox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)""",(value))
        varBody = cursor.fetchall()
        #This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize that data to keep it consistent in the db
    var_fname = var_fname.strip() #this will remove any blank spaces before and after the users entry
    var_lname = var_lname.strip()#this will ensure the first character in each word is cap
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))#combine our normalised names into a full name
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if(len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and(len(var_email) > 0): #enforce the user to provide
        conn= sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            #Check the database for existance of the full name is so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname)
            count = cursor.fetchone()[0]
            chkName=count
            if chkName == 0:#if this is 0 than there is no existence of the fullname if so we will alert user and disregard request
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?,?)"""
                self.lstList1.insert(END, var_fullname)#update listbox with the new function
                onClear(self)#call the function to clear all of the textboxes
            else:
                messagebox.
                           
                              
         
