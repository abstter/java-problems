"""
Worksheet # 17: Additional Widgets
Student Code
Python Level 3

Student Name:
Class Section (if any):
"""

print('\n <<< Part 1 >>>')

print('\n *** Problem 1 *** ')

"""
Debug the following code snippet. It is intended to attach a scrollbar to a
Listbox in Tkinter, but it's not functioning correctly.
"""
print("See GUI window.")

import tkinter as tk

root = tk.Tk()
root.title("Problem 1")
root.geometry("350x300")

listbox = tk.Listbox(root)
scrollbar = tk.Scrollbar(root)

scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand = scrollbar.set)

for i in range(100):
    listbox.insert(tk.END, i)

listbox.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")

root.mainloop()


print('\n *** Problem 2 *** ')

"""
Describe the purpose of the yscrollcommand and command attributes when linking
a scrollbar with a Text widget in Tkinter. Why are both needed?
"""

"""
Answer: The yscrollcommand attribute makes the scrollbar update its position when the listbox is scrolled.
the command attribute of the scrollbar to the yview method of the listbox to make sure that the listbox scrolls when the scrollbar is moved. 



"""
print("Answer in comment.")


print('\n *** Problem 3 *** ')

"""
Write a Python script to include a Tkinter window with a Text widget and a
Button widget. The Text widget should have the following properties:

a. Width of 40 characters and height of 10 lines.
b. Background color is light gray, and the text color is blue.
c. Default text that reads "Enter your text here." is inserted at the beginning.

Include a button labeled "Clear Text". When this button is clicked, it should
clear all text from the Text widget.
"""
print("See GUI window.")
import tkinter as tk
root = tk.Tk()
label = tk.Label(root,bg="lightgray", fg="blue")
label.pack()

label.pack()
root = tk.Tk()
text_widget = tk.Text(root, width=40, height=10)
text_widget.grid(row=0, column=0, sticky='nsew')
text_widget.insert(tk.END, 
                   "Enter your text here!")
text_widget.delete("1.0", tk.END)

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=1, sticky='ns')

text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

root.mainloop()



print('\n *** Problem 4 *** ')

"""
Modify the program you created in Problem 3 by adding another button labeled
"Submit Text" (on the same row and to the right of the "Clear Text" button).
Clicking this button should output the contents of the Text widget to the
console. Test this by entering text of your own into the Text field and then
clicking "Submit Text".
"""
print("See GUI window.")



print('\n *** Problem 5: Challenge Problem *** ')

"""
Modify the code from problem 4 to add the following features:

a. Clicking on the Text field for the first time should automatically clear
   the widget so that the user can begin typing into a blank field. This
   should only happen the first time the user clicks in the field.
   
b. Every time the user clicks Submit Text, the text in the widget should be 
   saved in a data structure (instead of immediately printing to console) and
   then cleared from the Text widget.
   
c. Add a button called "Retrieve Text" to print to the console all the text
   messages submitted so far.

"""
print("See GUI window.")



