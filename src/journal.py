import tkinter as tk

def journalWindow():
    new = tk.Toplevel()
    new.geometry("650x250")
    new.title("Your Workout Journal")
    tk.Label(new, text="Journal Window").pack()