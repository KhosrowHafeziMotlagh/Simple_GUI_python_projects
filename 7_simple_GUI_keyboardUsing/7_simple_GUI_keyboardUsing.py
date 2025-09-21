"""
simple GUI keyboardUsing
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training : function tkinter GUI (place ,bind )
"""


from tkinter import *

X=250                                                                   # مکان اولیه افقی دکمه
Y=250                                                                   # مکان اولیه عمودی دکمه

def move_up(key):
    # تابع دکمه فلش رو به بالا
    global X,Y                                                          # دریافت مختصات فعلی
    Y=Y-1                                                               # کم کردن مقدار عمودی برای بالا رفتن دکمه
    btn.place(x=X, y=Y)                                                 # ست کردن مختصات جدید

def move_down(key):
    global X, Y
    Y = Y + 1
    btn.place(x=X, y=Y)

def move_left(key):
    global X, Y
    X = X - 1
    btn.place(x=X, y=Y)

def move_right(key):
    global X, Y
    X = X + 1
    btn.place(x=X, y=Y)

main_form = Tk()                                                         # ساخت فرم اصلی
main_form.geometry("500x500")                                            # تنظیم ابعاد فرم
main_form.title("simple GUI keyboardUsing by Khosrow Hafezi Motlagh")    # تنظیم تایتل برای فرم
main_form.config(bg = "black")                                           # تنظیم رنگ پس زمینه فرم به مشکی
btn = Button(main_form,text="Press Arrows...",bd =8)                     # تعریف دکمه

main_form.bind("<Right>",move_right)                                     # پیوند دادن فرم به دکمه فلش راست
main_form.bind("<Left>",move_left)                                       # پیوند دادن فرم به دکمه فلش چپ
main_form.bind("<Up>",move_up)                                           # پیوند دادن فرم به دکمه فلش بالا
main_form.bind("<Down>",move_down)                                       # پیوند دادن فرم به دکمه فلش پایین

btn.place(x=X, y=Y)                                                      # جانمایی اولیه دکمه
main_form.mainloop()
