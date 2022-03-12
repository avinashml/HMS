from tkinter import *
from tkinter import filedialog,messagebox

import random

import time
#functions

def reset():
    textReceipt.delete(1.0,END)


def send():
    def send_msg():
        message=textarea.get(1.2,END)
        number=numberfield.get()

    root2=Toplevel()

    root2.title("SEND BILL")
    root2.config(bg='red4')
    root2.geometry('485x620+50+50')

    numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
    numberLabel.pack(pady=5)

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)

    billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    billLabel.pack(pady=5)

    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=62,height=20)
    textarea.pack(pady=5)
    textarea.insert(END,'Receipt RefL\t\t'+billnumber+'\t\t'+date+'\n')


    if costoffoodvar.get()!='0 Rs':
        textarea.insert(END,f'Cost of Food\t\t\t{priceofFood}Rs\n')
    if costofdrinksvar.get() != '0 Rs':
        textarea.insert(END,f'Cost of Drinks\t\t\t{priceofDrinks}Rs\n')
    if costofcakesvar.get() != '0 Rs':
        textarea.insert(END,f'Cost of Cakes\t\t\t{priceofCakes}Rs\n')
    textarea.insert(END,f'Sub Total\t\t\t{subtotalofitems}Rs\n')
    textarea.insert(END,f'Service Tax\t\t\t{50}Rs\n')
    textarea.insert(END,f'Total Cost\t\t\t{subtotalofitems+50}Rs\n')

    sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_message)
    sendButton.pack(pady=5)









    root2.mainloop()

def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')

    bill_data=textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your bill is succesfully saved ')


def receipt():
    global billnumber,date
    textReceipt.delete(1.0,END)
    x=random.randint(100,1500)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t'+date+'\n')
    textReceipt.insert(END,'**************************************************************\n')
    textReceipt.insert(END,'Items:\t\t Cost of items(Rs)\n')
    textReceipt.insert(END, '**************************************************************\n')
    if e_roti.get()!='0':
        textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*15}\n\n')

    if e_daal.get()!='0':
        textReceipt.insert(END,f'daal\t\t\t{int(e_daal.get())*100}\n\n')

    if e_paneer.get()!='0':
        textReceipt.insert(END,f'paneer\t\t\t{int(e_paneer.get())*150}\n\n')

    if e_chicken.get()!='0':
        textReceipt.insert(END,f'chicken\t\t\t{int(e_chicken.get())*250}\n\n')

    if e_fish.get()!='0':
        textReceipt.insert(END,f'fish\t\t\t{int(e_fish.get())*275}\n\n')

    if e_biryani.get()!='0':
        textReceipt.insert(END,f'biryani\t\t\t{int(e_biryani.get())*250}\n\n')

    if e_noodles.get()!='0':
        textReceipt.insert(END,f'noodles\t\t\t{int(e_noodles.get())*150}\n\n')

    if e_kabab.get()!='0':
        textReceipt.insert(END,f'kabab\t\t\t{int(e_kabab.get())*200}\n\n')

    if e_manchurian.get()!='0':
        textReceipt.insert(END,f'manchurian\t\t\t{int(e_manchurian.get())*150}\n\n')

    if e_lassi.get()!='0':
        textReceipt.insert(END,f'lassi\t\t\t{int(e_lassi.get())*50}\n\n')

    if e_coffee.get()!='0':
        textReceipt.insert(END,f'coffee\t\t\t{int(e_coffee.get())*35}\n\n')

    if e_buttermilk.get()!='0':
        textReceipt.insert(END,f'buttermilk\t\t\t{int(e_buttermilk.get())*25}\n\n')

    if e_milkshake.get()!='0':
        textReceipt.insert(END,f'milkshake\t\t\t{int(e_milkshake.get())*40}\n\n')

    if e_roohafza.get()!='0':
        textReceipt.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*40}\n\n')

    if e_coldcoffee.get()!='0':
        textReceipt.insert(END,f'coldcoffee\t\t\t{int(e_coldcoffee.get())*45}\n\n')

    if e_fanta.get()!='0':
        textReceipt.insert(END,f'fanta\t\t\t{int(e_fanta.get())*25}\n\n')

    if e_thumsup.get()!='0':
        textReceipt.insert(END,f'thumsup\t\t\t{int(e_thumsup.get())*25}\n\n')

    if e_mangojuice.get()!='0':
        textReceipt.insert(END,f'mangojuice\t\t\t{int(e_mangojuice.get())*45}\n\n')

    if e_chocolate.get()!='0':
        textReceipt.insert(END,f'chocolate\t\t\t{int(e_chocolate.get())*60}\n\n')

    if e_pineapple.get()!='0':
        textReceipt.insert(END,f'pineapple\t\t\t{int(e_pineapple.get())*50}\n\n')

    if e_mango.get()!='0':
        textReceipt.insert(END,f'mango\t\t\t{int(e_mango.get())*55}\n\n')

    if e_redvelvet.get()!='0':
        textReceipt.insert(END,f'Redvelvet\t\t\t{int(e_redvelvet.get())*70}\n\n')

    if e_butterscotch.get()!='0':
        textReceipt.insert(END,f'butterscotch\t\t\t{int(e_butterscotch.get())*60}\n\n')

    if e_blueberry.get()!='0':
        textReceipt.insert(END,f'blueberry\t\t\t{int(e_blueberry.get())*65}\n\n')

    if e_blackcurrent.get()!='0':
        textReceipt.insert(END,f'blackcurrent\t\t\t{int(e_blackcurrent.get())*65}\n\n')

    if e_caramel.get()!='0':
        textReceipt.insert(END,f'caramel\t\t\t{int(e_caramel.get())*75}\n\n')

    textReceipt.insert(END,'**************************************************************\n')
    if costoffoodvar.get()!='0 Rs':
        textReceipt.insert(END,f'Cost of Food\t\t\t{priceofFood}Rs\n\n')
    if costofdrinksvar.get() != '0 Rs':
        textReceipt.insert(END,f'Cost of Drinks\t\t\t{priceofDrinks}Rs\n\n')
    if costofcakesvar.get() != '0 Rs':
        textReceipt.insert(END,f'Cost of Cakes\t\t\t{priceofCakes}Rs\n\n')
    textReceipt.insert(END,f'Sub Total\t\t\t{subtotalofitems}Rs\n\n')
    textReceipt.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
    textReceipt.insert(END,f'Total Cost\t\t\t{subtotalofitems+50}Rs\n\n')
    textReceipt.insert(END,'**************************************************************\n')

def totalcost():

    global priceofFood,priceofDrinks,priceofCakes,subtotalofitems

    item1=int(e_roti.get())
    item2=int(e_daal.get())
    item3=int(e_paneer.get())
    item4=int(e_chicken.get())
    item5=int(e_fish.get())
    item6=int(e_biryani.get())
    item7=int(e_noodles.get())
    item8=int(e_kabab.get())
    item9=int(e_manchurian.get())


    item10=int(e_lassi.get())
    item11=int(e_coffee.get())
    item12=int(e_buttermilk.get())
    item13=int(e_milkshake.get())
    item14=int(e_roohafza.get())
    item15=int(e_coldcoffee.get())
    item16=int(e_fanta.get())
    item17=int(e_thumsup.get())
    item18=int(e_mangojuice.get())


    item19=int(e_chocolate.get())
    item20=int(e_pineapple.get())
    item21=int(e_strawberry.get())
    item22=int(e_mango.get())
    item23=int(e_redvelvet.get())
    item24=int(e_butterscotch.get())
    item25=int(e_blueberry.get())
    item26=int(e_blackcurrent.get())
    item27=int(e_caramel.get())

    priceofFood=(item1*15)+(item2*100)+(item3*150)+(item4*250)+(item5*275)+(item6*250)+(item7*150)+(item8*200)+(item9*150)
    priceofDrinks=(item10*50)+(item11*35)+(item12*25)+(item13*40)+(item14*40)+(item15*45)+(item16*25)+(item17*25)+(item18*45)
    priceofCakes=(item19*60)+(item20*50)+(item21*55)+(item22*45)+(item23*70)+(item24*60)+(item25*65)+(item26*65)+(item27*75)

    costoffoodvar.set(str(priceofFood)+'Rs')
    costofdrinksvar.set(str(priceofDrinks)+'Rs')
    costofcakesvar.set(str(priceofCakes)+'Rs')

    subtotalofitems=priceofFood+priceofDrinks+priceofCakes
    subtotalvar.set(str(subtotalofitems)+'Rs')

    servicetaxvar.set('50 Rs')

    totalcost=subtotalofitems+50
    totalcostvar.set(str(totalcost)+'Rs')




def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def paneer():
    if var3.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def chicken():
    if var4.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        textchicken.set('0')

def fish():
    if var5.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def biryani():
    if var6.get()==1:
        textbiryani.config(state=NORMAL)
        textbiryani.delete(0,END)
        textbiryani.focus()
    else:
        textbiryani.config(state=DISABLED)
        e_biryani.set('0')

def noodles():
    if var7.get()==1:
        textnoodles.config(state=NORMAL)
        textnoodles.delete(0,END)
        textnoodles.focus()
    else:
        textnoodles.config(state=DISABLED)
        e_noodles.set('0')

def kabab():
    if var8.get()==1:
        textkabab.config(state=NORMAL)
        textkabab.delete(0,END)
        textkabab.focus()
    else:
        textkabab.config(state=DISABLED)
        e_kabab.set('0')

def manchurian():
    if var9.get()==1:
        textmanchurian.config(state=NORMAL)
        textmanchurian.delete(0,END)
        textmanchurian.focus()
    else:
        textmanchurian.config(state=DISABLED)
        e_manchurian.set('0')

def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def buttermilk():
    if var12.get()==1:
        textbuttermilk.config(state=NORMAL)
        textbuttermilk.delete(0,END)
        textbuttermilk.focus()
    else:
        textbuttermilk.config(state=DISABLED)
        e_buttermilk.set('0')

def milkshake():
    if var13.get()==1:
        textmilkshake.config(state=NORMAL)
        textmilkshake.delete(0,END)
        textmilkshake.focus()
    else:
        textmilkshake.config(state=DISABLED)
        e_milkshake.set('0')

def roohafza():
    if var14.get()==1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()
    else:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')

def coldcoffee():
    if var15.get()==1:
        textcoldcoffee.config(state=NORMAL)
        textcoldcoffee.delete(0,END)
        textcoldcoffee.focus()
    else:
        textcoldcoffee.config(state=DISABLED)
        e_coldcoffee.set('0')

def fanta():
    if var16.get()==1:
        textfanta.config(state=NORMAL)
        textfanta.delete(0,END)
        textfanta.focus()
    else:
        textfanta.config(state=DISABLED)
        e_fanta.set('0')

def thumsup():
    if var17.get()==1:
        textthumsup.config(state=NORMAL)
        textthumsup.delete(0,END)
        textthumsup.focus()
    else:
        textthumsup.config(state=DISABLED)
        e_thumsup.set('0')

def mangojuice():
    if var18.get()==1:
        textmangojuice.config(state=NORMAL)
        textmangojuice.delete(0,END)
        textmangojuice.focus()
    else:
        textmangojuice.config(state=DISABLED)
        e_mangojuice.set('0')

def chocolate():
    if var19.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')

def pineapple():
    if var20.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')

def strawberry():
    if var21.get()==1:
        textstrawberry.config(state=NORMAL)
        textstrawberry.delete(0,END)
        textstrawberry.focus()
    else:
        textstrawberry.config(state=DISABLED)
        e_strawberry.set('0')

def mango():
    if var22.get()==1:
        textmango.config(state=NORMAL)
        textmango.delete(0,END)
        textmango.focus()
    else:
        textmango.config(state=DISABLED)
        e_mango.set('0')

def redvelvet():
    if var23.get()==1:
        textredvelvet.config(state=NORMAL)
        textredvelvet.delete(0,END)
        textredvelvet.focus()
    else:
        textredvelvet.config(state=DISABLED)
        e_redvelvet.set('0')

def butterscotch():
    if var24.get()==1:
        textbutterscotch.config(state=NORMAL)
        textbutterscotch.delete(0,END)
        textbutterscotch.focus()
    else:
        textbutterscotch.config(state=DISABLED)
        e_butterscotch.set('0')

def blueberry():
    if var25.get()==1:
        textblueberry.config(state=NORMAL)
        textblueberry.delete(0,END)
        textblueberry.focus()
    else:
        textblueberry.config(state=DISABLED)
        e_blueberry.set('0')

def blackcurrent():
    if var26.get()==1:
        textblackcurrent.config(state=NORMAL)
        textblackcurrent.delete(0,END)
        textblackcurrent.focus()
    else:
        textblackcurrent.config(state=DISABLED)
        e_blackcurrent.set('0')

def caramel():
    if var27.get()==1:
        textcaramel.config(state=NORMAL)
        textcaramel.delete(0,END)
        textcaramel.focus()
    else:
        textcaramel.config(state=DISABLED)
        e_caramel.set('0')


root=Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('Hotel Management System created by  Gautham Avinash')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Restaurant Management System',font=('Arial',30,'bold'),fg='Yellow',bd=9,bg='red4',width=51)
labelTitle.grid(row=0,column=0)

#framework

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',bg='white')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE)
drinksFrame.pack(side=LEFT)


cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE)
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE)
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE)
receiptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()

#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_paneer=StringVar()
e_chicken=StringVar()
e_fish=StringVar()
e_biryani=StringVar()
e_noodles=StringVar()
e_kabab=StringVar()
e_manchurian=StringVar()
e_lassi=StringVar()
e_coffee=StringVar()
e_buttermilk=StringVar()
e_milkshake=StringVar()
e_roohafza=StringVar()
e_coldcoffee=StringVar()
e_fanta=StringVar()
e_thumsup=StringVar()
e_mangojuice=StringVar()
e_chocolate=StringVar()
e_pineapple=StringVar()
e_strawberry=StringVar()
e_mango=StringVar()
e_redvelvet=StringVar()
e_butterscotch=StringVar()
e_blueberry=StringVar()
e_blackcurrent=StringVar()
e_caramel=StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_roti.set('0')
e_daal.set('0')
e_paneer.set('0')
e_chicken.set('0')
e_fish.set('0')
e_biryani.set('0')
e_noodles.set('0')
e_kabab.set('0')
e_manchurian.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_buttermilk.set('0')
e_milkshake.set('0')
e_roohafza.set('0')
e_coldcoffee.set('0')
e_fanta.set('0')
e_thumsup.set('0')
e_mangojuice.set('0')

e_chocolate.set('0')
e_pineapple.set('0')
e_strawberry.set('0')
e_mango.set('0')
e_redvelvet.set('0')
e_butterscotch.set('0')
e_blueberry.set('0')
e_blackcurrent.set('0')
e_caramel.set('0')


#Foodmenu

roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var3,command=paneer)
paneer.grid(row=2,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var4,command=chicken)
chicken.grid(row=3,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var5,command=fish)
fish.grid(row=4,column=0,sticky=W)

biryani=Checkbutton(foodFrame,text='Biryani',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var6,command=biryani)
biryani.grid(row=5,column=0,sticky=W)

noodles=Checkbutton(foodFrame,text='Noodles',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var7,command=noodles)
noodles.grid(row=6,column=0,sticky=W)

kabab=Checkbutton(foodFrame,text='Kabab',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var8,command=kabab)
kabab.grid(row=7,column=0,sticky=W)

manchurian=Checkbutton(foodFrame,text='Manchurian',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var9,command=manchurian)
manchurian.grid(row=8,column=0,sticky=W)

#Entry fields for food items

textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textpaneer=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=2,column=1)

textchicken=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=3,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=4,column=1)

textbiryani=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_biryani)
textbiryani.grid(row=5,column=1)

textnoodles=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_noodles)
textnoodles.grid(row=6,column=1)

textkabab=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kabab)
textkabab.grid(row=7,column=1)

textmanchurian=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_manchurian)
textmanchurian.grid(row=8,column=1)

#Drinks

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

buttermilk=Checkbutton(drinksFrame,text='ButterMilk',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var12,command=buttermilk)
buttermilk.grid(row=2,column=0,sticky=W)

milkshake=Checkbutton(drinksFrame,text='Milkshake',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var13,command=milkshake)
milkshake.grid(row=3,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var14,command=roohafza)
roohafza.grid(row=4,column=0,sticky=W)

coldcoffee=Checkbutton(drinksFrame,text='Coldcoffee',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var15,command=coldcoffee)
coldcoffee.grid(row=5,column=0,sticky=W)

fanta=Checkbutton(drinksFrame,text='Fanta',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var16,command=fanta)
fanta.grid(row=6,column=0,sticky=W)

thumsup=Checkbutton(drinksFrame,text='Thumsup',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var17,command=thumsup)
thumsup.grid(row=7,column=0,sticky=W)

mangojuice=Checkbutton(drinksFrame,text='Mangojuice',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var18,command=mangojuice)
mangojuice.grid(row=8,column=0,sticky=W)

#Enrty fields for drinks

textlassi=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textbuttermilk=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_buttermilk)
textbuttermilk.grid(row=2,column=1)

textmilkshake=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_milkshake)
textmilkshake.grid(row=3,column=1)

textroohafza=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=4,column=1)

textcoldcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coldcoffee)
textcoldcoffee.grid(row=5,column=1)

textfanta=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fanta)
textfanta.grid(row=6,column=1)

textthumsup=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textthumsup.grid(row=7,column=1)

textmangojuice=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mangojuice)
textmangojuice.grid(row=8,column=1)

#Cakes menu

chocolate=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var19,command=chocolate)
chocolate.grid(row=0,column=0,sticky=W)

pineapple=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var20,command=pineapple)
pineapple.grid(row=1,column=0,sticky=W)

strawberry=Checkbutton(cakesFrame,text='Strawberry',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var21,command=strawberry)
strawberry.grid(row=2,column=0,sticky=W)

mango=Checkbutton(cakesFrame,text='Mango',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var22,command=mango)
mango.grid(row=3,column=0,sticky=W)

redvelvet=Checkbutton(cakesFrame,text='Redvelvet',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var23,command=redvelvet)
redvelvet.grid(row=4,column=0,sticky=W)

butterscotch=Checkbutton(cakesFrame,text='Butterscotch',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var24,command=butterscotch)
butterscotch.grid(row=5,column=0,sticky=W)

blueberry=Checkbutton(cakesFrame,text='Blueberry',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var25,command=blueberry)
blueberry.grid(row=6,column=0,sticky=W)

blackcurrent=Checkbutton(cakesFrame,text='Blackcurrent',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var26,command=blackcurrent)
blackcurrent.grid(row=7,column=0,sticky=W)

caramel=Checkbutton(cakesFrame,text='Caramel',font=('arial',18,'bold'),onvalue=0,offvalue=1,variable=var27,command=caramel)
caramel.grid(row=8,column=0,sticky=W)

#Entry list for cakes

textchocolate=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=0,column=1)

textpineapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=1,column=1)

textstrawberry=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_strawberry)
textstrawberry.grid(row=2,column=1)

textmango=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mango)
textmango.grid(row=3,column=1)

textredvelvet=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_redvelvet)
textredvelvet.grid(row=4,column=1)

textbutterscotch=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_butterscotch)
textbutterscotch.grid(row=5,column=1)

textblueberry=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blueberry)
textblueberry.grid(row=6,column=1)

textblackcurrent=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blackcurrent)
textblackcurrent.grid(row=7,column=1)

textcaramel=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_caramel)
textcaramel.grid(row=8,column=1)

#Costlabels and entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubtotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubtotal.grid(row=0,column=2)

textSubtotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubtotal.grid(row=0,column=3,padx=41)

labelServicetax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelServicetax.grid(row=1,column=2)

textServicetax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServicetax.grid(row=1,column=3,padx=41)

labelTotalcost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalcost.grid(row=2,column=2)

textTotalcost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalcost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=1,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=1,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=1,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=1,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=1,command=reset)
buttonReset.grid(row=0,column=4)

#text area for receipt

textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator


operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=30,bd=2)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)




root.mainloop()
