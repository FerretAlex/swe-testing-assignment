import tkinter as tk
import calc_logic as cl
root = tk.Tk()

root.title("Quick-Calc")

tk.Label(root, text="First variable").grid(row=0, column=0)
tk.Label(root, text="Second variable").grid(row=1, column=0)
tk.Label(root, text="Answer").grid(row=2, column=0)

var_a = tk.Entry(root)
var_b = tk.Entry(root)
ans_text = tk.Label(root)

var_a.grid(row=0, column=1)
var_b.grid(row=1, column=1)
ans_text.grid(row=2, column=1)

def read_variables():
    a = int(var_a.get())
    b = int(var_b.get())
    return a, b

def add_button():
    a, b = read_variables()
    ans = cl.addition(a, b)
    ans_text.config(text=ans)

add_button = tk.Button(root, text="Add", width=25, command=add_button)
add_button.grid(row=0, column=2)

def sub_button():
    a, b = read_variables()
    ans = cl.subtraction(a, b)
    ans_text.config(text=ans)

sub_button = tk.Button(root, text="Subtract", width=25, command=sub_button)
sub_button.grid(row=1, column=2)

def mult_button():
    a, b = read_variables()
    ans = cl.multiplication(a, b)
    ans_text.config(text=ans)


mult_button = tk.Button(root, text="Multiply", width=25, command=mult_button)
mult_button.grid(row=2, column=2)

def div_button():
    a, b = read_variables()
    ans = cl.division(a, b)
    ans_text.config(text=ans)


div_button = tk.Button(root, text="Divide", width=25, command=div_button)
div_button.grid(row=3, column=2)

def c_button():
    var_a.delete(0, tk.END)
    var_b.delete(0, tk.END)
    var_a.insert(0, 0)
    var_b.insert(0, 0)
    ans_text.config(text=0)

c_button = tk.Button(root, text="Clear", width=25, command=c_button)
c_button.grid(row=4, column=2)

root.mainloop()
