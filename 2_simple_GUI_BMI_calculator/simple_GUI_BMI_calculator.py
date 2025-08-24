"""
simple GUI BMI calculator
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training for : tkinter GUI , functions , lambda
"""


from tkinter import *

font_size = 15
def calculate(weight_inp, heghit_inp):
    bmi = float(weight_inp.get()) / (float(heghit_inp.get()) ** 2)
    result_label.config(text="BMI : " + str(bmi))


main_form = Tk()
weight_inp = StringVar()
heghit_inp = StringVar()

main_form.title("simple GUI BMI calculator by Khosrow Hafezi Motlagh")
main_form.config(bg="silver")

weight_label = Label(text="Weight (kg):", font=("arial", font_size), width=11).grid(row=0, column=0)
weight_entry = Entry(textvariable=weight_inp, bd=6, font=("arial", font_size),width=30).grid(row=0, column=1)

heghit_label = Label(text="Height (m):", font=("arial", font_size), width=11).grid(row=1, column=0)
heghit_entry = Entry(textvariable=heghit_inp, bd=6, font=("arial", font_size),width=30).grid(row=1, column=1)

result_label = Label(text="Bmi : ", bg="yellow", font=("arial", font_size))

calculate_btn = Button(text="Calculate:", font=("arial", font_size),
                       command=lambda: calculate(weight_inp, heghit_inp),bg="green",fg = "white", bd=6).grid(row=3, column=0, columnspan=2)

result_label.grid(row=2, column=0, columnspan=2)

main_form.mainloop()
