import tkinter
from tkinter import *
root = Tk()

root.geometry("250x480+250+250")
root.title("Calculator")
root.resizable(0,0)

val = ""
A = 0
operator = ""

def btn_1isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2isclicked():
    global val
    val = val + "2"
    data.set(val)
    
def btn_3isclicked():
    global val
    val = val + "3"
    data.set(val)
    
def btn_4isclicked():
    global val
    val = val + "4"
    data.set(val)
    
def btn_5isclicked():
    global val
    val = val + "5"
    data.set(val)
    
def btn_6isclicked():
    global val
    val = val + "6"
    data.set(val)
    
def btn_7isclicked():
    global val
    val = val + "7"
    data.set(val)
    
def btn_8isclicked():
    global val
    val = val + "8"
    data.set(val)
    
def btn_9isclicked():
    global val
    val = val + "9"
    data.set(val)
    
def btn_0isclicked():
    global val
    val = val + "0"
    data.set(val)
    
def btn_plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + " + "
    data.set(val)

def btn_minus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + " - "
    data.set(val)
    
def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + " * "
    data.set(val)    

def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + " / "
    data.set(val)
    
def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int(val2.split("+")[1])
        C = A + x
        val = str(C)
        data.set(val)
    elif operator == "-":
        x = int(val2.split("-")[1])
        C = A - x
        val = str(C)
        data.set(val)
    elif operator == "*":
        x = int(val2.split("*")[1])
        C = A * x
        val = str(C)
        data.set(val)
    elif operator == "/":
        x = int(val2.split("/")[1])
        if x == 0:
            A = 0
            val ="Not Defined"
            data.set(val)
        else:
            C = round(A / x,2)
            val = str(C)
            data.set(val)
                                       

data = StringVar()

lbl = Label(
    root,
    text = "",
    font = ("Comic Sans MS",33),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
    anchor = SE
)
def c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)


lbl.pack(expand = True,fill = "both")

btn1row = Frame(root)
btn1row.pack(expand = True,fill = "both")

btn2row = Frame(root)
btn2row.pack(expand = True,fill = "both")

btn3row = Frame(root)
btn3row.pack(expand = True,fill = "both")

btn4row = Frame(root)
btn4row.pack(expand = True,fill = "both")

btn1 = Button(
     btn1row,
     text ="1",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_1isclicked
)
btn1.pack(side = LEFT, expand = True,fill ="both",)

btn2 = Button(
     btn1row,
     text ="2",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_2isclicked
)
btn2.pack(side = LEFT, expand = True,fill ="both",)

btn3 = Button(
     btn1row,
     text ="3",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_3isclicked
)
btn3.pack(side = LEFT, expand = True,fill ="both",)

btn_plus = Button(
    btn1row,
    text ="+",
    font = ("comic Sans MS", 33),
    border = 0,
    command = btn_plus_clicked
)
btn_plus.pack(side =LEFT,expand = True,fill ="both")

btn4 = Button(
     btn2row,
     text ="4",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_4isclicked
)
btn4.pack(side = LEFT, expand = True,fill ="both",)

btn5 = Button(
     btn2row,
     text ="5",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_5isclicked
)
btn5.pack(side = LEFT, expand = True,fill ="both",)

btn6 = Button(
     btn2row,
     text ="6",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_6isclicked
)
btn6.pack(side = LEFT, expand = True,fill ="both",)

btn_minus = Button(
    btn2row,
    text ="-",
    font = ("Comic Sans MS",33),
    border = 0,
    command = btn_minus_clicked
)
btn_minus.pack(side= LEFT, expand = True,fill ="both")


btn7 = Button(
     btn3row,
     text ="7",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_7isclicked
)
btn7.pack(side = LEFT, expand = True,fill ="both",)
btn8 = Button(
     btn3row,
     text ="8",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_8isclicked
)
btn8.pack(side = LEFT, expand = True,fill ="both",)

btn9 = Button(
     btn3row,
     text ="9",
     font = ("Comic Sans MS", 33),
     border = 0,
     command = btn_9isclicked
)
btn9.pack(side = LEFT, expand = True,fill ="both",)

btn_multiply = Button(
    btn3row,
    text ="*",
    font = ("Comic Sans MS",33),
    border = 0,
    command = btn_mul_clicked
)
btn_multiply.pack(side= LEFT, expand = True,fill ="both")

btn_c = Button(
    btn4row,
    text ="C",
    font = ("Comic Sans MS",33),
    border = 0,
    command = c_pressed
)
btn_c.pack(side= LEFT, expand = True,fill ="both")

btn0 = Button(
    btn4row,
    text ="0",
    font = ("Comic Sans MS",33),
    border = 0,
    command = btn_0isclicked
)
btn0.pack(side= LEFT, expand = True,fill ="both")

btn_equal = Button(
    btn4row,
    text ="=",
    font = ("Comic Sans MS",33),
    border = 0,
    command = result
)
btn_equal.pack(side= LEFT, expand = True,fill ="both")

btn_divide = Button(
    btn4row,
    text ="/",
    font = ("Comic Sans MS",33),
    border = 0,
    command = btn_div_clicked
)
btn_divide.pack(side= LEFT, expand = True,fill ="both")

root.mainloop()