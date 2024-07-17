"""
Worksheet # 12: Introduction to GUI programming
Student Code
Python Level 3

Student Name:
Class Section (if any):
"""

print('\n *** Problem 1 *** ')

"""
In your own words, what is the biggest advantage of a GUI over a text-based,
command-line interface?
"""
print("Answer in the comment.")

"""
Answer:
Provides higher level of security and requires less memory.
Easier to use for non-experts.
Performs complex tasks faster and requires less memory.
Requires less processing power.

"""


print('\n *** Problem 2 *** ')

"""
What is the primary purpose of a window in tkinter?
"""
print("Answer in the comment.")

"""
Answer: The foundational element of a Tkinter GUI is the window.
Windows are the containers in which all other GUI elements live.
These other GUI elements, such as text boxes, labels, and buttons, are known as widgets.
Widgets are contained inside of windows.


"""


print('\n *** Problem 3 *** ')

"""
Write a Python tkinter script below to create a window titled "Problem 3", and
add a button with the text "Click Me". Manually resize the window to verify the
window title.
"""
print("See GUI window.")
import tkinter as tk

root = tk.Tk()

root.title('Problem 3')

def display():
    pass
button1 = tk.Button(root,text = 'Click Button',command=display)
button1.pack()


print('\n *** Problem 4 *** ')

"""
Add a function to your GUI code from Problem 3 to print "Yay you clicked me!"
whenever the button is clicked. Rename the root window title to "Problem 4".
"""
print("See GUI window.")
import tkinter as tk

root = tk.Tk()

root.title('Problem 4')

def display():
    print("Yay you clicked me!")
button1 = tk.Button(root,text = 'Click Button',command=display)
button1.pack()


print('\n *** Problem 5 *** ')

"""
Explain the use of "import tkinter as tk" in a tkinter program.
"""
print("Answer in the comment.")

"""
Answer: Tkinter is a built-in GUI library to create cross-platform GUI applications.
This library is lightweight and easy to use compared to other GUI libraries.

"""


print('\n *** Problem 6 *** ')

"""
Create a tkinter window with the title "Problem 6".
Add a label to the tkinter window that displays the text "Hello, World!"
Comment out any previous tkinter code to enable this code to run.
"""
print("See GUI window.")
import tkinter as tk

root = tk.Tk()

root.title('Problem 6')

label = tk.Label(root,text = 'Hello World!')
label.pack()


print('\n *** Problem 7 *** ')

"""
Modify the code in Problem 6 to extend the text in the label to display
"Hello, World! This string is longer to demonstrate window resizing."
Title the root window "Problem 7".
"""
print("See GUI window.")
import tkinter as tk

root = tk.Tk()

root.title('Problem 6')

label = tk.Label(root,text = 'Hello World! This string is longer to demonstrate window resizing')
label.pack()



print('\n *** Problem 8 *** ')

"""
Identify and fix the error in the code. 
"""
print("See GUI window.")

import tkinter as tk

main = tk.Tk()
main.title("Error Search")
def display():
    pass
button = tk.Button(main, text="Press Me")
button.pack()
main.mainloop()