from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import tkinter as tk
import random

connection = sqlite3.connect('flight_reservation_system.db')
cursor = connection.cursor()


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        main_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.bg = PhotoImage(file="main.png")
        self.bg_image = Label(main_frame, image=self.bg).place(x=00, y=00, relwidth=1, relheight=1)

        def def_login():
            obj = Login(root)

        def def_signup():
            obj = SignUp(root)

        login_btn = Button(main_frame, text="LOGIN", font=("Raleway", 20), command=def_login, bg="#647789",
                           cursor="hand2", fg="white").place(x=278, y=417, height=50, width=300)
        signup_btn = Button(main_frame, text="SIGN UP", font=("Raleway", 20), command=def_signup, bg="#647789",
                            cursor="hand2", fg="white").place(x=703, y=417, height=50, width=300)


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        login_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(login_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        frame_login = Frame(login_frame, bg="white")
        frame_login.place(x=150, y=150, height=370, width=500)

        title = Label(frame_login, text="Login Here", font=("Raleway", 35, "bold"), fg="#1D1D23",
                      bg="white").place(x=30, y=30)
        desc = Label(frame_login, text="Flight Reservation System Login", font=("Dancing Script", 15), fg="#647789",
                     bg="white").place(x=30, y=100)

        lbl_user = Label(frame_login, text="Username/Email", font=("Raleway", 14), fg="#1D1D23", bg="white").place(x=30,
                                                                                                                   y=140)
        email = StringVar()
        self.txt_user = Entry(frame_login, font=("Raleway", 14), textvariable=email, bg="#647789", fg="white")
        self.txt_user.place(x=30, y=170, width=400, height=35)

        lbl_pass = Label(frame_login, text="Password", font=("Raleway", 14), fg="#1D1D23", bg="white").place(x=30,
                                                                                                             y=210)
        passw = StringVar()
        self.txt_pass = Entry(frame_login, show="*", font=("Raleway", 15), textvariable=passw, bg="#647789", fg="white")
        self.txt_pass.place(x=30, y=240, width=400, height=35)

        def def_signup():
            obj = SignUp(root)

        def def_Home():
            if len(email.get()) == 0:
                messagebox.showwarning("Empty fields", "Username/Email is not entered.")
            elif len(passw.get()) == 0:
                messagebox.showwarning("Empty fields", "Password is not entered.")

            else:
                check = cursor.execute("SELECT * FROM USER WHERE Email = ?", (email.get(),))
                data = cursor.fetchone()
                if data != None:
                    if data[3] == passw.get():
                        messagebox.showinfo("Logged In", "You have been logged in successfully.")
                        call = Home(root, email.get())
                    else:
                        messagebox.showerror("Error", "Incorrect Password.")
                else:
                    messagebox.showerror("Error", "Account does not exist.")

        forget_btn = Button(frame_login, text="Forgot Password?", font=("Raleway", 9), cursor="hand2", bg="white",
                            fg="#647789").place(x=30, y=290)
        go_to_signup_btn = Button(frame_login, text="Don't have an account? Sign Up here.", font=("Raleway", 9),
                                  command=def_signup, cursor="hand2", bg="white", fg="#647789").place(x=150, y=290)
        login_btn = Button(login_frame, text="LOGIN", font=("Raleway", 20), bg="#647789", cursor="hand2", fg="white",
                           command=def_Home).place(x=250, y=495, height=50, width=300)

        login_frame.pack()


class SignUp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        signup_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(signup_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        frame_signup = Frame(signup_frame, bg="white")
        frame_signup.place(x=150, y=60, height=550, width=500)

        title = Label(frame_signup, text="Sign Up Here", font=("Raleway", 35, "bold"), fg="#1D1D23",
                      bg="white").place(x=30, y=15)
        desc = Label(frame_signup, text="Flight Reservation System Sign Up", font=("Dancing Script", 15), fg="#647789",
                     bg="white").place(x=30, y=83)

        lbl_f_name = Label(frame_signup, text="First Name", font=("Raleway", 14), fg="#1D1D23", bg="white").place(x=30,
                                                                                                                  y=120)
        f_name = StringVar()
        self.f_name_entry = Entry(frame_signup, font=("Raleway", 14), textvariable=f_name, bg="#647789", fg="white")
        self.f_name_entry.place(x=30, y=150, width=195, height=35)

        lbl_l_name = Label(frame_signup, text="Last Name", font=("Raleway", 14), fg="#1D1D23", bg="white").place(x=235,
                                                                                                                 y=120)
        l_name = StringVar()
        self.l_name_entry = Entry(frame_signup, font=("Raleway", 14), textvariable=l_name, bg="#647789", fg="white")
        self.l_name_entry.place(x=235, y=150, width=195, height=35)

        lbl_email = Label(frame_signup, text="Email", font=("Raleway", 14), fg="#1D1D23", bg="white").place(x=30, y=190)
        email = StringVar()
        self.email_entry = Entry(frame_signup, font=("Raleway", 14), textvariable=email, bg="#647789", fg="white")
        self.email_entry.place(x=30, y=220, width=400, height=35)

        lbl_phone1 = Label(frame_signup, text="Phone Number", font=("Raleway", 14), fg="#1D1D23",
                           bg="white").place(x=30, y=260)
        phone1 = StringVar()
        self.phone_entry = Entry(frame_signup, font=("Raleway", 14), textvariable=phone1, bg="#647789", fg="white")
        self.phone_entry.place(x=30, y=290, width=195, height=35)

        lbl_phone2 = Label(frame_signup, text="Alt. Phone No. (opt)", font=("Raleway", 14), fg="#1D1D23",
                           bg="white").place(x=235, y=260)
        phone2 = StringVar()
        phone2.set("")
        self.phone_entry = Entry(frame_signup, font=("Raleway", 14), textvariable=phone2, bg="#647789", fg="white")
        self.phone_entry.place(x=235, y=290, width=195, height=35)

        lbl_date = Label(frame_signup, text="Date of Birth", font=("Raleway", 14), fg="#1D1D23",
                         bg="white").place(x=30, y=330)
        cal = StringVar()
        self.cal_entry = DateEntry(frame_signup, width=12, font=("Raleway", 10), textvariable=cal, fg="#1D1D23",
                                   bg="white",
                                   borderwidth=2)
        self.cal_entry.place(x=30, y=360, width=400, height=35)

        lbl_passw = Label(frame_signup, text="Password", font=("Raleway", 14), fg="#1D1D23",
                          bg="white").place(x=30, y=400)
        passw = StringVar()
        self.passw_entry = Entry(frame_signup, show="*", font=("Raleway", 14), textvariable=passw, bg="#647789",
                                 fg="white")
        self.passw_entry.place(x=30, y=430, width=195, height=35)

        lbl_con_pass = Label(frame_signup, text="Confirm Password", font=("Raleway", 14), fg="#1D1D23",
                             bg="white").place(x=235, y=400)
        con_pass = StringVar()
        self.con_pass_entry = Entry(frame_signup, show="*", font=("Raleway", 14), textvariable=con_pass, bg="#647789",
                                    fg="white")
        self.con_pass_entry.place(x=235, y=430, width=195, height=35)

        def def_login():
            obj = Login(root)

        def insert_user():
            if len(f_name.get()) == 0:
                messagebox.showwarning("Empty fields", "First Name is not entered.")
            elif len(l_name.get()) == 0:
                messagebox.showwarning("Empty fields", "Last Name is not entered.")
            elif len(email.get()) == 0:
                messagebox.showwarning("Empty fields", "Email is not entered.")
            elif len(phone1.get()) == 0:
                messagebox.showwarning("Empty fields", "Phone Number is not entered.")
            elif len(passw.get()) == 0:
                messagebox.showwarning("Empty fields", "Password is not entered.")
            elif len(con_pass.get()) == 0:
                messagebox.showwarning("Empty fields", "Password is not entered again.")

            else:
                if phone2.get() != "":
                    if phone2.get() == phone1.get():
                        messagebox.showwarning("Repeat Entry", "You have entered the same number twice.")

                    elif phone2.get() != "" and phone2.get() != phone1.get():
                        if passw.get() == con_pass.get():
                            if messagebox.askokcancel("Create Account", "Do you want to create an account?"):
                                messagebox.showinfo("Account Created", "Account created successfully. Login to use your account"
                                                                       ".")
                                cursor.execute("INSERT INTO USER VALUES(?,?,?,?,?)", (email.get(), f_name.get(), l_name.get(),
                                                                                      passw.get(), cal.get()))
                                connection.commit()
                                cursor.execute("INSERT INTO USER_PHONENO VALUES(?,?)", (email.get(), phone1.get()))
                                connection.commit()
                                cursor.execute("INSERT INTO USER_PHONENO VALUES(?,?)", (email.get(), phone2.get()))
                                connection.commit()
                                def_login()
                        else:
                            messagebox.showerror("Error", "Passwords do not match.")

                elif phone2.get() == "":
                    if passw.get() == con_pass.get():
                        if messagebox.askokcancel("Create Account", "Do you want to create an account?"):
                            messagebox.showinfo("Account Created",
                                                        "Account created successfully. Login to use your account"
                                                        ".")
                            cursor.execute("INSERT INTO USER VALUES(?,?,?,?,?)", (email.get(), f_name.get(),
                                                                                  l_name.get(), passw.get(), cal.get()))
                            connection.commit()
                            cursor.execute("INSERT INTO USER_PHONENO VALUES(?,?)", (email.get(), phone1.get()))
                            connection.commit()
                            def_login()
                    else:
                        messagebox.showerror("Error", "Passwords do not match.")


        go_to_signup_btn = Button(frame_signup, text="Already have an account? Login here.", font=("Raleway", 9),
                                  command=def_login, cursor="hand2", bg="white", fg="#647789").place(x=30, y=480)
        signup_btn = Button(signup_frame, text="SIGN UP", font=("Raleway", 20), command=insert_user, bg="#647789",
                            cursor="hand2",
                            fg="white").place(x=250, y=585, height=50, width=300)

        signup_frame.pack()


class Home:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)
        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_profile).place(x=-10, y=400, height=50, width=220)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_home = Frame(home_frame, bg="white")
        frame_home.place(x=300, y=225, height=200, width=750)

        heading = Label(frame_home, text="Welcome,", bg="White", font=("Raleway", 40, "bold")).place(x=20, y=10)

        cursor.execute("SELECT * FROM USER WHERE Email = ?", (self.email,))
        data = cursor.fetchone()
        name = data[1]
        n = StringVar()
        n.set(name)

        heading1 = Label(frame_home, textvariable=n, bg="White", font=("Raleway", 40, "bold")).place(x=290, y=10)
        heading2 = Label(frame_home, text="Kindly select your preference from the Side Menu.", bg="White",
                         font=("Raleway", 20,
                               "bold")).place(x=20, y=100)

        home_frame.pack()


class Book:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)
        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20, "bold"), bg="white", cursor="hand2",
                             fg="#1D1D23", command=Call_book).place(x=-10, y=40, height=50, width=240)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_profile).place(x=-10, y=400, height=50, width=220)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_book = Frame(self.root, bg="white")
        frame_book.place(x=300, y=40, height=580, width=840)

        Label_heading = Label(frame_book, text="Book a Flight", font=('Raleway', 40, "bold"), bg="White").place(x=20, y=10)
        from_label = Label(frame_book, text="From:", font=('Raleway', 20), bg="White").place(x=20, y=100)
        to_label = Label(frame_book, text="To:", font=('Raleway', 20), bg="White").place(x=20, y=140)

        from_var = StringVar()
        to_var = StringVar()

        from_combobox = ttk.Combobox(frame_book, width=27, font=("Raleway", 15), textvariable=from_var)

        from_combobox['values'] = ('Delhi', 'Mumbai', 'Pune', 'Hyderabad')

        from_combobox.place(x=100, y=100, height=40, width=200)

        from_combobox.current()

        to_combobox = ttk.Combobox(frame_book, width=27, font=("Raleway", 15), textvariable=to_var)
        to_combobox['values'] = ('Delhi', 'Mumbai', 'Pune', 'Hyderabad')
        to_combobox.place(x=100, y=140, height=40, width=200)

        to_combobox.current()

        date = StringVar()
        date_of_departure = Label(frame_book, text="Date of Departure:", font=('Raleway', 20), bg="White").place(x=20,
                                                                                                             y=180)

        date_entry = DateEntry(frame_book, width=12, font=("Raleway", 15), textvariable=date).place(x=150, y=220, height=35, width=150)
        label_format = Label(frame_book, text="MM/DD/YY", font=('Raleway', 15), bg="White").place(x=20, y=220)

        dash = Label(frame_book, text="_______________________________________________________",
                     font=("Raleway", 20), fg="#647789", bg="white").place(x=20, y=280)

        label = Label(frame_book, text="Enter the flight number of the selected flight:", font=('Raleway', 20),
                      bg="White").place(x=20, y=325)
        t = StringVar()
        label_entry = Entry(frame_book, textvariable=t, font=("Raleway", 14), bg="#647789",
                            fg="white").place(x=600, y=325, width=200, height=40)
        passenger_var = IntVar()
        pasengers = Label(frame_book, text="Number of passengers:", font=('Raleway', 20), bg="White").place(x=20, y=370)
        passenger_entry = Entry(frame_book, textvariable=passenger_var, font=("Raleway", 15), bg="#647789",
                                fg="white").place(x=320, y=370, width=100, height=40)
        passenger_var.set(1)

        def btn2():

            print("r=", self.r)
            a = from_var.get()
            b = to_var.get()
            c = date.get()
            d = t.get()
            e = passenger_var.get()
            cursor.execute("select * from flights where flight_number=(?) and Date_depart=(?) and origin=(?) and "
                           "destination=(?)", (d, c, a, b))
            data = cursor.fetchone()
            h = data[4]
            i = data[5]
            j = data[6]
            if e == 0 or e == "":
                messagebox.showinfo("Incomplete data", "Please enter the number of passenger")

            elif e >= 1:
                obj = passengerdetails(root, a, b, c, d, e, self.v, h, i, j, email)

        def btn1():

            if from_var.get() == "":
                messagebox.showinfo("Incomplete data", "Please enter the origin")
            elif to_var.get() == "":
                messagebox.showinfo("Incomplete data", "Please enter the destination")
            elif date.get() == "":
                messagebox.showinfo("Incomplete data", "Please enter the date of departure")
            else:
                a = str(from_var.get())
                b = to_var.get()
                c = date.get()
                create_list(a, b, c)

        search_flight_btn = Button(frame_book, text="Search Flights", command=btn1, font=("Raleway", 18), bg="#647789",
                                   cursor="hand2", fg="white").place(x=20, y=260, height=40, width=280)
        book_flight_btn = Button(frame_book, text="Click Here to Add Passenger Details", command=btn2, font=("Raleway", 18), bg="#647789", cursor="hand2",
                                 fg="white").place(x=20, y=520, height=40, width=800)

        def create_list(a, b, c):
            cursor.execute("select * from flights where origin=? and destination=? and Date_depart=?", (a, b, c))
            check = cursor.fetchone()
            cursor.execute("select * from flights where origin=? and destination=? and Date_depart=?", (a, b, c))
            data = cursor.fetchall()
            if check is None:
                messagebox.showerror("Flights Unavailable", "No flights are available on the entered date.")

            frame5 = Frame(frame_book)
            tree = ttk.Treeview(frame5, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"),
                                show='headings')
            scrollbar = Scrollbar(frame5, orient=HORIZONTAL)
            tree.config(xscrollcommand=scrollbar.set)
            scrollbar.config(command=tree.xview)
            scrollbar.pack(side=BOTTOM, fill=BOTH)
            tree.column("#1", anchor=tk.CENTER)
            tree.heading("#1", text="Flight Number")
            tree.column("#2", anchor=tk.CENTER)
            tree.heading("#2", text="Origin")
            tree.column("#3", anchor=tk.CENTER)
            tree.heading("#3", text="Destination")
            tree.column("#4", anchor=tk.CENTER)
            tree.heading("#4", text="Date of Departure")
            tree.column("#5", anchor=tk.CENTER)
            tree.heading("#5", text="Date of Arrival")
            tree.column("#6", anchor=tk.CENTER)
            tree.heading("#6", text="Time of Departure")
            tree.column("#7", anchor=tk.CENTER)
            tree.heading("#7", text="Time of Arrival")
            tree.column("#8", anchor=tk.CENTER)
            tree.heading("#8", text="Seats Booked")
            tree.column("#9", anchor=tk.CENTER)
            tree.heading("#9", text="Seats Available")
            tree.column("#10", anchor=tk.CENTER)
            tree.heading("#10", text="Price")
            tree.pack()
            for row in data:
                print(row)
                tree.insert("", tk.END, values=row)

            frame5.place(x=310, y=100, height=200, width=510)

        label_fares = Label(frame_book, text="Special Fares:", font=('Raleway', 20), bg="White").place(x=20, y=420)
        self.v = IntVar()
        self.v.set(0)
        r1 = Radiobutton(frame_book, text="Armed Forces", variable=self.v, value=1, font=('Raleway', 18), bg="White").place(
            x=200, y=420)
        r2 = Radiobutton(frame_book, text="Students", variable=self.v, value=2, font=('Raleway', 18), bg="White").place(
            x=400, y=420)
        r3 = Radiobutton(frame_book, text="Medical", variable=self.v, value=3, font=('Raleway', 18), bg="White").place(
            x=600,y=420)
        r4 = Radiobutton(frame_book, text="Infants", variable=self.v, value=4, font=('Raleway', 18), bg="White").place(
            x=200, y=460)
        r5 = Radiobutton(frame_book, text="None", variable=self.v, value=5, font=('Raleway', 18), bg="White").place(
            x=400, y=460)
        self.r = self.v.get()

        home_frame.pack()


class passengerdetails:
    def __init__(self, root, a, b, c, d, e, r, h, i, j, email):
        self.root = root
        self.root.title("Passenger Details")

        frame3 = Frame(self.root, bg="red").place(x=0, y=0, height=1080, width=1920)
        self.image1 = PhotoImage(file="bg.png")

        self.image_label = Label(frame3, image=self.image1).place(x=0, y=0, relheight=1, relwidth=1)
        self.email = email
        frame1 = Frame(frame3, bg="white")
        self.fromplace = a
        self.to = b
        self.date = c
        self.id = d
        self.e = int(e)
        self.g = e
        print(self.e)
        self.details = []
        self.name_var = StringVar()
        self.DOB_var = StringVar()
        self.nationality_var = StringVar()
        self.v = IntVar()
        self.h = h
        self.i = i
        self.j = j
        self.r = r
        self.age_var = IntVar()
        sp = self.r.get()
        print("r=", self.r.get())

        def btn5():
            if messagebox.askokcancel("Cancel Booking", "Are you sure you want to go cancel the current booking?"):
                obj = Home(root, email)

        self.home_button = Button(self.root, text="Cancel Booking", command=btn5, font=("Raleway", 18), bg="#647789",
                                  cursor="hand2", fg="white").place(x=1080, y=20, height=40, width=200)

        def btn4():
            if len(self.name_var.get()) == 0:
                messagebox.showwarning("Empty fields", "Name is not entered.")
            elif len(self.DOB_var.get()) == 0:
                messagebox.showwarning("Empty fields", "Date of Birth is not entered.")
            elif len(self.nationality_var.get()) == 0:
                messagebox.showwarning("Empty fields", "Nationality is not entered.")
            elif self.age_var.get() == 0:
                messagebox.showwarning("Empty fields", "Age is not entered.")
            elif self.v.get() == 0:
                messagebox.showwarning("Empty fields", "Gender is not selected.")

            else:
                g = self.v.get()
                if g == 1:
                    self.details.append((str(self.name_var.get()), str(self.DOB_var.get()), str(self.nationality_var.get()),
                                         "Male", int(self.age_var.get())))
                elif g == 2:
                    self.details.append((str(self.name_var.get()), str(self.DOB_var.get()), str(self.nationality_var.get()),
                                         "Female", int(self.age_var.get())))
                print("age", self.age_var.get())
                self.name_var.set("")
                self.DOB_var.set("")
                self.nationality_var.set("")
                self.age_var.set("")
                if self.e > 0:
                    btn3()

                else:
                    print(self.details)
                    obj = confirmbooking(root, a, b, c, d, e, self.details, sp, h, i, j, email)

        def btn3():
            labe_heading = Label(frame1, text="Enter Passenger Details", font=('Raleway', 40, "bold"), bg="White").place(x=20,
                                                                                                                  y=20)
            name_label = Label(frame1, text="Name:", font=('Raleway', 20), bg="White").place(x=20, y=120)
            DOB_label = Label(frame1, text="Date of Birth:", font=('Raleway', 20), bg="White").place(x=20, y=170)
            Nationality = Label(frame1, text="Nationality:", font=('Raleway', 20), bg="White").place(x=20, y=220)
            age_label = Label(frame1, text="Age:", font=('Raleway', 20), bg="White").place(x=20, y=320)

            name_entry = Entry(frame1, textvariable=self.name_var, font=("Raleway", 14), bg="#647789",
                               fg="white").place(x=200, y=120, width=300, height=40)
            DOB_entry = DateEntry(frame1, textvariable=self.DOB_var, font=("Raleway", 14), bg="#647789",
                                  fg="white").place(x=200, y=170, width=300, height=40)
            Nationality_entry = Entry(frame1, textvariable=self.nationality_var, font=("Raleway", 14), bg="#647789",
                                      fg="white").place(x=200, y=220, width=400, height=40)
            Gender_label = Label(frame1, text="Gender:", font=('Raleway', 20), bg="White").place(x=20, y=270)

            age_entry = Entry(frame1, textvariable=self.age_var, font=("Raleway", 14), bg="#647789", fg="white").place(
                x=200, y=320, width=400, height=40)

            r1 = Radiobutton(frame1, text="Male", variable=self.v, value=1, font=('Raleway', 20), bg="White").place(
                x=200, y=265)
            r2 = Radiobutton(frame1, text="Female", variable=self.v, value=2, font=('Raleway', 20), bg="White").place(
                x=320, y=265)

            next_btn = Button(self.root, text="Next", command=btn4, font=("Raleway", 18), bg="#647789", cursor="hand2",
                              fg="white").place(x=250, y=480, height=40, width=500)
            self.e = self.e - 1

            print("name=", self.name_var.get())

            print(self.v.get())

        btn3()
        frame1.place(x=100, y=100, height=400, width=800)


class confirmbooking:
    def __init__(self, root, a, b, c, d, e, details, sp, h, i, j, email):
        self.root = root
        self.root.title("Flight details")

        frame3 = Frame(self.root, bg="red").place(x=0, y=0, height=1080, width=1920)
        self.image1 = PhotoImage(file="bg.png")
        self.email = email
        self.image_label = Label(frame3, image=self.image1).place(x=0, y=0, relheight=1, relwidth=1)
        self.fromplace = a
        self.to = b
        self.date = c
        self.id = d
        self.e = int(e)
        self.g = e
        self.details = details
        # self.r=r
        self.sp = sp
        s1 = StringVar()
        s2 = StringVar()
        self.h = h
        self.i = i
        self.j = j
        self.details = details
        frame1 = Frame(frame3, bg="white")
        def btn7():
            if messagebox.askokcancel("Cancel Booking", "Are you sure you want to go cancel the current booking?"):
                obj = Home(root, email)
        self.home_button = Button(self.root, text="Cancel Booking", command=btn7, font=("Raleway", 18), bg="#647789",
                                  cursor="hand2", fg="white").place(x=1080, y=20, height=40, width=200)
        label = Label(frame1, text="Confirm Booking", font=('Raleway', 40, "bold"), bg="White").place(x=20, y=20)
        from_label = Label(frame1, text="Origin:", font=('Raleway', 20), bg="White").place(x=20, y=100)
        to_label = Label(frame1, text="Destination:", font=('Raleway', 20), bg="White").place(x=420, y=100)
        name_label = Label(frame1, text="Passengers:", font=('Raleway', 20), bg="White").place(x=20, y=250)
        date = StringVar()
        date_label = Label(frame1, text="Date of Departure:", font=('Raleway', 20), bg="White").place(x=20, y=150)
        date_label_arr = Label(frame1, text="Date of Arrival:", font=('Raleway', 20), bg="White").place(x=420, y=150)
        date_entry = Label(frame1, width=12, textvariable=date, font=("Raleway", 14), bg="#647789", fg="white").place(
            x=270, y=150, width=100, height=40)
        date_arr = StringVar()
        time_d = StringVar()
        time_a = StringVar()
        date_entry_arr = Label(frame1, width=12, textvariable=date_arr, font=("Raleway", 14), bg="#647789",
                               fg="white").place(x=620, y=150, width=100, height=40)
        time_label_d = Label(frame1, text="Time of Departure:", font=('Raleway', 20), bg="White").place(x=20, y=200)
        time_entry_d = Label(frame1, width=12, textvariable=time_d, font=("Raleway", 14), bg="#647789",
                             fg="white").place(x=270, y=200, width=100, height=40)
        time_label_a = Label(frame1, text="Time of Arrival:", font=('Raleway', 20), bg="White").place(x=420, y=200)
        time_entry_a = Label(frame1, width=12, textvariable=time_a, font=("Raleway", 14), bg="#647789",
                             fg="white").place(x=620, y=200, width=100, height=40)
        date.set(self.date)
        date_arr.set(self.h)
        time_d.set(self.i)
        time_a.set(self.j)
        from_Entry = Label(frame1, width=12, textvariable=s1, font=("Raleway", 14), bg="#647789", fg="white").place(
            x=270, y=100, width=100, height=40)
        s1.set(a)
        to_Entry = Label(frame1, width=12, textvariable=s2, font=("Raleway", 14), bg="#647789",
                         fg="white").place(x=620, y=100, width=100, height=40)
        s2.set(b)

        frame5 = Frame(frame1)

        tree = ttk.Treeview(frame5, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
        scrollbar = Scrollbar(frame5, orient=HORIZONTAL)
        tree.config(xscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.xview)
        scrollbar.pack(side=BOTTOM, fill=BOTH)
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="Name")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="DOB")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Nationality")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Gender")
        tree.column("#5", anchor=tk.CENTER)
        tree.heading("#5", text="Age")

        tree.pack()
        for row in self.details:
            print(row)
            tree.insert("", tk.END, values=row)

        frame5.place(x=20, y=300, height=100, width=760)
        frame1.place(x=100, y=100, height=460, width=800)

        def btn5():
            pnr = random.randrange(100, 1000, 1)
            cursor.execute("select PNR from Bookings")
            data = cursor.fetchall()

            # if data is not None:

            # print("data=", data)
            # print("data[0]=", data[0])
            l1 = []
            for i in data:
                l1.append(int(i[0]))
            print("l1=", l1)
            while pnr in l1:
                pnr = random.randrange(100, 1000)
            print(pnr)

            cursor.execute("select price from flights where origin=? and destination=? and Date_depart=?",
                           (self.fromplace, self.to, self.date))
            price = cursor.fetchone()
            print("price=", price)
            totalamt = self.e * price[0]

            cursor.execute("select flight_number from flights where origin=? and destination=? and Date_depart=?",
                           (self.fromplace, self.to, self.date))
            flight_num = cursor.fetchone()
            flight_no = flight_num[0]
            print("flight_nuum=", flight_num)
            if sp == 1:
                totalamt = totalamt - totalamt * 0.1 * self.e
                s = "Armed forces"
            elif sp == 2:
                totalamt = totalamt - totalamt * 0.2 * self.e
                s = "Student"
            elif sp == 3:
                totalamt = totalamt - totalamt * 0.3 * self.e
                s = "Medical"
            elif sp == 4:
                totalamt = totalamt - totalamt * 0.4 * self.e
                s = "Infants"
            else:
                totalamt = totalamt
                s = "None"
            print(pnr, self.sp, totalamt, self.e, self.email, flight_no)
            pnr = str(pnr)
            cursor.execute("insert into Bookings values(?,?,?,?,?,?)",
                           (pnr, s, totalamt, self.e, self.email, flight_no))
            connection.commit()
            print(self.details)
            for i in self.details:
                t = random.randrange(1000, 2000, 1)
                cursor.execute("select Ticket_no from Passengers")
                data = cursor.fetchall()
                l2 = []

                for j in data:
                    l2.append(j[0])
                while (t in l2):
                    t = random.randrange(1000, 2000, 1)
                print(i)
                l = 10

                cursor.execute("insert into Passengers values(?,?,?,?,?,?,?)", (t, i[0], i[1], i[3], i[4], i[2], pnr))
                connection.commit()

            cursor.execute("update flights set seats_booked=seats_booked+(?)", (self.e,))
            cursor.execute("update flights set seats_available=seats_available-(?)", (self.e,))
            connection.commit()

            obj = Home(root, email)

        confirmbooking = Button(self.root, text="Confirm Booking", command=btn5, font=("Raleway", 18), bg="#647789",
                                cursor="hand2", fg="white").place(x=120, y=505, height=40, width=760)


class MyBookings:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)
        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20, "bold"), bg="white",
                                 cursor="hand2",
                                 fg="#1D1D23", command=Call_bookings).place(x=-10, y=130, height=50, width=240)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_profile).place(x=-10, y=400, height=50, width=220)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_flightstatus = Frame(self.root, bg="white")
        frame_flightstatus.place(x=300, y=40, height=580, width=840)

        flightstatus = Label(frame_flightstatus, text="My Bookings", bg="White", font=('Raleway', 40,
                                                                                       "bold")).place(x=20, y=10)
        frame_list1 = Frame(frame_flightstatus, bg="white")
        frame_list1.place(x=20, y=100, height=90, width=760)

        cursor.execute("SELECT PNR, f.flight_number, origin, destination, no_of_passengers, totalamt, Date_depart, "
                       "Time_depart, Date_arrival, Time_arrival, sp FROM FLIGHTS f inner JOIN Bookings b on "
                       "f.flight_number = b.flight_number where email = (?)", (self.email,))
        data = cursor.fetchall()
        tree = ttk.Treeview(frame_list1, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11",),
                            show='headings')
        scrollbar = Scrollbar(frame_list1, orient=HORIZONTAL)
        tree.config(xscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.xview)
        scrollbar.pack(side=BOTTOM, fill=BOTH)
        tree.column("#1", anchor=tk.CENTER)
        tree.heading("#1", text="PNR")
        tree.column("#2", anchor=tk.CENTER)
        tree.heading("#2", text="Flight Number")
        tree.column("#3", anchor=tk.CENTER)
        tree.heading("#3", text="Origin")
        tree.column("#4", anchor=tk.CENTER)
        tree.heading("#4", text="Destination")
        tree.column("#5", anchor=tk.CENTER)
        tree.heading("#5", text="No. of Passengers")
        tree.column("#6", anchor=tk.CENTER)
        tree.heading("#6", text="Total Amount")
        tree.column("#7", anchor=tk.CENTER)
        tree.heading("#7", text="Date of Departure")
        tree.column("#8", anchor=tk.CENTER)
        tree.heading("#8", text="Time of Departure")
        tree.column("#9", anchor=tk.CENTER)
        tree.heading("#9", text="Date of Arrival")
        tree.column("#10", anchor=tk.CENTER)
        tree.heading("#10", text="Time of Arrival")
        tree.column("#11", anchor=tk.CENTER)
        tree.heading("#11", text="Special Fare")
        tree.pack()
        for row in data:
            print(row)
            tree.insert("", tk.END, values=row)

        def status():
            cursor.execute("SELECT * FROM BOOKINGS WHERE PNR = ?", (pnr.get(),))
            data = cursor.fetchone()
            if data != None:
                sp = StringVar()
                sp.set(data[1])
                total = StringVar()
                total.set(data[2])
                no = StringVar()
                if data[3] == "":
                    no = "None"
                else:
                    no.set(data[3])
                flight_no = StringVar()
                flight_no.set(data[5])

                cursor.execute("SELECT * FROM FLIGHTS WHERE flight_number = ?", (flight_no.get(),))
                data2 = cursor.fetchone()
                Origin = StringVar()
                Origin.set(data2[1])
                dest = StringVar()
                dest.set(data2[2])
                dod = StringVar()
                dod.set(data2[3])
                doa = StringVar()
                doa.set(data2[4])
                tod = StringVar()
                tod.set(data2[5])
                toa = StringVar()
                toa.set(data2[6])

                pnr_display = Label(frame_flightstatus, text="PNR:", font=('Raleway', 20),
                                    bg="White").place(x=20, y=265)
                pnr_display2 = Label(frame_flightstatus, textvariable=pnr, font=('Raleway', 20),
                                     bg="White").place(x=120, y=265)
                Origin_display = Label(frame_flightstatus, text="Origin:", font=('Raleway', 20),
                                       bg="White").place(x=20, y=305)
                Origin_display2 = Label(frame_flightstatus, textvariable=Origin, font=('Raleway', 20),
                                        bg="White").place(x=120, y=305)
                no_display = Label(frame_flightstatus, text="No of Passengers:", font=('Raleway', 20),
                                   bg="White").place(x=20, y=345)
                no_display2 = Label(frame_flightstatus, textvariable=no, font=('Raleway', 20),
                                    bg="White").place(x=260, y=345)
                dod_display = Label(frame_flightstatus, text="Date of Departure:", font=('Raleway', 20),
                                    bg="White").place(x=20, y=385)
                dod_display2 = Label(frame_flightstatus, textvariable=dod, font=('Raleway', 20),
                                     bg="White").place(x=260, y=385)
                tod_display = Label(frame_flightstatus, text="Time of Departure:", font=('Raleway', 20),
                                    bg="White").place(x=20, y=425)
                tod_display2 = Label(frame_flightstatus, textvariable=tod, font=('Raleway', 20),
                                     bg="White").place(x=260, y=425)

                flight_no_display = Label(frame_flightstatus, text="Flight No:", font=('Raleway', 20),
                                          bg="White").place(x=420, y=265)
                flight_no_display2 = Label(frame_flightstatus, textvariable=flight_no, font=('Raleway', 20),
                                           bg="White").place(x=620, y=265)
                dest_display = Label(frame_flightstatus, text="Destination:", font=('Raleway', 20),
                                     bg="White").place(x=420, y=305)
                dest_display2 = Label(frame_flightstatus, textvariable=dest, font=('Raleway', 20),
                                      bg="White").place(x=620, y=305)
                total_display = Label(frame_flightstatus, text="Total Amount:", font=('Raleway', 20),
                                      bg="White").place(x=420, y=345)
                total_display2 = Label(frame_flightstatus, textvariable=total, font=('Raleway', 20),
                                       bg="White").place(x=620, y=345)
                doa_display = Label(frame_flightstatus, text="Date of Arrival:", font=('Raleway', 20),
                                    bg="White").place(x=420, y=385)
                doa_display2 = Label(frame_flightstatus, textvariable=doa, font=('Raleway', 20),
                                     bg="White").place(x=620, y=385)
                toa_display = Label(frame_flightstatus, text="Time of Arrival:", font=('Raleway', 20),
                                    bg="White").place(x=420, y=425)
                toa_display2 = Label(frame_flightstatus, textvariable=toa, font=('Raleway', 20),
                                     bg="White").place(x=620, y=425)

                frame_list2 = Frame(frame_flightstatus, bg="white")
                frame_list2.place(x=20, y=465, height=105, width=760)

                cursor.execute("SELECT * FROM Passengers where PNR=(?)", (pnr.get(),))
                data2 = cursor.fetchall()
                tree = ttk.Treeview(frame_list2,
                                    column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
                scrollbar = Scrollbar(frame_list2, orient=HORIZONTAL)
                tree.config(xscrollcommand=scrollbar.set)
                scrollbar.config(command=tree.xview)
                scrollbar.pack(side=BOTTOM, fill=BOTH)
                tree.column("#1", anchor=tk.CENTER)
                tree.heading("#1", text="Ticket No.")
                tree.column("#2", anchor=tk.CENTER)
                tree.heading("#2", text="Passenger Name")
                tree.column("#3", anchor=tk.CENTER)
                tree.heading("#3", text="Date of Birth")
                tree.column("#4", anchor=tk.CENTER)
                tree.heading("#4", text="Gender")
                tree.column("#5", anchor=tk.CENTER)
                tree.heading("#5", text="Age")
                tree.column("#6", anchor=tk.CENTER)
                tree.heading("#6", text="Nationality")
                tree.column("#7", anchor=tk.CENTER)
                tree.heading("#7", text="PNR")
                tree.pack()
                for row in data2:
                    print(row)
                    tree.insert("", tk.END, values=row)



            else:
                messagebox.showerror("Error", "Booking does not exist.")

        pnr = StringVar()
        pnr_label = Label(frame_flightstatus, text="Enter your PNR number:", font=('Raleway', 20),
                          bg="White").place(x=20, y=225)
        pnr_entry = Entry(frame_flightstatus, font=("Raleway", 14), textvariable=pnr, bg="#647789",
                          fg="white").place(x=340, y=225, width=270, height=40)

        show_btn = Button(frame_flightstatus, text="Show Details", font=("Raleway", 18), bg="#647789", cursor="hand2",
                          fg="white", command=status).place(x=620, y=225, height=40, width=200)

        dash = Label(frame_flightstatus, text="______________________________________________________________________"
                                              "_______________________________________",
                     font=("Raleway", 10), fg="#647789", bg="white").place(x=20, y=190)

        home_frame.pack()


class Status:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)

        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20, "bold"), bg="white",
                               cursor="hand2",
                               fg="#1D1D23", command=Call_status).place(x=-10, y=220, height=50, width=240)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_profile).place(x=-10, y=400, height=50, width=220)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_flightstatus = Frame(self.root, bg="white")
        frame_flightstatus.place(x=300, y=110, height=440, width=840)

        flightstatus = Label(frame_flightstatus, text="Flight Status", bg="White", font=('Raleway', 40,
                                                                                         "bold")).place(x=20, y=10)

        no = StringVar()
        no_label = Label(frame_flightstatus, text="Enter the Flight No.:", font=('Raleway', 20),
                         bg="White").place(x=20, y=100)
        no_entry = Entry(frame_flightstatus, font=("Raleway", 14), textvariable=no, bg="#647789",
                         fg="white").place(x=20, y=140, width=400, height=40)

        def status():
            cursor.execute("SELECT * FROM Flights WHERE flight_number = ?", (no.get(),))
            data2 = cursor.fetchone()
            if data2 != None:
                Origin = StringVar()
                Origin.set(data2[1])
                dest = StringVar()
                dest.set(data2[2])
                dod = StringVar()
                dod.set(data2[3])
                doa = StringVar()
                doa.set(data2[4])
                tod = StringVar()
                tod.set(data2[5])
                toa = StringVar()
                toa.set(data2[6])
                sa = StringVar()
                sa.set(data2[8])
                sb = StringVar()
                sb.set(data2[7])
                price = StringVar()
                price.set(data2[9])

                flight_no_display = Label(frame_flightstatus, text="Flight No:", font=('Raleway', 20),
                                          bg="White").place(x=20, y=220)
                flight_no_display2 = Label(frame_flightstatus, textvariable=no, font=('Raleway', 20),
                                           bg="White").place(x=160, y=220)
                Origin_display = Label(frame_flightstatus, text="Origin:", font=('Raleway', 20),
                                       bg="White").place(x=20, y=260)
                Origin_display2 = Label(frame_flightstatus, textvariable=Origin, font=('Raleway', 20),
                                        bg="White").place(x=160, y=260)
                sa_display = Label(frame_flightstatus, text="Seats Available:", font=('Raleway', 20),
                                   bg="White").place(x=20, y=300)
                sa_display2 = Label(frame_flightstatus, textvariable=sa, font=('Raleway', 20),
                                    bg="White").place(x=260, y=300)
                dod_display = Label(frame_flightstatus, text="Date of Departure:", font=('Raleway', 20),
                                    bg="White").place(x=20, y=340)
                dod_display2 = Label(frame_flightstatus, textvariable=dod, font=('Raleway', 20),
                                     bg="White").place(x=260, y=340)
                tod_display = Label(frame_flightstatus, text="Time of Departure:", font=('Raleway', 20),
                                    bg="White").place(x=20, y=380)
                tod_display2 = Label(frame_flightstatus, textvariable=tod, font=('Raleway', 20),
                                     bg="White").place(x=260, y=380)

                price_display = Label(frame_flightstatus, text="Price per ticket:", font=('Raleway', 20),
                                      bg="White").place(x=420, y=220)
                price_display2 = Label(frame_flightstatus, textvariable=price, font=('Raleway', 20),
                                       bg="White").place(x=620, y=220)
                dest_display = Label(frame_flightstatus, text="Destination:", font=('Raleway', 20),
                                     bg="White").place(x=420, y=260)
                dest_display2 = Label(frame_flightstatus, textvariable=dest, font=('Raleway', 20),
                                      bg="White").place(x=620, y=260)
                sb_display = Label(frame_flightstatus, text="Seats Booked:", font=('Raleway', 20),
                                   bg="White").place(x=420, y=300)
                sb_display2 = Label(frame_flightstatus, textvariable=sb, font=('Raleway', 20),
                                    bg="White").place(x=620, y=300)
                doa_display = Label(frame_flightstatus, text="Date of Arrival:", font=('Raleway', 20),
                                    bg="White").place(x=420, y=340)
                doa_display2 = Label(frame_flightstatus, textvariable=doa, font=('Raleway', 20),
                                     bg="White").place(x=620, y=340)
                toa_display = Label(frame_flightstatus, text="Time of Arrival:", font=('Raleway', 20),
                                    bg="White").place(x=420, y=380)
                toa_display2 = Label(frame_flightstatus, textvariable=toa, font=('Raleway', 20),
                                     bg="White").place(x=620, y=380)

            else:
                messagebox.showerror("Error", "Booking does not exist.")

        show_btn = Button(frame_flightstatus, text="Show Details", font=("Raleway", 18), bg="#647789", cursor="hand2",
                          fg="white", command=status).place(x=530, y=140, height=40, width=200)

        dash = Label(frame_flightstatus, text="______________________________________________________",
                     font=("Raleway", 20), fg="#647789", bg="white").place(x=20, y=180)

        home_frame.pack()


class Search:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)

        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20, "bold"), bg="white",
                               cursor="hand2",
                               fg="#1D1D23", command=Call_Search).place(x=-10, y=310, height=50, width=240)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_profile).place(x=-10, y=400, height=50, width=220)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_Search = Frame(self.root, bg="white")
        frame_Search.place(x=300, y=40, height=580, width=840)

        flight_search = Label(frame_Search, text="Search Flights", bg="White", font=('Raleway', 40,
                                                                                     "bold")).place(x=20, y=10)

        date = StringVar()
        date_label = Label(frame_Search, text="Enter the Date of Departure:", font=('Raleway', 20),
                           bg="White").place(x=20, y=180)
        date_entry = DateEntry(frame_Search, font=("Raleway", 14), textvariable=date, bg="#647789",
                               fg="white").place(x=20, y=220, width=395, height=40)

        Origin = StringVar()
        Origin_label = Label(frame_Search, text="Enter the Origin:", font=('Raleway', 20),
                             bg="White").place(x=20, y=100)
        Origin_entry = Entry(frame_Search, font=("Raleway", 14), textvariable=Origin, bg="#647789",
                             fg="white").place(x=20, y=140, width=395, height=40)

        dest = StringVar()
        dest_label = Label(frame_Search, text="Enter the Destination:", font=('Raleway', 20),
                           bg="White").place(x=425, y=100)
        dest_entry = Entry(frame_Search, font=("Raleway", 14), textvariable=dest, bg="#647789",
                           fg="white").place(x=425, y=140, width=395, height=40)

        def show():
            frame_list = Frame(frame_Search, bg="white")
            frame_list.place(x=20, y=320, height=230, width=760)
            '''listbox = Listbox(frame_list).place(x=0, y=00, height=230, width=760)
            scrollbar = Scrollbar(frame_list)
            scrollbar.pack(side=RIGHT, fill=BOTH)'''

            cursor.execute("SELECT * FROM Flights WHERE Date_depart = ? AND origin = ? AND destination = ?",
                           (date.get(), Origin.get(), dest.get(),))
            check = cursor.fetchone()
            cursor.execute("SELECT * FROM Flights WHERE Date_depart = ? AND origin = ? AND destination = ?",
                           (date.get(), Origin.get(), dest.get(),))
            data = cursor.fetchall()
            if check is not None:
                tree = ttk.Treeview(frame_list, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"),
                                    show='headings')
                scrollbar = Scrollbar(frame_list, orient=HORIZONTAL)
                tree.config(xscrollcommand=scrollbar.set)
                scrollbar.config(command=tree.xview)
                scrollbar.pack(side=BOTTOM, fill=BOTH)
                tree.column("#1", anchor=tk.CENTER)
                tree.heading("#1", text="Flight Number")
                tree.column("#2", anchor=tk.CENTER)
                tree.heading("#2", text="Origin")
                tree.column("#3", anchor=tk.CENTER)
                tree.heading("#3", text="Destination")
                tree.column("#4", anchor=tk.CENTER)
                tree.heading("#4", text="Date of Departure")
                tree.column("#5", anchor=tk.CENTER)
                tree.heading("#5", text="Date of Arrival")
                tree.column("#6", anchor=tk.CENTER)
                tree.heading("#6", text="Time of Departure")
                tree.column("#7", anchor=tk.CENTER)
                tree.heading("#7", text="Time of Arrival")
                tree.column("#8", anchor=tk.CENTER)
                tree.heading("#8", text="Seats Booked")
                tree.column("#9", anchor=tk.CENTER)
                tree.heading("#9", text="Seats Available")
                tree.column("#10", anchor=tk.CENTER)
                tree.heading("#10", text="Price")
                tree.pack()
                for row in data:
                    print(row)
                    tree.insert("", tk.END, values=row)

            else:
                messagebox.showerror("Error", "No flights available.")

        show_btn = Button(frame_Search, text="Show Details", font=("Raleway", 18), bg="#647789", cursor="hand2",
                          fg="white", command=show).place(x=530, y=220, height=40, width=200)

        dash = Label(frame_Search, text="______________________________________________________",
                     font=("Raleway", 20), fg="#647789", bg="white").place(x=20, y=260)

        home_frame.pack()


class Profile:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Call_edit():
            obj = EditProfile(root, email, phone1.get(), phone2.get())

        def Call_delete():
            messagebox.showwarning("Delete Profile", "If you delete your account, you cannot recover it again.")
            if messagebox.askokcancel("Delete Profile", "Are you sure you want to delete this profile?"):
                cursor.execute("DELETE FROM USER WHERE Email = ?", (self.email,))
                connection.commit()
                messagebox.showinfo("Account Deleted", "Your account was deleted successfully.")
                exit(0)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)

        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20, "bold"), bg="white", cursor="hand2",
                            fg="#1D1D23", command=Call_profile).place(x=-10, y=400, height=50, width=240)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_contactus = Frame(self.root, bg="white")
        frame_contactus.place(x=300, y=90, height=490, width=640)
        profile = Label(frame_contactus, text="My Profile", bg="White", font=("Raleway", 40, "bold")).place(x=20, y=10)

        cursor.execute("SELECT * FROM USER WHERE Email = ?", (self.email,))
        data = cursor.fetchone()
        f_name = StringVar()
        f_name.set(data[1])
        l_name = StringVar()
        l_name.set(data[2])
        passw = StringVar()
        passw.set(data[3])
        dob = StringVar()
        dob.set(data[4])

        cursor.execute("SELECT PhoneNo FROM USER_PHONENO WHERE EMAIL = ?", (self.email,))
        data3 = cursor.fetchall()
        l1 = []
        for i in data3:
            l1.append(i[0])

        phone1 = StringVar()
        phone2 = StringVar()
        phone1.set(l1[0])
        if len(l1) > 1:
            phone2.set(l1[1])
        else:
            phone2.set("")

        name_display = Label(frame_contactus, text="First Name:", font=('Raleway', 20, 'bold'),
                             bg="White").place(x=20, y=100)
        name_display2 = Label(frame_contactus, textvariable=f_name, font=('Raleway', 20),
                              bg="White").place(x=230, y=100)
        name_display3 = Label(frame_contactus, text="Last Name:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=140)
        name_display4 = Label(frame_contactus, textvariable=l_name, font=('Raleway', 20),
                              bg="White").place(x=230, y=140)
        email_display = Label(frame_contactus, text="Email:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=180)
        email_display2 = Label(frame_contactus, text=self.email, font=('Raleway', 20),
                               bg="White").place(x=230, y=180)
        phone_display = Label(frame_contactus, text="Phone Number:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=220)
        phone_display2 = Label(frame_contactus, textvariable=phone1, font=('Raleway', 20),
                               bg="White").place(x=230, y=220)

        phone_display3 = Label(frame_contactus, text="Alt. Phone No.:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=260)
        phone_display4 = Label(frame_contactus, textvariable=phone2, font=('Raleway', 20),
                               bg="White").place(x=230, y=260)

        dob_display = Label(frame_contactus, text="Date of Birth:", font=('Raleway', 20, 'bold'),
                            bg="White").place(x=20, y=300)
        dob_display2 = Label(frame_contactus, textvariable=dob, font=('Raleway', 20),
                             bg="White").place(x=230, y=300)
        pass_display = Label(frame_contactus, text="Password:", font=('Raleway', 20, 'bold'),
                             bg="White").place(x=20, y=340)
        pass_display2 = Label(frame_contactus, textvariable=passw, font=('Raleway', 20),
                              bg="White").place(x=230, y=340)

        Edit = Button(frame_contactus, text="Edit Profile", font=('Raleway', 20), height=1, width=15,
                      bg="#647789", command=Call_edit, fg="White").place(x=50, y=400)

        Delete = Button(frame_contactus, text="Delete Profile", font=('Raleway', 20), height=1, width=15,
                        bg="#647789", fg="White", command=Call_delete).place(x=330, y=400)

        home_frame.pack()


class EditProfile:
    def __init__(self, root, email, phone1, phone2):
        self.root = root
        self.email = email
        self.phone1 = phone1
        self.phone2 = phone2
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)

        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20, "bold"), bg="white", cursor="hand2",
                            fg="#1D1D23", command=Call_profile).place(x=-10, y=400, height=50, width=240)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_edit = Frame(self.root, bg="white")
        frame_edit.place(x=300, y=90, height=490, width=640)
        profile = Label(frame_edit, text="Edit Profile", bg="White", font=("Raleway", 40, "bold")).place(x=20, y=10)

        f_name = StringVar()
        l_name = StringVar()
        phone_entry1 = StringVar()
        phone_entry2 = StringVar()
        passw = StringVar()
        dob = StringVar()

        name_display = Label(frame_edit, text="First Name:", font=('Raleway', 20, 'bold'),
                             bg="White").place(x=20, y=100)
        name_display2 = Entry(frame_edit, textvariable=f_name, font=('Raleway', 20),
                              bg="#647789", fg="white").place(x=230, y=100, width=350, height=35)
        name_display3 = Label(frame_edit, text="Last Name:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=140)
        name_display4 = Entry(frame_edit, textvariable=l_name, font=('Raleway', 20),
                              bg="#647789", fg="white").place(x=230, y=140, width=350, height=35)
        email_display = Label(frame_edit, text="Email:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=180)
        email_display2 = Label(frame_edit, text=self.email, font=('Raleway', 20),
                               bg="White").place(x=230, y=180)
        phone_display = Label(frame_edit, text="Phone Number:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=220)
        phone_display2 = Entry(frame_edit, textvariable=phone_entry1, font=('Raleway', 20),
                               bg="#647789", fg="white").place(x=230, y=220, width=350, height=35)
        phone_display3 = Label(frame_edit, text="Alt Phone No.:", font=('Raleway', 20, 'bold'),
                              bg="White").place(x=20, y=260)
        phone_display4 = Entry(frame_edit, textvariable=phone_entry2, font=('Raleway', 20),
                               bg="#647789", fg="white").place(x=230, y=260, width=350, height=35)
        dob_display = Label(frame_edit, text="Date of Birth:", font=('Raleway', 20, 'bold'),
                            bg="White").place(x=20, y=300)
        dob_display2 = Entry(frame_edit, textvariable=dob, font=('Raleway', 20),
                             bg="#647789", fg="white").place(x=230, y=300, width=350, height=35)
        pass_display = Label(frame_edit, text="Password:", font=('Raleway', 20, 'bold'),
                             bg="White").place(x=20, y=340)
        pass_display2 = Entry(frame_edit, textvariable=passw, font=('Raleway', 20),
                              bg="#647789", fg="white").place(x=230, y=340, width=350, height=35)

        def confirm():
            if messagebox.askokcancel("Confirm Changes",
                                      "Are you sure you want to make these changes to your account?"):
                if len(f_name.get()) != 0:
                    cursor.execute("UPDATE USER SET First_Name = ? WHERE Email = ?", (f_name.get(), self.email,))
                    connection.commit()
                if len(l_name.get()) != 0:
                    cursor.execute("UPDATE USER SET Last_Name = ? WHERE Email = ?", (l_name.get(), self.email,))
                    connection.commit()
                if len(passw.get()) != 0:
                    cursor.execute("UPDATE USER SET Password = ? WHERE Email = ?", (passw.get(), self.email,))
                    connection.commit()
                if len(phone_entry1.get()) != 0:
                    cursor.execute("UPDATE USER_PHONENO SET PhoneNo = ? WHERE PhoneNo = ?",
                                   (phone_entry1.get(), self.phone1))
                    connection.commit()
                if len(phone_entry2.get()) != 0:
                    cursor.execute("UPDATE USER_PHONENO SET PhoneNo = ? WHERE PhoneNo = ?",
                                   (phone_entry2.get(), self.phone2))
                    connection.commit()
                if len(dob.get()) != 0:
                    cursor.execute("UPDATE USER SET DOB = ? WHERE Email = ?", (dob.get(), self.email,))
                    connection.commit()
                Call_profile()

        Confirm = Button(frame_edit, text="Confirm Changes", font=('Raleway', 20), height=1, width=15,
                         bg="#647789", fg="White", command=confirm).place(x=230, y=400, width=350, height=50)

        home_frame.pack()


class Contact:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)

        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_profile).place(x=-10, y=400, height=50, width=220)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20, "bold"), bg="white", cursor="hand2",
                            fg="#1D1D23").place(x=-10, y=490, height=50, width=240)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_faq).place(x=-10, y=580, height=50, width=220)

        frame_contactus = Frame(self.root, bg="white")
        frame_contactus.place(x=300, y=110, height=450, width=750)

        contact = Label(frame_contactus, text="Contact Us", bg="White", font=("Raleway", 40, "bold")).place(x=20, y=10)
        info_reg = Label(frame_contactus, text="Registered Office", bg="White", font=("Raleway", 20,
                                                                                      "bold")).place(x=20, y=100)

        info = Label(frame_contactus,
                     text="Upper Ground Floor, Thapar House, Gate No. 2, Western Wing, 124 Janpath, New Delhi – 110001 India. Fax: +91 11-43513200.",
                     bg="White", font=("Raleway", 8)).place(x=20, y=140)
        info = Label(frame_contactus,
                     text="To share your feedback/complaints/suggestions or to reach out to our Customer Relations Team, please mail us on the email given below.",
                     bg="White", font=("Raleway", 8)).place(x=20, y=160)
        info = Label(frame_contactus,
                     text="For comments, concerning Civil Aviation Requirement, Section -3, please contact- Air Transport, Series M, Part IV. You may write to:",
                     bg="White", font=("Raleway", 8)).place(x=20, y=180)
        info = Label(frame_contactus,
                     text="Nodal Officer, Mitali Gera at nodalofficer@FRS.in.Appellate authority, Priyaah Sundaraam at appellateauthority@FRS.in",
                     bg="White", font=("Raleway", 8)).place(x=20, y=200)

        info_cor = Label(frame_contactus, text="Corporate Office", bg="White", font=("Raleway", 20, "bold")).place(x=20,
                                                                                                                   y=240)

        info1 = Label(frame_contactus,
                      text="Level 1, Tower C, Global Business Park, Mehrauli-Gurgaon Road, Gurgaon – 122 002, Haryana, India.",
                      bg="White", font=("Raleway", 8)).place(x=20, y=280)

        info1 = Label(frame_contactus,
                      text="Tel : +91 (0)124 435 2500 Fax : +91 (0)124 406 8536",
                      bg="White", font=("Raleway", 8)).place(x=20, y=300)

        info_cust = Label(frame_contactus, text="Customer Support", bg="White", font=('Raleway', 20, 'bold')).place(
            x=20, y=340)
        info2 = Label(frame_contactus, text="India : 0124-6173838, 0124-4973838.", bg="White",
                      font=('Raleway', 8)).place(x=20, y=380)
        info2 = Label(frame_contactus, text="Outside India: +__4006063838.", bg="White", font=('Raleway', 8)).place(
            x=20, y=400)

        home_frame.pack()


class FAQs:
    def __init__(self, root, email):
        self.root = root
        self.email = email
        self.root.title("Flight Reservation System")
        self.root.geometry("1920x1080+0+0")
        home_frame = Frame(self.root).place(x=0, y=0, height=1920, width=1080)
        self.image = PhotoImage(file="bg.png")
        self.image_label = Label(home_frame, image=self.image).place(x=00, y=00, relwidth=1, relheight=1)

        def Call_book():
            obj = Book(root, email)

        def Call_bookings():
            obj = MyBookings(root, email)

        def Call_status():
            obj = Status(root, email)

        def Call_Search():
            obj = Search(root, email)

        def Call_profile():
            obj = Profile(root, email)

        def Call_contact():
            obj = Contact(root, email)

        def Call_faq():
            obj = FAQs(root, email)

        def Logout():
            if messagebox.askokcancel("Confirm Logout", "Do you want to logout?"):
                exit(0)

        logout = Button(home_frame, text="Logout", font=("Raleway", 15), bg="white", cursor="hand2",
                        fg="#1D1D23", command=Logout).place(x=1180, y=20, height=40, width=100)

        book_button = Button(home_frame, text="Book a Flight", font=("Raleway", 20), bg="#647789", cursor="hand2",
                             fg="white", command=Call_book).place(x=-10, y=40, height=50, width=220)
        bookings_button = Button(home_frame, text="My Bookings", font=("Raleway", 20), bg="#647789", cursor="hand2",
                                 fg="white", command=Call_bookings).place(x=-10, y=130, height=50, width=220)
        flight_status = Button(home_frame, text="Flight Status", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_status).place(x=-10, y=220, height=50, width=220)
        flight_search = Button(home_frame, text="Search Flights", font=("Raleway", 20), bg="#647789", cursor="hand2",
                               fg="white", command=Call_Search).place(x=-10, y=310, height=50, width=220)
        my_profile = Button(home_frame, text="My Profile", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_profile).place(x=-10, y=400, height=50, width=220)
        contact_us = Button(home_frame, text="Contact Us", font=("Raleway", 20), bg="#647789", cursor="hand2",
                            fg="white", command=Call_contact).place(x=-10, y=490, height=50, width=220)
        faq_button = Button(home_frame, text="FAQs", font=("Raleway", 20, "bold"), bg="white", cursor="hand2",
                            fg="#1D1D23", command=Call_faq).place(x=-10, y=580, height=50, width=240)

        frame_faq = Frame(self.root, bg="white")
        frame_faq.place(x=300, y=85, height=500, width=800)

        faq = Label(frame_faq, text="Frequently Asked Questions", bg="white", font=('Raleway', 40, 'bold')).place(x=20,
                                                                                                                  y=10)

        query1 = Label(frame_faq, text="Select your Query:", bg="White", font=('Raleway', 20, 'bold')).place(x=20,
                                                                                                             y=100)
        faques = StringVar()
        ques = ttk.Combobox(frame_faq, textvariable=faques, width=100, font=("Raleway", 8))
        ques['values'] = ('What if I exceed my free baggage weight allowance?',
                          'What item are not permitted in the flights?',
                          'How can I change/cancel my reservation?',
                          'How can a refund for a a cancelled ticket be obtained?',
                          'Will I be contacted in advance if my flight is delayed, pre-poned or cancelled?',
                          'Do I need to book a separate seat for an infant?',
                          'How do I book snacks for my flight online and what are the charges?',
                          'What items are considered as special baggage and how can I carry them?',
                          'Who can I contact for feedbacks and comments?')
        ques.place(x=20, y=150)
        ques.current()

        def getans():
            if ques.get() == 'What if I exceed my free baggage weight allowance':
                messagebox.askokcancel("Query Result",
                                       "Customers carrying more than exceeded baggage limit will be charged the folllowing excess baggage fees:\n Domestic: INR 500/kg\nInternational: INR 525/kg")
            elif ques.get() == 'What item are not permitted in the flights':
                messagebox.askokcancel("Query Result",
                                       "Prohibited in checked and cabin baggage:\nAcids,\nPoisons,\nToxic,\nFlammable Liquids,\nExplosives,\nBleach,\netc")
            elif ques.get() == 'How can I change/cancel my reservation':
                messagebox.askokcancel("Query Result", "Visit 'my bookings' section")
            elif ques.get() == 'How can a refund for a a cancelled ticket be obtained?':
                messagebox.askokcancel("Query Result",
                                       "Refund for the cancelled tickets will be processed after the deduction of appropriate cancellation fees,which may take up to 7 working days in your registered bank account")
            elif ques.get() == 'Will I be contacted in advance if my flight is delayed, pre-poned or cancelled?':
                messagebox.askokcancel("Query Result",
                                       "Yes you'll recieve a mail and a message on your registered email id and contact number")
            elif ques.get() == 'Do I need to book a separate seat for an infant?':
                messagebox.askokcancel("Query Result",
                                       "For safety reasons, children above the age of seven 7 days and under the age of two 2 years, as on the date of travel, can travel as Infants. Age proof needs to be provided at the time of check-in and no extra bookings is required for them")
            elif ques.get() == 'How do I book snacks for my flight online and what are the charges?':
                messagebox.askokcancel("Query Result",
                                       "You may pre-book the snacks at the time of booking pr add it later either by visiting my bookings section or by calling our contact center")
            elif ques.get() == 'What items are considered as special baggage and how can I carry them?':
                messagebox.askokcancel("Query Result",
                                       "Following are considered as special baggage:\nSports/skiing equipment,\ngolf bags,\nbicycles,\nLCD/LED TVs,\nany other large or add size items.\n\n Following charges are applied:\nDomestic: INR 1200/bag\nInterational: INR 2500/bag")
            elif ques.get() == 'Who can I contact for feedbacks and comments?':
                messagebox.askokcancel("Query Result",
                                       "You can visit 'contact us' page and mail us your feedbacks on the provided email")

        ShowResult = Button(frame_faq, text="Show Query Result", font=('Raleway', 20), height=1, width=30,
                            command=getans, bg="#647789", fg="White").place(x=20, y=270)

        query = Label(frame_faq, text="**If your query in not resolved, please visit the CONTACT US page!**",
                      font=('Raleway', 10), bg="White").place(x=20, y=370)

        querycontact = Button(frame_faq, text="Contact Us Here", font=('Raleway', 20), height=1, width=30,
                              command=Call_contact, bg="#647789", fg="White").place(x=20, y=400)

        home_frame.pack()


root = Tk()
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)
root.state("zoomed")
obj = Main(root)
root.mainloop()

cursor.close()
connection.close()
