import re
import Logger

# Function to check the input fields for the register account form and return if they are valid or not
def check_input(email, password, first_name, last_name, label_result):
    emailPat = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    passPat = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    namePat = r'^[a-zA-Z]+$'

    validation_rules = [
        (email, emailPat, "Invalid email!"),
        (password, passPat, "Password must be at least 8 characters long and contain at least one letter and one number!"),
        (first_name, namePat, "First name must only contain letters!"),
        (last_name, namePat, "Last name must only contain letters!")
    ]

        # iterates throught the tuple and checks if the field matches the pattern, if not it prints the error message
    for field, pattern, error_message in validation_rules:
        if not re.match(pattern, field):
            label_result.config(text=error_message, fg="red")
            Logger.logger.error(f' - Invalid {field} detected!')
            return False

    label_result.config(text="Account registered successfully!", fg="green")
    Logger.logger.info(f' - All Fields are correct!')
    return True

def sanitize_input(input):
        words_to_replace = ["SELECT", "DROP", "DELETE", "JOIN", "CREATE", "UPDATE", "INSERT"]
        for word in words_to_replace:
                input = input.replace(word, "")
        return input
    