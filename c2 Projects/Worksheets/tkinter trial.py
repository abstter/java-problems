import tkinter as tk

root = tk.Tk()

root.title('My first GUI')

label = tk.Label(root,text = 'Hello GUI')
label.pack()
def display():
    print('Suiii Mbappe')
button1 = tk.Button(root,text = 'Oh hell nah Brother',command=display)
button1.pack()


def getinput():
    info = entry.get()
    print(info)
entry = tk.Entry(root)
entry.pack()
button2 = tk.Button(root, text = "GOAT", command = getinput)
button2.pack()


check1 = tk.Checkbutton(root, text = "option1")
check2 = tk.Checkbutton(root, text = "option2")
check1.pack()
check2.pack()

listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.pack()

root.mainloop()




