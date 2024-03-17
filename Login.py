#Import for the GUI interface
import tkinter as tk

# Set the DPI awareness, so the window doesn't get blurry on high DPI displays
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

#import the listapp for a correct login
import ListApp
import Register
import pyodbc
import hashlib

def main():
    def login():
        
        if not entry_username.get() or not entry_password.get():
            label_result.config(text="Please fill in all fields!", fg="red")
            return
        else:
            # Get the entered username and password
            username = entry_username.get()
            password = entry_password.get()

            # Connect to the database
            conn = pyodbc.connect('Driver={SQL Server}; Server=localhost\\sqlexpress; Database=Grocery_List; Trusted_Connection=yes;')
            mycursor = conn.cursor()
            
            #Gets the email from the database
            mycursor.execute("SELECT * FROM Accounts WHERE Email = ?", (username,))
            checker = mycursor.fetchone()
            conn.commit()
            
            #Checks to see if an email was found in the database
            if(checker):
                # print("Email found!")
                try:
                    #Compares the password to the hashed password in the database
                    if(checker[4] == hashlib.md5(password.encode()).hexdigest()):
                        del checker
                        del password
                        window.destroy()
                        ListApp.ListMain()
                    else:
                        label_result.config(text="Username or password was incorrect, please try again", fg="red")
                except:
                    print("DB Failure!")
            else:
                label_result.config(text="Email was not found", fg="red")
            conn.close()
    def register():
        Register.register_account()
        
        
    # Create the main window and how big it should be
    window = tk.Tk()
    window.geometry("800x500")
    window.config(bg="grey")
    window.resizable(True, True)
    window.title("Grocery List App")

    # Create the username label and entry
    label_username = tk.Label(window, text="Username:")
    label_username.config(bg="grey", font=("Arial", 12))
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    # Create the password label and entry
    label_password = tk.Label(window, text="Password:")
    label_password.config(bg="grey", font=("Arial", 12))
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    # Create the login button
    button_login = tk.Button(window, text="Login", bg="grey", command=login)
    button_login.pack()
    
    button_register = tk.Button(window, text="Register", bg="grey", command=register)
    button_register.pack()

    # Create the result label
    label_result = tk.Label(window, text="", bg="grey", font=("Arial", 12))
    label_result.pack()

    # Start the main loop
    window.mainloop()
    
main()