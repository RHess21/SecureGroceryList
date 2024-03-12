#Import for the GUI interface
import tkinter as tk

# Set the DPI awareness, so the window doesn't get blurry on high DPI displays
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

#import the listapp for a correct login
import ListApp

def main():
    def login():
        # Get the entered username and password
        username = entry_username.get()
        password = entry_password.get()
        
        # Check if the username and password are correct
        if username == "admin" and password == "password":
            ListApp.ListMain()
        else:
            label_result.config(text="Username or password was incorrect, please try again", fg="red")

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

    # Create the result label
    label_result = tk.Label(window, text="", bg="grey", font=("Arial", 12))
    label_result.pack()

    # Start the main loop
    window.mainloop()
    
main()