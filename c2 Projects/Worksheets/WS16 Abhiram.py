"""
Worksheet # 16: Event Handling Logic
Student Code
Python Level 3

Student Name: Abhiram
Class Section (if any): D14-8B
"""
          
print('\n *** Problem 1 *** ')

"""
The following code is supposed to print the position of a mouse click on the
label, but it's not working. Find, fix, and explain the error.
"""
print("See GUI window.")

import tkinter as tk

def get_position(event):
    print("Clicked at:", event.x, event.y)

root = tk.Tk()
root.title("Problem 1")
root.geometry("350x80")

label = tk.Label(root, text="Click anywhere on this label", width=60, height=20)
label.pack()
label.bind("<Button-1>", get_position)

root.mainloop()


print('\n *** Problem 2 *** ')

"""
Write a program where two labels change their background color to green when the
mouse hovers over them. Bind both events to the same function.
"""
print("See GUI window.")
def on_hover(event):
    event.widget.config(bg='green')

root = tk.Tk()

label1 = tk.Label(root, text="Hover over me!")
label2 = tk.Label(root, text="And me!")

label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

label1.bind("<Enter>", on_hover)
label2.bind("<Enter>", on_hover)

root.mainloop()



print('\n *** Problem 3 *** ')

"""
Modify this code to display the selected item from the listbox in the label.
"""
print("See GUI window.")

import tkinter as tk

root = tk.Tk()
root.title("Problem 3")
root.geometry("350x350")

def on_select(event):
    widget = event.widget
    sel = widget.curselection() 
    if sel:
        index = sel[0]
        value = widget.get(index)
        label.config(text=f'Selected: {value}')

listbox = tk.Listbox(root)
for item in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, item)
listbox.pack()

label = tk.Label(root, text="Select an item:")
label.pack()
listbox.bind("<<ListboxSelect>>", on_select) 
root.mainloop()


print('\n *** Problem 4 *** ')

"""
Explain why special variables like StringVar are used in Tkinter and give an
example of where you might use one.
"""
print("Answer in comment.")

"""
Answer: The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectively.  By linking the StringVar to the Entry widget, we establish a dynamic connection between them.
As a result, any time the user enters data into the Entry widget, the linked StringVar (var) is automatically updated to reflect this data. 
"""


print('\n *** Problem 5 *** ')

"""
The following code is supposed to change the label text when the user
types "Hello" in the entry. Find and fix the error.
"""
print("See GUI window.")

import tkinter as tk

def update_label(event):
    if entry_var.get() == "Hello":
        label.config(text="Greeting detected!")

root = tk.Tk()
root.title("Problem 5")
root.geometry("400x100")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

label = tk.Label(root, text="")
label.pack()

entry.bind("<KeyRelease>", update_label)
root.mainloop()


print('\n *** Problem 6: Challenge Problem *** ')

"""
Create a Tkinter application with two checkbuttons labeled "Bold" and "Italic".
There should also be a label displaying some text. When a checkbutton is
selected, the corresponding style (bold or italic) should be applied to the
label's text. If both are selected, the text should be both bold and italic.

To make a font both bold and italic, the style string (the third element of the
font tuple) should be "bold italic", e.g.,

    label = tk.Label(root, text="Special Font Label", 
                     font=("Arial", 12, "bold italic"))
                 
Note: When you associate an IntVar with a checkbutton, the IntVar becomes a flag
for the checkbutton's status. It holds the value 1 when the checkbutton is
checked, indicating a 'True' state. Conversely, when the checkbutton is
unchecked, the IntVar is set to 0, representing a 'False' state. (In Python,
non-zero values are treated as True in conditions, and zero is treated as
False.) Thus, you can use the IntVar value directly in conditional statements
to determine the state of the checkbutton.
"""
print("See GUI window.")
root = tk.Tk()
print(root)


print('\n *** Problem 7: Challenge Problem *** ')

"""
Create a tkinter application where selecting a fruit from a set of radiobuttons
updates a label to display the possible colors for that fruit. The label should
change in real-time to report the colors associated with each fruit.

Steps (these don’t necessarily reflect the correct order of the code):
1. Create a dictionary to map some fruits to their possible colors (e.g.,
   "Apple" would map to a string "red, green, yellow, white"; "Banana" would
   map to "yellow, red, pink, purple"; etc.)
2. Set up a tkinter window with a group of radiobuttons for the different fruits
   (e.g., Apple, Banana, Cherry).
3. Create a StringVar to link to the radiobuttons, storing the value of the
   selected radiobutton (its fruit string, e.g., "Apple").
4. Add a label.
5. Implement a function to update the label's text based on the fruit selected
   via the radiobuttons.
6. Assign each radiobutton's command attribute to the function from step 5.
"""
print("See GUI window.")
