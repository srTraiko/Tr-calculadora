from tkinter import *

root = Tk()
root.title("Calculadora simple")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Modo

global math
math = ""

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global add
    first_number = e.get()

    if first_number == "":
        print("")
    else:

        global f_num
        f_num = int(first_number)
        global math
        math = "add"
        e.delete(0, END)

def button_sub():
    first_number = e.get()

    if first_number == "":
        print("")
    else:
        global f_num
        f_num = int(first_number)
        global math
        math = "sub"
        e.delete(0, END)


def button_mul():
    first_number = e.get()

    if first_number == "":
        print("")
    else:
        global f_num
        f_num = int(first_number)
        global math
        math = "mul"
        e.delete(0, END)
    
def button_div():
    first_number = e.get()
    if first_number == "":
        print("")
    else:
        global f_num
        f_num = int(first_number)
        global math
        math = "div"
        e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, f_num + int(second_number))
    elif math == "sub":
        e.insert(0, f_num - int(second_number))
    elif math == "mul":
        e.insert(0, f_num * int(second_number))
    elif math == "div": 
        e.insert(0, f_num / int(second_number))
    else:
        print("")

# create bottons
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))

button_sum = Button(root, text="+", padx=30, pady=20, command= button_add)
button_subtract = Button(root, text="-", padx=30, pady=20, command= button_sub)
button_multiply = Button(root, text="*", padx=30, pady=20, command= button_mul)
button_divide = Button(root, text="/", padx=30, pady=20, command= button_div)

buttton_equal = Button(root, text="=", padx=30, pady=20, command= button_equal)
buttton_clear = Button(root, text="clear", padx=60, pady=20, command=button_clear)

# put the bottons in the screen

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_sum.grid(row=4, column=1)
buttton_equal.grid(row=4, column=2)
buttton_clear.grid(row=5, column=0, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=5, column=2)

root.mainloop()
