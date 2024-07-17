"""
Quiz # 4: Graphical User Interfaces
Student Code
Python Level 3

Name: Abhiram
Class Section: D14
"""

import tkinter as tk

print('\n *** Problem 1 *** ')  # 20 points

"""
a. Initialize a root window (4 points)
b. Create a Listbox called listbox and a Scrollbar called scrollbar. (6 points)
c. Add code to synchronize the scrollbar with the listbox, enabling each to
   scroll the other. (10 points)
"""
print("See GUI window.")

# Initialize the root window. The title and dimensions are already set for you:
root = tk.Tk()
root.title("Problem 1")
root.geometry("350x300")

# Create the listbox and scrollbar here:
listbox = tk.Listbox(root)
listbox.pack()
scrollbar = tk.Scrollbar(root)

# Placing listbox and scrollbar:
listbox.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')

# Filling in the listbox with the integers 0 through 49:
for i in range(50):  
    listbox.insert(tk.END, i)

# Add code to synchronize the listbox and scrollbar here:
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()



print('\n *** Problem 2 *** ')  # 20 points

"""
The following incomplete program is to contain a label and a text widget below 
the label. It will continuously count and display in the label, in real time,
the number of keypresses that have been typed into the text widget so far.

Fill in the missing code:

a. Create and place a label called count_label. It will display the total number
   of keypresses so far, which starts off at 0. The update function is provided
   for you, so all you need to do is place the label showing the text,
   "Total Keypresses: 0" (5 points)
   
b. Create and place a text widget with width 30 and height 10. (5 points)

c. Bind keypresses in the text widget to the update function using bind().
   Again, keypresses must specifically be in the text widget, not just the root
   window in general, so set your bind accordingly. (5 points)
"""
#print("See GUI window.")
#
#def update_keypress_count(event):
#    global keypress_count
#    keypress_count += 1
#    count_label.configure(text=f"Total Keypresses: {keypress_count}")
#    
#root = tk.Tk()
#root.title("Problem 2")
#root.geometry("350x150")
#
#keypress_count = 0
#
## Create and place the label (count_label) to display the keypress count:
#count_label = tk.Label(root, keypress_count)
#
## Create and place the text widget:
#text_widget = tk.Text(root, width=30, height=10)
#text_widget.grid(row=0, column=0)
#
#
## Bind keypresses in the text widget to the update function:
#text_widget.bind(update_keypress_count)
#root.mainloop()



print('\n *** Problem 3 *** ')  # 25 points

"""
The following incomplete program is to have a single widget--a label--whose text
changes from normal to bold style whenever the mouse hovers over the label, and
back to normal when the cursor leaves the label.

Fill in the missing code by following these instructions:

a. Create and place a Label containing the text "Hover the mouse cursor here!"
   Set height 10, width 40, and font Arial, size 12, normal style. (5 points)

Implement the following event handling:

b. When the cursor moves over the label widget, the label font style changes to
   "bold". (10 points)
   
c. When the cursor moves away from the label widget, the label font style changes 
   back to "normal". (10 points)
   
"""
print("See GUI window.")

import tkinter as tk

# Define the functions to adjust the label font style here:
def change(event):
    label.configure(font=("Arial", 12, "bold"))
def change1(event):
    label.configure(font=("Arial", 12, "normal"))
    
    
root = tk.Tk()
root.title("Problem 3")
root.geometry("400x300")

# Create and place the label widget here:
label = tk.Label(root, text="Hover the mouse cursor here!", 
                 font=("Arial", 12, "normal"), height=10, width=40)
label.pack()

# Bind each cursor event to the label and the matching function here:
root.bind("<Enter>", change)
root.bind("<Leave>", change1)

root.mainloop()



print('\n *** Problem 4 *** ')  # 35 points

"""
The following incomplete program is to have a label and three buttons, 
each of which change the label's font (foreground) to a different color.

Fill in the missing tkinter code to implement the following widgets and features
as instructed below:

_Interface appearance and behavior_

a. A Label with the text "Choose your favorite color:" (3 points)
b. Three Buttons labeled "Red", "Green", and "Blue" (6 points)

c. The Label should span three columns, and the three buttons should be
   side-by-side beneath the label as sketched below: (8 points)
   
       [ Choose your favorite color: ]
        [ Red ]  [ Green ]  [ Blue ]
   
d. When a button is clicked, the Label's font (foreground) color should change 
   to the selected color. See implementation details below. (6 points)
  
_Implementation details_
e. Define three separate functions, one to set each color. (6 points)
f. Use each button's command attribute to bind it to the right function.
   (6 points)

"""
print("See GUI window.")

import tkinter as tk

# Define the three color-change functions here:
def red():
    label.configure(fg="red")
def blue():
    label.configure(fg="blue")
def green():
    label.configure(fg="green")
    
root = tk.Tk()
root.title("Problem 4")
root.geometry("350x100")

# Create and place the label here:
label = tk.Label(root, text="Choose your favorite color:", fg="#00FF00")
label.pack()

# Create and place the buttons here:
button1 = tk.Button(root, text="Red", command=red)
button2 = tk.Button(root, text="Green", command=green)
button3 = tk.Button(root, text="Blue", command=blue)
button1.pack()
button2.pack()
button3.pack()








root.mainloop()