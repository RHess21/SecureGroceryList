import re


# Function to check the input fields for the register account form and return if they are valid or not
def check_input(email, password, first_name, last_name, label_result):
   
# Regular expression pattern for password security checks

    emailPat = r"^([A-Za-z0-9]+)@([A-Za-z0-9]+)\.([A-Za-z]{2,})$" #Email pattern
    passPat = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"          #Password pattern
    namePat = r"^([A-Za-z]+)$"                                      #Name pattern

    if not re.match(emailPat, email):
            label_result.config(text="Invalid email!", fg="red")
            return False
    elif not re.match(passPat, password): 
            label_result.config(text="Password must be at least 8 characters long and contain at least one letter and one number!", fg="red")
            return False
    elif not re.match(namePat, first_name):
            label_result.config(text="First name must only contain letters!", fg="red")
            return False
    elif not re.match(namePat, last_name):
            label_result.config(text="Last name must only contain letters!", fg="red")
            return False
    else:
            label_result.config(text="Account registered successfully!", fg="green")
            return True