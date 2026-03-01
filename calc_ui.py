import tkinter as tk
import calc_logic as cl
root = tk.Tk()

root.title("Quick-Calc")

tk.Label(root, text="First variable").grid(row=0, column=0)
tk.Label(root, text="Second variable").grid(row=1, column=0)
tk.Label(root, text="Answer").grid(row=2, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Label(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

def button_press():
    a = int(entry1.get())
    b = int(entry2.get())
    return [a, b]

def add_button():
    a = button_press()[0]
    b = button_press()[1]
    ans = cl.addition(a, b)
    entry3.config(text=ans)

add_button = tk.Button(root, text="Add", width=25, command=add_button)
add_button.grid(row=0, column=2)

def sub_button():
    a = button_press()[0]
    b = button_press()[1]
    ans = cl.subtraction(a, b)
    entry3.config(text=ans)

sub_button = tk.Button(root, text="Subtract", width=25, command=sub_button)
sub_button.grid(row=1, column=2)

def mult_button():
    a = button_press()[0]
    b = button_press()[1]
    ans = cl.multiplication(a, b)
    entry3.config(text=ans)

mult_button = tk.Button(root, text="Multiply", width=25, command=mult_button)
mult_button.grid(row=2, column=2)

def div_button():
    a = button_press()[0]
    b = button_press()[1]
    ans = cl.division(a, b)
    entry3.config(text=ans)

div_button = tk.Button(root, text="Divide", width=25, command=div_button)
div_button.grid(row=3, column=2)

def c_button():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.insert(0, 0)
    entry2.insert(0, 0)
    entry3.config(text=0)

c_button = tk.Button(root, text="Clear", width=25, command=c_button)
c_button.grid(row=4, column=2)

root.mainloop()
