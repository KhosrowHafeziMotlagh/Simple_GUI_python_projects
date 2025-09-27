"""
simple GUI TrafficLight
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training : function tkinter GUI (place ,bind )
"""

from tkinter import *
import time

color = ["red", "yellow", "lime"]                                                           #تعریف لیستی از رنگ ها


def change_light(main_form, color,x0,y0,x1,y1):
    # تابع تغییر رنگ و روشن شدن دایره ها

    main_form.update()                                                                    #به روز رسانی فرم برای نشان دادن تغییرات
    conv.create_oval(x0,y0,x1,y1, fill=color)                                             # رسم دایره و پرکردن آن با رنگ دریافتی
    main_form.update()                                                                    #به روز رسانی فرم برای نشان دادن تغییرات
    time.sleep(0.5)                                                                       # ایجاد تاخیر برای دیدن تغییرات
    conv.create_oval(x0, y0, x1, y1, fill="black")                                        # مشکی کردن دایره (خاموش کردن چراغ)



main_form = Tk()                                                                            # ساخت فرم اصلی
main_form.title("simple GUI TrafficLight by Khosrow Hafezi Motlagh")                        # تنظیم تایتل برای فرم
main_form.geometry("440x305")                                                               #تنظیم سایز فرم
conv = Canvas(main_form, bg="black", width=120, height=300)                                 # تعریف و تنظیم رنگ و تنظیم ابعاد بوم نقاشی
conv.grid(row=0, column=0)                                                                  # تنظیم جانمایی بوم نقاشی


while True:                                                                                 #ایجاد یک حلقه بی پایان
    color_index = 0                                                                         # انتخاب اندیس صفر برای شروع
    change_light(main_form, color[color_index],15, 10, 110,100)            # فرستادن رنگ و جایگاه ترسیم دایره به تابع
    color_index += 1                                                                        # اضافه کردن ایندکس برای انخاب رنگ بعدی
    change_light(main_form, color[color_index], 15, 110, 110, 200)         # فرستادن رنگ و جایگاه ترسیم دایره به تابع
    color_index += 1                                                                        # اضافه کردن ایندکس برای انخاب رنگ بعدی
    change_light(main_form, color[color_index], 15, 210, 110, 300)         # فرستادن رنگ و جایگاه ترسیم دایره به تابع


main_form.mainloop()
