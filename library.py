from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1530x800+0+0")
        
        #========================================================Variable============================================================================
        self.memeber_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.actualprice_var = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        #=================================================DataFrameLeft=================================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=12, 
                                 relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.memeber_var, font=("arial", 12, "bold"), width=29, state="readonly")
        comMember["values"] = ("Admin Staff", "Student", "Faculty")
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN No:", padx=2, bg="powder blue")
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.prn_var, width=29) 
        txtPRN_No.grid(row=1, column=1, padx=2, pady=6) 

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID No:", padx=2, pady=4, bg="powder blue")
        lblTitle.grid(row=2, column=0, sticky=W) 
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.id_var, width=29) 
        txtTitle.grid(row=2, column=1, padx=2, pady=6)  

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="First Name:", padx=2, pady=4, bg="powder blue")
        lblFirstName.grid(row=3, column=0, sticky=W) 
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width=29) 
        txtFirstName.grid(row=3, column=1, padx=2, pady=6)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Last Name:", padx=2, pady=4, bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W) 
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var, width=29) 
        txtLastName.grid(row=4, column=1, padx=2, pady=6)

        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address1:", padx=2, pady=4, bg="powder blue")
        lblAddress1.grid(row=5, column=0, sticky=W) 
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var, width=29) 
        txtAddress1.grid(row=5, column=1, padx=2, pady=6)

        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address2:", padx=2, pady=4, bg="powder blue")
        lblAddress2.grid(row=6, column=0, sticky=W) 
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address2_var, width=29) 
        txtAddress2.grid(row=6, column=1, padx=2, pady=6)

        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=4, bg="powder blue")
        lblPostCode.grid(row=7, column=0, sticky=W) 
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.postcode_var, width=29) 
        txtPostCode.grid(row=7, column=1, padx=2, pady=6)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=4, bg="powder blue")
        lblMobile.grid(row=8, column=0, sticky=W) 
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width=29) 
        txtMobile.grid(row=8, column=1, padx=2, pady=6)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Id:", padx=2, pady=4, bg="powder blue")
        lblBookId.grid(row=0, column=2, sticky=W) 
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.bookid_var, width=29) 
        txtBookId.grid(row=0, column=3, padx=2, pady=6)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=4, bg="powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W) 
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.booktitle_var, width=29) 
        txtBookTitle.grid(row=1, column=3, padx=2, pady=6)

        lblAuther = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Auther Name:", padx=2, pady=4, bg="powder blue")
        lblAuther.grid(row=2, column=2, sticky=W) 
        txtAuther = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.author_var, width=29) 
        txtAuther.grid(row=2, column=3, padx=2, pady=6)

        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=4, bg="powder blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W) 
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateborrowed_var, width=29) 
        txtDateBorrowed.grid(row=3, column=3, padx=2, pady=6)

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=4, bg="powder blue")
        lblDateDue.grid(row=4, column=2, sticky=W) 
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.datedue_var, width=29) 
        txtDateDue.grid(row=4, column=3, padx=2, pady=6)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=4, bg="powder blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W) 
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.daysonbook_var, width=29) 
        txtDaysOnBook.grid(row=5, column=3, padx=2, pady=6)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=4, bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W) 
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.latereturnfine_var, width=29) 
        txtLateReturnFine.grid(row=6, column=3, padx=2, pady=6)

        lblDateOverDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=4, bg="powder blue")
        lblDateOverDate.grid(row=7, column=2, sticky=W) 
        txtDateOverDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.dateoverdue_var, width=29) 
        txtDateOverDate.grid(row=7, column=3, padx=2, pady=6)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=4, bg="powder blue")
        lblActualPrice.grid(row=8, column=2, sticky=W) 
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.actualprice_var, width=29) 
        txtActualPrice.grid(row=8, column=3, padx=2, pady=6)

        #=================================================DataFrameRight=================================================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=12, 
                                  relief=RIDGE, font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky='ns')

        listBooks = [
            "Automate the Boring Stuff with Python", "Python Crash Course", "Fluent Python", 
            "Learning Python", "Effective Python", "Python Cookbook", "Think Python", 
            "Head-First Python", "Python Programming: An Introduction to Computer Science", 
            "Introduction to Machine Learning with Python", "Python for Data Analysis", 
            "Serious Python", "Python Tricks: A Buffet of Awesome Python Features", 
            "Black Hat Python", "Python Testing with pytest", "Natural Language Processing with Python", 
            "Django for Beginners", "Web Development with Django", "Deep Learning with Python", 
            "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"
        ]

        def Selectbook(event=""):
            try:
                value = str(listBox.get(listBox.curselection()))
                if value == "Automate the Boring Stuff with Python":
                    self.bookid_var.set("BKID5454")
                    self.booktitle_var.set("Automate the Boring Stuff with Python")
                    self.author_var.set("Al Sweigart")
                    
                    d1 = datetime.datetime.today()
                    d2 = d1 + datetime.timedelta(days=15)
                    self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                    self.datedue_var.set(d2.strftime("%d/%m/%Y"))
                    self.daysonbook_var.set(15)
                    self.latereturnfine_var.set("Rs. 50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs. 500")

                elif value == "Python Crash Course":
                    self.bookid_var.set("BKID1234")
                    self.booktitle_var.set("Python Crash Course")
                    self.author_var.set("Eric Matthes")

                    d1 = datetime.datetime.today()
                    d2 = d1 + datetime.timedelta(days=15)
                    self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                    self.datedue_var.set(d2.strftime("%d/%m/%Y"))
                    self.daysonbook_var.set(15)
                    self.latereturnfine_var.set("Rs. 50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs. 600")

                elif value == "Fluent Python":
                    self.bookid_var.set("BKID5678")
                    self.booktitle_var.set("Fluent Python")
                    self.author_var.set("Luciano Ramalho")
                    
                    d1 = datetime.datetime.today()
                    d2 = d1 + datetime.timedelta(days=15)
                    self.dateborrowed_var.set(d1.strftime("%d/%m/%Y"))
                    self.datedue_var.set(d2.strftime("%d/%m/%Y"))
                    self.daysonbook_var.set(15)
                    self.latereturnfine_var.set("Rs. 50")
                    self.dateoverdue_var.set("NO")
                    self.actualprice_var.set("Rs. 700")
                    
            except Exception as e:
                print(f"Error in Selectbook: {e}")

        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", Selectbook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        #=================================================Buttons Frame=================================================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(Framebutton, command=self.fetch_data, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(Framebutton, command=self.update_data, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Framebutton, command=self.delete_data, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset = Button(Framebutton, command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit = Button(Framebutton, command=self.root.quit, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnExit.grid(row=0, column=5)

        #=================================================Information Frame=================================================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        Table_frame = Frame(FrameDetails, bd=12, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, columns=(
            "Member Type", "PRN No", "ID No", "First Name", "Last Name",
            "Address1", "Address2", "Post Code", "Mobile", "Book Id", 
            "Book Title", "Auther Name", "Date Borrowed", "Date Due", 
            "Days On Book", "Late Return Fine", "Date Over Due",
            "Actual Price"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("Member Type", text="Member Type")
        self.library_table.heading("PRN No", text="PRN No") 
        self.library_table.heading("ID No", text="ID No")
        self.library_table.heading("First Name", text="First Name")
        self.library_table.heading("Last Name", text="Last Name")
        self.library_table.heading("Address1", text="Address1")
        self.library_table.heading("Address2", text="Address2")
        self.library_table.heading("Post Code", text="Post Code")
        self.library_table.heading("Mobile", text="Mobile")
        self.library_table.heading("Book Id", text="Book Id")
        self.library_table.heading("Book Title", text="Book Title")
        self.library_table.heading("Auther Name", text="Auther Name")
        self.library_table.heading("Date Borrowed", text="Date Borrowed")
        self.library_table.heading("Date Due", text="Date Due")
        self.library_table.heading("Days On Book", text="Days On Book")
        self.library_table.heading("Late Return Fine", text="Late Return Fine")
        self.library_table.heading("Date Over Due", text="Date Over Due")
        self.library_table.heading("Actual Price", text="Actual Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("Member Type", width=100)
        self.library_table.column("PRN No", width=100)
        self.library_table.column("ID No", width=100)
        self.library_table.column("First Name", width=100)
        self.library_table.column("Last Name", width=100)
        self.library_table.column("Address1", width=100)
        self.library_table.column("Address2", width=100)
        self.library_table.column("Post Code", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("Book Id", width=100)
        self.library_table.column("Book Title", width=100)
        self.library_table.column("Auther Name", width=100)
        self.library_table.column("Date Borrowed", width=100)
        self.library_table.column("Date Due", width=100)
        self.library_table.column("Days On Book", width=100)
        self.library_table.column("Late Return Fine", width=100)
        self.library_table.column("Date Over Due", width=100)
        self.library_table.column("Actual Price", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="vcet123", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.memeber_var.get(),
                    self.prn_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.author_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook_var.get(),
                    self.latereturnfine_var.get(),
                    self.dateoverdue_var.get(),
                    self.actualprice_var.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Member has been inserted successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="vcet123", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']
        
        if row:
            self.memeber_var.set(row[0])
            self.prn_var.set(row[1])
            self.id_var.set(row[2])
            self.firstname_var.set(row[3])
            self.lastname_var.set(row[4])
            self.address1_var.set(row[5])
            self.address2_var.set(row[6])
            self.postcode_var.set(row[7])
            self.mobile_var.set(row[8])
            self.bookid_var.set(row[9])
            self.booktitle_var.set(row[10])
            self.author_var.set(row[11])
            self.dateborrowed_var.set(row[12])
            self.datedue_var.set(row[13])
            self.daysonbook_var.set(row[14])
            self.latereturnfine_var.set(row[15])
            self.dateoverdue_var.set(row[16])
            self.actualprice_var.set(row[17])

    def update_data(self):
        if self.prn_var.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="vcet123", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("update library set MemberType=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostCode=%s,Mobile=%s,BookID=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,ActualPrice=%s where PRN=%s", (
                    self.memeber_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.author_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook_var.get(),
                    self.latereturnfine_var.get(),
                    self.dateoverdue_var.get(),
                    self.actualprice_var.get(),
                    self.prn_var.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record updated successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.prn_var.get() == "":
            messagebox.showerror("Error", "Please select a record to delete")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="vcet123", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("delete from library where PRN=%s", (self.prn_var.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset()
                messagebox.showinfo("Delete", "Record deleted successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset(self):
        self.memeber_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue_var.set("")
        self.actualprice_var.set("")

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()