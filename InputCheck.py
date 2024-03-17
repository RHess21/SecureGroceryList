import re


# Function to check the input fields for the register account form and return if they are valid or not
def check_input(email, password, first_name, last_name, label_result):
   
# Regular expression pattern for password security checks

    pattern1 = r"^([A-Za-z0-9]+)@([A-Za-z0-9]+)\.([A-Za-z]{2,})$" #Email pattern
    pattern2 = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"          #Password pattern
    pattern3 = r"^([A-Za-z]+)$"                                      #Name pattern

    if not re.match(pattern1, email):
            label_result.config(text="Invalid email!", fg="red")
            return False
    elif not re.match(pattern2, password): 
            label_result.config(text="Password must be at least 8 characters long and contain at least one letter and one number!", fg="red")
            return False
    elif not re.match(pattern3, first_name):
            label_result.config(text="First name must only contain letters!", fg="red")
            return False
    elif not re.match(pattern3, last_name):
            label_result.config(text="Last name must only contain letters!", fg="red")
            return False
    else:
            label_result.config(text="Account registered successfully!", fg="green")
            return True