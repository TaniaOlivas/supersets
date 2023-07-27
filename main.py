import tkinter as tk
from src.logging import loggingWindow
from PIL import ImageTk, Image


root = tk.Tk()
root.title("Home")
root.geometry('400x400')

db = Image.open("/Users/taniaolivas/Documents/SDEV140/superSets/src/dumbbells.png")
resize_db = db.resize((100,100))
dumbbells = ImageTk.PhotoImage(resize_db)

sw = Image.open("/Users/taniaolivas/Documents/SDEV140/superSets/src/stopwatch.png")
resize_sw = sw.resize((100,100))
stopwatch = ImageTk.PhotoImage(resize_sw)

tk.Label(root,text="What would you like to do?").pack()

loggingButton = tk.Button(root, text="Log your workout", command=loggingWindow)
loggingButton.pack()

exitButton = tk.Button(root, text="Exit", command=root.destroy)
exitButton.pack()

dumbbellImage = tk.Label(root, image=dumbbells).pack(side=tk.LEFT)
stopwatchImage = tk.Label(root, image=stopwatch).pack(side=tk.RIGHT)


root.mainloop()