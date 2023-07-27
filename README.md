# SuperSets

SuperSets is a python program that allows the user to track their workouts. It is made using the Tkinter GUI Library. This application has two windows: a home window and a logging window. The user can navigate to the logging window by pressing a button. Once the "Log your own workout" is clicked, a new window appears. This window has user entry boxes that allow the user to insert information. This information has data validation built into it to make sure the user enters the right information. From here the user can click submit to ensure their workout gets logged, or they can click exit to return to the original window.

## Installation

You will need the Tkinter Library as well as the PIL Library to be able to view this program on a GUI. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install both.

```bash
pip install tk
```

```bash
pip install Pillow
```

## Usage

```python
import tkinter as tk

# initializes a new window'
root = tk.TK()

# returns a label on the new window with the text "Hello World"
tk.Label(root,text="Hello World").pack()

# returns a user input box for an email address
tk.Entry(root, textvariable="email").pack()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Citation

This software can be cited by using my first and last name: Tania Olivas

## Contact

Email: taniaolivas24@gmail.com
