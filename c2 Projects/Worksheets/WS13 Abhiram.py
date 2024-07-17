"""
Worksheet # 13: Geometry Managers
Student Code
Python Level 3
"""

print('\n *** Problem 1 *** ')

"""
Given the code snippet below, identify and fix the errors and fill in
any missing code to ensure both labels appear in the tkinter window.
"""
print("See GUI window.")
#import tkinter as tk
#root = tk.Tk()
#root.title("Problem 1")
#
#label1 = tk.Label(root,text="First Label")
#label1.pack()
#label2 = tk.Label(root,text="Second Label")
#label2.pack()
#root.mainloop()


print('\n *** Problem 2 *** ')

"""
Write a script that creates a window titled "Problem 2" with two buttons,
"Hello" and "Goodbye", arranged side by side using the grid() method.
Comment out any previous tkinter code to allow this code to run.
"""
print("See GUI window.")
#import tkinter as tk
#
#root = tk.Tk()
#root.title('Problem 2')
#def display():
#    pass
#button1 = tk.Button(root, text='Hello', command=display)
#button2 = tk.Button(root, text='Goodbye', command=display)
#button1.pack()
#button1.grid(row=0, column=0)
#button2.grid(row=0, column=1)


print('\n *** Problem 3 *** ')

"""
In the following code, why does the button "Submit" not appear in the expected
position? Correct the code. Comment out any previous tkinter code to allow this
code to run.
"""
print("See GUI window.")

import tkinter as tk

root = tk.Tk()
root.title("Problem 3")

btn_submit = tk.Button(root, text="Submit")
btn_submit.place(x=200, y=300)

root.mainloop()

print('\n *** Problem 4 *** ')

"""
Write a tkinter program that creates an entry widget and a button
labeled "Submit". Place them in a window using the grid() geometry
manager so that the entry widget is in the first row and spans the
first three columns, and the button is in the second row and column.
Comment out any previous tkinter code to allow this code to run.
"""
print("See GUI window.")
#root = tk.Tk()
#root.title("Submit")
#def display():
#    entry = tk.Entry(root)
#    entry.grid(row = 0, column = 0, columnspan = 3)
#button1 = tk.Button(root, text = "Submit", command = display)
#button1.grid(row = 1, column = 1)
#root.mainloop()


print('\n *** Problem 5 *** ')

"""
The following code intends to place an entry widget and a button side by side,
but they are not displayed correctly. Identify and fix the issue.
"""
print("See GUI window.")

#import tkinter as tk
#
#root = tk.Tk()
#root.title("Problem 5")
#
#entry = tk.Entry(root)
#submit_btn = tk.Button(root, text="Submit")
#
#entry.place(x=150, y=20)
#submit_btn.place(x=250, y=20)
#
#root.mainloop()


print('\n *** Problem 6 *** ')

"""
In the following code, the checkbuttons are supposed to be aligned in a row,
but they are not. Find and correct the error.
"""
print("See GUI window.")

#import tkinter as tk
#
#root = tk.Tk()
#root.title("Problem 6")
#
#ck_btns = []
#
#for i in range(3):
#    ck_btns.append(tk.Checkbutton(root, text=f"Option {i}"))
#    ck_btns[i].grid(column=i, row=0)
#
#root.mainloop()


print('\n *** Problem 7: Challenge Problem *** ')

"""
a. Write a tkinter program to create a window with a title "Problem 7"
   and a label containing the question:

    "Which of the following can be found on Earth's axis of rotation?"

b. Below the label, create a group of four radiobuttons with the text

   "A. The North Pole", "B. The South Pole",
   "C. Neither", and "D. Both"

   The first two radiobuttons should be on the second row, and the
   last two should be on the third row.
   
c. Add a button with the text "Submit Answer" below the radiobuttons.

d. The radiobuttons should be aligned on the left of their grid cells.

e. The label and the "Submit Answer" button should span both columns.

f. Add some padding around every widget to add clear separation 
   between the graphical elements, making them easier to see.

Note that the radiobuttons will all appear pre-selected because they have
not yet been grouped together or tracked with a variable; you will
learn how to do this in the section on Event Handling.
"""
print("See GUI window.")
