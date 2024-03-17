from tkinter import Tk, Label, Entry, Button
from ctypes import windll
import re
import InputCheck
import pyodbc
import hashlib

windll.shcore.SetProcessDpiAwareness(1)

# Function to register an account
def register_account():
    def submit():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        
        #SECURITY CHECKS FOR PASSWORD
        if not first_name or not last_name or not email or not password:
             label_result.config(text="Please fill in all fields!", fg="red")
        else:
            checkStatus = InputCheck.check_input(email, password, first_name, last_name, label_result)
            
        if(checkStatus == True):
            try:
                conn = pyodbc.connect('Driver={SQL Server}; Server=localhost\\sqlexpress; Database=Grocery_List; Trusted_Connection=yes;')
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO Accounts (FirstName, LastName, Email, Password) VALUES (?, ?, ?, ?)", (first_name, last_name, email, hashlib.md5(password.encode()).hexdigest()))
                conn.commit()
                conn.close()
                del first_name
                del last_name
                del email
                del password
                label_result.config(text="Account registered successfully!", fg="green")
            except:
                print("DB Error!")   
        else:
            print("Account registration failed!")

    # Create the main window
    window = Tk()
    window.geometry("800x500")
    window.config(bg="grey")
    window.resizable(True, True)
    window.title("Register Account")

    label_result = Label(window, text="", bg="grey", font=("Arial", 12))
    label_result.pack()

    # Create labels and entry fields for each input
    first_name_label = Label(window, text="First Name:", bg="grey", font=("Arial", 12))
    first_name_label.pack()
    first_name_entry = Entry(window)
    first_name_entry.pack()

    last_name_label = Label(window, text="Last Name:", bg="grey", font=("Arial", 12))
    last_name_label.pack()
    last_name_entry = Entry(window)
    last_name_entry.pack()

    email_label = Label(window, text="Email:", bg="grey", font=("Arial", 12))
    email_label.pack()
    email_entry = Entry(window)
    email_entry.pack()

    password_label = Label(window, text="Password:", bg="grey", font=("Arial", 12))
    password_label.pack()
    password_entry = Entry(window, show="*")
    password_entry.pack()

    # Create a submit button
    submit_button = Button(window, text="Register", command=submit)
    submit_button.pack()

    # Start the main loop
    window.mainloop()

#register_account()