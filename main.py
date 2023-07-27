"""
This main.py module sets up the main window of the program.
It includes two buttons, one that will open up another window
and another that will exit the program.
"""

# Imports tkinter and PIL to use for the GUI
# Imports the loggingWindow function from the logging.py module
import tkinter as tk
from src.logging import loggingWindow
from PIL import ImageTk, Image

# Initializes the main window 
root = tk.Tk() # Variable assigned to initialized window to call to it easier
root.title("Home")
root.geometry('400x400')

# Opens and resizes the dumbbell picture
db = Image.open("/Users/taniaolivas/Documents/SDEV140/superSets/src/dumbbells.png")
resize_db = db.resize((100,100))
dumbbells = ImageTk.PhotoImage(resize_db)

# Opens and resizes the stopwatch picture
sw = Image.open("/Users/taniaolivas/Documents/SDEV140/superSets/src/stopwatch.png")
resize_sw = sw.resize((100,100))
stopwatch = ImageTk.PhotoImage(resize_sw)

# First label to ask the user what they would like to do
tk.Label(root,text="What would you like to do?").pack()

# Provides a button that will take them to the logging page once clicked
loggingButton = tk.Button(root, text="Log your workout", command=loggingWindow)
loggingButton.pack()

# An exit button to leave the window
exitButton = tk.Button(root, text="Exit", command=root.destroy)
exitButton.pack()

# Two labels that have images instead of text
dumbbellImage = tk.Label(root, image=dumbbells).pack(side=tk.LEFT) 
stopwatchImage = tk.Label(root, image=stopwatch).pack(side=tk.RIGHT)


root.mainloop()