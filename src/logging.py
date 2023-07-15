import tkinter as tk

def loggingWindow():
    new = tk.Toplevel()
    new.geometry("650x250")
    new.title("Log Your Workout")
    tk.Label(new, text="Logging Window").pack()