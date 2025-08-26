"""
simple_GUI_APR_(Annual_Percentage_Rate)
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training for : functions , lambda, round ,tkinter GUI(sticky ,Separator,state)
"""


"""
formula explnation
A=P(1+r/n)(nt)
A: ارزش نهایی سرمایه‌گذاری یا سود نهایی به‌دست‌آمده
P: مبلغ اولیه سرمایه‌گذاری
r: نرخ سود (میزان سودی که در هر معامله انتظار داریم)
n: تعداد دفعات سود مرکب (تعداد دفعاتی که با این سود در یک بازه زمانی کسب درآمد می‌کنیم)
t: مدت‌زمان مورد نظر برای سرمایه‌گذاری
"""

from tkinter import *                                                           #ایمپورت کتبخانه گرافیکی tkinter
from tkinter import ttk                                                         #ایمپورت یک فایل از tkinter که به ما اجازه ساخت message box  رو میده

label_width = 18                                                                # تعریف یک متغیر برای طول لیبل ها
border = 5                                                                      # تعریف یک متغیر برای حاشیه های عناصر
font_size = 15                                                                  #تعریف یک متغیر برای انداره فونت ها

def calculate():
    #تابع محسبه سود مرکب

    p = float(original_investment_inp.get())                                    # دریافت مقدار اولیه سرمایه
    r = float(profit_percent_inp.get()) / 100                                   #دریافت مقدار درصد سود
    n = 1                                                                       # تعداد دفعات سود در بازه (برای بانک های عموما یکه)
    t = float(year_of_investment_inp.get())                                     #دریافت مقدار زمان سرمایه گذاری (به سال)
    a = round(float(p * (1 + (r / n)) ** (n * t)))                              # محاسبه سود
    profit_inp.set(a - p)                                                       # نمایش سود
    total_proprty_inp.set(a)                                                    # نمایش کل دارایی


main_form = Tk()                                                                # ساخت فرم اصلی
main_form.config(bg='silver')                                                   # تغییر رنک پس زیمنه به نقره ای
main_form.title("simple_GUI_APR by Khosrow Hafezi Motlagh")                     # تنظیم تایتل برای فرم

original_investment_inp = StringVar()                                           # تعریف متغیر برای دریافت سرمایه اولیه
profit_percent_inp = StringVar()                                                #تعریف متغیر برای دریافت درصد سود
year_of_investment_inp = StringVar()                                            #تعریف متغیر برای دریافت تعداد سال سرمایه گذاری
profit_inp = StringVar()                                                        #تعریف متغیر برای نمایش میزان سود
total_proprty_inp = StringVar()                                                 #تعریف متغیر برای نمایش کل دارایی

original_investment_label = Label(main_form, text='Original investment:',
                                  width=label_width,font = ("arial",font_size)).grid(row=0, column=0)
original_investment_entry = Entry(main_form, bd=border, textvariable=original_investment_inp,font = ("arial",font_size)).grid(row=0, column=1)

year_label = Label(main_form, text='Year of investment:', width=label_width,font = ("arial",font_size)).grid(row=1,
                                                                       column=0)
year_of_investment_entry = Entry(main_form, bd=border, textvariable=year_of_investment_inp,font = ("arial",font_size)).grid(row=1, column=1)

profit_percent_label = Label(main_form, text='Profit percent:', width=label_width,font = ("arial",font_size)).grid(row=2,
                                                                             column=0)
profit_percent_entry = Entry(main_form, bd=border, textvariable=profit_percent_inp,font = ("arial",font_size)).grid(row=2, column=1)

profit_label = Label(main_form, text='Profit:', width=label_width,font = ("arial",font_size)).grid(row=3, column=0)
profit_entry = Entry(main_form, bd=border, textvariable=profit_inp,font = ("arial",font_size),bg="yellow",state="disabled").grid(row=3, column=1)

total_property_label = Label(main_form, text='Total income:', width=label_width,font = ("arial",font_size)).grid(
    row=4, column=0)
total_proprty_entry = Entry(main_form, bd=border, textvariable=total_proprty_inp,font = ("arial",font_size),bg="yellow",state="disabled").grid(row=4, column=1)

separator = ttk.Separator(main_form, orient=HORIZONTAL).grid(row=5, column=0, columnspan=2, sticky=EW )

caculate_btn = Button(main_form, text='Calculate', bd=border, command=lambda: calculate(),bg="lime",font=("",font_size)).grid(row=6, column=0, columnspan=2)

main_form.mainloop()
