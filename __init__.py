from faulthandler import disable
from tkinter import*
import pygame
from tkinter import ttk
from tkinter.font import BOLD, Font
import webbrowser as web
from tkinter import messagebox


#heading

window=Tk()
window.geometry("1920x1080")
window.title("Swiggy")
window.config(bg="white")
window.iconbitmap("delivery.ico")

pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\Asvatahmed\\AppData\\Local\\Programs\\Microsoft VS Code\\main_project\\2.mp3')
pygame.mixer.music.play()



font_style=Font(family="Proxima Nova",size=26,weight="bold",slant="italic")
lab=Label(window , text = " Welcome to Swiggy",font=font_style,bg="#f4b41a",fg="#143d59",pady=20,width=100)
lab.pack ()

lab2=Label( window , text = "Order and Enjoy the Food",font=font_style,bg="#f4b41a",fg="#143d59",pady=20,width=100)
lab2.pack(side="bottom")

#sign Up
heading=Label(window,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',30,'bold'))
heading.place(x=250,y=100)

name=Entry (window,width= 25, fg = 'black', border = 2 , bg = "white" , font = ('Microsoft YaHei UI Light',30))
name.place (x=80,y=200)
name.insert (0,'Username') 

phone=Entry (window,width= 25, fg = 'black', border = 2 , bg = "white" , font = ('Microsoft YaHei UI Light',30))
phone.place (x=80,y=300)
phone.insert (0,'Phone')

add=Entry (window,width= 25, fg = 'black', border = 2 , bg = "white" , font = ('Microsoft YaHei UI Light',30))
add.place (x=80,y=400)
add.insert (0,'Address') 

state=["Tamil Nadu","Rajasthan","Madhya Pradeshi","Maharashtra","Uttar Pradesh","Gujarat","Karnataka","Andhra Pradesh","Odisha","Chhattisgarh",
        "Telangana","Bihar","West Bengal","Arunachal Pradesh","	Jharkhand","Assam","Ladakh","Himachal Pradeshi","Uttarakhand","Kerala","Delhi"]
add2=Label(window,text="choose your State", fg = 'black', border = 2 , bg = "white" , font = ('Microsoft YaHei UI Light',30))
add2.place (x=80,y=480,)

cmb=ttk.Combobox(window,value=state,width=25,text="Select your state",font = ('Microsoft YaHei UI Light',30))
cmb.place(x=80,y=550)


def exit():
    window.exit=messagebox.askyesno("INTIMATION","do you want to exit")
    if window.exit>0:
        window.destroy()
        return    
exi=Button(window,text='Exit',fg='black',bg='#57a1f8',font=('Microsoft YaHei UI Light',20,'bold'),command=exit,width=8)
exi.place(x=270,y=650)

def clear():
    name.delete(0,'end')
    add.delete(0,'end')
    cmb.delete(0,'end')
    phone.delete(0,'end')
cle=Button(window,text='Clear',fg='black',bg='#57a1f8',font=('Microsoft YaHei UI Light',20,'bold'),command=clear,width=8)
cle.place(x=480,y=650)

def sign():    
    A=name.get()
    B=add.get()
    C=cmb.get()
    D=phone.get()
    if A=="" or B=="" or C=="" or D=="":
        messagebox.showwarning("Error","Please enter the details to order the food")        
    else:
        submit.config(state=NORMAL)            
sb=Button(window,text='Submit',fg='black',bg='#57a1f8',font=('Microsoft YaHei UI Light',20,'bold'),command=sign)
sb.place(x=100,y=650)


def main():
    exi.destroy()
    cle.destroy()
    submit.destroy()
    heading.destroy()
    sb.destroy()
    name.destroy()
    add.destroy()
    logo.destroy()
    add2.destroy()
    cmb.destroy()
    phone.destroy()
    
    #Rasikas Button
    def btn1():
        pygame.mixer.music.play()
        
        label1.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        label5.destroy()
        submit.destroy()
        ras.destroy()
        sal.destroy()
        kfc.destroy()
        food.destroy()
        lab.destroy()
        lab2.destroy()

        #names
        global cb1,mb1,vt1,ds1,cc1,mj1,bh1,tm1
        cb1=StringVar()
        mb1=StringVar()
        vt1=StringVar()
        ds1=StringVar()
        cc1=StringVar()
        mj1=StringVar()
        bh1=StringVar()
        tm1=StringVar()

        

        window.title("Rasikas")
        window.iconbitmap("Rasikas.ico")
        rasikas_lab=Label(window , text = " Welcome to Rasikas",font=font_style,bg="#f4b41a",fg="#143d59",pady=20,width=100)
        rasikas_lab.pack ()
        

        #chicken Briyani
        global cb
        cb=Label(window,text="Chicken Briyani\n₹100",bg="white",width=20,height=2,font=("bold",20)).place(x = 10, y = 270)
        
        global cb_value
        cb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cb1).place(x=110,y=340)
        
        global cbimg
        cbimg=PhotoImage(file = "cb.png")
        briyani_image=Label(window,image=cbimg,bg="white")
        briyani_image.place(x = 7, y = 100,relheight=0.2,relwidth=0.2)
        
        #Mutton Briyani
        global mb
        mb=Label(window,text="Mutton Briyani\n₹200",bg="white",width=20,height=2,font=("bold",20)).place(x = 260, y = 270)
        
        global mb_value
        mb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mb1).place(x=370,y=340)
        
        global mbimg
        mbimg=PhotoImage(file = "mb.png")
        briyani_image=Label(window,image=mbimg,bg="white")
        briyani_image.place(x = 270, y = 100,relheight=0.2,relwidth=0.2)
        
        #Veg Thali
        global vt
        vt=Label(window,text="Veg Thali\n₹145",bg="white",width=20,height=2,font=("bold",20)).place(x = 520, y = 270)
        
        global vt_value
        vt_value=Spinbox(window,from_=0,to=100,width=15,textvariable=vt1).place(x=625,y=340)
        
        global vtimg
        vtimg=PhotoImage(file = "vt.png")
        briyani_image=Label(window,image=vtimg,bg="white")
        briyani_image.place(x = 530, y = 100,relheight=0.2,relwidth=0.2)

        
        #dosa
        global ds
        ds=Label(window,text="Dosa\n₹15",bg="white",width=20,height=2,font=("bold",20)).place(x = 760, y = 270)
        
        global ds_value
        ds_value=Spinbox(window,from_=0,to=100,width=15,textvariable=ds1).place(x=880,y=340)
        
        global dosaimg
        dosaimg=PhotoImage(file = "dosa.png")
        dosa_image=Label(window,image=dosaimg,bg="white")
        dosa_image.place(x = 770, y = 100,relheight=0.2,relwidth=0.2)

        #coca cola
        global cc
        cc=Label(window,text="Coco Cola\n₹60",bg="white",width=20,height=2,font=("bold",20)).place(x =2, y = 580)
        
        global cc_value
        cc_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cc1).place(x=110,y=650)
        
        global ccimg
        ccimg=PhotoImage(file = "cc.png")
        cc_image=Label(window,image=ccimg,bg="white")
        cc_image.place(x = 7, y = 410,relheight=0.2,relwidth=0.2)

        #mojito
        global mj
        mj=Label(window,text="Mojito\n40",bg="white",width=20,height=2,font=("bold",20)).place(x =260, y = 580)
        
        global mj_value
        mj_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mj1).place(x=370,y=650)
        
        global mjimg
        mjimg=PhotoImage(file = "mj.png")
        mj_image=Label(window,image=mjimg,bg="white")
        mj_image.place(x =270, y = 410,relheight=0.2,relwidth=0.2)

        #bread halwa
        global bh
        bh=Label(window,text="Bread Halwa\n₹80",bg="white",width=20,height=2,font=("bold",20)).place(x =520, y = 580)
        
        global bh_value
        bh_value=Spinbox(window,from_=0,to=100,width=15,textvariable=bh1).place(x=620,y=650)
        
        global bhimg
        bhimg=PhotoImage(file = "bh.png")
        bh_image=Label(window,image=bhimg,bg="white")
        bh_image.place(x =530, y = 410,relheight=0.2,relwidth=0.2)


        #thaen mittai
        global tm
        tm=Label(window,text="Thean Mittai\n₹5",bg="white",width=20,height=2,font=("bold",20)).place(x =760, y = 580)
        
        global tm_value
        tm_value=Spinbox(window,from_=0,to=100,width=15,textvariable=tm1).place(x=870,y=650)
        
        global tmimg
        tmimg=PhotoImage(file = "tm.png")
        tm_image=Label(window,image=tmimg,bg="white")
        tm_image.place(x =770, y = 410,relheight=0.2,relwidth=0.2)
        

        def final():
            web.open_new_tab("http://rasikasrestaurant.com/")
        global final_button
        final_button=Button(window,text="Click Here To Website",command=final,bg="#f4b41a",fg="#143d59",font=font_style).place(x=400,y=700)
            
        
        def order():   
            cb_total=int(cb1.get())*100
            mb_total=int(mb1.get())*200
            vt_total=int(vt1.get())*145
            ds_total=int(ds1.get())*15
            cc_total=int(cc1.get())*60
            mj_total=int(mj1.get())*40
            bh_total=int(bh1.get())*80
            tm_total=int(tm1.get())*5
                
            global total_bill
            total_bill=cb_total + mb_total + vt_total + ds_total +cc_total + mj_total + bh_total + tm_total

            global bill
            bill=Label(window,text="Your total Bill:Rs."+str(total_bill),font=font_style,bg="white").place(x=1120,y=400)

        global total_button 
        total_button=Button(window,text="Total",font=("Bold",20),command=order,bg="#f4b41a",fg="#143d59").place(x=1200,y=300)
         
        def onClick():
            window.onclick=messagebox.showinfo("Welcome to Rasikas.",  "Order placed \n your order will Deliver soon!")
             

        # Create a Button
        order = Button(window, text="Place your Order",font=font_style, command=onClick,bg="#f4b41a",fg="#143d59").place(x=1120,y=470)
    
    #Salem RR Button
    def btn2():
        pygame.mixer.music.play()
         

        label1.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        label5.destroy()
        submit.destroy()
        ras.destroy()
        sal.destroy()
        kfc.destroy()
        food.destroy()
        lab.destroy()
        lab2.destroy()

        #names
        global cb1,mb1,vt1,ds1,cc1,mj1,bh1,tm1
        cb1=StringVar()
        mb1=StringVar()
        vt1=StringVar()
        ds1=StringVar()
        cc1=StringVar()
        mj1=StringVar()
        bh1=StringVar()
        tm1=StringVar()

        

        window.title("Salem RR")
        window.iconbitmap("salemRR.ico")
        rasikas_lab=Label(window , text = " Welcome to Salem RR",font=font_style,bg="#f4b41a",fg="#143d59",pady=20,width=100)
        rasikas_lab.pack ()
        

        #chicken Briyani
        global cb
        cb=Label(window,text="Chicken Briyani\n₹100",bg="white",width=20,height=2,font=("bold",20)).place(x = 10, y = 270)
        
        global cb_value
        cb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cb1).place(x=110,y=340)
        
        global cbimg
        cbimg=PhotoImage(file = "cb.png")
        briyani_image=Label(window,image=cbimg,bg="white")
        briyani_image.place(x = 7, y = 100,relheight=0.2,relwidth=0.2)
        
        #Mutton Briyani
        global mb
        mb=Label(window,text="Mutton Briyani\n₹200",bg="white",width=20,height=2,font=("bold",20)).place(x = 260, y = 270)
        
        global mb_value
        mb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mb1).place(x=370,y=340)
        
        global mbimg
        mbimg=PhotoImage(file = "mb.png")
        briyani_image=Label(window,image=mbimg,bg="white")
        briyani_image.place(x = 270, y = 100,relheight=0.2,relwidth=0.2)
        
        #Veg Thali
        global vt
        vt=Label(window,text="Veg Thali\n₹145",bg="white",width=20,height=2,font=("bold",20)).place(x = 520, y = 270)
        
        global vt_value
        vt_value=Spinbox(window,from_=0,to=100,width=15,textvariable=vt1).place(x=625,y=340)
        
        global vtimg
        vtimg=PhotoImage(file = "vt.png")
        briyani_image=Label(window,image=vtimg,bg="white")
        briyani_image.place(x = 530, y = 100,relheight=0.2,relwidth=0.2)

        
        #dosa
        global ds
        ds=Label(window,text="Dosa\n₹15",bg="white",width=20,height=2,font=("bold",20)).place(x = 760, y = 270)
        
        global ds_value
        ds_value=Spinbox(window,from_=0,to=100,width=15,textvariable=ds1).place(x=880,y=340)
        
        global dosaimg
        dosaimg=PhotoImage(file = "dosa.png")
        dosa_image=Label(window,image=dosaimg,bg="white")
        dosa_image.place(x = 770, y = 100,relheight=0.2,relwidth=0.2)

        #coca cola
        global cc
        cc=Label(window,text="Coco Cola\n₹60",bg="white",width=20,height=2,font=("bold",20)).place(x =2, y = 580)
        
        global cc_value
        cc_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cc1).place(x=110,y=650)
        
        global ccimg
        ccimg=PhotoImage(file = "cc.png")
        cc_image=Label(window,image=ccimg,bg="white")
        cc_image.place(x = 7, y = 410,relheight=0.2,relwidth=0.2)

        #mojito
        global mj
        mj=Label(window,text="Mojito\n40",bg="white",width=20,height=2,font=("bold",20)).place(x =260, y = 580)
        
        global mj_value
        mj_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mj1).place(x=370,y=650)
        
        global mjimg
        mjimg=PhotoImage(file = "mj.png")
        mj_image=Label(window,image=mjimg,bg="white")
        mj_image.place(x =270, y = 410,relheight=0.2,relwidth=0.2)

        #bread halwa
        global bh
        bh=Label(window,text="Bread Halwa\n₹80",bg="white",width=20,height=2,font=("bold",20)).place(x =520, y = 580)
        
        global bh_value
        bh_value=Spinbox(window,from_=0,to=100,width=15,textvariable=bh1).place(x=620,y=650)
        
        global bhimg
        bhimg=PhotoImage(file = "bh.png")
        bh_image=Label(window,image=bhimg,bg="white")
        bh_image.place(x =530, y = 410,relheight=0.2,relwidth=0.2)


        #thaen mittai
        global tm
        tm=Label(window,text="Thean Mittai\n₹5",bg="white",width=20,height=2,font=("bold",20)).place(x =760, y = 580)
        
        global tm_value
        tm_value=Spinbox(window,from_=0,to=100,width=15,textvariable=tm1).place(x=870,y=650)
        
        global tmimg
        tmimg=PhotoImage(file = "tm.png")
        tm_image=Label(window,image=tmimg,bg="white")
        tm_image.place(x =770, y = 410,relheight=0.2,relwidth=0.2)
        

        def final():
            web.open_new_tab("https://salemrrbiryani.com/")
        global final_button
        final_button=Button(window,text="Click Here To Website",command=final,bg="#f4b41a",fg="#143d59",font=font_style).place(x=400,y=700)
        
        def order():   
            cb_total=int(cb1.get())*100
            mb_total=int(mb1.get())*200
            vt_total=int(vt1.get())*145
            ds_total=int(ds1.get())*15
            cc_total=int(cc1.get())*60
            mj_total=int(mj1.get())*40
            bh_total=int(bh1.get())*80
            tm_total=int(tm1.get())*5
                
            global total_bill
            total_bill=cb_total + mb_total + vt_total + ds_total +cc_total + mj_total + bh_total + tm_total

            global bill
            bill=Label(window,text="Your total Bill:Rs."+str(total_bill),font=font_style,bg="white").place(x=1120,y=400)

        global total_button 
        total_button=Button(window,text="Total",font=("Bold",20),command=order,bg="#f4b41a",fg="#143d59").place(x=1200,y=300)
         
        def onClick():
            window.onclick=messagebox.showinfo("Welcome to Salem RR",  "Order placed \n your order will Deliver soon!")
             

        # Create a Button
        order = Button(window, text="Place your Order",font=font_style, command=onClick,bg="#f4b41a",fg="#143d59").place(x=1120,y=470)
    
    #Kfc Button
    def btn3():
        pygame.mixer.music.play()
        
        label1.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        label5.destroy()
        submit.destroy()
        ras.destroy()
        sal.destroy()
        kfc.destroy()
        food.destroy()
        lab.destroy()
        lab2.destroy()

        #names
        global cb1,mb1,vt1,ds1,cc1,mj1,bh1,tm1
        cb1=StringVar()
        mb1=StringVar()
        vt1=StringVar()
        ds1=StringVar()
        cc1=StringVar()
        mj1=StringVar()
        bh1=StringVar()
        tm1=StringVar()

        

        window.title("KFC")
        window.iconbitmap("kfc.ico")
        rasikas_lab=Label(window , text = " Welcome to KFC",font=font_style,bg="#f4b41a",fg="#143d59",pady=20,width=100)
        rasikas_lab.pack ()
        

        #chicken piece
        global cb
        cb=Label(window,text="Chicken 5Pcs\n₹100",bg="white",width=20,height=2,font=("bold",20)).place(x = 7, y = 270)
        
        global cb_value
        cb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cb1).place(x=110,y=340)
        
        global cbimg
        cbimg=PhotoImage(file = "ck.png")
        briyani_image=Label(window,image=cbimg,bg="white")
        briyani_image.place(x = 7, y = 100,relheight=0.2,relwidth=0.2)
        
        #Chicken leg
        global mb
        mb=Label(window,text="Chicken leg\n₹200",bg="white",width=20,height=2,font=("bold",20)).place(x = 260, y = 270)
        
        global mb_value
        mb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mb1).place(x=370,y=340)
        
        global mbimg
        mbimg=PhotoImage(file = "leg.png")
        briyani_image=Label(window,image=mbimg,bg="white")
        briyani_image.place(x = 270, y = 100,relheight=0.2,relwidth=0.2)
        
        #chicken burger
        global vt
        vt=Label(window,text="Chicken burger\n₹199",bg="white",width=20,height=2,font=("bold",20)).place(x = 500, y = 270)
        
        global vt_value
        vt_value=Spinbox(window,from_=0,to=100,width=15,textvariable=vt1).place(x=625,y=340)
        
        global vtimg
        vtimg=PhotoImage(file = "ckb.png")
        briyani_image=Label(window,image=vtimg,bg="white")
        briyani_image.place(x = 530, y = 100,relheight=0.2,relwidth=0.2)

        
        #veg burger
        global ds
        ds=Label(window,text="veg burger\n₹149",bg="white",width=20,height=2,font=("bold",20)).place(x = 760, y = 270)
        
        global ds_value
        ds_value=Spinbox(window,from_=0,to=100,width=15,textvariable=ds1).place(x=880,y=340)
        
        global dosaimg
        dosaimg=PhotoImage(file = "veb.png")
        dosa_image=Label(window,image=dosaimg,bg="white")
        dosa_image.place(x = 770, y = 100,relheight=0.2,relwidth=0.2)

        #coca cola
        global cc
        cc=Label(window,text="Coco Cola\n₹60",bg="white",width=20,height=2,font=("bold",20)).place(x =2, y = 580)
        
        global cc_value
        cc_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cc1).place(x=110,y=650)
        
        global ccimg
        ccimg=PhotoImage(file = "cck.png")
        cc_image=Label(window,image=ccimg,bg="white")
        cc_image.place(x = 7, y = 410,relheight=0.2,relwidth=0.2)

        #sprite
        global mj
        mj=Label(window,text="Sprite\n₹60",bg="white",width=20,height=2,font=("bold",20)).place(x =260, y = 580)
        
        global mj_value
        mj_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mj1).place(x=370,y=650)
        
        global mjimg
        mjimg=PhotoImage(file = "sprite.png")
        mj_image=Label(window,image=mjimg,bg="white")
        mj_image.place(x =270, y = 410,relheight=0.2,relwidth=0.2)

        #chicken piza
        global bh
        bh=Label(window,text="Chicken pizza\n₹249",bg="white",width=20,height=2,font=("bold",20)).place(x =500, y = 580)
        
        global bh_value
        bh_value=Spinbox(window,from_=0,to=100,width=15,textvariable=bh1).place(x=620,y=650)
        
        global bhimg
        bhimg=PhotoImage(file = "ckp.png")
        bh_image=Label(window,image=bhimg,bg="white")
        bh_image.place(x =530, y = 410,relheight=0.2,relwidth=0.2)


        #veg pizza
        global tm
        tm=Label(window,text="Veg pizza\n₹149",bg="white",width=20,height=2,font=("bold",20)).place(x =760, y = 580)
        
        global tm_value
        tm_value=Spinbox(window,from_=0,to=100,width=15,textvariable=tm1).place(x=870,y=650)
        
        global tmimg
        tmimg=PhotoImage(file = "vep.png")
        tm_image=Label(window,image=tmimg,bg="white")
        tm_image.place(x =770, y = 410,relheight=0.2,relwidth=0.2)
        

        def final():
            web.open_new_tab("https://restaurants.kfc.co.in/kfc-omalur-main-road-restaurants-omalur-main-road-salem-35129/Home")
        global final_button
        final_button=Button(window,text="Click Here To Website",command=final,bg="#f4b41a",fg="#143d59",font=font_style).place(x=400,y=700)
        
        def order():   
            cb_total=int(cb1.get())*100
            mb_total=int(mb1.get())*200
            vt_total=int(vt1.get())*199
            ds_total=int(ds1.get())*149
            cc_total=int(cc1.get())*60
            mj_total=int(mj1.get())*60
            bh_total=int(bh1.get())*249
            tm_total=int(tm1.get())*149
                
            global total_bill
            total_bill=cb_total + mb_total + vt_total + ds_total +cc_total + mj_total + bh_total + tm_total

            global bill
            bill=Label(window,text="Your total Bill:Rs."+str(total_bill),font=font_style,bg="white").place(x=1120,y=400)

        global total_button 
        total_button=Button(window,text="Total",font=("Bold",20),command=order,bg="#f4b41a",fg="#143d59").place(x=1200,y=300)
         
        def onClick():
            window.onclick=messagebox.showinfo("Welcome to Kfc RR",  "Order placed \n your order will Deliver soon!")
             

        # Create a Button
        order = Button(window, text="Place your Order",font=font_style, command=onClick,bg="#f4b41a",fg="#143d59").place(x=1120,y=470)
    
    #Food Court Button
    def btn4():
        pygame.mixer.music.play()
        label1.destroy()
        label2.destroy()
        label3.destroy()
        label4.destroy()
        label5.destroy()
        submit.destroy()
        ras.destroy()
        sal.destroy()
        kfc.destroy()
        food.destroy()
        lab.destroy()
        lab2.destroy()

        #names
        global cb1,mb1,vt1,ds1,cc1,mj1,bh1,tm1
        cb1=StringVar()
        mb1=StringVar()
        vt1=StringVar()
        ds1=StringVar()
        cc1=StringVar()
        mj1=StringVar()
        bh1=StringVar()
        tm1=StringVar()

        

        window.title("Food Court")
        window.iconbitmap("fc.ico")
        rasikas_lab=Label(window , text = " Welcome to Food Court",font=font_style,bg="#f4b41a",fg="#143d59",pady=20,width=100)
        rasikas_lab.pack ()
        

        #chicken Briyani
        global cb
        cb=Label(window,text="Chicken Briyani\n₹100",bg="white",width=20,height=2,font=("bold",20)).place(x = 10, y = 270)
        
        global cb_value
        cb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cb1).place(x=110,y=340)
        
        global cbimg
        cbimg=PhotoImage(file = "cb.png")
        briyani_image=Label(window,image=cbimg,bg="white")
        briyani_image.place(x = 7, y = 100,relheight=0.2,relwidth=0.2)
        
        #Mutton Briyani
        global mb
        mb=Label(window,text="Mutton Briyani\n₹200",bg="white",width=20,height=2,font=("bold",20)).place(x = 260, y = 270)
        
        global mb_value
        mb_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mb1).place(x=370,y=340)
        
        global mbimg
        mbimg=PhotoImage(file = "mb.png")
        briyani_image=Label(window,image=mbimg,bg="white")
        briyani_image.place(x = 270, y = 100,relheight=0.2,relwidth=0.2)
        
        #chicken leg
        global vt
        vt=Label(window,text="chicken leg\n₹200",bg="white",width=20,height=2,font=("bold",20)).place(x = 520, y = 270)
        
        global vt_value
        vt_value=Spinbox(window,from_=0,to=100,width=15,textvariable=vt1).place(x=625,y=340)
        
        global vtimg
        vtimg=PhotoImage(file = "leg.png")
        briyani_image=Label(window,image=vtimg,bg="white")
        briyani_image.place(x = 530, y = 100,relheight=0.2,relwidth=0.2)

        
        #chicken burger
        global ds
        ds=Label(window,text="Chicken burger\n₹199",bg="white",width=20,height=2,font=("bold",20)).place(x = 760, y = 270)
        
        global ds_value
        ds_value=Spinbox(window,from_=0,to=100,width=15,textvariable=ds1).place(x=880,y=340)
        
        global dosaimg
        dosaimg=PhotoImage(file = "ckb.png")
        dosa_image=Label(window,image=dosaimg,bg="white")
        dosa_image.place(x = 770, y = 100,relheight=0.2,relwidth=0.2)

        #coca cola
        global cc
        cc=Label(window,text="Coco Cola\n₹60",bg="white",width=20,height=2,font=("bold",20)).place(x =2, y = 580)
        
        global cc_value
        cc_value=Spinbox(window,from_=0,to=100,width=15,textvariable=cc1).place(x=110,y=650)
        
        global ccimg
        ccimg=PhotoImage(file = "cc.png")
        cc_image=Label(window,image=ccimg,bg="white")
        cc_image.place(x = 7, y = 410,relheight=0.2,relwidth=0.2)

        #mojito
        global mj
        mj=Label(window,text="Mojito\n40",bg="white",width=20,height=2,font=("bold",20)).place(x =260, y = 580)
        
        global mj_value
        mj_value=Spinbox(window,from_=0,to=100,width=15,textvariable=mj1).place(x=370,y=650)
        
        global mjimg
        mjimg=PhotoImage(file = "mj.png")
        mj_image=Label(window,image=mjimg,bg="white")
        mj_image.place(x =270, y = 410,relheight=0.2,relwidth=0.2)

        #chicken pizza
        global bh
        bh=Label(window,text="chicken pizza\n₹249",bg="white",width=20,height=2,font=("bold",20)).place(x =500, y = 580)
        
        global bh_value
        bh_value=Spinbox(window,from_=0,to=100,width=15,textvariable=bh1).place(x=620,y=650)
        
        global bhimg
        bhimg=PhotoImage(file = "ckb.png")
        bh_image=Label(window,image=bhimg,bg="white")
        bh_image.place(x =530, y = 410,relheight=0.2,relwidth=0.2)


        #veg pizza
        global tm
        tm=Label(window,text="veg pizza\n₹149",bg="white",width=20,height=2,font=("bold",20)).place(x =760, y = 580)
        
        global tm_value
        tm_value=Spinbox(window,from_=0,to=100,width=15,textvariable=tm1).place(x=870,y=650)
        
        global tmimg
        tmimg=PhotoImage(file = "vep.png")
        tm_image=Label(window,image=tmimg,bg="white")
        tm_image.place(x =770, y = 410,relheight=0.2,relwidth=0.2)
        

        def final():
            web.open_new_tab("https://www.swiggy.com/?utm_source=Google-Sok&utm_medium=CPC&utm_campaign=google_search_sok_food_na_narm_order_web_m_web_clubbedcities_neev_brand_newuser_v3_ei_brand_em&gclid=Cj0KCQjwpeaYBhDXARIsAEzItbHSnaM7TGzjxRdAuPOB1XKs1Pg9OAmAClqPJWAGhRiD1ZSxwaaM1qoaAvoREALw_wcB")
        global final_button
        final_button=Button(window,text="Click Here To Website",command=final,bg="#f4b41a",fg="#143d59",font=font_style).place(x=400,y=700)
        
        def order():   
            cb_total=int(cb1.get())*100
            mb_total=int(mb1.get())*200
            vt_total=int(vt1.get())*200
            ds_total=int(ds1.get())*199
            cc_total=int(cc1.get())*60
            mj_total=int(mj1.get())*40
            bh_total=int(bh1.get())*249
            tm_total=int(tm1.get())*149
                
            global total_bill
            total_bill=cb_total + mb_total + vt_total + ds_total +cc_total + mj_total + bh_total + tm_total

            global bill
            bill=Label(window,text="Your total Bill:Rs."+str(total_bill),font=font_style,bg="white").place(x=1120,y=400)

        global total_button 
        total_button=Button(window,text="Total",font=("Bold",20),command=order,bg="#f4b41a",fg="#143d59").place(x=1200,y=300)
         
        def onClick():
            window.onclick=messagebox.showinfo("Welcome to Food Court",  "Order placed \n your order will Deliver soon!")
             

        # Create a Button
        order = Button(window, text="Place your Order",font=font_style, command=onClick,bg="#f4b41a",fg="#143d59").place(x=1120,y=470)

        


    global bg
    bg=PhotoImage(file = "Rasikas.png")
    label1=Label(window,image=bg,bg='white')
    label1.place(x = -4, y = 100,relheight=0.3,relwidth=0.3)    

    #Rasikas Restratunt
    ras=Button(window,text="Rasikas",bg="#030E4F",fg="#F49F1C",padx=35,pady=20,width=15,font=font_style,command=btn1)
    ras.pack(fill=X,side="left") 
    

    #SalemRR Image
    global bg2
    bg2=PhotoImage(file = "salemRR.png")
    label2=Label(window,image=bg2,bg='white')
    label2.place(x = 340, y = 100,relheight=0.3,relwidth=0.3)

    #SalemRR Restratunt
    sal=Button(window,text="Salem RR",bg="#030E4F",fg="#F49F1C",padx=35,pady=20,width=15,font=font_style,command=btn2)
    sal.pack(fill=X,side="left")


    #Foodcourt Images
    global bg3
    bg3=PhotoImage(file = "kfc.png")
    label3=Label(window,image=bg3,bg='white')
    label3.place(x = 720, y = 100,relheight=0.3,relwidth=0.3)

    #Foodcourt
    food=Button(window,text="Foodcourt",bg="#030E4F",fg="#F49F1C",padx=35,pady=20,width=15,font=font_style,command=btn4)
    food.pack(fill=X,side="right")

    #Kfc Image
    global bg4
    bg4=PhotoImage(file = "fc.png")
    label4=Label(window,image=bg4,bg='white')
    label4.place(x = 1100, y = 100,relheight=0.3,relwidth=0.3)
    #Kfc
    kfc=Button(window,text="Kfc",bg="#030E4F",fg="#F49F1C",padx=50,pady=20,width=15,font=font_style,command=btn3)
    kfc.pack(fill=X,side="right")

    #Swiggy logo
    global bg5
    bg5=PhotoImage(file ="Swiggy.png")
    label5=Label(window,image=bg5,bg="white")
    label5.place(x = 50, y =500,relheight=0.25,relwidth=1)


logoimg=PhotoImage(file = "logo.png")
logo=Label(window,image=logoimg,bg='white')
logo.place(x = 820, y = 100,relheight=0.3,relwidth=0.3)
 
submit=Button(window,text="click Here to order the Food",bg="#030E4F",fg="#F49F1C",padx=35,pady=20,width=20,font=font_style,command=main,state=DISABLED)
submit.place(x=800,y=450)

window.mainloop()

