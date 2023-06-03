from tkinter import *
import math

def leftClickButton(event):
    result_BMI = 0
    result_level = ""
    result_BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    #print(result_BMI)
    if result_BMI >= 30:
        result_level = "อ้วนมาก"
    elif result_BMI >= 25 and result_BMI <= 29.9:
        result_level = "อ้วน"
    elif result_BMI >= 23 and result_BMI <= 24.9:
        result_level = "น้ำหนักเกิน"
    elif result_BMI >= 18.6 and result_BMI <= 22.9:
        result_level = "น้ำหนักปกติ เหมาะสม"
    elif result_BMI <=18.5:
        result_level = "ผอมเกินไป"
    labelResult.configure(text=result_level)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()