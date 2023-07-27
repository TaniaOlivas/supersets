import tkinter as tk
from tkinter import messagebox

def loggingWindow():
    new = tk.Toplevel()
    new.geometry("650x250")
    new.title("Log Your Workout")
    nameValidation = new.register(validate_name)
    lengthValidation = new.register(validate_length)
    caloriesValidation = new.register(validate_calories)
    rateValidation = new.register(validate_rate)
    tk.Label(new, text="Name:").pack()
    workoutName = tk.Entry(new, textvariable="name")
    workoutName.config(validate="focusout", validatecommand=(nameValidation,"%P"))
    workoutName.pack()
    tk.Label(new, text="Length:").pack()
    length = tk.Entry(new, textvariable="length")
    length.config(validate="focusout", validatecommand=(lengthValidation,"%P"))
    length.pack()
    tk.Label(new, text="Calories Burned:").pack()
    calories = tk.Entry(new, textvariable="calories")
    calories.config(validate="focusout", validatecommand=(caloriesValidation,"%P"))
    calories.pack()
    tk.Label(new, text="Rate the workout from 1-10:").pack()
    rate = tk.Entry(new, textvariable="rate")
    rate.config(validate="focusout", validatecommand=(rateValidation,"%P"))
    rate.pack()
    tk.Button(new, text="Submit", command=lambda: addToLog(workoutName,length,calories,rate)).pack()


def addToLog(workoutName, length, calories, rate):
    print(workoutName.get())
    print(length.get())
    print(calories.get())
    print(rate.get())

def validate_name(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please provide a name.')
    else:
        return True

def validate_calories(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please provide the amount of calories burned.')
    else:
        if input.isdigit() and int(input) in range(0,10000):
            return True
        else:
            messagebox.showerror('Error', 'Please enter a valid number between 0-10000.')
            return False

def validate_length(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please provide the length of the workout.')
    else:
        if input.isdigit() and int(input) in range(0,10000):
            return True
        else:
            messagebox.showerror('Error', 'Please enter a valid number of minutes between 0-10000.')
            return False
        
def validate_rate(input):
    if input == "":
        messagebox.showerror('Error', 'This field cannot be empty, please rate the workout.')
    else:
        if input.isdigit() and int(input) in range(1,10):
            return True
        else:
            messagebox.showerror('Error', 'Please enter a valid rating between 0-10.')
            return False