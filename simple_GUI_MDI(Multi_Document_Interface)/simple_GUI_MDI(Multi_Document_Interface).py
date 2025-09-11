"""
simple_GUI_MDI(Multi_Document_Interface)
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training : function,lambda, tkinter GUI (MDI,Entry,Label,StringVar)
"""

from tkinter import *


def close_second_form(second_form):
    # تابع بستن فرم دوم
    second_form.destroy()                                                            # ستن فرم دوم


def second_form(inp):
    #تابع اجرای فرم دوم

    second_form = Toplevel()                                                         # غیر از فرم اول که از TK سخته میشه، بقهی فرم ها ازToplevel ساخته میشن
    second_form.title("Second form")                                                 # تنظیم تایتل برای فرم دوم
    second_form.config(bg="silver")                                                  # تغییر رنک پس زیمنه به نقره ای
    second_form.geometry("250x170")                                                  #تنظیم ابعاد فرم
    second_form.focus()                                                              # در حالت فعال قرار دادن فرم دوم
    label = Label(second_form, width=20, bd=8)
    label.config(text=inp.get())                                                     # گرفتن مقدار درون اینتری فرم اول و  قرار دادن ان در لیبل فرم دوم
    close_second_form_btn = (Button(second_form,                                     # تعریف یک دکمه برای بستن فرم دوم
                                   text="Click to close Second Form",
                                   bd=8,
                                   command=lambda: close_second_form(second_form))   # صدا زدن تابع بستن فرم دو و ارسال خود فرم به تابع
                                   .grid(row=1, column=0,padx=10, pady=15))
    label.grid(row=0, column=0, padx=50, pady=15)
    second_form.mainloop()


def main():
    # تابع اصلی برنامه

    main_form = Tk()                                                             # ساخت فرم اصلی
    main_form.title("simple GUI MDI by Khosrow Hafezi Motlagh")                  # تنظیم تایتل برای فرم
    main_form.config(bg="white")                                                 # تغییر رنک پس زیمنه به سفید


    inp = StringVar()                                                            # تعریف متغیر برای دریافت متن از فرم اصلی

    input_label = Label(main_form,                                               # تعریف لیبیل
                        text="type something :",                                 # متن لیبل
                        bg="magenta",                                            # رنگ لیبل
                        bd=5,                                                    # مقدار حاشیه لیبل
                        font=("arial",15)).grid(row=0, column=0)                 # فونت لیبل

    input_entry = Entry(main_form,
                        textvariable=inp, width=40,
                        bd=8).grid(row=0, column=1, padx=10, pady=15)

    second_form_btn = (Button(main_form,                                        #تعریف یک دکمه برای یاز شدن فرم دوم
                             text="Click to open Second Form",bd=8,
                             command=lambda: second_form(inp))                  #دستور دکمه رو برابر با صدا زدن تابع فرم دوم قرار میدیم
                             .grid(row=1, column=0,columnspan=2, pady=15))

    main_form.mainloop()


main()                                                                          # صدا زدن فرم اصلی و اجرای برنامه
