from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=10)
e.grid(row=0, column=0, columnspan=3) #padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    

def button_add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_num)
    e.delete(0, END)

def button_clear():
    e.delete(0, END)

def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_num))
    if math == "subtraction":
        e.insert(0, f_num - float(second_num))
    if math == "multiplication":
        e.insert(0, f_num * float(second_num))
    if math == "division":
        e.insert(0, f_num / float(second_num))
    if math == "remainder":
        e.insert(0, f_num % float(second_num))

def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_num)
    e.delete(0, END)

def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_num)
    e.delete(0, END)

def button_remainder():
    first_num = e.get()
    global f_num
    global math
    math = "remainder"
    f_num = float(first_num)
    e.delete(0, END)

button_1 = Button(root, text="1", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click(0))
button_dot = Button(root, text=".", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=lambda: button_click("."))
button_add = Button(root, text="+", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=button_add)
button_clear = Button(root, text="Clear", font=("Century Gothic",10,"bold"), padx=60, pady=20, command=button_clear)
button_equal = Button(root, text="=", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=button_equal)
button_subtract = Button(root, text="-", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=button_multiply)
button_divide = Button(root, text="/", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=button_divide)
button_perc = Button(root, text="%", font=("Century Gothic",10,"bold"), padx=30, pady=20, command=button_remainder)

button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)

button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)

button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_clear.grid(row=6, column=1)
button_equal.grid(row=4, column=2)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_dot.grid(row=4, column=1)
button_perc.grid(row=6, column=2)

myLabel = Label(root, text="copyright@ UDAY. LOL").grid(row=7, column=1)

root.mainloop()
