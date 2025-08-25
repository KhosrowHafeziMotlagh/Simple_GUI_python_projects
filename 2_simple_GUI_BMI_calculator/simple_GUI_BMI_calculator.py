"""
simple GUI BMI calculator
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training for : tkinter GUI , functions , lambda
"""

"""
فرمول bmi :
bmi = (ghad / (wazn**2))
"""

from tkinter import *                                                                                                   #وارد کردن کتابخانه گرافیکی tkinter

font_size = 15                                                                                                          #تعریف یه متغیر عمومی برای فونت (از همین جا که تغییر بدیم، هر جا استفتده شده، اعمال میشه)
def calculate(weight_inp, heghit_inp):
    #تابع محسابه BMI
    bmi = float(weight_inp.get()) / (float(heghit_inp.get()) ** 2)                                                      #شاخص توده بدنی قد و وزن گرفته شده رو رو حساب می کنیم
    result_label.config(text="BMI : " + str(bmi))                                                                       #و نتیجه رو در لیبل نمایش میدیم


main_form = Tk()                                                                                                        #ایجاد فرم
weight_inp = StringVar()                                                                                                #تعریف ورودی وزن
heghit_inp = StringVar()                                                                                                #تعریف ورودی قد

main_form.title("simple GUI BMI calculator by Khosrow Hafezi Motlagh")                                                  #نام گذاری فرم(بالا سمت راست فرم)
main_form.config(bg="silver")

weight_label = Label(main_form ,text="Weight (kg):", font=("arial", font_size), width=11).grid(row=0, column=0)                    #ساخت لیبل وزن
weight_entry = Entry(main_form ,textvariable=weight_inp, bd=6, font=("arial", font_size),width=30).grid(row=0, column=1)           #ساخت اینتری وزن

heghit_label = Label(main_form ,text="Height (m):", font=("arial", font_size), width=11).grid(row=1, column=0)                     #ساخت لیبل قد
heghit_entry = Entry(main_form ,textvariable=heghit_inp, bd=6, font=("arial", font_size),width=30).grid(row=1, column=1)           #ساخت اینتری قد

result_label = Label(main_form ,text="Bmi : ", bg="yellow", font=("arial", font_size))                                             #ساخت لیبل نتیجه

calculate_btn = Button(main_form ,text="Calculate:", font=("arial", font_size),command=lambda: calculate(weight_inp, heghit_inp),bg="green",fg = "white", bd=6).grid(row=3, column=0, columnspan=2)    #ساخت دکمه محاسه

result_label.grid(row=2, column=0, columnspan=2)                                                                        #جانمایی لیبل نتیجه
                                                                                                                        #جانمایی رو در آخر گذاشتیم چ.ت بعد از اعمل جانمایی نمیشه عناصر رو کانفیگ کرد
main_form.mainloop()
