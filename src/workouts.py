import tkinter as tk

def workoutsWindow():
    new = tk.Toplevel()
    new.geometry("650x250")
    new.title("Other Workouts")
    tk.Label(new, text="Workout Window").pack()