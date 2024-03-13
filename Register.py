from tkinter import Tk, Label, Entry, Button
from ctypes import windll
import re
windll.shcore.SetProcessDpiAwareness(1)


def register_account():
    def submit():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        
        #SECURITY CHECKS FOR PASSWORD
        if not first_name or not last_name or not email or not password:
             label_result.config(text="Please fill in all fields!", fg="red")

        # Regular expression pattern for password security checks
        pattern1 = r"^([A-Za-z0-9]+)@([A-Za-z0-9]+)\.([A-Za-z]{2,})$" #Email pattern
        pattern2 = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"          #Password pattern
        pattern3 = r"^([A-Za-z])$"                                      #Name pattern

        if not re.match(pattern2, password):
            label_result.config(text="Password must contain at least one letter and one digit, and be at least 8 characters long!", fg="red")
        else:
            if not re.match(pattern1, email):
                label_result.config(text="Email is not valid!", fg="red")
            else:
                if not re.match(pattern3, first_name) or not re.match(pattern3, last_name):
                    label_result.config(text="First and Last name must contain only letters!", fg="red")
                else:
                    label_result.config(text="Account creating successfully, you may now close this tab.", fg="Green")    
                
                
        

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

register_account()