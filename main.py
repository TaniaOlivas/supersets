import tkinter as tk
from src.logging import loggingWindow
from src.journal import journalWindow



root = tk.Tk()
root.title("Home")
root.geometry("750x250")

tk.Label(root,text="What would you like to do?").pack()


loggingButton = tk.Button(root, text="Log your workout", command=loggingWindow)
loggingButton.pack()

journalButton = tk.Button(root, text="View your journal", command=journalWindow)
journalButton.pack()

exitButton = tk.Button(root, text="Exit", command=root.destroy)
exitButton.pack()

root.mainloop()