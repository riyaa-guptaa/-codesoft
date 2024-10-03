from tkinter import *

class CustomButton(Button):
    def _init_(self, master=None, **kwargs):
        super()._init_(master, **kwargs)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# Function to update the display
def button_click(value):
    current = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, current + value)

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Function to clear the display
def clear():
    entry.delete(0, END)

# Create the main window
root = Tk()
root.resizable(False, False)
root.title("Calculator")

# Create the display
entry = Entry(root, width=22, font=("Arial", 18), insertontime=0, bd=5, borderwidth=8, foreground="#ff0000", highlightthickness=3, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0", justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipadx=11, ipady=8)

# Define button layout
button_layout = [
    ("C", 1, 0, 3, "#ff4d4d", "#6699ff", clear),
    ("/", 1, 3, 1, "#ffe46b", "#d0c6f5", lambda value="/": button_click(value)),
    ("7", 2, 0, 1, "#73f5d7", "#FFFFFF", lambda value="7": button_click(value)),
    ("8", 2, 1, 1, "#73f5d7", "#FFFFFF", lambda value="8": button_click(value)),
    ("9", 2, 2, 1, "#73f5d7", "#FFFFFF", lambda value="9": button_click(value)),
    ("", 2, 3, 1, "#ffe46b", "#d0c6f5", lambda value="": button_click(value)),
    ("4", 3, 0, 1, "#73f5d7", "#FFFFFF", lambda value="4": button_click(value)),
    ("5", 3, 1, 1, "#73f5d7", "#FFFFFF", lambda value="5": button_click(value)),
    ("6", 3, 2, 1, "#73f5d7", "#FFFFFF", lambda value="6": button_click(value)),
    ("-", 3, 3, 1, "#ffe46b", "#d0c6f5", lambda value="-": button_click(value)),
    ("1", 4, 0, 1, "#73f5d7", "#FFFFFF", lambda value="1": button_click(value)),
    ("2", 4, 1, 1, "#73f5d7", "#FFFFFF", lambda value="2": button_click(value)),
    ("3", 4, 2, 1, "#73f5d7", "#FFFFFF", lambda value="3": button_click(value)),
    ("+", 4, 3, 1, "#ffe46b", "#d0c6f5", lambda value="+": button_click(value)),
    ("0", 5, 0, 2, "#73f5d7", "#FFFFFF", lambda value="0": button_click(value)),
    (".", 5, 2, 1, "#73f5d7", "#FFFFFF", lambda value=".": button_click(value)),
    ("=", 5, 3, 1, "#6dff6b", "#c6f5ea", calculate),
]

# Create buttons using a loop
for (text, row, column, columnspan, active_bg, bg_color, cmd) in button_layout:
    Button(
        root,
        text=text,
        width=9 if text == "0" else 4,
        height=1 if text in ["0", "="] else 1,
        padx=39.4 if text == "0" else 20,
        pady=10,
        activebackground=active_bg,
        bg=bg_color,
        font=("20"),
        command=cmd,
    ).grid(row=row, column=column, columnspan=columnspan)

# Run the application
root.mainloop()
