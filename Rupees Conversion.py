from tkinter import *
from forex_python.converter import CurrencyRates
c = CurrencyRates()

def Rupees_conversion():
    calc.geometry("619x190")
    Result=Label(calc, text="Result (    in Rupees    )",font=("Arial",18),bg="light green").grid(row=1, column=0, sticky=W)
    arrow=Label(calc, text="  →  ",font=("Arial",20),bg="light green").grid(row=1,column=1)
    result_display=Entry(calc, width=10, font=("Arial",18),bg="light yellow")
    result_display.grid(row=1,column=2)
    result_display.delete(0, "end")
    entered_value= float(dollar_input.get())
    entered_value = entered_value * (c.get_rate('USD', 'INR'))
    result= '{0:.5g}'.format(entered_value)
    result_display.insert(END, result)

def Swissfranc_conversion():
    calc.geometry("619x190")
    Result=Label(calc, text="Result ( in SwissFranc )",font=("Arial",18),bg="light green").grid(row=1, column=0, sticky=W)
    arrow=Label(calc, text="  →  ",font=("Arial",20),bg="light green").grid(row=1,column=1)
    result_display=Entry(calc, width=10, font=("Arial",18),bg="light yellow")
    result_display.grid(row=1,column=2)
    result_display.delete(0, "end")
    entered_value= float(dollar_input.get())
    entered_value = entered_value * (c.get_rate('USD', 'CHF'))
    result= '{0:.5g}'.format(entered_value)
    result_display.insert(END, result)

def Lira_conversion():
    calc.geometry("619x190")
    Result=Label(calc, text="Result (       in Lira       )",font=("Arial",18),bg="light green").grid(row=1, column=0, sticky=W)
    arrow=Label(calc, text="  →  ",font=("Arial",20),bg="light green").grid(row=1,column=1)
    result_display=Entry(calc, width=10, font=("Arial",18),bg="light yellow")
    result_display.grid(row=1,column=2)
    result_display.delete(0, "end")
    entered_value= float(dollar_input.get())
    entered_value = entered_value * (c.get_rate('USD', 'TRY'))
    result= '{0:.5g}'.format(entered_value)
    result_display.insert(END, result)

def Dirham_conversion():
    calc.geometry("619x190")
    Result=Label(calc, text="Result (    in Dirham     )",font=("Arial",18),bg="light green").grid(row=1, column=0, sticky=W)
    arrow=Label(calc, text="  →  ",font=("Arial",20),bg="light green").grid(row=1,column=1)
    result_display=Entry(calc, width=10, font=("Arial",18),bg="light yellow")
    result_display.grid(row=1,column=2)
    result_display.delete(0, "end")
    entered_value= float(dollar_input.get())
    result= '{0:.5g}'.format(entered_value*3.67)
    result_display.insert(END, result)


calc=Tk()
calc.title('CURRENCY CALCULATOR')
calc['bg']='light green'
calc.geometry("619x157")


Dollar=Label(calc, text="Enter the amount in Dollars",font=("Arial",18),bg="light green").grid(row=0, column=0,sticky=W)
arrow=Label(calc, text="  →  ",font=("Arial",20),bg="light green").grid(row=0,column=1)
dollar_input=Entry(calc, width=10, font=("Arial",18),bg="light yellow")
dollar_input.insert(END,str(0))
dollar_input.grid(row=0, column=2)


mid=Label(calc, text="=============================",font=("Arial",18),bg="light green").grid(row=4)


Ruppes=Button(calc,width=12,text="RUPEES",command=Rupees_conversion,font=("Arial",15),bg="orange").grid(row=5, column=0, sticky=W)

Swissfranc=Button(calc,width=12,text="SWISSFRANC",command=Swissfranc_conversion,font=("Arial",15),bg="orange").grid(row=5, column=0, sticky=E)

Lira=Button(calc,text="LIRA",width=12,command=Lira_conversion,font=("Arial",15),bg="orange").grid(row=6, column=0, sticky=W)

Dirham=Button(calc,width=12,text="DIRHAM",command=Dirham_conversion,font=("Arial",15),bg="orange").grid(row=6, column=0, sticky=E)
