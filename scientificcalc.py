from tkinter import *
import math
import argparse
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator using Python")
root.configure(background="aquamarine")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

# Function declarations for numberpad
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    # Function declaration for equal operation
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    # Function declaration for add, sub, multi, divide and mod
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    # function declaration for clear
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    # Function declaration for all clear
    def all_clear_entry(self):
        self.Clear_Entry()
        self.total = 0

    # Function declaration for pi
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    # Function declaration for 2pi
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    # function declaration for 'e'
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    # function declaration of sqrt
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    # Function declaration of various trignometric functions
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cot(self):
        self.result = False
        self.current = math.atan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sec(self):
        self.result = False
        self.current = math.acos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosec(self):
        self.result = False
        self.current = math.asin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # function declaration of log
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    # function declaration of log2
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    # function declaration of log10
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    # function declaration of log1p
    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    # function declaration of exp
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    # function declaration of expml
    def expml(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    # function declaration of lgamma
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    # function declaration of deg
    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'),
                   bg="white", bd=25, width=29, justify=CENTER)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

# The Number Pad section
numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=(
            'arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1


# -------||||| Simple Calci Operations |||||-------
# the 'C' button
btnClear = Button(calc, text="C", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg="aquamarine", command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)

# the 'CE' Button
btnClearAll = Button(calc, text="CE", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="aquamarine", command=added_value.all_clear_entry).grid(row=1, column=1, pady=1)

# the '√ ' button
btnSqrt = Button(calc, text="√ ", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="aquamarine", command=added_value.squared).grid(row=1, column=2, pady=1)

# the '+' Button
btnAdd = Button(calc, text="+", width=6, height=5, font=('arial', 20, 'bold'), bd=4, bg="aquamarine",
                command=lambda: added_value.operation("add")).grid(row=4, column=3, rowspan=2, pady=1)

# the '-' Button
btnSub = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="aquamarine", command=lambda: added_value.operation("sub")).grid(row=3, column=3, pady=1)

# the 'x' Button
btnMult = Button(calc, text="x", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="aquamarine", command=lambda: added_value.operation("multi")).grid(row=1, column=3, pady=1)

# the '÷' Button
btnDiv = Button(calc, text="÷", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="aquamarine", command=lambda: added_value.operation("divide")).grid(row=2, column=3, pady=1)

# the '0' Button
btn0 = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
              bg="aquamarine", command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

# the '.' Button
btnDot = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="aquamarine", command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

# the '=' Button
btnEq = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'),
               bd=4, bg="cyan", command=added_value.sum_of_total).grid(row=5, column=2, pady=1)


# -------||||| Scientific Calci Operations |||||-------
# the 'C' button
btnClear = Button(calc, text="C", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg="aquamarine", command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)

# the 'CE' Button
btnClearAll = Button(calc, text="CE", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="aquamarine", command=added_value.all_clear_entry).grid(row=1, column=1, pady=1)

# the '√ ' button
btnSqrt = Button(calc, text="√ ", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="aquamarine", command=added_value.squared).grid(row=1, column=2, pady=1)

# the '+' Button
btnAdd = Button(calc, text="+", width=6, height=5, font=('arial', 20, 'bold'), bd=4, bg="aquamarine",
                command=lambda: added_value.operation("add")).grid(row=4, column=3, rowspan=2, pady=1)

# the '-' Button
btnSub = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="aquamarine", command=lambda: added_value.operation("sub")).grid(row=3, column=3, pady=1)

# the 'x' Button
btnMult = Button(calc, text="x", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="aquamarine", command=lambda: added_value.operation("multi")).grid(row=1, column=3, pady=1)

# the '÷' Button
btnDiv = Button(calc, text="÷", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="aquamarine", command=lambda: added_value.operation("divide")).grid(row=2, column=3, pady=1)

# the '0' Button
btn0 = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
              bg="aquamarine", command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

# the '.' Button
btnDot = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="aquamarine", command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

# the '=' Button
btnEq = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'),
               bd=4, bg="cyan", command=added_value.sum_of_total).grid(row=5, column=2, pady=1)

# Basic Trignometric operations

# the '𝝿' Button
btnPi = Button(calc, text="𝝿", width=6, height=2, font=('arial', 20, 'bold'),
               bd=4, bg="aquamarine", command=added_value.pi).grid(row=1, column=4, pady=1)

# the '2𝝿' Button
btn2Pi = Button(calc, text="2𝝿", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.tau).grid(row=2, column=4, pady=1)

# the 'Cos' Button
btnCos = Button(calc, text="cos", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.cos).grid(row=1, column=5, pady=1)

# the 'sec' Button
btnsec = Button(calc, text="sec", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.sec).grid(row=2, column=5, pady=1)

# the 'sin' Button
btnSin = Button(calc, text="sin", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.sin).grid(row=1, column=7, pady=1)

# the 'Cosec' Button
btnCosec = Button(calc, text="cosec", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="aquamarine", command=added_value.cosec).grid(row=2, column=7, pady=1)

# the 'Tan' Button
btnTan = Button(calc, text="tan", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.tan).grid(row=1, column=6, pady=1)

# the 'Cot' Button
btnCot = Button(calc, text="cot", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.cot).grid(row=2, column=6, pady=1)

# Basic Logarithmic functions

# the 'Log' Button
btnLog = Button(calc, text="log", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.log).grid(row=3, column=4, pady=1)

# the 'Exp' Button
btnExp = Button(calc, text="Exp", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.exp).grid(row=3, column=5, pady=1)

# the 'Mod' Button
btnMod = Button(calc, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="aquamarine", command=lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)

# the 'e' Button
btnE = Button(calc, text="e", width=6, height=2, font=('arial', 20, 'bold'),
              bd=4, bg="aquamarine", command=added_value.e).grid(row=3, column=7, pady=1)

# the 'Log2' Button
btnLog2 = Button(calc, text="log2", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="aquamarine", command=added_value.log2).grid(row=4, column=4, pady=1)

# the 'deg' Button
btnDeg = Button(calc, text="deg", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="aquamarine", command=added_value.deg).grid(row=4, column=5, pady=1)

# the 'cosh' Button
btncosh = Button(calc, text="cosh", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="aquamarine", command=added_value.cosh).grid(row=4, column=6, pady=1)

# the 'sinh' Button
btnsinh = Button(calc, text="sinh", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="aquamarine", command=added_value.sinh).grid(row=4, column=7, pady=1)

# the 'Log10' Button
btnLog10 = Button(calc, text="log10", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="aquamarine", command=added_value.log10).grid(row=5, column=4, pady=1)

# the 'Log1p' Button
btnLog1p = Button(calc, text="log1p", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="aquamarine", command=added_value.log1p).grid(row=5, column=5, pady=1)

# the 'Expm1' Button
btnExpml = Button(calc, text="expm1", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="aquamarine", command=added_value.expml).grid(row=5, column=6, pady=1)

# the 'lgamma' Button
btnlgamma = Button(calc, text="lgamma", width=6, height=2, font=('arial', 20, 'bold'),
                   bd=4, bg="aquamarine", command=added_value.lgamma).grid(row=5, column=7, pady=1)


# ----------Menu----------


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Mode", menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)

root.config(menu=menubar)
root.mainloop()
