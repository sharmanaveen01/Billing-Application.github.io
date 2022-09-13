
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import random, os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x735+0+0")
        self.root.title("Billing Software")

        # ********************** Varibales ********************** 
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()




        #Product Categories List
        self.Category=["Select Option","Clothing","Lifestyle","Mobiles"]
        
        #SubCatClothing
        self.SubCatClothing=["Lower","Shirt","T-shirt"]

        self.lower=["Levis","Polo","Here & Now"]
        self.price_Levis=1000
        self.price_Polo=990
        self.price_Here=500

        self.Shirt=["Peter England","Louis Phillipe","Park Avenue"]
        self.price_Peter=450
        self.price_Louis=800
        self.price_Park= 900

        self.T_shirt=["Polo","Roadster","Jack&Jones"]
        self.price_polo=1500
        self.price_roadster=500
        self.price_jack=1200

        self.SubCatLifestyle=["Bath Soap","Face Wash","Hair Oil"]
        self.Bath_soap=["LifeBuy","Lux","Dettol","Pearl"]
        self.price_life=20
        self.price_lux=20
        self.price_dettol=45
        self.price_pearl=35

        self.Face_creame=["Fair&Lovely","Pond","Olay","Garnier"]
        self.price_fair=45
        self.price_pond=80
        self.price_olay= 50
        self.price_garnier=110

        self.Hair_oil=["Jasmin","Bajaj","Parasuite"]
        self.price_jasmine=150
        self.price_bajaj=50
        self.price_parasuite=60


        self.SubCatMobiles=["Iphone","Samsung","Xiome",'Real Me',"One Plus"]
        self.Iphone=["Iphone-x",'Iphone-11','Iphone_12']
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000

        self.Samsung=["Samsung M16","Samsung M12","Samsung Galaxy"]
        self.price_m16=16000
        self.price_m12=12000
        self.price_galaxy=9000

        self.Xiome=["Red11",'Redme-12','Redme Pro']
        self.price_11=11000
        self.price_12=12000
        self.price_pro=9000

        self.Realme=["RealMe 12","RealMe 13","RealMe Pro"]
        self.price_r12=11000
        self.price_r13=12000
        self.price_rpro=30000
        
        self.one_plus=["OnePlus1",'Oneplus2','Oneplus3']
        self.price_one1=45000
        self.price_one12=60000
        self.price_one3=45800

        


        img=Image.open("image/image1.png")
        img=img.resize((1350,130),Image.ANTIALIAS)

    
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=1350,height=130)

        lbl_title=Label(self.root,text="Your Bill", font=("times new roman",35,"bold"),bg="White",fg="black")
        lbl_title.place(x=0,y=130,width=1350,height=45)
        
        # Time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time) 

        lbl = Label(lbl_title, font = ('time new roman', 16, 'bold'),background = 'white', foreground='black' ) 
        lbl.place(x=0,y=0,width=120,height=45)
        time()  


        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1350,height=570)

        #Customer Label Frame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="black")
        Cust_Frame.place(x=0,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",10,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=3)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1)


        self.lblCustName=Label(Cust_Frame,text="Customer Name",font=("times new roman",10,"bold"),bg="white",fg="black")
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",10,"bold"),width=20)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        
        self.lblEmail=Label(Cust_Frame,text="Email",font=("times new roman",10,"bold"),bg="white",fg="black")
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",10,"bold"),width=20)
        self.txtEmail.grid(row=2,column=1,padx=5,pady=3)

        


        #Product Label Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="black")
        Product_Frame.place(x=370,y=5,width=530,height=140)

        #Category 
        self.lblCategory=Label(Product_Frame,text="Select Category",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=19,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        #Subcategory
        self.lblSubCategory=Label(Product_Frame,text="Subcategory",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #Product Name
        self.lblproduct=Label(Product_Frame,text="Product Name",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,text="Price",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=19,state="readonly")
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,text="Qty",font=("arial",10,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Combobox(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=19)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        
        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=0,y=150,width=895,height=340)

        img12=Image.open("image/image2.jpg")
        img12=img12.resize((800,340),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=873,height=340)



        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=910,y=10,width=400,height=40)

        self.lblBill=Label(Search_Frame,font=("arial",10,'bold'),fg='black',bg='white',text='Bill Number')
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',10,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="black",fg='white',width=12,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)
        
        
        #Right Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Section",font=("times new roman",12,"bold"),bg="white")
        RightLabelFrame.place(x=910,y=40,width=420,height=401)

        scroll_y= Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #Bill Counter
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",15,"bold"),bg="white",fg="black")
        Bottom_Frame.place(x=0,y=440,width=1330,height=113)


        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("arial",8,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",8,"bold"),width=19)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)


        self.lbl_tax=Label(Bottom_Frame,text="Gov. Tax",font=("arial",8,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("arial",8,"bold"),width=19)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("arial",8,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("arial",8,"bold"),width=19,)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        #Button Add To Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=('arial',15,'bold'),bg="black",fg='white',width=12,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        #Button Generate Bill
        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="black",fg='white',width=12,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        #Button Save
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="black",fg='white',width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        #Button Print
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="black",fg='white',width=12,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        #Button Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="black",fg='white',width=12,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        #Button Exit
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="black",fg='white',width=12,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
    # =======================Function Declaration ==========================
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n ===========================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n =========================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You want to Save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved Successfully")
            f1.close()


    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'print')


    def find_bill(self):
        found='no'
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found='yes'

        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

            
    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
        

        

        





    # For Bill Area Design
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t THANK YOU ")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n ===========================================")
        self.textarea.insert(END,"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n ===========================================")
    

    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Lifestyle":
            self.ComboSubCategory.config(value=self.SubCatLifestyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)


    def Product_add(self,event=''):
        if self.ComboSubCategory.get()=="Lower":
            self.ComboProduct.config(value=self.lower)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="T-shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        # Lifestyle
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Face Wash":
            self.ComboProduct.config(value=self.Face_creame)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

        #Mobiles
        if self.ComboSubCategory.get()=="Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.Realme)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=="One Plus":
            self.ComboProduct.config(value=self.one_plus)
            self.ComboProduct.current(0)


    def price(self,event=""):
        # Lower
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_Polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Here & Now":
            self.ComboPrice.config(value=self.price_Here)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Shirt
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # T-shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_jack)
            self.ComboPrice.current(0)
            self.qty.set(1)


        # Bath Soap
        if self.ComboProduct.get()=="LifeBuy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Dettol":
            self.ComboPrice.config(value=self.price_dettol)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pearl":
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Face Wash
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Pond":
            self.ComboPrice.config(value=self.price_pond)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Hair Oil
        if self.ComboProduct.get()=="Jasmin":
            self.ComboPrice.config(value=self.price_jasmine)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Parasuite":
            self.ComboPrice.config(value=self.price_parasuite)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Mobiles
        if self.ComboProduct.get()=="Iphone-x":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone-11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Samsung
        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_m16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M12":
            self.ComboPrice.config(value=self.price_m12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung Galaxy":
            self.ComboPrice.config(value=self.price_galaxy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Xiome
        if self.ComboProduct.get()=="Red11":
            self.ComboPrice.config(value=self.price_11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redme-12":
            self.ComboPrice.config(value=self.price_12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redme Pro":
            self.ComboPrice.config(value=self.price_pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Realme
        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_r13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # One Plus
        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Oneplus2":
            self.ComboPrice.config(value=self.price_one12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Oneplus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)

    
   
    
    

    


        


        

if __name__ == '__main__':
    root=Tk()
    obj = Bill_App(root)
    root.mainloop()