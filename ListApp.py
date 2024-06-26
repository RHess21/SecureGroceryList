import tkinter as tk
import pyodbc
import Logger
import datetime
# Set the DPI awareness, so the window doesn't get blurry on high DPI displays
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)



def ListMain(accID):
    #Adds the item in the textbox to the list on press       
    def add_item():
        item = entry_listItem.get()
        if item:
            listbox_grocerys.insert(tk.END, item)
            entry_listItem.delete(0, tk.END)
            
    #Removes selected items from the list on press
    def remove_item():
        selected_indices = listbox_grocerys.curselection()
        for index in selected_indices[::-1]:
            listbox_grocerys.delete(index)
            
    #Window creation
    window = tk.Tk()
    window.config(bg="grey")
    window.resizable(True, True)
    window.state('zoomed')
    window.title("Grocery List App")
    
    #Start of Application
    label_title = tk.Label(window, text="Grocery List App", bg="grey", font=("Arial", 24))
    label_title.pack()
    
    #Label for the username
    Label_FirstName = tk.Label(window, text="Welcome "+get_info(accID), bg="grey", font=("Arial", 18))
    Label_FirstName.pack(pady=10, padx=75, side="top", anchor='w')
    
    #List Label
    label_List = tk.Label(window, text="List", bg="grey", font=("Arial", 18))
    label_List.pack(pady=10, padx=75, side="top", anchor='w')
    
    #Item entry box
    entry_listItem = tk.Entry(window)
    entry_listItem.pack(pady=10, padx=75, side="top", anchor='w')
    
    #Add button for entry submission
    button_add = tk.Button(window, text="Add", bg="white", font=("Arial", 12), command=add_item)
    button_add.pack(pady=10, padx=75, side="top", anchor='w')
    
    #Remove button for entry deletion
    button_remove = tk.Button(window, text="Remove", bg="white", font=("Arial", 12), command=remove_item)
    button_remove.pack(pady=10, padx=75, side="top", anchor='w')
    
    #Listbox to show you the grocerys you entered
    listbox_grocerys = tk.Listbox(window, width=50, height=20)
    listbox_grocerys.pack()
    
    window.mainloop()
    
def get_info(accID):
        try:
            conn = pyodbc.connect('Driver={SQL Server}; Server=localhost\\sqlexpress; Database=Grocery_List; Trusted_Connection=yes;')
            mycursor = conn.cursor()
            mycursor.execute ("SELECT FirstName, LastName FROM Accounts WHERE AccID = ?", (accID,))
            acc = mycursor.fetchone()
            conn.commit()
            conn.close()
            Logger.logger.info(f' - Database Connection Successful for ListMain!')
        except:
            Logger.logger.critical(f' - Database Failure for ListMain!')
            return
        fname= acc[0]
        lname= acc[1]
        del acc
        return  fname+ " " + lname