from tkinter import *  
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        #========================Variables=========================================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_address=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.discount=StringVar()
        self.total=StringVar()


        #Product Category List
        self.Category=["Select Option","Grocery","Household","LifeStyle"]

        #Sub CatGrocery
        self.SubGrocery=["Oil","Pulses","Rice","Sugar","Flour"]
        self.oil=["Sarsoo","Soyabean","groundnut"]
        self.sarsoo=160
        self.soyabean=150
        self.groundnut=190
        self.pulses=["Arahar","Chana","Matar"]
        self.rice=["Basmati","zeera32","soonam"]
        self.sugar=["Moti-chini","Medium-chini","Chini-bhura"]

        self.SubHousehold=["Soap","Detergent","Accessories"]
        self.soap=["Detol","Lifebouy","Lux"]
        self.detergent=["SurfExcel","Arial","Ghari"]
        self.accessories=["Broom","Handle-cleaner"]

        self.SubLifeStyle=["Perfume","FairCreame","Babyproduct"]
        self.perfume=["Fogg","Deniver"]
        self.faircreame=["Fair&Glow","Fair&handsome"]
        self.babyproduct=["Diper","Baby-oil","Baby-soap"]

        #Image1
        img=Image.open("image/grocery1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)


        #Image2
        img_1=Image.open("image/grocery.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)


        #Image1
        img_2=Image.open("image/grocery3.jpg")
        img_2=img_2.resize((530,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=530,height=130)


        lbl_title=Label(self.root,text="MANOJ BILLING SOFTWARE",font=("New Century Schoolbook",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=50)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font=('times new roman',16,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=(-15),width=120,height=50)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer Label Frame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details",font=("New Century Schoolbook",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile no.",font=("New Century Schoolbook",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("New Century Schoolbook",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,text="Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblCustAdd=Label(Cust_Frame,text="Address",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCustAdd.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtCustAdd=ttk.Entry(Cust_Frame,textvariable=self.c_address,font=("arial",10,"bold"),width=24)
        self.txtCustAdd.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        #Product Label Frame
        Product_Frame=LabelFrame(Main_Frame,text="Products Details",font=("New Century Schoolbook",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=650,height=140)

        #Category
        self.lblCategory=Label(Product_Frame,text="Select Categories",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #Sub_Category
        self.lblSubCategory=Label(Product_Frame,text="Sub Category",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSub_Category=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboSub_Category.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSub_Category.bind("<<ComboboxSelected>>",self.Product_add)

        #Product
        self.lblProduct=Label(Product_Frame,text="Product Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Quty
        self.lblQuantity=Label(Product_Frame,text="Quantity",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblQuantity.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.Combo_Quantity=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=24)
        self.Combo_Quantity.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bg="skyblue")
        MiddleFrame.place(x=10,y=150,width=1010,height=340)

        #Image2
        img_12=Image.open("image/grocery4.jpg")
        img_12=img_12.resize((505,340),Image.ANTIALIAS)
        self.photoimg_12=ImageTk.PhotoImage(img_12)

        lbl_img_12=Label(MiddleFrame,image=self.photoimg_12)
        lbl_img_12.place(x=0,y=0,width=505,height=340)

        #Image2
        img_13=Image.open("image/grocery5.jpg")
        img_13=img_13.resize((505,340),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=505,y=0,width=505,height=340)



        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="skyblue")
        Search_Frame.place(x=1030,y=15,width=480,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=('arial',12,'bold'),fg="white",bg="red",width=15)
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txtEntrySearch=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=24)
        self.txtEntrySearch.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #RigthSide Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1030,y=45,width=480,height=400)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter Label Frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("New Century Schoolbook",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",10,"bold"),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_discount=Label(Bottom_Frame,text="Discount",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_discount.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_discount=ttk.Entry(Bottom_Frame,textvariable=self.discount,font=("arial",10,"bold"),width=24)
        self.txt_discount.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblTotalAmount=Label(Bottom_Frame,text="Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblTotalAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txt_total=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",10,"bold"),width=24)
        self.txt_total.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerateBill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]

    #==================================Function Declaration==============================
    def AddItem(self):
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the product name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.discount.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*1)/100)))
            self.total.set(str('Rs.%.2f'%((sum(self.l)) - ((((sum(self.l)) - (self.prices.get()))*1)/100))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ==================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Discount:\t\t\t{self.discount.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ==================================================\n")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save this bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No.{self.bill_no.get()} Saved Successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_address.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.discount.set("")
        self.welcome()



    #bill generating
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome Manoj General Store")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Address:{self.c_address.get()}")

        self.textarea.insert(END,"\n ==================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n ==================================================\n")


    
    #function of calling product
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Grocery":
            self.ComboSub_Category.config(value=self.SubGrocery)
            self.ComboSub_Category.current(0)

        if self.Combo_Category.get()=="Household":
            self.ComboSub_Category.config(value=self.SubHousehold)
            self.ComboSub_Category.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSub_Category.config(value=self.SubLifeStyle)
            self.ComboSub_Category.current(0)

    def Product_add(self,event=""):
        if self.ComboSub_Category.get()=="Oil":
            self.ComboProduct.config(value=self.oil)
            self.ComboProduct.current(0)

        if self.ComboSub_Category.get()=="Pulses":
            self.ComboProduct.config(value=self.pulses)
            self.ComboProduct.current(0)

        if self.ComboSub_Category.get()=="Rice":
            self.ComboProduct.config(value=self.rice)
            self.ComboProduct.current(0)


    #Price function
    def price(self,event=""):
        if self.ComboProduct.get()=="Sarsoo":
            self.Combo_Price.config(value=self.sarsoo)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Soyabean":
            self.Combo_Price.config(value=self.soyabean)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="groundnut":
            self.Combo_Price.config(value=self.groundnut)
            self.Combo_Price.current(0)
            self.qty.set(1)
















if __name__== '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
