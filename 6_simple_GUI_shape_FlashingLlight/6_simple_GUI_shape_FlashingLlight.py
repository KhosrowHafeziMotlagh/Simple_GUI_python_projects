"""
simple_GUI_shape_Flashinglight
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training : function tkinter GUI (Canvas ,create_oval)
"""

from tkinter import *
import time


def flashing_light(main_form, color, x0, y0, x1, y1):
    #تابع چراغ چشمک زن
    conv.create_oval(x0, y0, x1, y1, fill=color)                                    # ساخت یک شکل دایره ای روی بوم و رنگ کردن داخل آن
    main_form.update()                                                              # اپدیت کردن فرم برای نسان دادن تغییرات
    time.sleep(0.5)                                                                 # نیم ثانیه تاخیر
    conv.create_oval(x0, y0, x1, y1, fill="black")                                  # تغییر رنگ شکل
    main_form.update()                                                              # اپدیت کردن فرم برای نسان دادن تغییرات
    time.sleep(0.5)                                                                 # نیم ثانیه تاخیر


main_form = Tk()                                                                    # # ساخت فرم اصلی
main_form.title("simple GUI shape Flashinglight by Khosrow Hafezi Motlagh")         # تنظیم تایتل برای فرم
conv = Canvas(main_form, bg="black", width=120, height=110)                         # ساخت یک بوم برای طراحی
conv.grid(row=0, column=0)                                                          # تنظیم جانمایی بوم
while True:                                                                         # ایجاد یک حلقه بینهایت
    flashing_light(main_form, "red", 15, 10, 110, 100)         # ارسال بی نهایت بار رنگ و مختصات مکانی به تابع چشمک زن

main_form.mainloop()
