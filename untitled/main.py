# coding=utf-8
from tkinter import *

from lagrange import Lagrange

func = "f(x,y,z) = x^2 + y^2 + z^2"
coefficients = "Ax + By + Cz + D = 0"


def sign(value):
    if value > 0:
        return "+ "
    else:
        return ""


def sign2(value):
    if value > 0:
        return "+ "
    else:
        return ""


def calculate(self):
    textbox.insert('1.0', "Starting.. \n")

    A = int(firstCoeff.get("1.0", END))
    B = int(secondCoeff.get("1.0", END))
    C = int(thirdCoeff.get("1.0", END))
    D = int(fourthCoeff.get("1.0", END))

    textbox.insert(END, 'Составим функцию Лагранжа: \n')
    textbox.insert(END, "F(x,y,z,lambda)= x^2 + y^2 + z^2 - lambda*(" + str(A) + "x " + sign(B) + str(B) + "y " + sign(
        C) + str(C) + "z " + sign(D) + str(D) + ")\n")

    textbox.insert(END, "dF/dx = 2x - lambda*" + str(A) + " = 0\n")
    textbox.insert(END, "dF/dy = 2y - lambda*" + str(B) + " = 0\n")
    textbox.insert(END, "dF/dz = 2z - lambda*" + str(C) + " = 0\n")
    textbox.insert(END, "dF/dlambda = " + sign2(A) + str(A) + "x " + sign2(B) + str(B)
                   + "y " + sign2(C) + str(C) + "z " + sign2(D) + str(D) + " = 0 \n")

    results = Lagrange.solve(A, B, C, D)
    rounded_results = []

    for result in results:
        result = round(result, 3)
        rounded_results.append(result)

    X = rounded_results[0]
    Y = rounded_results[1]
    Z = rounded_results[2]
    Lambda = rounded_results[3]

    textbox.insert(END, str(rounded_results) + "\n")

    textbox.insert(END, "X = " + str(X) + "\n")
    textbox.insert(END, "Y = " + str(Y) + "\n")
    textbox.insert(END, "Z = " + str(Z) + "\n")
    textbox.insert(END, "Lambda = " + str(Lambda) + "\n")


root = Tk()

width = 5
height = 8

panelFrame = Frame(root, height=60, bg='gray')
imageFrame = Frame(root, height=80, width=50, bg='red')
textFrame = Frame(root, height=34, width=60)
image2Frame = Frame(root, height=200)

panelFrame.pack(side='top', fill='both')
image2Frame.pack()
textFrame.pack()

textbox = Text(textFrame, font='Arial 14', wrap='word')

imagebox = PhotoImage()

labelFunction = Label(image2Frame, text=func)
labelFunction.pack()

labelCoefficients = Label(image2Frame, text=coefficients)
labelCoefficients.pack()

canvas = Canvas(image2Frame, height=200)
canvas.pack(side="bottom", fill="both", expand="yes")

firstCoeff = Text(image2Frame, height=1, width=4, wrap='word')
firstCoeff.insert("1.0", 'A')
firstCoeff.pack()

secondCoeff = Text(image2Frame, height=1, width=4, wrap='word')
secondCoeff.insert("1.0", 'B')
secondCoeff.pack()

thirdCoeff = Text(image2Frame, height=1, width=4, wrap='word')
thirdCoeff.insert("1.0", 'C')
thirdCoeff.pack()

fourthCoeff = Text(image2Frame, height=1, width=4, wrap='word')
fourthCoeff.insert("1.0", 'D')
fourthCoeff.pack()

textbox.pack()

startBtn = Button(panelFrame, text='Calculate')
quitBtn = Button(panelFrame, text='Quit')

startBtn.bind("<Button-1>", calculate)
quitBtn.bind("<Button-1>", quit)

quitBtn.place(x=110, y=10, width=100, height=40)
startBtn.place(x=10, y=10, width=100, height=40)

root.mainloop()
