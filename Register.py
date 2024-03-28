from tkinter import Tk, Label, Entry, Button
from ctypes import windll

import InputCheck
import pyodbc
import hashlib
import Logger

windll.shcore.SetProcessDpiAwareness(1)

# Function to register an account
def register_account():

    # Create the main window
    window = Tk()
    window.geometry("800x500")
    window.config(bg="grey")
    window.resizable(True, True)
    window.title(f'Register Account')

    label_result = Label(window, text="", bg="grey", font=("Arial", 12))
    label_result.pack()

    # Create labels and entry fields for each input
    first_name_label = Label(window, text=f"First Name:", bg="grey", font=("Arial", 12))
    first_name_label.pack()
    first_name_entry = Entry(window)
    first_name_entry.pack()

    last_name_label = Label(window, text=f"Last Name:", bg="grey", font=("Arial", 12))
    last_name_label.pack()
    last_name_entry = Entry(window)
    last_name_entry.pack()

    email_label = Label(window, text=f"Email:", bg="grey", font=("Arial", 12))
    email_label.pack()
    email_entry = Entry(window)
    email_entry.pack()

    password_label = Label(window, text=f"Password:", bg="grey", font=("Arial", 12))
    password_label.pack()
    password_entry = Entry(window, show="*")
    password_entry.pack()

    # Create a submit button
    submit_button = Button(window, text=f"Register", command=lambda: submit(first_name_entry.get(), last_name_entry.get(), 
                                                                    email_entry.get(),password_entry.get(), label_result, window))
    submit_button.pack()

    # Start the main loop
    window.mainloop()

def submit(firstName, lastName, email, password, label_result, window):
    
        #SECURITY CHECKS FOR PASSWORD
        if not firstName or not lastName or not email or not password:
             label_result.config(text=f'Please fill in all fields!', fg="red")
        else:
            sanitizedFName = InputCheck.sanitize_input(firstName)
            sanitizedLName = InputCheck.sanitize_input(lastName)
            sanitizedEmail = InputCheck.sanitize_input(email)
            sanitizedPass = InputCheck.sanitize_input(password)
            #SECURITY CHECKS FOR PASSWORD
            checkStatus = InputCheck.check_input(sanitizedEmail, sanitizedPass, sanitizedFName, sanitizedLName, label_result)
            
        if(checkStatus == True):
            try:
                sanitizedFName = InputCheck.sanitize_input(sanitizedFName)
                sanitizedLName = InputCheck.sanitize_input(sanitizedLName)
                sanitizedEmail = InputCheck.sanitize_input(sanitizedEmail)
                sanitizedPass = InputCheck.sanitize_input(sanitizedPass)
                
                conn = pyodbc.connect('Driver={SQL Server}; Server=localhost\\sqlexpress; Database=Grocery_List; Trusted_Connection=yes;')
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO Accounts (FirstName, LastName, Email, Password) VALUES (?, ?, ?, ?)", (sanitizedFName, sanitizedLName, sanitizedEmail, hashlib.md5(sanitizedPass.encode()).hexdigest()))
                conn.commit()
                conn.close()
                del firstName
                del lastName
                del email
                del password
                del sanitizedFName
                del sanitizedLName
                del sanitizedEmail
                del sanitizedPass
                window.destroy()
                label_result.config(text=f'Account registered successfully!', fg="green")
                Logger.logger.info(f'- Account registered successfully!')
                from Login import createLogin
                createLogin()
            except:
                Logger.logger.critical(f' - Database Failure!')   
        else:
            Logger.logger.error(f' - Invalid input detected, Account Registration failed!')