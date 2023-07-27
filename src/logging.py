"""
The logging.py module runs the second window opened in
the application. Here a user is introduced with entries
to log their workout information. There is also data 
validation functions within this page to validate the
user entries. 
"""

# Imports the necessary tools for the GUI
import tkinter as tk
from tkinter import messagebox

# The main function that is fired once the button from the 
# main page is clicked
def loggingWindow():
    
    new = tk.Toplevel() # Initialized a new window to open
    new.geometry("650x250")
    new.title("Log Your Workout")

    # Initializes the valiation functions to assign them to each of 
    # the entry boxes (name, length, calories, rate)
    nameValidation = new.register(validate_name) # Initializes the validate_name function
    lengthValidation = new.register(validate_length) # Initializes the validate_length function
    caloriesValidation = new.register(validate_calories) # Initializes the validate_calories function
    rateValidation = new.register(validate_rate) # Initializes the validate_rate function

    # Creates a label and entry to the Workout Name entry
    tk.Label(new, text="Workout name:").pack()
    workoutName = tk.Entry(new, textvariable="name") # Assigns the entry to a variable to call later

    # Allows for data validation on the workout name entry
    workoutName.config(validate="focusout", validatecommand=(nameValidation,"%P"))
    workoutName.pack()

    # Creates a label and entry to the Workout Length entry
    tk.Label(new, text="Workout length:").pack()
    length = tk.Entry(new, textvariable="length") # Assigns the entry to a variable to call later
    # Allows for data validation on the workout length entry
    length.config(validate="focusout", validatecommand=(lengthValidation,"%P"))
    length.pack()

    # Creates a label and entry to the calories entry
    tk.Label(new, text="Amount of calories burned:").pack()
    calories = tk.Entry(new, textvariable="calories") # Assigns the entry to a variable to call later
    # Allows for data validation on the calories entry
    calories.config(validate="focusout", validatecommand=(caloriesValidation,"%P"))
    calories.pack()

    # Creates a label and entry to the rate entry
    tk.Label(new, text="Rate the workout from 1-10:").pack()
    rate = tk.Entry(new, textvariable="rate") # Assigns the entry to a variable to call later
    # Allows for data validation on the rate entry
    rate.config(validate="focusout", validatecommand=(rateValidation,"%P"))
    rate.pack()

    # Creates a submit button once all the information is filled out
    submitButton = tk.Button(new, text="Submit", command=addToLog) # Assigns the entry to a variable to call later
    submitButton.pack()

    # Creates an exit button to escape from this new window and return to the root window
    exitButton = tk.Button(new, text="Exit", command=new.destroy) # Assigns the entry to a variable to call later
    exitButton.pack()


# Function that fires once the submit button is clicked
def addToLog():
    # A message box appears to confirm that the workout was submitted
    messagebox.showinfo('Submitted', 'Your workout was submitted!')

# Validation function that checks for an empty field
def validate_name(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please provide a name.')
    else:
        return True

# Validation function that checks for an empty field and if the characters are numbers
def validate_calories(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please provide the amount of calories burned.')
    else:
        if input.isdigit() and int(input) in range(0,10000):
            return True
        else:
            messagebox.showerror('Error', 'Please enter a valid number between 0-10000.')
            return False

# Validation function that checks for an empty field and if the characters are numbers
def validate_length(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please provide the length of the workout.')
    else:
        if input.isdigit() and int(input) in range(0,10000):
            return True
        else:
            messagebox.showerror('Error', 'Please enter a valid number of minutes between 0-10000.')
            return False

# Validation function that checks for an empty field and if the characters are numbers       
def validate_rate(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please rate the workout.')
    else:
        if input.isdigit() and int(input) in range(1,10):
            return True
        else:
            messagebox.showerror('Error', 'Please enter a valid rating between 0-10.')
            return False