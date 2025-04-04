from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter
import datetime
import tkinter as tk
from tkintermapview import TkinterMapView

def main():
    win=Tk()
    app=Choice(win)
    win.mainloop()

class Choice:
    def __init__(self,root):
        self.root=root
        self.root.title("CHOICE")
        self.root.geometry("2000x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\choice bg1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)



#=======================frame====================================================================================

        
        Framebutton1=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="RED")
        Framebutton1.place(x=300,y=420,width=455,height=57)

        Framebutton2=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="RED")
        Framebutton2.place(x=1100,y=420,width=455,height=57)

        btnAddData=Button(Framebutton1,command=self.manager,text="MANAGER",font=("arial",12,"bold"),width=42,bg="#3D405B",fg="WHITE")
        btnAddData.grid(row=0,column=1,sticky=W)

        btnAddData=Button(Framebutton2,command=self.driver,text="DRIVER",font=("arial",12,"bold"),width=42,bg="#3D405B",fg="WHITE")
        btnAddData.grid(row=0,column=3)


    def manager(self):
        self.new_window=Toplevel(self.root)
        self.app=Manager_Login_Window(self.new_window)


    def driver(self):
        self.new_window=Toplevel(self.root)
        self.app=DriverLogin_Window(self.new_window)

#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================

class InsideManager:
    def __init__(self,root):
        self.root=root
        self.root.title("MANAGER")
        self.root.geometry("1980x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\main menu bg3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)



#=======================frame====================================================================================

        
        Framebutton1=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="blue")
        Framebutton1.place(x=750,y=250,width=455,height=57)

        Framebutton2=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="yellow")
        Framebutton2.place(x=750,y=350,width=455,height=57)

        Framebutton3=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="red")
        Framebutton3.place(x=750,y=450,width=455,height=57)

        Framebutton4=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="green")
        Framebutton4.place(x=750,y=550,width=455,height=57)

        Framebutton5=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="#2F3651")
        Framebutton5.place(x=750,y=650,width=455,height=57)

        btnAddData=Button(Framebutton1,command=self.map,text="PARKING SPOTS NEAR YOU",font=("arial",12,"bold"),width=42,bg="#3C3D50",fg="white")
        btnAddData.grid(row=0,column=1,sticky=W)

        btnAddData=Button(Framebutton2,command=self.bookspot,text="BOOK YOUR SPOT",font=("arial",12,"bold"),width=42,bg="#46332E",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton3,command=self.membership,text="MEMBERSHIP DETAILS",font=("arial",12,"bold"),width=42,bg="#9A7CF8",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton4,command=self.complaint,text="FILE A COMPLAINT",font=("arial",12,"bold"),width=42,bg="#2F3651",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton5,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=42,bg="#2A86FF",fg="white")
        btnAddData.grid(row=0,column=3)


    def map(self):
        self.new_window=Toplevel(self.root)
        self.app=Map(self.new_window)

    def bookspot(self):
        self.new_window=Toplevel(self.root)
        self.app=Book(self.new_window)

    def membership(self):
        self.new_window=Toplevel(self.root)
        self.app=Membership_Plan(self.new_window)

    def complaint(self):
        self.new_window=Toplevel(self.root)
        self.app=FileComplaint(self.new_window)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("conform","Do you want to exit from the main menu")
        if iExit>0:
            self.root.destroy()


#======================================================================

class Book:
    def __init__(self,root):
        self.root=root
        self.root.title("SLOT BOOKING")
        self.root.geometry("1910x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\SLOT BOOKING BG.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#83bbc8")
        frame.place(x=650,y=250,width=535,height=280)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#355070",fg="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=470,height=240)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=5,column=1)

       
               #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="blue")
        Framebutton.place(x=770,y=550,width=285,height=57)

        btnAddData=Button(Framebutton,command=self.adda_data,text="BOOK SLOT",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        FrameDetails.place(x=0,y=1800,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_data()
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")

        #==================================================================
        root_tk=tk.Tk()
class Map:
    def __init__(self,root_tk):
        self.root_tk=root_tk



        gmap_widget = TkinterMapView(root_tk, width=750, height=600)
        gmap_widget.pack(fill="both", expand=True)

        gmap_widget.set_tile_server("https://tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=22)
        gmap_widget.set_address("19.1201068 72.9975504", marker=True)
        gmap_widget.set_address("ghansoli station", marker=True)
        gmap_widget.set_address("19.1232859 72.9946452", marker=True)
        gmap_widget.set_address("grand plaza ghansoli", marker=True)
        gmap_widget.set_zoom(16)

        Framebutton2=Frame(self.root_tk,bd=5,relief=RIDGE,padx=0,bg="blue")
        Framebutton2.place(x=550,y=850,width=240,height=43)

        btnAddData=Button(Framebutton2,command=self.bookspot,text="BOOK YOUR SPOT",font=("arial",12,"bold"),width=22,bg="orange",fg="white")
        btnAddData.grid(row=0,column=3)


        root_tk.title("Country Lookup")
        root_tk.geometry("1800x900+0+0")
        root_tk.resizable(False, False)
        root_tk.mainloop()

        

    def bookspot(self):
        self.new_window=Toplevel(self.root_tk)
        self.app=Book(self.new_window)
                

#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================

class Book:
    def __init__(self,root):
        self.root=root
        self.root.title("SLOT BOOKING")
        self.root.geometry("1910x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\SLOT BOOKING BG.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        #===================variable=======================================

        self.location_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.slotno_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#83bbc8")
        frame.place(x=250,y=250,width=1415,height=305)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#355070",fg="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=890,height=270)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblPayment_mode=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Location :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPayment_mode.grid(row=2,column=2,sticky=W)

        comPayment_mode=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.location_var,width=24,state="readonly")
        comPayment_mode["value"]=("Grand Plaza,Ghansoli","SMT.Indira Gandhi College,Ghansoli","Ghansoli village","Ghansoli Railway Station")
        comPayment_mode.grid(row=2,column=3)

        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Slot no :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)

        comv_no=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.slotno_var,width=24,state="readonly")
        comv_no["value"]=[str(i) for i in range(1, 101)]
        comv_no.grid(row=3,column=3)

        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)

        comv_no=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.vehicletype_var,width=24,state="readonly")
        comv_no["value"]=("🏍","🛺","🚗","🚛","🛒")
        comv_no.grid(row=4,column=3)

        #==================================================================================================================================

        DataFrameRight=LabelFrame(frame,text="SLOT",bg="#355070",fg="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=900,y=5,width=450,height=270)
       
               #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="blue")
        Framebutton.place(x=310,y=580,width=1303,height=57)

        btnAddData=Button(Framebutton,command=self.add_data,text="BOOK SLOT",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)


        btnAdd=Button(Framebutton,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        btnAdd.grid(row=0,column=1,padx=1)

        btnUpdate=Button(Framebutton,command=self.update,text="UPDATE",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        btnUpdate.grid(row=0,column=2,padx=1)

        #btnDelete=Button(Framebutton,command=self.delete,text="DELETE",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        #btnDelete.grid(row=0,column=3,padx=1)

        btnReset=Button(Framebutton,command=self.reset_data,text="RESET",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        btnReset.grid(row=0,column=3,padx=1)

        btnAddData=Button(Framebutton,text="SLOT",command=self.update_statusss,font=("arial",12,"bold"),width=22,bg="#2F3651",fg="white")
        btnAddData.grid(row=0,column=4,padx=1)

        #========================count=====================================================

            
        # Create a label to display the row count
        frame=LabelFrame(frame,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        frame.place(x=1490,y=5,width=278,height=350)

        l=Label(frame,bg="#48416C",fg="cyan2",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30,pady=-30)
        l.grid(row=4,column=2)


        self.table_frame = Frame(self.root,bd=5,bg="#355070")
        self.table_frame.place(x=1200,y=285,width=420,height=230)


        #============tabel frame search system=====

        Table_Frame=LabelFrame(self.root,bd=2,text="show room details",relief=RIDGE)
        Table_Frame.place(x=0,y=2800,width=1630,height=195)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_Frame,column=("slotno","firstname","lastname","vehiclenumber","vehiclename","mobile","location","vehicletype",))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("firstname",text="First Name")
        self.room_table.heading("lastname",text="Last Name")
        self.room_table.heading("vehiclenumber",text="Vehicle Number")
        self.room_table.heading("vehiclename",text="Vehicle Name")
        self.room_table.heading("mobile",text="Mobile")
        self.room_table.heading("vehicletype",text="Vehicle Type")
        self.room_table.heading("slotno",text="Slot No")
        self.room_table.heading("location",text="Location")

        self.room_table["show"]="headings"

        self.room_table.column("firstname",width=100)
        self.room_table.column("lastname",width=100)
        self.room_table.column("vehiclenumber",width=100)
        self.room_table.column("vehiclename",width=100)
        self.room_table.column("mobile",width=100)
        self.room_table.column("vehicletype",width=100)
        self.room_table.column("slotno",width=10)
        self.room_table.column("location",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        

        #=====================information frame================



    def add_data(self):
        if self.slotno_var.get()=="" or self.vehicletype_var.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.slotno_var.get(),
                                                                                            self.firstname_var.get(),
                                                                                            self.lastname_var.get(),
                                                                                            self.vehiclenumber_var.get(),
                                                                                            self.vehiclename_var.get(),
                                                                                            self.mobile_var.get(),
                                                                                            self.location_var.get(),
                                                                                            self.vehicletype_var.get(),
                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", f"Slot [{self.slotno_var.get()}] at [{self.location_var.get()}] BOOKED SUCCESSFULLY for Vehicle Number [{self.vehiclenumber_var.get()}]!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","THIS SLOT IS ALREADY BOOKED BY THE OTHER USER! Please Book Another SLOT.",parent=self.root)

    def update(self):
        if self.slotno_var.get()=="":
            messagebox.showerror("Error","Please enter SLOT NUMBER",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set First_Name=%s,Last_Name=%s,Vehicle_Name=%s,Mobile=%s,Location=%s,Slot_No=%s where Vehicle_Number=%s",(
                                                                                            self.slotno_var.get(),
                                                                                            self.firstname_var.get(),
                                                                                            self.lastname_var.get(),
                                                                                            self.vehiclenumber_var.get(),
                                                                                            self.vehiclename_var.get(),
                                                                                            self.mobile_var.get(),
                                                                                            self.location_var.get(),
                                                                                            self.vehicletype_var.get(),
                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New room details has been updated",parent=self.root)

        

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.vehicletype_var.set(row[4]),
        self.slotno_var.set(row[5]),
        self.location_var.set(row[6]),
        self.mobile_var.set(row[7]),
        

    
        

    def reset_data(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.vehicletype_var.set(""),
        self.slotno_var.set(""),
        self.location_var.set(""),
        self.mobile_var.set(""),
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")

#====================================================================================================================================================================================
#====================================================================================================================================================================================
#====================================================================================================================================================================================
#=============================================================================================================================

    def create_database(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()

        

    def update_status(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        self.display_table()
        slot_id = self.slotno_var.get()
        status = self.vehicletype_var.get()
        my_cursor.execute('UPDATE slots_table SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
        conn.commit()
        self.display_table()

    def display_table(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{slot_id}:{ slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)

    def display_tablee(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table2 ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{slot_id}:{slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)

    def display_tableee(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table3 ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{slot_id}:{slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)

    def display_tableeee(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table4 ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{ slot_id}:{slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)



    def update_statusss(self):
        if self.location_var.get()=="Grand Plaza,Ghansoli":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_table()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table SET slot_status =  %s WHERE slot_id =  %s', (status, slot_id))
            conn.commit()
            self.display_table()

        elif self.location_var.get()=="SMT.Indira Gandhi College,Ghansoli":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_tablee()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table2 SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
            conn.commit()
            self.display_tablee()

        elif self.location_var.get()=="Ghansoli village":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_tableee()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table3 SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
            conn.commit()
            self.display_tableee()

        elif self.location_var.get()=="Ghansoli Railway Station":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_tableeee()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table4 SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
            conn.commit()
            self.display_tableeee()


        else :
            messagebox.showerror("Error","First Select the Location")


 #==================================================================
       



#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================


class Manager_Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1995x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\bg1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=810,y=230,width=340,height=400)

        img1=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\user logo.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=120,y=5,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


            #========Icon Images========

        img2=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\user logo small.png")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(frame,image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=43,y=153,width=25,height=25)


        img3=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\passsword logo.png")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(frame,image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=43,y=223,width=25,height=25)

        #loginButton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text=">New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=350,width=160)

        #forgetpassbtn
        registerbtn=Button(frame,text=">Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=00,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Parkometer(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

            #==============================reset Password Window============

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)

        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)

        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)

            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)

                self.root2.destroy()
                

            #==============================forgetPassword Window====================


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="white",bg="black")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),fg="White",bg="green")
                btn.place(x=100,y=290)
                    

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #========varibleas=========

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #=============bg image============

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\bg3.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===============left image===========

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\bg4.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=120,width=470,height=550)

        #=============main Frame==========

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=120,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="blue")
        register_lbl.place(x=20,y=20)


        #===========label and entry===========

        #----------row 1

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #==========row2===

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #=========row3=========

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        #================row4=============

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #===============checkbutton================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #============buttons==================

        img=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\register now button.png")
        img=img.resize((600,50))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\login now button.png")
        img1=img1.resize((600,50))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=133,y=420,width=200)


        #=========function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")


    def return_login(self):
        self.root.destroy()



class ParkingManagementSystem:
    def _init_(self,root):
        self.root=root
        self.root.title("Parking Management System")
        self.root.geometry("1630x800+0+0")


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()






        

        lbltitle=Label(self.root,text="PARKING MANAGEMENT SYSTEM",bg="maroon",fg="cyan2",bd=20,relief=RIDGE,font=("Foobar Pro",50),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="RosyBrown1")
        frame.place(x=0,y=130,width=1630,height=400)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="tan1",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1000,height=350)

        lblMember=Label(DataFrameLeft,bg="tan1",text="🟈 Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=24,state="readonly")
        comMember["value"]=("New","Existing")
        comMember.grid(row=0,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)

        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Bill Amount :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=7,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.billamount_var,width=29)
        txtv_no.grid(row=7,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=0,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=0,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parking Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingtime_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parkoff Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkofftime_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Slot Status :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotstatus_var,width=29)
        txtv_no.grid(row=5,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=6,column=3)


        lblPayment_mode=Label(DataFrameLeft,bg="tan1",text="🟈 Payment Mode",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPayment_mode.grid(row=7,column=2,sticky=W)

        comPayment_mode=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.paymentmode_var,width=24,state="readonly")
        comPayment_mode["value"]=("Cash","Online")
        comPayment_mode.grid(row=7,column=3)

        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="VEHICLE INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameRight.place(x=1020,y=5,width=550,height=350)

        self.txtBox=Text(DataFrameRight, font=("Courier new",12,"bold"),width=30,height=15,padx=3,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['▷ TWO WHEELER','▷ FOUR WHEELER','▷ CYCLE','▷ GOODS CARRIER','▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="▷ TWO WHEELER"):
                self.charges_var.set("Rs 30/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("TWO WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ THREE WHEELER"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ FOUR WHEELER"):
                self.charges_var.set("Rs 70/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x60 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ CYCLE"):
                self.charges_var.set("Rs 10/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("20x20 sq.m")
                self.vehicletype_var.set("CYCLE")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1630,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=25,bg="#FF8674",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=25,bg="#6CD300",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=25,bg="#0AFFFF",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=25,bg="#2C3539",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=25,bg="#B87333",fg="white")
        btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light yellow")
        FrameDetails.place(x=0,y=600,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_data()
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")



#====================================================================================================================================================================================================
#==========================================================================================================================================================================================
#==========================================================================================================================================================================================
#======================================================================================================================================================================================

class DriverLogin_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1995x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\bg1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=810,y=230,width=340,height=400)

        img1=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\user logo.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=120,y=5,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=100,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


            #========Icon Images========

        img2=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\user logo small.png")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(frame,image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=43,y=153,width=25,height=25)


        img3=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\passsword logo.png")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(frame,image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=43,y=223,width=25,height=25)

        #loginButton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text=">New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=350,width=160)

        #forgetpassbtn
        registerbtn=Button(frame,text=">Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=00,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=InsideManager(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

            #==============================reset Password Window============

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)

        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)

        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)

            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)

                self.root2.destroy()
                

            #==============================forgetPassword Window====================


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="white",bg="black")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),fg="White",bg="green")
                btn.place(x=100,y=290)
                    

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1980x1000+0+0")

        #========varibleas=========

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #=============bg image============

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\bg3.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===============left image===========

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\bg4.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=120,width=470,height=550)

        #=============main Frame==========

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=120,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="blue")
        register_lbl.place(x=20,y=20)


        #===========label and entry===========

        #----------row 1

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #==========row2===

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #=========row3=========

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        #================row4=============

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #===============checkbutton================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #============buttons==================

        img=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\register now button.png")
        img=img.resize((600,50))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=60,y=460,width=200)

        img1=Image.open(r"C:\Users\Admin\OneDrive\Desktop\New folder\login now button.png")
        img1=img1.resize((600,50))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=343,y=460,width=200)


        #=========function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")


    def return_login(self):
        self.root.destroy()



class ParkingManagementSystem:
    def _init_(self,root):
        self.root=root
        self.root.title("Parking Management System")
        self.root.geometry("1630x800+0+0")


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()






        

        lbltitle=Label(self.root,text="PARKING MANAGEMENT SYSTEM",bg="maroon",fg="cyan2",bd=20,relief=RIDGE,font=("Foobar Pro",50),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="RosyBrown1")
        frame.place(x=0,y=130,width=1630,height=400)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="tan1",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1000,height=350)

        lblMember=Label(DataFrameLeft,bg="tan1",text="🟈 Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=24,state="readonly")
        comMember["value"]=("New","Existing")
        comMember.grid(row=0,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)

        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Bill Amount :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=7,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.billamount_var,width=29)
        txtv_no.grid(row=7,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=0,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=0,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parking Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingtime_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parkoff Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkofftime_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Slot Status :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotstatus_var,width=29)
        txtv_no.grid(row=5,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=6,column=3)


        lblPayment_mode=Label(DataFrameLeft,bg="tan1",text="🟈 Payment Mode",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPayment_mode.grid(row=7,column=2,sticky=W)

        comPayment_mode=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.paymentmode_var,width=24,state="readonly")
        comPayment_mode["value"]=("Cash","Online")
        comPayment_mode.grid(row=7,column=3)

        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="VEHICLE INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameRight.place(x=1020,y=5,width=550,height=350)

        self.txtBox=Text(DataFrameRight, font=("Courier new",12,"bold"),width=30,height=15,padx=3,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['▷ TWO WHEELER','▷ FOUR WHEELER','▷ CYCLE','▷ GOODS CARRIER','▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="▷ TWO WHEELER"):
                self.charges_var.set("Rs 30/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("TWO WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ THREE WHEELER"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ FOUR WHEELER"):
                self.charges_var.set("Rs 70/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x60 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ CYCLE"):
                self.charges_var.set("Rs 10/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("20x20 sq.m")
                self.vehicletype_var.set("CYCLE")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1630,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=25,bg="#FF8674",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=25,bg="#6CD300",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=25,bg="#0AFFFF",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=25,bg="#2C3539",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=25,bg="#B87333",fg="white")
        btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light yellow")
        FrameDetails.place(x=0,y=600,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_data()
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")


                
           
                

#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================


class ComplaintFile:
    def __init__(self,root):
        self.root=root
        self.root.title("Parking Management System")
        self.root.geometry("2000x1000+0+0")

        self.selected_slot = tk.StringVar()
        self.slot_status_var = tk.StringVar(value='Available')

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\parkometer.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()






        

        

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="#07161B")
        frame.place(x=50,y=130,width=1815,height=385)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#3d737f",fg="#CEC7BF",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameLeft.place(x=10,y=5,width=890,height=350)

        lblMember=Label(DataFrameLeft,bg="tan1",text="🟈 Slot NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.selected_slot,font=("times new roman",15,"bold"),width=24,state="readonly")
        comMember["value"]=[str(i) for i in range(1, 101)]
        comMember.grid(row=0,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)

        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Bill Amount :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=7,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.billamount_var,width=29)
        txtv_no.grid(row=7,column=1)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=0,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=0,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parking Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingtime_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parkoff Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkofftime_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Slot Status :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotstatus_var,width=29)
        txtv_no.grid(row=5,column=3)


        lblv_no=Label(DataFrameLeft,bg="tan1",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=6,column=3)


        lblPayment_mode=Label(DataFrameLeft,bg="tan1",text="🟈 Slot Pic",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPayment_mode.grid(row=7,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slot_status_var,width=29)
        txtv_no.grid(row=7,column=3)

         
        

        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="VEHICLE INFORMATION",bg="#3d737f",fg="#CEC7BF",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameRight.place(x=905,y=5,width=490,height=350)

        self.txtBox=Text(DataFrameRight, font=("Courier new",12,"bold"),width=30,height=15,padx=3,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['▷ TWO WHEELER','▷ FOUR WHEELER','▷ CYCLE','▷ GOODS CARRIER','▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="▷ TWO WHEELER"):
                self.charges_var.set("Rs 30/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("TWO WHEELER")
                self.slot_status_var.set("🏍")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ THREE WHEELER"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")
                self.slot_status_var.set("🛺")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ FOUR WHEELER"):
                self.charges_var.set("Rs 70/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x60 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")
                self.slot_status_var.set("🚗")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ CYCLE"):
                self.charges_var.set("Rs 10/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("20x20 sq.m")
                self.vehicletype_var.set("CYCLE")
                self.slot_status_var.set("🚲")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                self.slot_status_var.set("🚛")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")
                self.slot_status_var.set("🛒")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",10,"bold"),width=18,height=18)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listVehicles:
            listBox.insert(END,item)

        #========================count=====================================================

            
        # Create a label to display the row count
        frame=LabelFrame(frame,bd=12,relief=RIDGE,padx=20,bg="#3d737f")
        frame.place(x=1452,y=5,width=278,height=105)

        l=Label(frame,bg="#3d737f",fg="WHITE",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30,pady=-30)
        l.grid(row=4,column=2)


        self.table_frame = Frame(self.root,bd=5,bg="#3d737f")
        self.table_frame.place(x=1460,y=280,width=390,height=215)

        

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton.place(x=50,y=530,width=1804,height=57)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=22,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=21,bg="#FF8674",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=21,bg="#6CD300",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=21,bg="#0AFFFF",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=21,bg="#2C3539",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=21,bg="#B87333",fg="white")
        btnAddData.grid(row=0,column=5)

        btnAddData=Button(Framebutton,text="Members",command=self.allmembers,font=("arial",12,"bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=6)

        btnAddData=Button(Framebutton,text="Slot",command=self.update_status,font=("arial",12,"bold"),width=22,bg="black",fg="white")
        btnAddData.grid(row=0,column=7)

        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="#07161B")
        FrameDetails.place(x=250,y=610,width=1455,height=255)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1430,height=230)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="SLOT PIC")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        

        
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        my_cursor.execute('select COUNT(*) from vehicle')
        count = my_cursor.fetchone()[0]
        # Update the label to display the count
        frame=Frame(self.root,relief=RIDGE,padx=14,bg="#3d737f")
        frame.place(x=1532,y=159,width=240,height=75)
        frame1=LabelFrame(frame,bd=0,relief=RIDGE,padx=20,bg="#48416C")
        frame1.place(x=1580,y=5,width=278,height=350)
        l=Label(frame,bg="#3d737f",fg="WHITE",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30)
        l.grid(row=1,column=1,sticky=W)
        l.config(text=f'  {  100 - count  }  ')
        # Close the database connection
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_data()
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            my_cursor.execute('select COUNT(*) from vehicle')
            count = my_cursor.fetchone()[0]
            # Update the label to display the count
            frame=Frame(self.root,relief=RIDGE,padx=14,bg="#3d737f")
            frame.place(x=1532,y=159,width=240,height=75)
            frame1=LabelFrame(frame,bd=12,relief=RIDGE,padx=20,bg="#48416C")
            frame1.place(x=1580,y=5,width=278,height=350)
            l=Label(frame,bg="#3d737f",fg="WHITE",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30)
            l.grid(row=1,column=1,sticky=W)
            l.config(text=f'  {  100 - count  }  ')
            conn.close()

            messagebox.showinfo("Success","DELETED!!")

    def allmembers(self):
        self.new_window=Toplevel(self.root)
        self.app=NewMembers(self.new_window)


#=============================================================================================================================================================
#=============================================================================================================================================================
#===============================================================slot==========================================================================================


            


    def create_database(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()

        

    def update_status(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        slot_id = int(self.selected_slot.get())
        status = self.slot_status_var.get()
        my_cursor.execute('UPDATE slots_table SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
        conn.commit()
        self.display_table()

    def display_table(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#48416C",fg="white" ,text=f'{slot_id}:{slot_status}',font=("times new roman",11), padx=00, pady=00)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)



#==============================member window=================================
#==============================member window=================================
#==============================member window=================================
#==============================member window=================================
#==============================member window=================================

class NewMembers:
    def __init__(self,root):
        self.root=root
        self.root.title("Parking Management System")
        self.root.geometry("1930x1200+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\manager login bg3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()






        

        

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=10,bg="#48416C")
        frame.place(x=480,y=170,width=950,height=310)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#0AAFFF",fg="yellow",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=270)



        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Total Duration :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.paymentmode_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=5,column=3)


        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="VEHICLE INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameRight.place(x=11020,y=5,width=550,height=350)

        self.txtBox=Text(DataFrameRight, font=("Courier new",12,"bold"),width=30,height=15,padx=3,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['▷ TWO WHEELER','▷ FOUR WHEELER','▷ CYCLE','▷ GOODS CARRIER','▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="▷ TWO WHEELER"):
                self.charges_var.set("Rs 30/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("TWO WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ THREE WHEELER"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ FOUR WHEELER"):
                self.charges_var.set("Rs 70/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x60 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ CYCLE"):
                self.charges_var.set("Rs 10/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("20x20 sq.m")
                self.vehicletype_var.set("CYCLE")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=3,pady=1,bg="powder blue")
        Framebutton.place(x=450,y=500,width=1010,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=16,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=15,bg="#FF8674",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=15,bg="#6CD300",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=15,bg="#0AFFFF",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=15,bg="#2C3539",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=16,bg="#B87333",fg="white")
        btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

#=====================information frame================


        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="#48416C")
        FrameDetails.place(x=450,y=590,width=1010,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=0,width=985,height=170)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","vehicletype","parkingdate","charges","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("paymentmode",text="TOTAL DURATION")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("paymentmode",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotarea",width=100)
        

        self.fatch_dataTwo()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursorTwo)



        

#======================================================================================================================================================

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_dataTwo(),
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_dataTwo(),
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        


    def fatch_dataTwo(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    def get_cursorTwo(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.vehicletype_var.set(row[6]),
        self.parkingdate_var.set(row[7]),
        self.charges_var.set(row[8]),
        self.slotarea_var.set(row[9]),
        self.paymentmode_var.set(row[10]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_dataTwo()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")



#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================

class FileComplaint:
    def __init__(self,root):
        self.root=root
        self.root.title("SLOT BOOKING")
        self.root.geometry("1910x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\complaint bg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#436372")
        frame.place(x=650,y=200,width=535,height=340)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="FILL YOUR INFORMATION",bg="#fcd7b6",fg="maroon",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=470,height=300)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=5,column=1)

        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Complaint :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.billamount_var,width=29)
        txtv_no.grid(row=6,column=1)

       
               #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="powder blue")
        Framebutton.place(x=770,y=580,width=285,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="REGISTER COMPLAINT",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        FrameDetails.place(x=0,y=1800,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Your Complaint Has been Registered successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_data()
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")


#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================
#==========================================================================================================================================================================================================================================

class Parkometer:
    def __init__(self,root):
        self.root=root
        self.root.title("Parking Management System")
        self.root.geometry("2000x1000+0+0")

        self.selected_slot = tk.StringVar()
        self.slot_status_var = tk.StringVar(value='Available')

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\parkometer.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()






        

        

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="#07161B")
        frame.place(x=50,y=130,width=1815,height=385)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#3d737f",fg="#CEC7BF",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameLeft.place(x=10,y=5,width=890,height=350)

        lblMember=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Slot NO.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.selected_slot,font=("times new roman",15,"bold"),width=24,state="readonly")
        comMember["value"]=[str(i) for i in range(1, 101)]
        comMember.grid(row=0,column=1)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)

        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Bill Amount :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=7,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.billamount_var,width=29)
        txtv_no.grid(row=7,column=1)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=0,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=0,column=3)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Parking Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingtime_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Parkoff Time :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkofftime_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Slot Status :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotstatus_var,width=29)
        txtv_no.grid(row=5,column=3)


        lblv_no=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=6,column=3)


        lblPayment_mode=Label(DataFrameLeft,bg="#3d737f",fg="#EDC18D",text="🟈 Slot Pic",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPayment_mode.grid(row=7,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slot_status_var,width=29)
        txtv_no.grid(row=7,column=3)

         
        

        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="VEHICLE INFORMATION",bg="#3d737f",fg="#CEC7BF",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameRight.place(x=905,y=5,width=490,height=350)

        self.txtBox=Text(DataFrameRight, font=("Courier new",12,"bold"),width=30,height=15,padx=3,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['▷ TWO WHEELER','▷ FOUR WHEELER','▷ CYCLE','▷ GOODS CARRIER','▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="▷ TWO WHEELER"):
                self.charges_var.set("Rs 30/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("TWO WHEELER")
                self.slot_status_var.set("🏍")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ THREE WHEELER"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")
                self.slot_status_var.set("🛺")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ FOUR WHEELER"):
                self.charges_var.set("Rs 70/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x60 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")
                self.slot_status_var.set("🚗")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ CYCLE"):
                self.charges_var.set("Rs 10/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("20x20 sq.m")
                self.vehicletype_var.set("CYCLE")
                self.slot_status_var.set("🚲")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                self.slot_status_var.set("🚛")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")
                self.slot_status_var.set("🛒")

                d1=datetime.date.today()
                d2=datetime.datetime.today().strftime("%H:%M:%S")
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",10,"bold"),width=18,height=18)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listVehicles:
            listBox.insert(END,item)

        #========================count=====================================================

            
        # Create a label to display the row count
        frame=LabelFrame(frame,bd=12,relief=RIDGE,padx=20,bg="#3d737f")
        frame.place(x=1452,y=5,width=278,height=105)

        l=Label(frame,bg="#3d737f",fg="WHITE",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30,pady=-30)
        l.grid(row=4,column=2)


        self.table_frame = Frame(self.root,bd=5,bg="#07161B")
        self.table_frame.place(x=1460,y=280,width=390,height=215)

        

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton.place(x=50,y=530,width=1804,height=57)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=29,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=29,bg="#FF8674",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=28,bg="#6CD300",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=28,bg="#0AFFFF",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=29,bg="#2C3539",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=29,bg="#B87333",fg="white")
        btnAddData.grid(row=0,column=5)

        Framebutton1=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton1.place(x=1520,y=610,width=285,height=160)

        btnAddData=Button(Framebutton1,text="Members",command=self.allmembers,font=("arial",13,"bold"),width=25,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton1,text="Slot Availability",command=self.update_status,font=("arial",13,"bold"),width=25,bg="black",fg="white")
        btnAddData.grid(row=1,column=0)

        btnAddData=Button(Framebutton1,text="Complaints",command=self.cuscomplaint,font=("arial",13,"bold"),width=25,bg="#FF8674",fg="white")
        btnAddData.grid(row=2,column=0)

        btnAddData=Button(Framebutton1,text="Slot Bookings",command=self.slotbookingss,font=("arial",13,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=3,column=0)


        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="#07161B")
        FrameDetails.place(x=50,y=610,width=1455,height=255)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1430,height=230)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="SLOT PIC")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        

        
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        my_cursor.execute('select COUNT(*) from vehicle')
        count = my_cursor.fetchone()[0]
        # Update the label to display the count
        frame=Frame(self.root,relief=RIDGE,padx=14,bg="#3d737f")
        frame.place(x=1532,y=159,width=240,height=75)
        frame1=LabelFrame(frame,bd=0,relief=RIDGE,padx=20,bg="#48416C")
        frame1.place(x=1580,y=5,width=278,height=350)
        l=Label(frame,bg="#3d737f",fg="WHITE",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30)
        l.grid(row=1,column=1,sticky=W)
        l.config(text=f'  {  100 - count  }  ')
        # Close the database connection
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_data()
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            my_cursor.execute('select COUNT(*) from vehicle')
            count = my_cursor.fetchone()[0]
            # Update the label to display the count
            frame=Frame(self.root,relief=RIDGE,padx=14,bg="#3d737f")
            frame.place(x=1532,y=159,width=240,height=75)
            frame1=LabelFrame(frame,bd=12,relief=RIDGE,padx=20,bg="#48416C")
            frame1.place(x=1580,y=5,width=278,height=350)
            l=Label(frame,bg="#3d737f",fg="WHITE",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30)
            l.grid(row=1,column=1,sticky=W)
            l.config(text=f'  {  100 - count  }  ')
            messagebox.showinfo("Success","DELETED!!")
            conn.close()


            

    def allmembers(self):
        self.new_window=Toplevel(self.root)
        self.app=NewMembers(self.new_window)

    def cuscomplaint(self):
        self.new_window=Toplevel(self.root)
        self.app=CustomerComplaint(self.new_window)

    def slotbookingss(self):
        self.new_window=Toplevel(self.root)
        self.app=BookingsSlot(self.new_window)


        


#=============================================================================================================================================================
#=============================================================================================================================================================
#===============================================================slot==========================================================================================


            


    def create_database(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()

        

    def update_status(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        self.display_table()
        
        slot_id = self.selected_slot.get()
        status = self.slot_status_var.get()
        my_cursor.execute('UPDATE slots_table SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
        conn.commit()
        self.display_table()

    def display_table(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#07161B",fg="white" ,text=f'{slot_id}:{slot_status}',font=("times new roman",11), padx=00, pady=00)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)



#==============================member window=================================
#==============================member window=================================
#==============================member window=================================
#==============================member window=================================
#==============================member window=================================

class NewMembers:
    def __init__(self,root):
        self.root=root
        self.root.title("Parking Management System")
        self.root.geometry("1930x1200+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\manager login bg3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()






        

        

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=10,bg="#48416C")
        frame.place(x=480,y=170,width=950,height=310)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#0AAFFF",fg="yellow",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=270)



        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Total Duration :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.paymentmode_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=5,column=3)


        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="VEHICLE INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Display",12,"bold"))
        DataFrameRight.place(x=11020,y=5,width=550,height=350)

        self.txtBox=Text(DataFrameRight, font=("Courier new",12,"bold"),width=30,height=15,padx=3,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['▷ TWO WHEELER','▷ FOUR WHEELER','▷ CYCLE','▷ GOODS CARRIER','▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="▷ TWO WHEELER"):
                self.charges_var.set("Rs 30/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("TWO WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ THREE WHEELER"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ FOUR WHEELER"):
                self.charges_var.set("Rs 70/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x60 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="▷ CYCLE"):
                self.charges_var.set("Rs 10/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("20x20 sq.m")
                self.vehicletype_var.set("CYCLE")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=3,pady=1,bg="powder blue")
        Framebutton.place(x=450,y=500,width=1010,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=16,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=15,bg="#FF8674",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=15,bg="#6CD300",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=15,bg="#0AFFFF",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=15,bg="#2C3539",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=16,bg="#B87333",fg="white")
        btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

#=====================information frame================


        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="#48416C")
        FrameDetails.place(x=450,y=590,width=1010,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=0,width=985,height=170)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","vehicletype","parkingdate","charges","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("paymentmode",text="TOTAL DURATION")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("paymentmode",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotarea",width=100)
        

        self.fatch_dataTwo()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursorTwo)



        

#======================================================================================================================================================

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),                                                                           
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),                                                                           
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_dataTwo(),
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_dataTwo(),
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        


    def fatch_dataTwo(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    def get_cursorTwo(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[11]),
        self.vehicletype_var.set(row[6]),
        self.parkingtime_var.set(row[12]),
        self.parkofftime_var.set(row[13]),
        self.parkingdate_var.set(row[7]),
        self.charges_var.set(row[8]),
        self.slotstatus_var.set(row[14]),
        self.slotarea_var.set(row[9]),
        self.paymentmode_var.set(row[10]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_dataTwo()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")



#===============================================================================================================================================================================================
#=====================================================================================================================================================================================================
#=====================================================================================================================================================================================================

class BookingsSlot:
    def __init__(self,root):
        self.root=root
        self.root.title("SLOT BOOKING")
        self.root.geometry("1910x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\SLOT BOOKING BG.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        #===================variable=======================================

        self.location_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.slotno_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#83bbc8")
        frame.place(x=250,y=5250,width=1415,height=305)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#355070",fg="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=890,height=270)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblPayment_mode=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Location :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPayment_mode.grid(row=2,column=2,sticky=W)

        comPayment_mode=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.location_var,width=24,state="readonly")
        comPayment_mode["value"]=("Grand Plaza,Ghansoli","SMT.Indira Gandhi College,Ghansoli","Ghansoli village","Ghansoli Railway Station")
        comPayment_mode.grid(row=2,column=3)

        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Slot no :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)

        comv_no=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.slotno_var,width=24,state="readonly")
        comv_no["value"]=[str(i) for i in range(1, 101)]
        comv_no.grid(row=3,column=3)

        lblv_no=Label(DataFrameLeft,bg="#355070",fg="white",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)

        comv_no=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.vehicletype_var,width=24,state="readonly")
        comv_no["value"]=("🏍","🛺","🚗","🚛","🛒")
        comv_no.grid(row=4,column=3)

        #==================================================================================================================================

        DataFrameRight=LabelFrame(frame,text="SLOT",bg="#355070",fg="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=900,y=5555,width=450,height=270)
       
               #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="blue")
        Framebutton.place(x=670,y=580,width=548,height=57)

        #btnAddData=Button(Framebutton,command=self.add_data,text="BOOK SLOT",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        #btnAddData.grid(row=0,column=0,sticky=W)


        btnAdd=Button(Framebutton,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        btnAdd.grid(row=0,column=0,padx=1)

        #btnUpdate=Button(Framebutton,command=self.update,text="UPDATE",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        #btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(Framebutton,command=self.delete,text="DELETE",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        btnDelete.grid(row=0,column=1,padx=1)

        #btnReset=Button(Framebutton,command=self.reset_data,text="RESET",font=("arial",12,"bold"),width=25,bg="#2F3651",fg="white")
        #btnReset.grid(row=0,column=3,padx=1)

        #btnAddData=Button(Framebutton,text="SLOT",command=self.update_statusss,font=("arial",12,"bold"),width=22,bg="#2F3651",fg="white")
        #btnAddData.grid(row=0,column=4,padx=1)

        #========================count=====================================================

            
        # Create a label to display the row count
        frame=LabelFrame(frame,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        frame.place(x=1490,y=5,width=278,height=350)

        l=Label(frame,bg="#48416C",fg="cyan2",relief=RIDGE,font=("Lemon tuesday",50), text='  00  ',padx=30,pady=-30)
        l.grid(row=4,column=2)


        self.table_frame = Frame(self.root,bd=5,bg="#355070")
        self.table_frame.place(x=1200,y=5285,width=420,height=230)


        #============tabel frame search system=====
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="#07161B")
        FrameDetails.place(x=130,y=170,width=1635,height=395)
        
        Table_Frame=Frame(FrameDetails,relief=RIDGE)
        Table_Frame.place(x=0,y=2,width=1610,height=365)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_Frame,column=("slotno","firstname","lastname","vehiclenumber","vehiclename","mobile","location","vehicletype",))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("firstname",text="First Name")
        self.room_table.heading("lastname",text="Last Name")
        self.room_table.heading("vehiclenumber",text="Vehicle Number")
        self.room_table.heading("vehiclename",text="Vehicle Name")
        self.room_table.heading("mobile",text="Mobile")
        self.room_table.heading("vehicletype",text="Vehicle Type")
        self.room_table.heading("slotno",text="Slot No")
        self.room_table.heading("location",text="Location")

        self.room_table["show"]="headings"

        self.room_table.column("firstname",width=70)
        self.room_table.column("lastname",width=70)
        self.room_table.column("vehiclenumber",width=70)
        self.room_table.column("vehiclename",width=70)
        self.room_table.column("mobile",width=70)
        self.room_table.column("vehicletype",width=70)
        self.room_table.column("slotno",width=10)
        self.room_table.column("location",width=70)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        

        #=====================information frame================



    def add_data(self):
        if self.slotno_var.get()=="" or self.vehicletype_var.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.slotno_var.get(),
                                                                                            self.firstname_var.get(),
                                                                                            self.lastname_var.get(),
                                                                                            self.vehiclenumber_var.get(),
                                                                                            self.vehiclename_var.get(),
                                                                                            self.mobile_var.get(),
                                                                                            self.location_var.get(),
                                                                                            self.vehicletype_var.get(),
                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", f"Slot [{self.slotno_var.get()}] at [{self.location_var.get()}] BOOKED SUCCESSFULLY for Vehicle Number [{self.vehiclenumber_var.get()}]!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","THIS SLOT IS ALREADY BOOKED BY THE OTHER USER! Please Book Another SLOT.",parent=self.root)

    def update(self):
        if self.slotno_var.get()=="":
            messagebox.showerror("Error","Please enter SLOT NUMBER",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set First_Name=%s,Last_Name=%s,Vehicle_Name=%s,Mobile=%s,Location=%s,Slot_No=%s where Vehicle_Number=%s",(
                                                                                            self.slotno_var.get(),
                                                                                            self.firstname_var.get(),
                                                                                            self.lastname_var.get(),
                                                                                            self.vehiclenumber_var.get(),
                                                                                            self.vehiclename_var.get(),
                                                                                            self.mobile_var.get(),
                                                                                            self.location_var.get(),
                                                                                            self.vehicletype_var.get(),
                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New room details has been updated",parent=self.root)

        

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.vehicletype_var.set(row[4]),
        self.slotno_var.set(row[5]),
        self.location_var.set(row[6]),
        self.mobile_var.set(row[7]),
        

    
        

    def reset_data(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.vehicletype_var.set(""),
        self.slotno_var.set(""),
        self.location_var.set(""),
        self.mobile_var.set(""),
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
            my_cursor=conn.cursor()
            query="delete from details where MOBILE=%s"
            value=(self.mobile_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")

#====================================================================================================================================================================================
#====================================================================================================================================================================================
#====================================================================================================================================================================================
#=============================================================================================================================

    def create_database(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()

        

    def update_status(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        self.display_table()
        slot_id = self.slotno_var.get()
        status = self.vehicletype_var.get()
        my_cursor.execute('UPDATE slots_table SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
        conn.commit()
        self.display_table()

    def display_table(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{slot_id}:{ slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)

    def display_tablee(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table2 ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{slot_id}:{slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)

    def display_tableee(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table3 ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{slot_id}:{slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)

    def display_tableeee(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
        my_cursor=conn.cursor()
        
        my_cursor.execute('SELECT slot_id, slot_status FROM slots_table4 ORDER BY slot_id')
        rows = my_cursor.fetchall()

        for widget in self.table_frame.winfo_children():
            widget.destroy()


        for i, row in enumerate(rows, start=1):
            slot_id, slot_status = row
            label = Label(self.table_frame,bg="#355070",fg="white" , text=f'{ slot_id}:{slot_status}',font=("times new roman",11), padx=3, pady=1)
            label.grid(row=(i - 1) // 10, column=(i - 1) % 10)



    def update_statusss(self):
        if self.location_var.get()=="Grand Plaza,Ghansoli":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_table()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table SET slot_status =  %s WHERE slot_id =  %s', (status, slot_id))
            conn.commit()
            self.display_table()

        elif self.location_var.get()=="SMT.Indira Gandhi College,Ghansoli":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_tablee()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table2 SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
            conn.commit()
            self.display_tablee()

        elif self.location_var.get()=="Ghansoli village":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_tableee()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table3 SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
            conn.commit()
            self.display_tableee()

        elif self.location_var.get()=="Ghansoli Railway Station":
            conn = mysql.connector.connect(host='localhost',user='root',password='Shubham@123',database='parking2')
            my_cursor=conn.cursor()
            self.display_tableeee()
            slot_id = self.slotno_var.get()
            status = self.vehicletype_var.get()
            my_cursor.execute('UPDATE slots_table4 SET slot_status = %s WHERE slot_id = %s', (status, slot_id))
            conn.commit()
            self.display_tableeee()


        else :
            messagebox.showerror("Error","First Select the Location")



#===================================================================================================================================================================================================
#===================================================================================================================================================================================================
#===================================================================================================================================================================================================
class CustomerComplaint:
    def __init__(self,root):
        self.root=root
        self.root.title("SLOT BOOKING")
        self.root.geometry("1910x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\complaint bg1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        
        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=10,bg="#436372")
        frame.place(x=650,y=200,width=535,height=340)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="FILL YOUR INFORMATION",bg="#fcd7b6",fg="maroon",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=490,height=300)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=5,column=1)

        lblv_no=Label(DataFrameLeft,bg="#fcd7b6",text="🟈 Complaint :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.billamount_var,width=29)
        txtv_no.grid(row=6,column=1)

       
               #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="powder blue")
        Framebutton.place(x=750,y=550,width=345,height=57)

        btnAddData=Button(Framebutton,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=15,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        btnAddData=Button(Framebutton,command=self.delete,text="DELETE",font=("arial",12,"bold"),width=15,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=1,sticky=W)


        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=0,bg="#48416C")
        FrameDetails.place(x=550,y=620,width=695,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=670,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","mobile","billamount","address","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="COMPLAINT")
        

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        
        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.mobile_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.address_var.get(),
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
       

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("update vehicle set FIRST_NAME=%s, LAST_NAME=%s, VEHICLE_NAME=%s, ADDRESS=%s, MOBILE=%s, BILL_AMOUNT=%s, VEHICLE_TYPE=%s, PARKING_TIME=%s, PARKOFF_TIME=%s, PARKING_DATE=%s, CHARGES=%s, SLOT_STATUS=%s, SLOT_AREA=%s, PARMENT_MODE=%s WHERE VEHICLE_NUMBER=%s",(
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.vehiclename_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.billamount_var.get(),
                                                                                        self.vehicletype_var.get(),
                                                                                        self.parkingtime_var.get(),
                                                                                        self.parkofftime_var.get(),
                                                                                        self.parkingdate_var.get(),
                                                                                        self.charges_var.get(),
                                                                                        self.slotstatus_var.get(),
                                                                                        self.slotarea_var.get(),
                                                                                        self.paymentmode_var.get(),
                                                                                        self.vehiclenumber_var.get(),
                                                                                      ))
        conn.commit(),
        self.fatch_data()
        self.reset(),
        conn.close(),

        messagebox.showinfo("Success","Member has been Updated")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.mobile_var.set(row[4]),
        self.billamount_var.set(row[5]),
        self.address_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),


    def showData(self):
        self.txtBox.insert(END,"FIRST NAME :\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LAST NAME :\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE NUMBER :\t\t"+ self.vehiclenumber_var.get() + "\n")
        self.txtBox.insert(END,"MOBILE :\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"BILL AMOUNT :\t\t"+ self.billamount_var.get() + "\n")
        self.txtBox.insert(END,"VEHICLE TYPE :\t\t"+ self.vehicletype_var.get() + "\n")
        self.txtBox.insert(END,"PARKING TIME :\t\t"+ self.parkingtime_var.get() + "\n")
        self.txtBox.insert(END,"PARK OFF TIME :\t\t"+ self.parkofftime_var.get() + "\n")
        self.txtBox.insert(END,"PARKING DATE :\t\t"+ self.parkingdate_var.get() + "\n")
        

    def reset(self):
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.vehiclenumber_var.set(""),
        self.vehiclename_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.billamount_var.set(""),
        self.vehicletype_var.set(""),
        self.parkingtime_var.set(""),
        self.parkofftime_var.set(""),
        self.parkingdate_var.set(""),
        self.charges_var.set(""),
        self.slotstatus_var.set(""),
        self.slotarea_var.set(""),
        self.paymentmode_var.set("")
        self.txtBox.delete("1.0",END)
        

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Vehicle Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.firstname_var.get()=="" or self.vehiclenumber_var.get()=="":
            messagebox.showerror("Error","First Select the Item")

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking3")
            my_cursor=conn.cursor()
            query="delete from vehicle where Vehicle_Number=%s"
            value=(self.vehiclenumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","DELETED!!")
            

#=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================
#=======================================================================================================================================================================================================================

class Membership_Plan:
    def __init__(self,root):
        self.root=root
        self.root.title("Membership Plans")
        self.root.geometry("1980x1000+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\MEMBERSHIP PLAN 5.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


#==========================FRAME BUTTON ============================================================================================

        Framebutton1=Frame(self.root,bd=4,relief=RIDGE,padx=0,bg="BLUE")
        Framebutton1.place(x=300,y=480,width=118,height=41)

        Framebutton2=Frame(self.root,bd=4,relief=RIDGE,padx=0,bg="BLUE")
        Framebutton2.place(x=908,y=480,width=118,height=41)

        Framebutton3=Frame(self.root,bd=4,relief=RIDGE,padx=0,bg="BLUE")
        Framebutton3.place(x=1508,y=480,width=118,height=41)

        Framebutton4=Frame(self.root,bd=4,relief=RIDGE,padx=0,bg="BLUE")
        Framebutton4.place(x=600,y=825,width=118,height=41)

        Framebutton5=Frame(self.root,bd=4,relief=RIDGE,padx=0,bg="BLUE")
        Framebutton5.place(x=1220,y=825,width=118,height=41)

        btnAddData=Button(Framebutton1,command=self.TwoWheel,text="APPLY",font=("arial",12,"bold"),width=10,bg="#EFAB9C",fg="BLACK")
        btnAddData.grid(row=0,column=1,sticky=W)

        btnAddData=Button(Framebutton2,command=self.ThreeWheel,text="APPLY",font=("arial",12,"bold"),width=10,bg="#EFAB9C",fg="BLACK")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton3,command=self.FourWheel,text="APPLY",font=("arial",12,"bold"),width=10,bg="#EFAB9C",fg="BLACK")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton4,command=self.TroleyWheel,text="APPLY",font=("arial",12,"bold"),width=10,bg="#EFAB9C",fg="BLACK")
        btnAddData.grid(row=1,column=1)

        btnAddData=Button(Framebutton5,command=self.GoodsCarrierWheel,text="APPLY",font=("arial",12,"bold"),width=10,bg="#EFAB9C",fg="BLACK")
        btnAddData.grid(row=1,column=2)


    def TwoWheel(self):
        self.new_window=Toplevel(self.root)
        self.app=TwoWheelerMembership(self.new_window)


    def ThreeWheel(self):
        self.new_window=Toplevel(self.root)
        self.app=ThreeWheelerMembership(self.new_window)

    def FourWheel(self):
        self.new_window=Toplevel(self.root)
        self.app=FourWheelerMembership(self.new_window)


    def TroleyWheel(self):
        self.new_window=Toplevel(self.root)
        self.app=TroleyMembership(self.new_window)


    def GoodsCarrierWheel(self):
        self.new_window=Toplevel(self.root)
        self.app=GoodsCarrierMembership(self.new_window)

#=======================================================================================================================================

class TwoWheelerMembership:
    def __init__(self,root):
        self.root=root
        self.root.title("2 Wheeler Membership Apply")
        self.root.geometry("1910x1000+0+0")



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\MEMBESHIP APPLY BG1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()



        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        frame.place(x=420,y=250,width=1070,height=380)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#0AAFFF",fg="yellow",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1000,height=340)



        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Total Duration :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.paymentmode_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=5,column=3)


        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="SELECT",bg="powder blue",fg="green",relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=120,height=150)


        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['15 DAYS','1 MONTH','3 MONTHS','6 MONTHS']#,'▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="6 MONTHS"):
                self.charges_var.set("Rs 2700")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TWO WHEELER")
                self.paymentmode_var.set("6 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="15 DAYS"):
                self.charges_var.set("Rs 250")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TWO WHEELER")
                self.paymentmode_var.set("15 DAYS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="1 MONTH"):
                self.charges_var.set("Rs 450")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TWO WHEELER")
                self.paymentmode_var.set("1 MONTH")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="3 MONTHS"):
                self.charges_var.set("Rs 1300")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TWO WHEELER")
                self.paymentmode_var.set("3 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=0)
        listScrollbar.config(command=listBox.yview)
        

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton.place(x=800,y=640,width=285,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="APPLY",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        #btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=25,bg="#FF8674",fg="white")
        #btnAddData.grid(row=0,column=1)

        #btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=25,bg="#6CD300",fg="white")
        #btnAddData.grid(row=0,column=2)

        #btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=25,bg="#0AFFFF",fg="white")
        #btnAddData.grid(row=0,column=3)

        #btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=25,bg="#2C3539",fg="white")
        #btnAddData.grid(row=0,column=4)

        #btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=25,bg="#B87333",fg="white")
        #btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        FrameDetails.place(x=20000,y=60000,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=200,y=200,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),                                                                           
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),                                                                           
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[11]),
        self.vehicletype_var.set(row[6]),
        self.parkingtime_var.set(row[12]),
        self.parkofftime_var.set(row[13]),
        self.parkingdate_var.set(row[8]),
        self.charges_var.set(row[9]),
        self.slotstatus_var.set(row[14]),
        self.slotarea_var.set(row[10]),
        self.paymentmode_var.set(row[7]),



#==============================================================================2 wheeler over=================================================
#==============================================================================2 wheeler over=================================================
#==============================================================================2 wheeler over=================================================
#==============================================================================2 wheeler over=================================================
#==============================================================================2 wheeler over=================================================


class ThreeWheelerMembership:
    def __init__(self,root):
        self.root=root
        self.root.title("3 Wheeler Membership Apply")
        self.root.geometry("1910x1000+0+0")



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\MEMBESHIP APPLY BG1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()



        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        frame.place(x=420,y=250,width=1070,height=380)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#0AAFFF",fg="yellow",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1000,height=340)



        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Total Duration :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.paymentmode_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=5,column=3)


        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="SELECT",bg="powder blue",fg="green",relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=120,height=150)


        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['15 DAYS','1 MONTH','3 MONTHS','6 MONTHS']#,'▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="6 MONTHS"):
                self.charges_var.set("Rs 4000")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")
                self.paymentmode_var.set("6 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="15 DAYS"):
                self.charges_var.set("Rs 350")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")
                self.paymentmode_var.set("15 DAYS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="1 MONTH"):
                self.charges_var.set("Rs 700")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")
                self.paymentmode_var.set("1 MONTH")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="3 MONTHS"):
                self.charges_var.set("Rs 2100")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("THREE WHEELER")
                self.paymentmode_var.set("3 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=0)
        listScrollbar.config(command=listBox.yview)
        

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton.place(x=800,y=640,width=285,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="APPLY",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        #btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=25,bg="#FF8674",fg="white")
        #btnAddData.grid(row=0,column=1)

        #btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=25,bg="#6CD300",fg="white")
        #btnAddData.grid(row=0,column=2)

        #btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=25,bg="#0AFFFF",fg="white")
        #btnAddData.grid(row=0,column=3)

        #btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=25,bg="#2C3539",fg="white")
        #btnAddData.grid(row=0,column=4)

        #btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=25,bg="#B87333",fg="white")
        #btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        FrameDetails.place(x=20000,y=60000,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=200,y=200,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),                                                                           
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),                                                                           
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[11]),
        self.vehicletype_var.set(row[6]),
        self.parkingtime_var.set(row[12]),
        self.parkofftime_var.set(row[13]),
        self.parkingdate_var.set(row[8]),
        self.charges_var.set(row[9]),
        self.slotstatus_var.set(row[14]),
        self.slotarea_var.set(row[10]),
        self.paymentmode_var.set(row[7]),

#==============================================================================3 wheeler over=================================================
#==============================================================================3 wheeler over=================================================
#==============================================================================3 wheeler over=================================================
#==============================================================================3 wheeler over=================================================
#==============================================================================3 wheeler over=================================================



class FourWheelerMembership:
    def __init__(self,root):
        self.root=root
        self.root.title("4 Wheeler Membership Apply")
        self.root.geometry("1910x1000+0+0")



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\MEMBESHIP APPLY BG1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()



        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        frame.place(x=420,y=250,width=1070,height=380)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#0AAFFF",fg="yellow",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1000,height=340)



        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Total Duration :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.paymentmode_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=5,column=3)


        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="SELECT",bg="powder blue",fg="green",relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=120,height=150)


        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['15 DAYS','1 MONTH','3 MONTHS','6 MONTHS']#,'▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="6 MONTHS"):
                self.charges_var.set("Rs 4200")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")
                self.paymentmode_var.set("6 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="15 DAYS"):
                self.charges_var.set("Rs 450")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")
                self.paymentmode_var.set("15 DAYS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="1 MONTH"):
                self.charges_var.set("Rs 900")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")
                self.paymentmode_var.set("1 MONTH")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="3 MONTHS"):
                self.charges_var.set("Rs 2500")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("FOUR WHEELER")
                self.paymentmode_var.set("3 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=0)
        listScrollbar.config(command=listBox.yview)
        

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton.place(x=800,y=640,width=285,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="APPLY",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        #btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=25,bg="#FF8674",fg="white")
        #btnAddData.grid(row=0,column=1)

        #btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=25,bg="#6CD300",fg="white")
        #btnAddData.grid(row=0,column=2)

        #btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=25,bg="#0AFFFF",fg="white")
        #btnAddData.grid(row=0,column=3)

        #btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=25,bg="#2C3539",fg="white")
        #btnAddData.grid(row=0,column=4)

        #btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=25,bg="#B87333",fg="white")
        #btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        FrameDetails.place(x=20000,y=60000,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=200,y=200,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),                                                                           
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),                                                                           
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[6]),
        self.vehicletype_var.set(row[7]),
        self.parkingtime_var.set(row[8]),
        self.parkofftime_var.set(row[9]),
        self.parkingdate_var.set(row[10]),
        self.charges_var.set(row[11]),
        self.slotstatus_var.set(row[12]),
        self.slotarea_var.set(row[13]),
        self.paymentmode_var.set(row[14]),




#==============================================================================4 wheeler over=================================================
#==============================================================================4 wheeler over=================================================
#==============================================================================4 wheeler over=================================================
#==============================================================================4 wheeler over=================================================
#==============================================================================4 wheeler over=================================================


class TroleyMembership:
    def __init__(self,root):
        self.root=root
        self.root.title("Troley Membership Apply")
        self.root.geometry("1910x1000+0+0")



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\MEMBESHIP APPLY BG1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()



        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        frame.place(x=420,y=250,width=1070,height=380)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#0AAFFF",fg="yellow",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1000,height=340)



        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Total Duration :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.paymentmode_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=5,column=3)


        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="SELECT",bg="powder blue",fg="green",relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=120,height=150)


        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['15 DAYS','1 MONTH','3 MONTHS','6 MONTHS']#,'▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="6 MONTHS"):
                self.charges_var.set("Rs 13000")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TROLEY")
                self.paymentmode_var.set("6 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="15 DAYS"):
                self.charges_var.set("Rs 1100")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TROLEY")
                self.paymentmode_var.set("15 DAYS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="1 MONTH"):
                self.charges_var.set("Rs 2200")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TROLEY")
                self.paymentmode_var.set("1 MONTH")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="3 MONTHS"):
                self.charges_var.set("Rs 6400")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("TROLEY")
                self.paymentmode_var.set("3 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=0)
        listScrollbar.config(command=listBox.yview)
        

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton.place(x=800,y=640,width=285,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="APPLY",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        #btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=25,bg="#FF8674",fg="white")
        #btnAddData.grid(row=0,column=1)

        #btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=25,bg="#6CD300",fg="white")
        #btnAddData.grid(row=0,column=2)

        #btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=25,bg="#0AFFFF",fg="white")
        #btnAddData.grid(row=0,column=3)

        #btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=25,bg="#2C3539",fg="white")
        #btnAddData.grid(row=0,column=4)

        #btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=25,bg="#B87333",fg="white")
        #btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        FrameDetails.place(x=20000,y=60000,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=200,y=200,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),                                                                           
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),                                                                           
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[11]),
        self.vehicletype_var.set(row[6]),
        self.parkingtime_var.set(row[12]),
        self.parkofftime_var.set(row[13]),
        self.parkingdate_var.set(row[8]),
        self.charges_var.set(row[9]),
        self.slotstatus_var.set(row[14]),
        self.slotarea_var.set(row[10]),
        self.paymentmode_var.set(row[7]),



#==============================================================================TROLEY over=================================================
#==============================================================================TROLEY over=================================================
#==============================================================================TROLEY over=================================================
#==============================================================================TROLEY over=================================================
#==============================================================================TROLEY over=================================================

class GoodsCarrierMembership:
    def __init__(self,root):
        self.root=root
        self.root.title("Goods Carrier Membership Apply")
        self.root.geometry("1910x1000+0+0")



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\New folder\MEMBESHIP APPLY BG1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #===================variable=======================================

        self.member_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.vehiclenumber_var=StringVar()
        self.vehiclename_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.billamount_var=StringVar()
        self.vehicletype_var=StringVar()
        self.parkingtime_var=StringVar()
        self.parkofftime_var=StringVar()
        self.parkingdate_var=StringVar()
        self.charges_var=StringVar()
        self.slotstatus_var=StringVar()
        self.slotarea_var=StringVar()
        self.paymentmode_var=StringVar()



        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        frame.place(x=420,y=250,width=1070,height=380)

        #================DataFrameLeft==================

        DataFrameLeft=LabelFrame(frame,text="MEMBER INFORMATION",bg="#0AAFFF",fg="yellow",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=1000,height=340)



        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 First Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtv_no.grid(row=1,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Last Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtv_no.grid(row=2,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Number :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclenumber_var,width=29)
        txtv_no.grid(row=3,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Name :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehiclename_var,width=29)
        txtv_no.grid(row=4,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Address :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtv_no.grid(row=5,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Mobile :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=6,column=0,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtv_no.grid(row=6,column=1)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Vehicle Type :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=1,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.vehicletype_var,width=29)
        txtv_no.grid(row=1,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Total Duration :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=2,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.paymentmode_var,width=29)
        txtv_no.grid(row=2,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Parking Date :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=3,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.parkingdate_var,width=29)
        txtv_no.grid(row=3,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Charges :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=4,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.charges_var,width=29)
        txtv_no.grid(row=4,column=3)


        lblv_no=Label(DataFrameLeft,bg="#0AAFFF",text="🟈 Slot Area :",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblv_no.grid(row=5,column=2,sticky=W)
        txtv_no=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.slotarea_var,width=29)
        txtv_no.grid(row=5,column=3)


        #==============================DataFrame Right=================================
        DataFrameRight=LabelFrame(frame,text="SELECT",bg="powder blue",fg="green",relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=120,height=150)


        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listVehicles=['15 DAYS','1 MONTH','3 MONTHS','6 MONTHS']#,'▷ TROLEY','▷ THREE WHEELER']

        def SelectVehicles(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="6 MONTHS"):
                self.charges_var.set("Rs 15000")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                self.paymentmode_var.set("6 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="15 DAYS"):
                self.charges_var.set("Rs 1300")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                self.paymentmode_var.set("15 DAYS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="1 MONTH"):
                self.charges_var.set("Rs 2500")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                self.paymentmode_var.set("1 MONTH")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)


            elif (x=="3 MONTHS"):
                self.charges_var.set("Rs 7500")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("100x50 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                self.paymentmode_var.set("3 MONTHS")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ GOODS CARRIER"):
                self.charges_var.set("Rs 100/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("80x40 sq.m")
                self.vehicletype_var.set("GOODS CARRIER")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)



            elif (x=="▷ TROLEY"):
                self.charges_var.set("Rs 50/hr")
                self.slotstatus_var.set("Available")
                self.slotarea_var.set("120x80 sq.m")
                self.vehicletype_var.set("TROLEY")
                

                d1=datetime.date.today()
                d2=datetime.datetime.today()
                
                self.parkingdate_var.set(d1)
                self.parkingtime_var.set(d2)
                
                
                

        listBox=Listbox(DataFrameRight,font=("Arial CYR",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectVehicles)
        listBox.grid(row=0,column=0,padx=0)
        listScrollbar.config(command=listBox.yview)
        

        for item in listVehicles:
            listBox.insert(END,item)

        #========================BUTTONS FRAME========================================

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=00,bg="powder blue")
        Framebutton.place(x=800,y=640,width=285,height=60)

        btnAddData=Button(Framebutton,command=self.adda_data,text="APPLY",font=("arial",12,"bold"),width=25,bg="#348781",fg="white")
        btnAddData.grid(row=0,column=0,sticky=W)

        #btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=25,bg="#FF8674",fg="white")
        #btnAddData.grid(row=0,column=1)

        #btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=25,bg="#6CD300",fg="white")
        #btnAddData.grid(row=0,column=2)

        #btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=25,bg="#0AFFFF",fg="white")
        #btnAddData.grid(row=0,column=3)

        #btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=25,bg="#2C3539",fg="white")
        #btnAddData.grid(row=0,column=4)

        #btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=25,bg="#B87333",fg="white")
        #btnAddData.grid(row=0,column=5)
        

        #=====================information frame================

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="#48416C")
        FrameDetails.place(x=20000,y=60000,width=1630,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=200,y=200,width=1565,height=165)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.vehicle_table=ttk.Treeview(Table_frame,column=("firstname","lastname","vehiclenumber","vehiclename","address","mobile","billamount","vehicletype","parkingtime","parkofftime","parkingdate","charges","slotstatus","slotarea","paymentmode",),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.vehicle_table.xview)
        yscroll.config(command=self.vehicle_table.yview)



        self.vehicle_table.heading("firstname",text="FIRST NAME")
        self.vehicle_table.heading("lastname",text="LAST NAME")
        self.vehicle_table.heading("vehiclenumber",text="VEHICLE NUMBER")
        self.vehicle_table.heading("vehiclename",text="VEHICLE NAME")
        self.vehicle_table.heading("address",text="ADDRESS")
        self.vehicle_table.heading("mobile",text="MOBILE")
        self.vehicle_table.heading("billamount",text="BILL AMOUNT")
        self.vehicle_table.heading("vehicletype",text="VEHICLE TYPE")
        self.vehicle_table.heading("parkingtime",text="PARKING TIME")
        self.vehicle_table.heading("parkofftime",text="PARK OFF TIME")
        self.vehicle_table.heading("parkingdate",text="PARKING DATE")
        self.vehicle_table.heading("charges",text="CHARGES")
        self.vehicle_table.heading("slotstatus",text="SLOT STATUS")
        self.vehicle_table.heading("slotarea",text="SLOT AREA")
        self.vehicle_table.heading("paymentmode",text="PAYMENT MODE")

        self.vehicle_table["show"]="headings"
        self.vehicle_table.pack(fill=BOTH,expand=1)

        self.vehicle_table.column("firstname",width=100)
        self.vehicle_table.column("lastname",width=100)
        self.vehicle_table.column("vehiclenumber",width=100)
        self.vehicle_table.column("vehiclename",width=100)
        self.vehicle_table.column("address",width=100)
        self.vehicle_table.column("mobile",width=100)
        self.vehicle_table.column("billamount",width=100)
        self.vehicle_table.column("vehicletype",width=100)
        self.vehicle_table.column("parkingtime",width=100)
        self.vehicle_table.column("parkofftime",width=100)
        self.vehicle_table.column("parkingdate",width=100)
        self.vehicle_table.column("charges",width=100)
        self.vehicle_table.column("slotstatus",width=100)
        self.vehicle_table.column("slotarea",width=100)
        self.vehicle_table.column("paymentmode",width=100)

        self.fatch_data()
        self.vehicle_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.firstname_var.get(),
                                                                            self.lastname_var.get(),
                                                                            self.vehiclenumber_var.get(),
                                                                            self.vehiclename_var.get(),
                                                                            self.address_var.get(),
                                                                            self.mobile_var.get(),                                                                           
                                                                            self.vehicletype_var.get(),
                                                                            self.parkingdate_var.get(),
                                                                            self.charges_var.get(),                                                                           
                                                                            self.slotarea_var.get(),
                                                                            self.paymentmode_var.get(),
                                                                            self.slotstatus_var.get(),
                                                                            self.billamount_var.get(),
                                                                            self.parkingtime_var.get(),
                                                                            self.parkofftime_var.get(),
                                                                            ))
        conn.commit(),
        self.fatch_data()
        conn.close(),
        messagebox.showinfo("Success","Member Has been inserted successfully")

        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@123",database="parking2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vehicle")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.vehicle_table.delete(*self.vehicle_table.get_children())
            for i in rows:
                self.vehicle_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.vehicle_table.focus()
        content=self.vehicle_table.item(cursor_row)
        row=content['values']

        self.firstname_var.set(row[0]),
        self.lastname_var.set(row[1]),
        self.vehiclenumber_var.set(row[2]),
        self.vehiclename_var.set(row[3]),
        self.address_var.set(row[4]),
        self.mobile_var.set(row[5]),
        self.billamount_var.set(row[11]),
        self.vehicletype_var.set(row[6]),
        self.parkingtime_var.set(row[12]),
        self.parkofftime_var.set(row[13]),
        self.parkingdate_var.set(row[8]),
        self.charges_var.set(row[9]),
        self.slotstatus_var.set(row[14]),
        self.slotarea_var.set(row[10]),
        self.paymentmode_var.set(row[7]),




#==============================================================================Goods Carrier over=================================================
#==============================================================================Goods Carrier over =================================================
#==============================================================================Goods Carrier over=================================================
#==============================================================================Goods Carrier over=================================================
#==============================================================================Goods Carrier over=================================================

        



            

if __name__== "__main__":
    main()
