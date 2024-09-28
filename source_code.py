from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import time
import random

#=====EXIT FROM ADMIN=====
def Exit():
    master = Tk()
    master.withdraw()
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        login2.destroy()
        
#======EMPLOYEE INFO=======
def emp_info():
    con=mysql.connector.connect(host="localhost",user="root",passwd="mypassword",database="restaurant")
    cur=con.cursor()
    query1 = "SELECT * from employee;"
    cur.execute(query1)
    data=cur.fetchall()
    print("   ")
    print("{:<60}{:<20}{:<20}{:<20}".format("NAME","DESIGNATION","DATE OF JOINING", "SALARY"))
    print("   ")
    for i in data:
        print("{:<60}{:<20}{}{:>15}".format(    i[0],i[1],i[2],i[3]))
        print("   ")
    con.close()

#=======MENU=======    
def view_all():
    con=mysql.connector.connect(host="localhost",user="root",passwd="mypassword",database="restaurant")
    cur=con.cursor()
    query1 = "SELECT * from starters;"
    cur.execute(query1)
    data=cur.fetchall()
    print("{:<60}{:<20}".format( "STARTERS", "PRICE"))
    for i in data:
        print("{:<60}{:<20}".format(    i[0],i[1]))
    print("____________________________________________________________________________________________________")
   
    query3 = "SELECT * from main_course;"
    cur.execute(query3)
    data=cur.fetchall()
    print("{:<60}{:<20}".format("MAIN COURSE", "PRICE"))
    for i in data:
        print("{:<60}{:<20}".format(    i[0],i[1]))
    print("____________________________________________________________________________________________________")
    query4 = "SELECT * from side_dish;"
    cur.execute(query4)
    data=cur.fetchall()
    print("{:<60}{:<20}".format("SIDE DISH", "PRICE"))
    for i in data:
        print("{:<60}{:<20}".format(    i[0],i[1]))
    print("____________________________________________________________________________________________________")
    query5 = "SELECT * from chefs_specials;"
    cur.execute(query5)
    data=cur.fetchall()
    print("{:<60}{:<20}".format("CHEF'S SPECIALS", "PRICE"))
    for i in data:
        print("{:<60}{:<20}".format(    i[0],i[1]))
    print("____________________________________________________________________________________________________")            
    query6 = "SELECT * from beverages;"
    cur.execute(query6)
    data=cur.fetchall()
    print("{:<60}{:<20}".format("BEVERAGES", "PRICE"))
    for i in data:
        print("{:<60}{:<20}".format(    i[0],i[1]))
    print("____________________________________________________________________________________________________")
    query7 = "SELECT * from desserts;"
    cur.execute(query7)
    data=cur.fetchall()
    print("{:<60}{:<20}".format("HAPPY ENDINGS", "PRICE"))
    for i in data:
        print("{:<60}{:<20}".format(    i[0],i[1]))
    print("____________________________________________________________________________________________________")
    
    con.close()
    
#======CUSTOMER INFO===========
def cust_info():
    con=mysql.connector.connect(host="localhost",user="root",passwd="mypassword",database="restaurant")
    cur=con.cursor()
    query="select * from purchase_records"
    cur.execute(query)
    data=cur.fetchall()
    print("{:<20}{:>10}{:>20}{:>20}{:>20}".format("DATE","BILL NO","CUSTOMER NAME","CUSTOMER CONTACT", "TOTAL AMT"))
    for i in data:
        print("{:<20}{:>10}{:>20}{:>20}{:>20}".format(    i[0],i[1],i[2],i[3],i[4]))

    
#======TO ADD ITEM IN EXISTING MENU======
def add_item():
    con=mysql.connector.connect(host="localhost",user="root",passwd="mypassword",database="restaurant")
    cur=con.cursor()
    print("CATEGORIES","\n","STARTERS","\n","MAIN COURSE","\n","SIDE DISH","\n","CHEF'S SPECIAL","\n","BEVERAGES","\n","DESSERTS")
    cat=input("Enter category name:")
    item=input("Enter item name:")
    price=int(input("Enter price:"))
    query="INSERT INTO {0}(ITEM,PRICE) VALUES('{1}',{2})".format(cat,item,price)
    cur.execute(query)
    con.commit()
    print("Data successfully inserted!!")
    query1="SELECT * FROM {}".format(cat)
    cur.execute(query1)
    data=cur.fetchall()
    print(data)
    con.close()

#====TO DELETE AN ITEM FROM EXISTING MENU======
def delete_item():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mypassword",
        database="restaurant"
        )
    cur=con.cursor()
    print("CATEGORIES","\n","STARTERS","\n","MAIN COURSE","\n","SIDE DISH","\n","CHEF'S SPECIAL","\n","BEVERAGES","\n","DESSERTS")
    cat=input("Enter category name:")
    item=input("Enter item name:")

    sql="select * from {}".format(cat)
    cur.execute(sql)
    items=[]
    data=cur.fetchall()
    item_name=[]
    for eachrow in data:
        item_name.append(eachrow[0])
    for x in item_name:
        if x!=item:
            print("ITEM DOES NOT EXIST")
            break
        else:
            query="DELETE FROM {} WHERE ITEM='{}'".format(cat,item)
            cur.execute(query)
            con.commit()
            print("Data successfully deleted!!")
            query1="SELECT * FROM {}".format(cat)
            cur.execute(query1)
            data=cur.fetchall()
            print(data)
    con.close()

#=====TO UPDATE PRICE OF AN ITEM======    
def update_item():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mypassword",
        database="restaurant"
        )
    cur=con.cursor()
    print("CATEGORIES","\n","STARTERS","\n","MAIN COURSE","\n","SIDE DISH","\n","CHEF'S SPECIAL","\n","BEVERAGES","\n","DESSERTS")
    cat=input("Enter category name:")
    item=input("Enter item name:")
    n_price=int(input("Enter price:"))

    sql="select * from {}".format(cat)
    cur.execute(sql)
    items=[]
    data=cur.fetchall()
    item_name=[]
    for eachrow in data:
        item_name.append(eachrow[0])
    for x in item_name:
        if x!=item:
            print("ITEM DOES NOT EXIST")
            break
        else:
            query="UPDATE {0} SET PRICE = {1} WHERE ITEM='{2}'".format(cat,n_price,item)
            cur.execute(query)
            con.commit()
            print("Data successfully updated!!")
            query1="SELECT * FROM {}".format(cat)
            cur.execute(query1)
            data=cur.fetchall()
            print(data)
    con.close()

#=====TO SEARCH FOR DETAILS OF AN ITEM======
def search_item():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mypassword",
        database="restaurant"
        )
    cur=con.cursor()
    print("CATEGORIES","\n","STARTERS","\n","MAIN COURSE","\n","SIDE DISH","\n","CHEF'S SPECIAL","\n","BEVERAGES","\n","DESSERTS")
    cat=input("Enter category name:")
    item=input("Enter item name:")

    sql="select * from {}".format(cat)
    cur.execute(sql)
    items=[]
    data=cur.fetchall()
    item_name=[]
    for eachrow in data:
        item_name.append(eachrow[0])
    for x in item_name:
        if x!=item:
            print("ITEM DOES NOT EXIST")
            break
        else:
            query1="SELECT * FROM {0} WHERE ITEM='{1}'".format(cat,item)
            cur.execute(query1)
            data=cur.fetchall()
            print(data)
    con.close()
    
#=====MENU WINDOW FOR CUSTOMER==========
def cust_window():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mypassword",
        database="restaurant"
        )
    c=con.cursor()
    def calculate():
        c1=str(c_name_txt.get())
        c2=int(c_phn_txt.get())
        c3=int(c_bill_txt.get())
        c4=int(c_tbl_txt.get())
        if c1=="":
            master = Tk()
            master.withdraw()
            MsgBox = messagebox.showerror('Invalid input','Please enter customer name',icon = 'warning')
        elif c2=="0" or len(str(c2))!=10:
            master = Tk()
            master.withdraw()
            MsgBox = messagebox.showerror('Invalid input','Please enter valid contact number',icon = 'warning')
        elif c4==0:
            master = Tk()
            master.withdraw()
            MsgBox = messagebox.showerror('Invalid input','Please enter table number',icon = 'warning')
 
        print("{:>10}{:<25}{:>1}{:<10}".format("Customer Name:",c1,"Bill No.:",c3))
        print("{:>8}{:<30}{:>5}{:>1}".format("Contact:",c2,"Table No.:",c4))
        print("   ")
        print("{:>8}".format(localtime))
        print("                                                            ")
        print("----------------------------------------------------------------")
        print("{:<30}{:>5}{:>13}".format("Item", "Qty", "Price"))
        print("----------------------------------------------------------------")

        item1=int(a1_txt.get())
        item2=int(a2_txt.get())
        item3=int(a3_txt.get())
        item4=int(a4_txt.get())
        item5=int(a5_txt.get())
        item6=int(a6_txt.get())
        item7=int(a7_txt.get())
        item8=int(a8_txt.get())
       
        sql="select * from starters;"
        c.execute(sql)
        items=[]
        data=c.fetchall()
        starters_name=[]
        global starters_price
        starters_price=[]
        for eachrow in data:
            starters_name.append(eachrow[0])
            starters_price.append(eachrow[1])
       
        starters_qty=[item1,item2,item3,item4,item5,item6,item7,item8]

        for i in range (0,7):
            name=""
            price=""
            qty=""
            if starters_qty[i]>0:
                name=starters_name[i]
                qty=starters_qty[i]
                price=starters_price[i]*qty
                print("{:<30}{:>5}{:>12}".format(      name, qty, price))

        Cost_starters=0
        Cost_starters = (item1*260) + (item2*110) +(item3*265) + (item4*375) + (item5*385) + (item6*325) + (item7*325) + (item8*245)

        item21=int(m1_txt.get())
        item22=int(m2_txt.get())
        item23=int(m3_txt.get())
        item24=int(m4_txt.get())
        item25=int(m5_txt.get())
        item26=int(m6_txt.get())
        item27=int(m7_txt.get())
        item28=int(m8_txt.get())

        sql="select * from main_course;"
        c.execute(sql)
        items=[]
        data=c.fetchall()
        main_course_name=[]
        main_course_price=[]
        for eachrow in data:
            main_course_name.append(eachrow[0])
            main_course_price.append(eachrow[1])
        main_course_qty=[item21,item22,item23,item24,item25,item26,item27,item28]

        for i in range (0,7):
            name=""
            price=""
            qty=""
            if main_course_qty[i]>0:
                name=main_course_name[i]
                qty=main_course_qty[i]
                price=main_course_price[i]*qty
                print("{:<30}{:>5}{:>12}".format(      name, qty, price))

        Cost_MainCourse=0
        Cost_MainCourse = (item21*155) + (item22*55) +(item23*60) + (item24*195) + (item25*280) + (item26*270) + (item27*265) + (item28*210)

        item31=int(sd1_txt.get())
        item32=int(sd2_txt.get())
        item33=int(sd3_txt.get())
        item34=int(sd4_txt.get())
        item35=int(sd5_txt.get())
        item36=int(sd6_txt.get())
        item37=int(sd7_txt.get())
        item38=int(sd8_txt.get())

        sql="select * from side_dish;"
        c.execute(sql)
        items=[]
        data=c.fetchall()
        side_dish_name=[]
        side_dish_price=[]
        for eachrow in data:
            side_dish_name.append(eachrow[0])
            side_dish_price.append(eachrow[1])
        side_dish_qty=[item31,item32,item33,item34,item35,item36,item37,item38]

        for i in range (0,7):
            name=""
            price=""
            qty=""
            if side_dish_qty[i]>0:
                name=side_dish_name[i]
                qty=side_dish_qty[i]
                price=side_dish_price[i]*qty
                print("{:<30}{:>5}{:>12}".format(      name, qty, price))

        Cost_SideDish=0
        Cost_SideDish = (item31*250) + (item32*275) +(item33*290) + (item34*460) + (item35*290) + (item36*310) + (item37*405) + (item38*300)

        item41=int(cs1_txt.get())
        item42=int(cs2_txt.get())
        item43=int(cs3_txt.get())
        item44=int(cs4_txt.get())
        item45=int(cs5_txt.get())
        item46=int(cs6_txt.get())
        item47=int(cs7_txt.get())
        item48=int(cs8_txt.get())

        sql="select * from chefs_specials;"
        c.execute(sql)
        items=[]
        data=c.fetchall()
        chefs_specials_name=[]
        chefs_specials_price=[]
        for eachrow in data:
            chefs_specials_name.append(eachrow[0])
            chefs_specials_price.append(eachrow[1])
        chefs_specials_qty=[item41,item42,item43,item44,item45,item46,item47,item48]

        for i in range (0,7):
            name=""
            price=""
            qty=""
            if chefs_specials_qty[i]>0:
                name=chefs_specials_name[i]
                qty=chefs_specials_qty[i]
                price=chefs_specials_price[i]*qty
                print("{:<30}{:>5}{:>12}".format(      name, qty, price))

        Cost_ChefsSpecials=0
        Cost_ChefsSpecials = (item41*400) + (item42*400) +(item43*400) + (item44*400) + (item45*420) + (item46*315) + (item47*415) + (item48*475)

        item51=int(b1_txt.get())
        item52=int(b2_txt.get())
        item53=int(b3_txt.get())
        item54=int(b4_txt.get())
        item55=int(b5_txt.get())
        item56=int(b6_txt.get())
        item57=int(b7_txt.get())
        item58=int(b8_txt.get())

        sql="select * from beverages;"
        c.execute(sql)
        items=[]
        data=c.fetchall()
        beverages_name=[]
        beverages_price=[]
        for eachrow in data:
            beverages_name.append(eachrow[0])
            beverages_price.append(eachrow[1])
        beverages_qty=[item51,item52,item53,item54,item55,item56,item57,item58]

        for i in range (0,7):
            name=""
            price=""
            qty=""
            if beverages_qty[i]>0:
                name=beverages_name[i]
                qty=beverages_qty[i]
                price=beverages_price[i]*qty
                print("{:<30}{:>5}{:>12}".format(      name, qty, price))
      
        Cost_Beverages=0
        Cost_Beverages = (item51*105) + (item52*90) +(item53*160) + (item54*170) + (item55*170) + (item56*140) + (item57*140) + (item58*75)

        item61=int(d1_txt.get())
        item62=int(d2_txt.get())
        item63=int(d3_txt.get())
        item64=int(d4_txt.get())
        item65=int(d5_txt.get())
        item66=int(d6_txt.get())
        item67=int(d7_txt.get())
        item68=int(d8_txt.get())

        sql="select * from desserts;"
        c.execute(sql)
        items=[]
        data=c.fetchall()
        desserts_name=[]
        desserts_price=[]
        for eachrow in data:
            desserts_name.append(eachrow[0])
            desserts_price.append(eachrow[1])
        desserts_qty=[item61,item62,item63,item64,item65,item66,item67,item68]

        for i in range (0,7):
            name=""
            price=""
            qty=""
            if desserts_qty[i]>0:
                name=desserts_name[i]
                qty=desserts_qty[i]
                price=desserts_price[i]*qty
                print("{:<30}{:>5}{:>12}".format(      name, qty, price))
             
        Cost_Desserts=0
        Cost_Desserts = (item61*120) + (item62*135) +(item63*185) + (item64*155) + (item65*185) + (item66*200) + (item67*160) + (item68*160)

        print("----------------------------------------------------------------")

        sub_total=Cost_starters+Cost_MainCourse+Cost_ChefsSpecials+Cost_SideDish+Cost_Beverages+Cost_Desserts
        ptax=float(sub_total)*0.05
        total=float(sub_total+ptax)

        paid_tax.set(str(ptax))
        sub_var.set(str(sub_total))
        total_var.set(str(total))

        print("{:<35}{:>12}".format(      "Total",sub_total))
        print("----------------------------------------------------------------")
        print("{:<35}{:>12}".format(      "CGST_2.5%",ptax/2))
        print("{:<35}{:>12}".format(      "SGST_2.5%",ptax/2))
        print("----------------------------------------------------------------")
        print("{:<35}{:>12}".format(      "Grand Total",total))
        print("----------------------------------------------------------------")
        print("                                                                     ")
        print("           Thank You For Visiting!!!     ")
        query="INSERT INTO purchase_records(DATE,BILL_NO,CUSTOMER_NAME,CUSTOMER_CONTACT, TOTAL_AMT) VALUES (curdate(),{0},'{1}',{2},{3})".format(c3,c1,c2,total)
        c.execute(query)
        con.commit()
        print("Record Inserted!")
        con.close()
        
    #====EXIT WINDOW FOR CUSTOMER=======
    def Exit1():
        master = Tk()
        master.withdraw()
        MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            root.destroy()

    root = Tk()
    root.title("Food Billing System")
    root.geometry("1600x1000")
    root.configure(background='black')
    bg_color="black"
    login.destroy()

    #============CALCULATION OF BILL=========
    print("{:>32}".format("   FUSION FIESTA"))
    print("{:>35}".format("78, Lake Road"))
    print("{:>33}".format("Kolkata-29"))
    print("{:>36}".format("Tel: 9830511433" ))

    #===========Top frame design============
    top_frame=Frame(root,bg='sky blue',bd=3,relief=GROOVE)
    top_frame.pack(side=TOP)

    lblTitle=Label(top_frame,font=('viner hand itc',28,'bold'),bg="moccasin",text=" FUSION FIESTA ",relief=RIDGE,fg="Black",anchor='w')
    lblTitle.grid(row=0,column=0)

    #==========Show time=================
    f12=LabelFrame(root,bg='black')
    f12.place(x=0,y=5,width=270, height=30)

    localtime=time.asctime(time.localtime(time.time()))
    lblTitleDate=Label(f12,font=('times new roman',16),text=localtime,fg="Cyan",bg="black")
    lblTitleDate.grid(row=0,column=0)

    #=========Customer Detail Frame============
    f0=LabelFrame(root,text="Customer Details",font=("brush script mt",17),fg="gold",bg=bg_color)
    f0.place(x=0,y=55, width=3102)
    
    cname_lbl=Label(f0,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",13,"bold"))
    cname_lbl.grid(row=0,column=0,padx=20,pady=5)
    c_name_txt=Entry(f0,width=15,font="helvetica 13")
    c_name_txt.insert(0,"")
    c_name_txt.grid(row=0,column=1,pady=5,padx=5)

    cphn_lbl=Label(f0,text="Mob. No.",bg=bg_color,fg="white",font=("times new roman",13,"bold"))
    cphn_lbl.grid(row=0,column=2,padx=20)
    c_phn_txt=Entry(f0,width=12,font="helvetica 13")
    c_phn_txt.insert(0,"0")
    c_phn_txt.grid(row=0,column=3,padx=5)

    cbill_lbl=Label(f0,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",13,"bold"))
    cbill_lbl.grid(row=0,column=4,padx=20)
    c_bill_txt=Entry(f0,width=8,font="helvetica 13")
    c_bill_txt.insert(0,random.randint(100,999))
    c_bill_txt.grid(row=0,column=5,padx=5)

    ctbl_lbl=Label(f0,text="Table No.",bg=bg_color,fg="white",font=("times new roman",13,"bold"))
    ctbl_lbl.grid(row=0,column=6,padx=20)
    c_tbl_txt=Entry(f0,width=5,font="helvetica 13")
    c_tbl_txt.insert(0,"0")
    c_tbl_txt.grid(row=0,column=7,padx=5)


    #===============Starters================
    f1=LabelFrame(root,text="Starters",font=("brush script mt",17),fg="yellow",bg=bg_color)
    f1.place(x=0,y=110,width=360,height=260)

    sql="select * from starters;"
    c.execute(sql)
    items=[]
    data=c.fetchall()
    starters_name=[]
    global starters_price
    starters_price=[]
    for eachrow in data:
        starters_name.append(eachrow[0])
        starters_price.append(eachrow[1])

    lbl1=Label(f1,text="Item",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=0,padx=10,sticky="w")
    lbl2=Label(f1,text="Price",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=1,padx=10,sticky="w")
    lbl3=Label(f1,text="Qty",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=2,padx=10,sticky="w")

    a1_item_lbl=Label(f1,text=starters_name[0],font=("times new roman",13),bg=bg_color,fg="sky blue")
    a1_item_lbl.grid(row=1,column=0,padx=10,sticky="w")
    a1_price_lbl=Label(f1,text=starters_price[0],font=("times new roman",13,"bold"),bg=bg_color,fg="sky blue")
    a1_price_lbl.grid(row=1,column=1,padx=10,sticky="w")        
    a1_txt=Entry(f1,width=5,font=("times new roman",12,"bold"))
    a1_txt.insert(0,"0")
    a1_txt.grid(row=1,column=2,padx=10)

    a_lbl=Label(f1,text=starters_name[1],font=("times new roman",12),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=2,column=0,padx=10,sticky="w")
    a_lbl=Label(f1,text=starters_price[1],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=2,column=1,padx=10,sticky="w")
    a2_txt=Entry(f1,width=5,font=("times new roman",11,"bold"))
    a2_txt.insert(0,"0")
    a2_txt.grid(row=2,column=2,padx=10)

    a_lbl=Label(f1,text=starters_name[2],font=("times new roman",12),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=3,column=0,padx=10,sticky="w")
    a_lbl=Label(f1,text=starters_price[2],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=3,column=1,padx=10,sticky="w")
    a3_txt=Entry(f1,width=5,font=("times new roman",11,"bold"))
    a3_txt.insert(0,"0")
    a3_txt.grid(row=3,column=2,padx=10)


    a_lbl=Label(f1,text=starters_name[3],font=("times new roman",12),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=4,column=0,padx=10,sticky="w")
    a_lbl=Label(f1,text=starters_price[3],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=4,column=1,padx=10,sticky="w")
    a4_txt=Entry(f1,width=5,font=("times new roman",11,"bold"))
    a4_txt.insert(0,"0")
    a4_txt.grid(row=4,column=2,padx=10)


    a_lbl=Label(f1,text=starters_name[4],font=("times new roman",12),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=5,column=0,padx=10,sticky="w")
    a_lbl=Label(f1,text=starters_price[4],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=5,column=1,padx=10,sticky="w")
    a5_txt=Entry(f1,width=5,font=("times new roman",11,"bold"))
    a5_txt.insert(0,"0")
    a5_txt.grid(row=5,column=2,padx=10)
           
    a_lbl=Label(f1,text=starters_name[5],font=("times new roman",12),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=6,column=0,padx=10,sticky="w")
    a_lbl=Label(f1,text=starters_price[5],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=6,column=1,padx=10,sticky="w")
    a6_txt=Entry(f1,width=5,font=("times new roman",11,"bold"))
    a6_txt.insert(0,"0")
    a6_txt.grid(row=6,column=2,padx=10)

    a_lbl=Label(f1,text=starters_name[6],font=("times new roman",12),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=7,column=0,padx=10,sticky="w")
    a_lbl=Label(f1,text=starters_price[6],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=7,column=1,padx=10,sticky="w")
    a7_txt=Entry(f1,width=5,font=("times new roman",11,"bold"))
    a7_txt.insert(0,"0")
    a7_txt.grid(row=7,column=2,padx=10)

    a_lbl=Label(f1,text=starters_name[7],font=("times new roman",12),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=8,column=0,padx=10,sticky="w")
    a_lbl=Label(f1,text=starters_price[7],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    a_lbl.grid(row=8,column=1,padx=10,sticky="w")
    a8_txt=Entry(f1,width=5,font=("times new roman",11,"bold"))
    a8_txt.insert(0,"0")
    a8_txt.grid(row=8,column=2,padx=10)

    #===============Main Course =============
    f3=LabelFrame(root,text="Main Course",font=("brush script mt",17),fg="yellow",bg=bg_color)
    f3.place(x=330,y=110,width=341,height=260)

    sql="select * from main_course;"
    c.execute(sql)
    items=[]
    data=c.fetchall()
    main_course_name=[]
    main_course_price=[]
    for eachrow in data:
        main_course_name.append(eachrow[0])
        main_course_price.append(eachrow[1])

    lbl1=Label(f3,text="Item",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=0,padx=10,sticky="w")
    lbl2=Label(f3,text="Price",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=1,padx=30,sticky="w")
    lbl3=Label(f3,text="Qty",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=2,padx=10,sticky="w")

    m_lbl=Label(f3,text=main_course_name[0],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=1,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[0],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=1,column=1,padx=30,sticky="w")
    m1_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m1_txt.insert(0,"0")
    m1_txt.grid(row=1,column=2,padx=10)

    m_lbl=Label(f3,text=main_course_name[1],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=2,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[1],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=2,column=1,padx=30,sticky="w")
    m2_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m2_txt.insert(0,"0")
    m2_txt.grid(row=2,column=2,padx=10)

    m_lbl=Label(f3,text=main_course_name[2],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=3,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[2],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=3,column=1,padx=30,sticky="w")
    m3_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m3_txt.insert(0,"0")
    m3_txt.grid(row=3,column=2,padx=10)

    m_lbl=Label(f3,text=main_course_name[3],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=4,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[3],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=4,column=1,padx=30,sticky="w")
    m4_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m4_txt.insert(0,"0")
    m4_txt.grid(row=4,column=2,padx=10)

    m_lbl=Label(f3,text=main_course_name[4],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=5,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[4],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=5,column=1,padx=30,sticky="w")
    m5_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m5_txt.insert(0,"0")
    m5_txt.grid(row=5,column=2,padx=10)

    m_lbl=Label(f3,text=main_course_name[5],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=6,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[5],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=6,column=1,padx=30,sticky="w")
    m6_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m6_txt.insert(0,"0")
    m6_txt.grid(row=6,column=2,padx=10)

    m_lbl=Label(f3,text=main_course_name[6],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=7,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[6],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=7,column=1,padx=30,sticky="w")
    m7_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m7_txt.insert(0,"0")
    m7_txt.grid(row=7,column=2,padx=10)

    m_lbl=Label(f3,text=main_course_name[7],font=("times new roman",12),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=8,column=0,padx=10,sticky="w")
    m_lbl=Label(f3,text=main_course_price[7],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    m_lbl.grid(row=8,column=1,padx=30,sticky="w")
    m8_txt=Entry(f3,width=5,font=("times new roman",11,"bold"))
    m8_txt.insert(0,"0")
    m8_txt.grid(row=8,column=2,padx=10)

    #===============Side Dishes =============
    f4=LabelFrame(root,text="Side Dish",font=("brush script mt",17),fg="yellow",bg=bg_color)
    f4.place(x=660,y=110,width=341,height=260)

    sql="select * from side_dish;"
    c.execute(sql)
    items=[]
    data=c.fetchall()
    side_dish_name=[]
    side_dish_price=[]
    for eachrow in data:
        side_dish_name.append(eachrow[0])
        side_dish_price.append(eachrow[1])

    lbl1=Label(f4,text="Item",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=0,padx=10,sticky="w")
    lbl2=Label(f4,text="Price",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=1,padx=10,sticky="w")
    lbl3=Label(f4,text="Qty",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=2,padx=10,sticky="w")

    sd_lbl=Label(f4,text=side_dish_name[0],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=1,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[0],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=1,column=1,padx=10,sticky="w")
    sd1_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd1_txt.insert(0,"0")
    sd1_txt.grid(row=1,column=2,padx=10)

    sd_lbl=Label(f4,text=side_dish_name[1],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=2,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[1],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=2,column=1,padx=10,sticky="w")
    sd2_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd2_txt.insert(0,"0")
    sd2_txt.grid(row=2,column=2,padx=10)

    sd_lbl=Label(f4,text=side_dish_name[2],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=3,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[2],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=3,column=1,padx=10,sticky="w")
    sd3_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd3_txt.insert(0,"0")
    sd3_txt.grid(row=3,column=2,padx=10)

    sd_lbl=Label(f4,text=side_dish_name[3],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=4,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[3],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=4,column=1,padx=10,sticky="w")
    sd4_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd4_txt.insert(0,"0")
    sd4_txt.grid(row=4,column=2,padx=10)

    sd_lbl=Label(f4,text=side_dish_name[4],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=5,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[4],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=5,column=1,padx=10,sticky="w")
    sd5_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd5_txt.insert(0,"0")
    sd5_txt.grid(row=5,column=2,padx=10)

    sd_lbl=Label(f4,text=side_dish_name[5],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=6,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[5],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=6,column=1,padx=10,sticky="w")
    sd6_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd6_txt.insert(0,"0")
    sd6_txt.grid(row=6,column=2,padx=10)

    sd_lbl=Label(f4,text=side_dish_name[6],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=7,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[6],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=7,column=1,padx=10,sticky="w")
    sd7_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd7_txt.insert(0,"0")
    sd7_txt.grid(row=7,column=2,padx=10)

    sd_lbl=Label(f4,text=side_dish_name[7],font=("times new roman",12),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=8,column=0,padx=10,sticky="w")
    sd_lbl=Label(f4,text=side_dish_price[7],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    sd_lbl.grid(row=8,column=1,padx=10,sticky="w")
    sd8_txt=Entry(f4,width=5,font=("times new roman",11,"bold"))
    sd8_txt.insert(0,"0")
    sd8_txt.grid(row=8,column=2,padx=10)

    #===============Chefs Special=============
    f5=LabelFrame(root,text="Chef's Specials",font=("brush script mt",17),fg="yellow",bg=bg_color)
    f5.place(x=0,y=400,width=341,height=260)

    sql="select * from chefs_specials;"
    c.execute(sql)
    items=[]
    data=c.fetchall()
    chefs_specials_name=[]
    chefs_specials_price=[]
    for eachrow in data:
        chefs_specials_name.append(eachrow[0])
        chefs_specials_price.append(eachrow[1])

    lbl1=Label(f5,text="Item",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=0,padx=10,sticky="w")
    lbl2=Label(f5,text="Price",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=1,padx=15,sticky="w")
    lbl3=Label(f5,text="Qty",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=2,padx=15,sticky="w")

    cs_lbl=Label(f5,text=chefs_specials_name[0],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=1,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[0],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=1,column=1,padx=10,sticky="w")
    cs1_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs1_txt.insert(0,"0")
    cs1_txt.grid(row=1,column=2,padx=10)

    cs_lbl=Label(f5,text=chefs_specials_name[1],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=2,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[1],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=2,column=1,padx=10,sticky="w")
    cs2_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs2_txt.insert(0,"0")
    cs2_txt.grid(row=2,column=2,padx=10)

    cs_lbl=Label(f5,text=chefs_specials_name[2],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=3,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[2],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=3,column=1,padx=10,sticky="w")
    cs3_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs3_txt.insert(0,"0")
    cs3_txt.grid(row=3,column=2,padx=10)

    cs_lbl=Label(f5,text=chefs_specials_name[3],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=4,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[3],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=4,column=1,padx=10,sticky="w")
    cs4_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs4_txt.insert(0,"0")
    cs4_txt.grid(row=4,column=2,padx=10)

    cs_lbl=Label(f5,text=chefs_specials_name[4],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=5,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[4],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=5,column=1,padx=10,sticky="w")
    cs5_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs5_txt.insert(0,"0")
    cs5_txt.grid(row=5,column=2,padx=10)

    cs_lbl=Label(f5,text=chefs_specials_name[5],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=6,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[5],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=6,column=1,padx=10,sticky="w")
    cs6_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs6_txt.insert(0,"0")
    cs6_txt.grid(row=6,column=2,padx=10)

    cs_lbl=Label(f5,text=chefs_specials_name[6],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=7,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[6],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=7,column=1,padx=10,sticky="w")
    cs7_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs7_txt.insert(0,"0")
    cs7_txt.grid(row=7,column=2,padx=10)

    cs_lbl=Label(f5,text=chefs_specials_name[7],font=("times new roman",12),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=8,column=0,padx=10,sticky="w")
    cs_lbl=Label(f5,text=chefs_specials_price[7],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    cs_lbl.grid(row=8,column=1,padx=10,sticky="w")
    cs8_txt=Entry(f5,width=5,font=("times new roman",11,"bold"))
    cs8_txt.insert(0,"0")
    cs8_txt.grid(row=8,column=2,padx=10)

    #===============Beverages=============
    f6=LabelFrame(root,text="Beverages",font=("brush script mt",17),fg="yellow",bg=bg_color)
    f6.place(x=330,y=400,width=341,height=260)

    sql="select * from beverages;"
    c.execute(sql)
    items=[]
    data=c.fetchall()
    beverages_name=[]
    beverages_price=[]
    for eachrow in data:
        beverages_name.append(eachrow[0])
        beverages_price.append(eachrow[1])

    lbl1=Label(f6,text="Item",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=0,padx=10,sticky="w")
    lbl2=Label(f6,text="Price",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=1,padx=10,sticky="w")
    lbl3=Label(f6,text="Qty",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=2,padx=30,sticky="w")

    b_lbl=Label(f6,text=beverages_name[0],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=1,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[0],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=1,column=1,padx=10,sticky="w")
    b1_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b1_txt.insert(0,"0")
    b1_txt.grid(row=1,column=2,padx=30)

    b_lbl=Label(f6,text=beverages_name[1],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=2,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[1],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=2,column=1,padx=10,sticky="w")
    b2_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b2_txt.insert(0,"0")
    b2_txt.grid(row=2,column=2,padx=10)

    b_lbl=Label(f6,text=beverages_name[2],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=3,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[2],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=3,column=1,padx=10,sticky="w")
    b3_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b3_txt.insert(0,"0")
    b3_txt.grid(row=3,column=2,padx=10)

    b_lbl=Label(f6,text=beverages_name[3],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=4,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[3],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=4,column=1,padx=10,sticky="w")
    b4_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b4_txt.insert(0,"0")
    b4_txt.grid(row=4,column=2,padx=10)

    b_lbl=Label(f6,text=beverages_name[4],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=5,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[4],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=5,column=1,padx=10,sticky="w")
    b5_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b5_txt.insert(0,"0")
    b5_txt.grid(row=5,column=2,padx=10)

    b_lbl=Label(f6,text=beverages_name[5],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=6,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[5],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=6,column=1,padx=10,sticky="w")
    b6_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b6_txt.insert(0,"0")
    b6_txt.grid(row=6,column=2,padx=10)

    b_lbl=Label(f6,text=beverages_name[6],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=7,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[6],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=7,column=1,padx=10,sticky="w")
    b7_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b7_txt.insert(0,"0")
    b7_txt.grid(row=7,column=2,padx=10)

    b_lbl=Label(f6,text=beverages_name[7],font=("times new roman",12),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=8,column=0,padx=10,sticky="w")
    b_lbl=Label(f6,text=beverages_price[7],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    b_lbl.grid(row=8,column=1,padx=10,sticky="w")
    b8_txt=Entry(f6,width=5,font=("times new roman",11,"bold"))
    b8_txt.insert(0,"0")
    b8_txt.grid(row=8,column=2,padx=10)

    #===============Desserts=============
    f7=LabelFrame(root,text="Happy Endings",font=("brush script mt",17),fg="yellow",bg=bg_color)
    f7.place(x=660,y=400,width=341,height=260)

    sql="select * from desserts;"
    c.execute(sql)
    items=[]
    data=c.fetchall()
    desserts_name=[]
    desserts_price=[]
    for eachrow in data:
        desserts_name.append(eachrow[0])
        desserts_price.append(eachrow[1])

    lbl1=Label(f7,text="Item",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=0,sticky="w")
    lbl2=Label(f7,text="Price",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=1,sticky="w")
    lbl3=Label(f7,text="Qty",font=("times new roman",12,"bold"),bg=bg_color,fg="red").grid(row=0,column=2,padx=20,sticky="w")

    d_lbl=Label(f7,text=desserts_name[0],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=1,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[0],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=1,column=1,sticky="w")
    d1_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d1_txt.insert(0,"0")
    d1_txt.grid(row=1,column=2,padx=20)

    d_lbl=Label(f7,text=desserts_name[1],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=2,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[1],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=2,column=1,sticky="w")
    d2_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d2_txt.insert(0,"0")
    d2_txt.grid(row=2,column=2,padx=20)

    d_lbl=Label(f7,text=desserts_name[2],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=3,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[2],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=3,column=1,sticky="w")
    d3_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d3_txt.insert(0,"0")
    d3_txt.grid(row=3,column=2,padx=20)

    d_lbl=Label(f7,text=desserts_name[3],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=4,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[3],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=4,column=1,sticky="w")
    d4_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d4_txt.insert(0,"0")
    d4_txt.grid(row=4,column=2,padx=20)

    d_lbl=Label(f7,text=desserts_name[4],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=5,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[4],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=5,column=1,sticky="w")
    d5_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d5_txt.insert(0,"0")
    d5_txt.grid(row=5,column=2,padx=20)

    d_lbl=Label(f7,text=desserts_name[5],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=6,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[5],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=6,column=1,sticky="w")
    d6_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d6_txt.insert(0,"0")
    d6_txt.grid(row=6,column=2,padx=20)

    d_lbl=Label(f7,text=desserts_name[6],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=7,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[6],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=7,column=1,sticky="w")
    d7_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d7_txt.insert(0,"0")
    d7_txt.grid(row=7,column=2,padx=20)

    d_lbl=Label(f7,text=desserts_name[7],font=("times new roman",12),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=8,column=0,sticky="w")
    d_lbl=Label(f7,text=desserts_price[7],font=("times new roman",12,"bold"),bg=bg_color,fg="sky blue")
    d_lbl.grid(row=8,column=1,sticky="w")
    d8_txt=Entry(f7,width=5,font=("times new roman",11,"bold"))
    d8_txt.insert(0,"0")
    d8_txt.grid(row=8,column=2,padx=20)

    #=======Welcome Pane=======
    f9=LabelFrame(root,fg="black",bg='black',relief=RIDGE,bd=1)
    f9.place(x=1000,y=0,width=650,height=615)

    welcome_label=Label(f9,text="\n Welcome To \n FUSION FIESTA \n",font=("brush script mt",50),
                        bg=bg_color,fg="light green")
    welcome_label.grid(row=7,column=9)

    #===============Buttons===============
    lblPaidTax=Label(root,font=('times new roman',13,'bold'),text='Paid Tax',bg='powder blue',fg='black')
    lblPaidTax.place(x=1000,y=615)
    paid_tax= DoubleVar(root)
    txtPaidTax=Entry(root,state='readonly',textvariable=paid_tax,bg='white',font=('times new roman',13,'bold'),
                     width=8,justify=RIGHT)
    txtPaidTax.place(x=1075,y=615)

    lblSubTotal=Label(root,font=('times new roman',13,'bold'),text='Sub Total',bg='powder blue',fg='black')
    lblSubTotal.place(x=1160,y=615)
    sub_var = DoubleVar(root)
    txtSubTotal=Entry(root,state='readonly',textvariable=sub_var,bg='white',font=('times new roman',13,'bold'),
                      width=8,justify=RIGHT)
    txtSubTotal.place(x=1250,y=615)

    lblTotalCost=Label(root,font=('times new roman',13,'bold'),text='Total:',bg='powder blue',fg='black')
    lblTotalCost.place(x=1000,y=650)
    total_var=DoubleVar(root)
    txtTotalCost=Entry(root,bg='white',state='readonly',textvariable=total_var,fg="red",font=('times new roman',13,'bold'),
                       width=9,justify=RIGHT)
    txtTotalCost.place(x=1055,y=650)

    btnCalculate=Button(root,fg="navy blue",font=('times new roman',13,'bold'),text="Calculate",
                        bg="pink",width=12,command=calculate)
    btnCalculate.place(x=1160,y=650)

    btnExit=Button(root,fg="black",font=('times new roman',13,'bold'),text="Exit",bg="powder blue", command=Exit1)
    btnExit.place(x=1310,y=650)
    root.mainloop()

#=====Login form creation====
login=Tk()
login.title("Login>>")
login.minsize(width=350,height=150)
login.maxsize(width=350,height=150)
login.geometry("350x200")
login.configure(bg="black")

#===OPERATIONS FOR ADMIN=====
def admin_operations():
    con=mysql.connector.connect(host="localhost", user="root", passwd="mypassword",database="restaurant")
    cur=con.cursor()
    u=e1.get()
    p=e2.get()
    query="Select * from login where uid='{0}' and pass='{1}'".format(u,p)
    cur.execute(query)
    data1=cur.fetchone()
    nrec=cur.rowcount
    if nrec!=-1:
        login2=Tk()
        login2.title("Operations>>")
        login2.minsize(width=420,height=150)
        login2.maxsize(width=420,height=150)
        login2.geometry("420x150")
        login2.configure(bg="gray")
        l3=Label(login2,text="--Choose your operation--",font=("Arial",11,"bold"),bg="black",fg="white")
        l3.grid(row=1, column=2)
        b4=Button(login2,text="Add Item",font=("Arial",11,"bold"),padx=3,pady=3,bg="black",fg="white",command=add_item)
        b4.grid(row=2,column=1,padx=3,pady=3)
        b5=Button(login2,text="Delete Item",font=("Arial",11,"bold"),bg="black",fg="white",padx=3,pady=3,command=delete_item)
        b5.grid(row=2,column=2,padx=3,pady=3)
        b6=Button(login2,text="Update Item",font=("Arial",11,"bold"),bg="black",fg="white",padx=3,pady=3,command=update_item)
        b6.grid(row=2,column=3,padx=3,pady=3)
        b7=Button(login2,text="Search Item",font=("Arial",11,"bold"),bg="black",fg="white",padx=3,pady=3,command=search_item)
        b7.grid(row=3,column=1,padx=3,pady=3)
        b8=Button(login2,text="Customer Info",font=("Arial",11,"bold"),bg="black",fg="white",padx=3,pady=3,command=cust_info)
        b8.grid(row=3,column=3,padx=3,pady=3)
        b9=Button(login2,text="View All",font=("Arial",11,"bold"),bg="black",fg="white",padx=3,pady=3,command=view_all)
        b9.grid(row=3,column=2,padx=3,pady=3)
        b10=Button(login2,text="Employee Info",font=("Arial",11,"bold"),bg="black",fg="white",padx=3,pady=3,command=emp_info)
        b10.grid(row=4,column=2,padx=3,pady=3)
        b11=Button(login2,text="Exit",font=("Arial",11,"bold"),bg="black",fg="white",padx=3,pady=3,command=Exit)
        b11.grid(row=4,column=3,padx=3,pady=3)
    else:
        master = Tk()
        master.withdraw()
        MsgBox = messagebox.showerror('Invalid input','Either username or password is incorrect',icon = 'warning')
        
    con.close()
#=====LOGIN WINDOW FOR ADMIN======    
def admin():
    login1=Tk()
    login1.title("Admin>>")
    login1.minsize(width=400,height=200)
    login1.maxsize(width=400,height=200)
    login1.geometry("400x200")
    login1.configure(bg="black")
    
    l1=Label(login1,text="Enter Username",font=("Arial",10,"bold"),bg="gray",fg="white")
    l1.place(x=20,y=20)
    global e1
    e1=Entry(login1,width=25,font=(10))
    e1.place(x=150,y=20)

    l2=Label(login1,text="Enter Password",font=("Arial",10,"bold"),bg="gray",fg="white")
    l2.place(x=20,y=100)
    global e2
    e2=Entry(login1,width=25,font=(10),show="*")
    e2.place(x=150,y=100)

    b2=Button(login1,pady=6,fg="Red",font=('arial',10,'bold'),width=10,text="Login>>",bg="White", command=admin_operations)
    b2.place(x=150,y=150)

b3=Button(login,text="Admin",font=("Arial",16,"bold"),bg="gray",fg="black",command=admin)
b3.place(x=70,y=60)

b4=Button(login,text="Customer",font=("Arial",16,"bold"),bg="gray",fg="black", command=cust_window)
b4.place(x=170,y=60)




