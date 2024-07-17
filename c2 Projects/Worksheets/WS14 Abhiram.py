"""
Worksheet # 14: Configuring Widgets
Student Code
Python Level 3

Student Name:
Class Section (if any):
"""

print('\n *** Problem 1 *** ')

"""
Write tkinter code with the following graphical elements:

a. Create a label with the text, "Welcome to my colorful world!"
   with the following settings:
     i. a blue background
     ii. a yellow foreground (font)
     iii. font Arial, size 12, bold
b. Create a button with the text "Click me to change the label
   color!"
c. When the button is clicked, it should change the label's
   configuration settings to the following:
     i. a green background
     ii. a pink font
     iii. (font remains unchanged)
"""
print("See GUI window.")
import tkinter as tk
#
#root = tk.Tk()
#
#root.title('Problem 1')
#
#label = tk.Label(root, text="Welcome to my colorful world!", 
#                 font=("Arial", 12, "bold"))
#label.configure(bg="blue", fg="yellow")
#label.pack()   
#def change_color():
#    label.configure(bg="green", fg="pink")
#button = tk.Button(root, text="Click me to change the label color!",command=change_color)
#button.pack()


print('\n *** Problem 2 *** ')

"""
Modify the code in Problem 1 so that clicking the button changes the appearance
of the label from a to b to c and then back to a (detailed below). Use some of
the properties below in your conditionals to check the label's current state.

   a. blue background + yellow font
   b. green background + pink font
   c. red background + white font
   
Comment out previous tkinter code or close previous GUI windows as needed.
"""
print("See GUI window.")
#import tkinter as tk
#root = tk.Tk()
#root.title('Problem 2')
#label1 = tk.Label(root, text="Welcome to my colorful world!",bg="blue", fg="yellow", font=("Arial", 12, "bold"))
#label1.pack()
#def change_color():
#    back = label1.cget("bg")
#    if back == "blue":
#        label1.configure(bg="green", fg="pink")
#    elif back == "green":
#        label1.configure(bg="red", fg="white")
#    else:
#        label1.configure(bg="blue", fg="yellow")
#button1 = tk.Button(root, text="Click me to change the label color!",command=change_color)
#button1.pack()


print('\n *** Problem 3 *** ')

"""
Create a similar program to that in Problem 2, but display only a single 
button with the text "This is a dynamic font button!" that cycles through 
the following font settings when clicked:

    a. Arial, 12, bold font
    b. Georgia, 11, italic font
    c. Comic Sans MS, 12, underline font

Note that cget() returns a widget's font settings as a string of the font name,
font size, and font style, e.g. "Arial 12 bold". To get just one of those three
values, you must first use split() to separate the string into a list of its
words. Then, get the desired element of that string:

    font_data = widget_name.cget("font")
    font_name = font_data.split()[0]

Comment out previous tkinter code or close previous GUI windows as needed.
"""
print("See GUI window.")
#import tkinter as tk
#root = tk.Tk()
#root.title('Problem 3')
#label2 = tk.Label(root, text="Welcome to my colorful world!",font=("Arial", 12, "bold"))
#label2.pack()
#def change_font():
#    font_data = label2.cget("font")
#    font_name = font_data.split()[0]
#    if font_name == "Arial":
#        label2.configure(font=("Georgia", 11, "italic"))
#    elif font_name == "Georgia":
#        label2.configure(font=("Comic Sans MS", 12, "underline"))
#    else:
#        label2.configure(font=("Arial", 12, "bold"))
#button2 = tk.Button(root, text="This is a dynamic font button!",command=change_font)
#button2.pack()


print('\n *** Problem 4 *** ')

"""
Write a Python tkinter program to create a window of size 400x200 pixels. Inside
this window, add a Button widget with the text "Increase Window Size" and set
its width to 25 characters and height to 2 lines. After clicking the button, the
window should resize to 800x400 pixels.

Comment out previous tkinter code or close previous GUI windows as needed.
"""
print("See GUI window.")



print('\n *** Problem 5 *** ')

"""
Create a tkinter application with a window size of 600 x 300. Add
three buttons side-by-side labeled:

"Cursor: Hand", "Cursor: Heart", and "Cursor: Arrow".

a. When the "Cursor: Hand" button is clicked, the cursor should
   change to a hand (for the entire root window).
b. When the "Cursor: Heart" button is clicked, the cursor should
   change to a heart (for the entire root window).
c. When the "Cursor: Arrow" button is clicked, it should go back
   to the default arrow cursor (for the entire root window).
   
To set the cursor for the entire root window, configure root as you
would any other widget. For example:

    root.config(cursor="pirate")

Comment out previous tkinter code or close previous GUI windows as needed.
"""
root = tk.Tk()
root.title('Problem 5')
root.geometry("600*300")


print("See GUI window.")
