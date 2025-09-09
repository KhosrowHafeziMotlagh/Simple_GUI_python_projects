
"""
simple_GUI_unit_converter
Programmer : Khosrow Hafezi Motlagh
github : KhosrowHafeziMotlagh
python Version : 3.11
GUI : tkinter
Training : function,lambda, tkinter GUI (Entry,Label,StringVar)
"""




from tkinter import *                                                   # ایمپورت کتبخانه گرافیکی tkinter
from tkinter import ttk                                                 # ایمپورت یک فایل از tkinter که به ما اجازه ساخت Combobox  رو میده
import decimal                                                          # ایپمپورت کتابخانه دسیمال که به ما قدرت محاسبه اعداد اعشاری با دقت بالا رو میده

label_width = 8                                                         # تعریف یک متغیر برای طول لیبل ها
entry_width = 35                                                        # تعریف یک متغیر برای طول اینتری ها
fontsize = 15                                                           # تعریف یک متغیر برای انداره فونت ها
border = 8                                                              # تعریف یک متغیر برای حاشیه های عناصر

units = ["Metre", "Mile", "Inch"]                                       # تعریف یک لست که قرارا در داخل کمبو باکس ها لود بشه


def convert(entry_inp, entry_out, combobox_inp, combobox_out):
    # تابع تبدیل واحد ها به یکدیگر

    input_value = decimal.Decimal(entry_inp.get())                      # دریافت مقدار واحد اول
    input_unit = combobox_inp.get()                                     # دریافت واحد اول
    output_unit = combobox_out.get()                                    # دریافت واحد دوم

    if input_unit == "Metre":                                           # اگر واحد اول متر بود
        if output_unit == "Metre":                                      #و اگر واحد دوم همر متر بود
            entry_out.set(input_value)                                  # خود مقداری که کاربر وارد کرده رو در انتری دوم نشون بده
        elif output_unit == "Mile":                                     # اگر واحد دوم مایل بود
            result = input_value * decimal.Decimal("0.0006213712")      # مقدار اینتری اول رو در این عدده ضرب کن
            entry_out.set(result)                                       # و در انتری دوم نمایش بده
        elif output_unit == "Inch":                                     # اگر واحد دوم اینچ بود
            result = input_value * decimal.Decimal("39.37007")          # مقدار اینتری اول رو در این عدده ضرب کن
            entry_out.set(result)                                       # و در انتری دوم نمایش بده


    elif input_unit == "Mile":
        if output_unit == "Metre":
            result = input_value * decimal.Decimal("1609.3439")
            entry_out.set(result)
        elif output_unit == "Mile":
            entry_out.set(input_value)
        elif output_unit == "Inch":
            result = input_value * decimal.Decimal("63359.99")                                                   
            entry_out.set(result)


    elif input_unit == "Inch":
        if output_unit == "Metre":
            result = input_value * decimal.Decimal("0.0254")
            entry_out.set(result)
        elif output_unit == "Mile":
            result = input_value /decimal.Decimal( "63360")
            entry_out.set(result)
        elif output_unit == "Inch":
            entry_out.set(input_value)


def main():
    #تابع اصلی برنامه

    main_form = Tk()                                                         # ساخت فرم اصلی
    main_form.config(bg="gray")                                              # تغییر رنک پس زیمنه به نقره ای
    main_form.title("simple_GUI_unit_converter by Khosrow Hafezi Motlagh")   # تنظیم تایتل برای فرم
    entry_inp = StringVar()                                                  # تعریف متغیر برای دریافت مقدار واحد اولیه
    entry_out = StringVar()                                                  #تعریف متغیر برای نمایش مقدار واحد ثانویه
    combobox_inp = StringVar()                                               # تعریف متغیر برای انتخاب واحد اولیه از کمبو باکس اول
    combobox_out = StringVar()                                               # تعریف متغیر برای انتخاب واحد ثانویه از کمبو باکس دوم

    input_label = Label(main_form,                                           # تعریف لیبیل
                        text="Input:",                                       # متن لیبل
                        bg="magenta",                                        # رنگ لیبل
                        width=label_width,                                   # عرض لیبل
                        bd=border,                                           # مقدار حاشیه لیبل
                        font=("arial", fontsize)).grid(row=0, column=0)      #فونت لیبل

    input_entry = Entry(main_form,
                        bg="white",
                        width=entry_width,
                        bd=border,
                        textvariable=entry_inp,
                        font=("arial", fontsize)).grid(row=0, column=1)

    input_combobox = ttk.Combobox(main_form, textvariable=combobox_inp)      # تعریف کمبو باکس اول و اختصاص دادن مقدار StringVar به textvariable برای دریافت گزینه انتخابی

    output_label = Label(main_form,
                         text="Output:",
                         bg="lime",
                         width=label_width,
                         bd=border,
                         font=("arial", fontsize)).grid(row=1, column=0)
    output_entry = Entry(main_form,
                         bg="white",
                         width=entry_width,
                         textvariable=entry_out,
                         bd=border,
                         font=("arial", fontsize)).grid(row=1, column=1)

    output_combobox = ttk.Combobox(main_form, textvariable=combobox_out)    # تعریف کمبو باکس دوم و اختصاص دادن مقدار StringVar به textvariable برای دریافت گزینه انتخابی

    convert_btn = Button(main_form,
                         text="Convert",                                                   #
                         bg="black",                                                   #
                         fg="white",                                                   #
                         width=15,                                                   #
                         bd=border,                                                   #
                         font=("arial", fontsize),                                                   #
                         command=lambda: convert(entry_inp, entry_out, combobox_inp, combobox_out)).grid(row=2, column=0,
                                                                                                         columnspan=3)

    input_combobox["value"] = units                                         # پر کردن کمبو باکس اول با لیستی که ابتدای برنامه تعریف کردیم
    output_combobox["value"] = units                                        # پر کردن کمبو باکس دوم با لیستی که ابتدای برنامه تعریف کردیم

    input_combobox.current(0)                                               # انتخاب اولین گزینه کمبو باکس برای نمایش در بالا
    output_combobox.current(2)                                              # انتخاب سومین گزینه کمبو باکس برای نمایش در بالا

    input_combobox.grid(row=0, column=2)                                    # جانمایی کمبو باکس اول
    output_combobox.grid(row=1, column=2)                                   # جانمایی کمبو باکس دوم

    main_form.mainloop()


main()
