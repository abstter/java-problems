print('\n <<< Part 2 >>>')


print('\n *** Problem 6 *** ')

"""
Write code to display an informational message box with the title "Greetings"
and the message "Welcome to Python GUI programming!" This message box should be
triggered by clicking a button.
"""
print("See GUI window.")
import tkinter as tk
from tkinter import messagebox

def infobox():
    messagebox.showinfo("Greetings", 
                        "Welcome to Python GUI programmihng!")

root = tk.Tk()
btn = tk.Button(root, text="Click Me", command=infobox)
btn.grid(row=0, column=0)
root.mainloop() 




print('\n *** Problem 7 *** ')

"""
The following code is intended to create an error message box, but it has a bug
bug. Identify and fix the bug.
"""
print("See GUI window.")

import tkinter as tk
from tkinter import messagebox

def error_box():
    messagebox.showerror("Error", "This is an error.")

root = tk.Tk()
root.title("Problem 7")
root.geometry("350x50")

button = tk.Button(root, text="Show Error", command=error_box)
button.pack()
root.mainloop()


print('\n *** Problem 8 *** ')

"""
The following code is intended to create a warning message box, but it has a
bug. Identify and fix the error.
"""
print("See GUI window.")

import tkinter as tk
from tkinter import messagebox

def warning_box():
    messagebox.showwarning("Warning", "This is just a test warning.")

root = tk.Tk()
root.title("Problem 8")
root.geometry("350x50")

button = tk.Button(root, text="Show Warning", command=warning_box)
button.pack()
root.mainloop()


print('\n *** Problem 9 *** ')

"""
Write a script to display a message box that asks the user if they enjoy
eating pineapple on pizza. If the user clicks "Yes", display "Me too!" in
another message box. If "No", display "That's OK, it's not for everyone!".

Note: Technically, tkinter message boxes do not require you, the programmer, 
to explicitly create a root window, as modal dialogs like message boxes are
transient interface elements rather than widgets that attach to a window.
However, if you create a messagebox without first creating a root window,
tkinter will implicitly create a root window for you in the background. Thus,
you should still explicitly create a root window in most cases for consistency
and control over how that window looks and behaves.
"""
print("See GUI window.")
import tkinter as tk
from tkinter import messagebox

def questionbox():
    response = messagebox.askquestion("Pizza", 
                                      "Do you like eating pineapple on pizza?")
    if response == 'yes' or response == 'Yes':
        messagebox.showinfo("", "Me too!")
    else:
        messagebox.showinfo("", "That's ok, its not for everyone.")
questionbox()



print('\n *** Problem 10 *** ')

"""
Create a Tkinter GUI application with a menu bar containing two main menu items:
"Actions" and "Settings". Under "Actions", add two options: "Greet" and "Close".

The "Greet" option should display a message box saying "Hello, multiverse!"

The "Close" option should close the application.

Under "Settings", add an option "Info" that displays an informational message:
    "In another universe, this is where you would change the settings!"
"""
print("See GUI window.")
import tkinter as tk
import tkinter.messagebox as messagebox
def show_about():
    messagebox.showinfo("About", 
                        "Tkinter application")
root = tk.Tk()
root.title("Menu bar")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)  
file_menu = tk.Menu(menu_bar)

def greet():
    messagebox.showinfo("Greet", 
                        "Hello, multiverse!")
def show():
    messagebox.showinfo("Info", 
                        "In another universe, this is where you would change the settings!")

menu_bar.add_cascade(label="Actions", menu=file_menu)
file_menu.add_command(label="Close", command=root.destroy)
file_menu.add_command(label="Greet", command=greet)  
help_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Settings", menu=help_menu)
help_menu.add_command(label="Info", command=show)
root.mainloop() 


'''

print('\n *** Problem 11: Challenge Problem *** ')
"""
Create a Tkinter GUI application where users can input numbers and view them in
a Listbox. The application should have an entry field, a button to add numbers,
a Listbox with a scrollbar to display the numbers, and two menu options,
"Show Sum" and "Show Average", under a "Calculate" menu in a top menu bar.

The program should validate the input as a floating-point number and update the
Listbox with each new number added.

To check whether an input string can be converted into a valid floating-point 
number, use the provided is_float() function, which returns True if its string 
argument is a float and False otherwise.

Use messageboxes to output any error messages (e.g., the user enters an invalid
input--not a floating-point number) and the results of calculations.
"""
print("See GUI window.")

# Function to check if a string can be converted to a float
def is_float(string):
    # Check if the string starts with a minus sign
    if string.startswith("-"):
        string = string[1:]  # Remove the minus sign for further checks
    # Replace one decimal point and check if the rest of the string is numeric:
    return string.replace(".", "", 1).isnumeric()
'''