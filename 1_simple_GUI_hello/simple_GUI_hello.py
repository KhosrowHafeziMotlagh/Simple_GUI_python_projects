"""
simple_GUI_hello
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training : function,lambda, tkinter GUI (Entry,Label,StringVar)
"""

from tkinter import *

def func(inp1,inp2):
    # تابعی که فشردن دکه اجرا میشه

    temp = inp1.get()                                                           # هر چی داخا متغیر inp1 هست بریز داخا temp
    inp2.set("Hello "+temp)                                                     # به temp واژه Hello  رو بچسبون و بریز تو inp2
                                                                                #  هر چی که داخل inp2  ریته بشه توی اینتری2  نمایش داده میشه



main_form = Tk()                                                       # ساخت فرم اصلی که اجزا رو آن قرار می گیرد
main_form.config(bg = "dark gray")                                              #رنگ پس زمینه فرم اصلی رو خاکستری تیره کن

inp1 = StringVar()                                                              #تعریف  یک متغیر مخصوص برای دریافت و ست کردن خودکار ورودی های اینتری اول
inp2 = StringVar()                                                              #تعریف  یک متغیر مخصوص برای دریافتو ست کردن خودکار ورودی های اینتری دوم


# label = Label(main_form,text="Insert your name:",bg="#ff0000",fg="yellow")        # میشه تو بک خط هم چیز رو مقدار دهی کرد یا دونه دونه
label = Label(main_form)                                                        # بک لیبل روی فرم اصلی بساز
label.config(text="Insert your name:")                                          # متن روی لیبل رو برابر یا "Insert your name:"  قرار بده
label.config(bg="#ff0000")                                                      # رنگ پس زمینه لیبل رو برابر با کد رنگیff0000 کن (میشه قرمز-کدای رنگ ها تو نت هست)
label.config(fg="yellow")                                                       # رنگ متن لیبل رو زیر کن
label.config(height=3)                                                          # ارتفاع لیبل رو برابر با 3 قرار بده
label.grid(row=0, column=0)                                                     # و در آخر (حتما در آخر) لیبل رو در مختصات صفر و صفر نمایش بده


#entry1 = Entry(main_form, bg="white", bd=8,textvariable=inp)
entry1 = Entry(main_form)                                                       # بک اینتری روی فرم اصلی بساز
entry1.config(bg="white")                                                       # رنگ پس زمینه  انتری رو سفید کن
entry1.config(bd=8)                                                             # به اینتری 8 واحد حاشیه بده (برای زیبایی کار)
entry1.config(width=50)                                                         # عرض اینتری رو برابر با 50 قرار بده
entry1.config(textvariable=inp1)                                                #هر چیزی که در انتری وارد شد خودکار در متغیر inp قرار بده
entry1.grid(row=0, column=1)                                                    # و در آخر (حتما در آخر) اینتری رو در مختصات صفر و یک (جلوی لیبل) نمایش بده


#btn = Button(main_form, text="متن روی دکمه", bg="green", fg="white", bd=6,command=lambda : func(inp))
btn = Button(main_form)                                                         #بک دکمه روی فرم اصلی بساز
btn.config(text="Click")                                                        # متن روی دکمه رو برابر یا "Click"  قرار بده
btn.config(bg="green")                                                          # رنگ پس زمینه  دکمه رو سبز کن
btn.config(fg="white")                                                          # رنگ متن  دکمه رو سفید کن
btn.config(bd=6)                                                                # به دکمه 7 واحد حاشیه بده (برای زیبایی کار)
btn.config(command=lambda : func(inp1,inp2))                                    # هر وقت روی دکمه کلیک شده  متغیر inp1 , inp2  رو بفرست به  تابع  func و اجراش کن
btn.grid(row=2,column=0,columnspan=2)                                           #و در آخر (حتما در آخر) دکمه رو در مختصات یک و یک قرار بده به اندازه دوستون (از دو طرف در وسط) نمایش بده


# label = Label(main_form,text="Output:",bg="#ff0000",fg="yellow")        # میشه تو بک خط هم چیز رو مقدار دهی کرد یا دونه دونه
label = Label(main_form)                                                        # بک لیبل روی فرم اصلی بساز
label.config(text="Output:")                                                    # متن روی لیبل رو برابر یا "Output:"  قرار بده
label.config(bg="#ff0000")                                                      # رنگ پس زمینه لیبل رو برابر با کد رنگیff0000 کن (میشه قرمز-کدای رنگ ها تو نت هست)
label.config(fg="yellow")                                                       # رنگ متن لیبل رو زیر کن
label.config(height=3)                                                          # ارتفاع لیبل رو برابر با 3 قرار بده
label.grid(row=3, column=0)                                                     # و در آخر (حتما در آخر) لیبل رو در مختصات صفر و صفر نمایش بده



#entry2 = Entry(main_form, bg="white", bd=8,textvariable=inp)
entry2 = Entry(main_form)                                                       # بک اینتری روی فرم اصلی بساز
entry2.config(bg="white")                                                       # رنگ پس زمینه  انتری رو سفید کن
entry2.config(bd=8)                                                             # به اینتری 8 واحد حاشیه بده (برای زیبایی کار)
entry2.config(width=50)                                                         # عرض اینتری رو برابر با 50 قرار بده
entry2.config(textvariable=inp2)                                                #هر چیزی که در انتری وارد شد خودکار در متغیر inp2 قرار بده
entry2.grid(row=3, column=1)

main_form.mainloop()                                                    # ایجاد یک حلقه برای جلوگیری از بسته شدن برنامه
