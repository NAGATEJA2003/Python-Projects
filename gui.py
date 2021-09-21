from tkinter import *
import easygui
from easygui import *
import calendar as ca

def op1():
    q.destroy()
    main()

def op2():
    q.destroy()

def rop1():
    y.destroy()
    root.destroy()
    main()

def rop2():
    y.destroy()
    root.destroy()

def result1():
    r=easygui.msgbox("Do you want to Proceed","Notice","Yes")
    if(r=="Yes"):
        l=int(ce.get())
        if(l>0):
            r=True
            c.destroy()
            if(ca.isleap(l)):
                res="A Leap year"
            else:
                res="Not a Leap year"
        else:
            easygui.msgbox("You have entered invalid input\n\n\n[Hint : Enter values above 1]","Error")

    if(r==True):
        global q
        q=Tk()
        q.title("RESULT")
        q.attributes('-topmost',True)
        Label(q,text='****'+str(l)+'****',font=("Arial",20)).grid(row=0,column=1)
        Label(q,text="is",font=("Arial",20)).grid(row=1,column=1)
        Label(q,text=res,font=("Arial",50)).grid(row=2,column=1)
        Label(q,text="*******************-------*******************").grid(row=3,column=1)
        Button(q,text="Execute again",font=("Arial",20),bg="palegreen",command=op1).grid(row=5,column=0,sticky=W)        
        Button(q,text="Exit",font=("Arial",20),bg="palegreen",command=op2).grid(row=5,column=3,sticky=E)

def result2():
    global y
    global root
    
    s1=int(s.get())
    e1=int(e.get())
    if(s1<=e1):
        pp=easygui.msgbox("Do you want to Proceed","Notice","Yes")
        if(pp=="Yes"):
            root=Tk()
            root.attributes('-topmost',True)
            sizex = 860
            sizey = 700
            posx  = 100
            posy  = 100
            root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

            myframe=Frame(root,relief=GROOVE,width=50, height=100, bd=10)
            myframe.place(x=10,y=10)

            global canvas
            canvas=Canvas(myframe)
            
            d.destroy()
            y=Frame(canvas)
            myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
            canvas.configure(yscrollcommand=myscrollbar.set)
            root.title("RESULT")
            myscrollbar.pack(side="right",fill="y")
            canvas.pack(side="left")
            canvas.create_window((1,1),window=y,anchor='nw')
            y.bind("<Configure>",myfunction)

            count=0
            for i in range(s1,e1):
                if(ca.isleap(i)):
                    count+=1
            if(count==0):
                Label(y,text="There is no Leap years in given range ",font=("Arial",30),foreground="blue").grid()
            else:
                Label(y,text="No of leap years in given range are -------------------------->",font=("Arial",20),foreground="blue").grid(sticky=W)
                Label(y,text=count,font=("Arial",30),foreground="green").grid(row=0,column=1,sticky=W)
                
                j=5
                k=0
                ar=[]
                for i in range(s1,e1):
                    if(ca.isleap(i)):
                        ar.append(i)

                    if(len(ar)==10):
                        Label(y,text=ar,font=("Arial",20)).grid(row=j)
                        ar.clear()
                        j+=1
                Label(y,text=ar,font=("Arial",20)).grid(column=0,row=j,sticky=W)
                Button(y,text="Execute again",font=("Arial",20),bg="palegreen",command=rop1).grid(row=j+2)        
                Button(y,text="Exit",font=("Arial",20),bg="palegreen",command=rop2).grid(row=j+4)
   
    else:
        easygui.msgbox("You have entered in invalid input\n\n\n[Hint : Starting year should be less than Ending year]","Notice")

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=800,height=660)

def cl():
    global c
    c=Tk()
    c.title("OPERATION - 1")
    c.attributes('-topmost',True)
    Label(c,text="Enter the year",font=("Arial",20),foreground="red").grid(row=0,sticky=W)
    global ce
    ce=Entry(c,width=10,font=("Arial",20),bg="cyan")
    ce.grid(row=0,column=1)
    b=Button(c,text="Check",font=("Arial",20),bg="darkviolet",command=result1).grid(row=1,column=1,sticky=S)

def lr():
    global d
    d=Tk()
    d.title("OPERATION - 2")
    d.attributes('-topmost',True)
    Label(d,text="Enter the Starting Year",font=("Arial",20),foreground="red").grid(row=0,column=0,sticky=W)
    Label(d,text="Enter the Ending Year",font=("Arial",20),foreground="red").grid(row=1,column=0,sticky=W)
    global s
    global e
    s=Entry(d,width=10,font=("Arial",20),bg="cyan")
    s.grid(row=0, column=1,sticky=E)
    e=Entry(d,width=10,font=("Arial",20),bg="cyan")
    e.grid(row=1,column=1, sticky=E)
    Button(d,text="Enter",font=("Arial",20),bg="palegreen",command=result2).grid()

#2
def box():
    x1=int(choice.get())
    if(x1==1):
        ans=easygui.msgbox("Are you sure to do operation-1","Notice","Yes")
        if(ans=="Yes"):
            cl()
            a.destroy()
            
    elif(x1==2):
        ans=easygui.msgbox("Are you sure to do operation-2","Notice","Yes")
        if(ans=="Yes"):
            lr()
            a.destroy()
            
    else:
        easygui.msgbox("You have entered in invalid input\n\n\n[Hint : Enter either 1 or 2]","Notice")
        
#1
def main():
    global a
    global choice
    
    a=Tk()
    a.title("MENU")
    a.attributes('-topmost',True)
    Label(a,text="******MENU******",font=("Arial",20),foreground="darkviolet").grid(row=0,column=0)
    Label(a,text="1. Checking whether the year is Leap Year or not",foreground="red",font=("Arial",20)).grid(row=1,sticky=W)
    Label(a,text="2. Print Leap years in given range",foreground="red",font=("Arial",20)).grid(row=2,sticky=W)
    Label(a,text="Enter the choice",foreground="green",font=("Arial",20)).grid(row=3,column=0,sticky=W)

    choice=Entry(a,width=10,font=("Arial",20),bg="yellow")
    choice.grid(row=3,sticky=E)

    b=Button(a,text="Next",command=box,font=("Arial",20),bg="cyan").grid()

main()
