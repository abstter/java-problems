"""
Worksheet # 15: Basic Event Handling
Student Code
Python Level 3

Student Name:
Class Section (if any):
"""
          
print('\n *** Problem 1 *** ')

"""
Write tkinter code to create a button that alternates between red and blue
backgrounds when clicked. The foreground (text) should be white.
"""
print("See GUI window.")
#import tkinter as tk
#root = tk.Tk()
#root.title('Problem 1')
#label1 = tk.Label(root, text="Welcome to my colorful world!",bg="red", fg="white", font=("Arial", 12, "bold"))
#label1.pack()
#def change_color():
#    back = label1.cget("bg")
#    if back == "red":
#        label1.configure(bg="blue")
#    elif back == "blue":
#        label1.configure(bg="red")
#button1 = tk.Button(root, text="Click me to change the label color!",command=change_color)
#button1.pack()


print('\n *** Problem 2 *** ')

"""
Write a tkinter script where pressing any key changes the text of a Label widget
to "Key Pressed". Use bind() to bind your function to the root window.
(Sometimes, keypress detection is done for specific widgets, but in this case,
we just want to detect the keypress whenever the window is active.)
"""
print("See GUI window.")
#import tkinter as tk
#root = tk.Tk()
#label2 = tk.Label(root, text="Click Me")
#def button1(event):
#    label2.configure(text="Key Pressed!")
#label2.pack()
#root.bind("<Key>", button1)




print('\n *** Problem 3 *** ')

"""
Create a GUI with a label that changes its text to "Mouse Hovering" when the
mouse hovers over it and reverts back to "Hover over me" when the mouse leaves.
"""
print("See GUI window.")
#import tkinter as tk
#root = tk.Tk()
#label1 = tk.Label(root, text="Hover Over Me", 
#                   cursor="circle")
#label1.pack()
#def change(event):
#    label1.configure(text="Mouse Hovering")
#root.bind("<Enter>", change)
#def change(event):
#    label1.configure(text="Hover over me")
#root.bind("<Leave>", change)
#root.mainloop()




print('\n *** Problem 4 *** ')

"""
Write tkinter code to create a label with a width of 30 columns and a height of
10 rows. The label should display "Double Clicked!" when double-clicked.
"""
print("See GUI window. Double-click in the label to activate text.")
#import tkinter as tk
#root = tk.Tk()
#def double(event):
#    label2.configure(text = "Double Clicked")
#label2 = tk.Label(root, text="Click me")
#label2.pack()
#root.bind("<Double-Button-1>", double)
#root.mainloop()



print('\n *** Problem 5 *** ')

"""
Create a tkinter label with a width of 60 columns and a height of 30 rows. The
label should update to show the current mouse position (x, y) whenever the mouse
moves over it. Remember that a mouse event object has two attributes, event.x
and event.y, that report the current coordinates of the mouse.
"""
print("See GUI window.")
import tkinter as tk
root = tk.Tk()
def reporting(event):
    label1.configure(text=f"{event.x}, {event.y}")
label1 = tk.Label(root, text="Label", width = 60, height = 30)
root.bind("<Motion>", reporting)
label1.pack()
root.mainloop()


print('\n *** Problem 6: Challenge Problem *** ')

"""
Write Python tkinter code with two buttons and a label sandwiched between them,
all on the same line, placed using grid().

The left button should have the text "-" and the right button should have the
text "+". The label should start off displaying 0.

That label's display value should decrease by 1 whenever the "-" button is
clicked and whenever the minus key "-" on the keyboard is pressed. (Bind the
<KeyPress-minus> event code to root.)

Meanwhile, the label's value should increase by 1 whenever the "+" button is
clicked or whenever the "+" key is pressed. (Bind the <KeyPress-plus> event
code to root.)

Hints:
1. A label's text attribute is a string, so you must do conversions
   back and forth between string and integer types to increment/
   decrement and update the value.
2. Assigning a button's command attribute to a function does not
   pass an event object to the function. However, using bind() to
   bind an event to a function does pass an event object to that
   function. If you use the same function for both, you may get an
   error. You can resolve this by either:
      a. using only bind() for buttons instead of the command attribute, or
      b. making the function's event parameter optional with a default value of
         None so that it works with both the command attribute and bind(), or
      c. defining separate functions to assign to each button's command
         attribute and bind() events (the least efficient choice).
"""
print("See GUI window.")
