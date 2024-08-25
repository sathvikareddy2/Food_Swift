from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from PIL import Image, ImageTk
from mysql.connector import connect
import sqlite3
import random

conn = connect(
    host = 'localhost',
    user = 'root', 
    password = '',
    database = 'wise2'
)


cursor = conn.cursor()
class Home:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root, width=1700, height= 950, bd= 4, relief= 'ridge', bg= 'black')
        self.frame.place(x = 0,y = 0)

        image_path = "C:/Users/sathv/OneDrive/Desktop/Folders/Food Swift/plate.jpg"
        self.bg   = Image.open(image_path)
        self.bg = self.bg.resize((1700, 950))
        self.bg = ImageTk.PhotoImage(self.bg)

        self.bg_lbl = Label(self.frame, image= self.bg)
        self.bg_lbl.place(x= 0, y = 0)

        self.lbl=  Label(self.frame, text= 'Select the option', bg='burlywood1',fg = 'black', font=('Times new roman', 50, 'bold'))
        self.lbl.place(x = 500, y = 200)

        self.btn_1=  Button(self.frame, text= 'Warden',font=('Times new roman', 20, 'bold'), bg = 'burlywood1', cursor = 'hand2', command= self.login)
        self.btn_1.place(x = 500, y = 400)

        self.btn_2=  Button(self.frame, text= 'Student',font=('Times new roman', 20, 'bold'), bg = 'burlywood1', cursor = 'hand2', command= self.login_s)
        self.btn_2.place(x = 850, y = 400)

        self.goto_register = Label(self.frame, text= 'NOT A MEMBER YET? SIGNUP!',bg = 'white', font=('Courier New', 10, 'bold'))
        self.goto_register.place(x = 5, y = 600)
        self.goto_register.bind("<Button-1>", self.change_page)


    def change_page(self,event):
        self.frame.destroy()
        register = Register(root)

    def login_s(self):
        self.bg_lbl = Label(self.frame, image= self.bg)
        self.bg_lbl.place(x= 0, y = 0)

        self.lbl=  Label(self.frame, text= 'STUDENT LOGIN DETAILS', bg = 'white', fg = 'steel blue', font=('Courier New', 18, 'bold'))
        self.lbl.place(x = 500, y = 200)

        self.lbl=  Label(self.frame, text= 'USER NAME', bg = 'white', fg = 'steel blue', font=('Courier New', 20, 'bold'))
        self.lbl.place(x = 450, y = 250)
        self.stu_entry = Entry(self.frame, width = 20, font=('Courier New', 18, 'bold'), bg = 'white')
        self.stu_entry.place(x = 650, y = 250)

        self.lbl=  Label(self.frame, text= 'PASSWORD', bg = 'white', fg = 'steel blue', font=('Courier New', 20, 'bold'))
        self.lbl.place(x = 450, y = 300)
        self.stu_p = Entry(self.frame, width = 20, font=('Courier New', 18, 'bold'), bg = 'white')
        self.stu_p.place(x = 650, y = 300)
        
        self.btn = Button(self.frame, text = 'LOGIN',font=('Courier New', 18, 'bold'), bg = 'pink', cursor = 'hand2', command= self.stu)
        self.btn.place(x = 650, y = 550)

        self.bck_lbl = Label(self.frame, text = 'Back To Main Page', bg = 'white', fg = 'steel blue', font=('Courier New', 14, 'bold'), cursor = 'hand2')
        self.bck_lbl.place(x = 0, y = 650)
        self.bck_lbl.bind("<Button - 1>", self.back_to_main2)

    def login(self):
        self.bg_lbl = Label(self.frame, image= self.bg)
        self.bg_lbl.place(x= 0, y = 0)

        self.lbl=  Label(self.frame, text= 'WARDEN LOGIN DETAILS', bg = 'white', fg = 'black', font=('Courier New', 18, 'bold'))
        self.lbl.place(x = 500, y = 200)

        self.lbl=  Label(self.frame, text= 'USER NAME', bg = 'white', fg = 'steel blue', font=('Courier New', 20, 'bold'))
        self.lbl.place(x = 450, y = 300)
        self.War_u_entry = Entry(self.frame, width = 20, font=('Courier New', 18, 'bold'), bg = 'white')
        self.War_u_entry.place(x = 650, y = 300)

        self.lbl=  Label(self.frame, text= 'PASSWORD', bg = 'white', fg = 'steel blue', font=('Courier New', 20, 'bold'))
        self.lbl.place(x = 450, y = 400)
        self.entry_p = Entry(self.frame, width = 20, font=('Courier New', 18, 'bold'), bg = 'white')
        self.entry_p.place(x = 650, y = 400)
        
        self.btn = Button(self.frame, text = 'LOGIN',font=('Courier New', 18, 'bold'), bg = 'white', cursor = 'hand2', command= self.Admin)
        self.btn.place(x=550,y=550) 
        
        self.bck_lbl = Label(self.frame, text = 'Back To Main Page', bg = 'white', fg = 'steel blue', font=('Courier New', 14, 'bold'), cursor = 'hand2')
        self.bck_lbl.place(x = 0, y = 750)
        self.bck_lbl.bind("<Button - 1>", self.back_to_main2)

    def back_to_main(self):
        self.home = Home(root)

    def stu(self):
        self.stu_u = self.stu_entry.get()
        self.stu_p = self.stu_p.get()
        cursor.execute('select * from user_details;')
        self.data = cursor.fetchall()
        self.names = [name[0] for name in self.data]
        if self.stu_u == "":
            messagebox.showinfo('Invailed',f'INCORRECT USERNAME')
            self.back_to_main()
            return
        if self.stu_u in self.names:
            cursor.execute(f"select pwd from user_details where Name = '{self.stu_u}'")
            self.pasw = cursor.fetchall()
            self.pasw = [passw[0] for passw in self.pasw]
        else:
            messagebox.showinfo('Login failed',f'INCORRECT USERNAME')
            self.back_to_main()
            return
        if self.stu_p in self.pasw:
            messagebox.showinfo('Login Succesfull',f'Welcome {self.stu_u}')
            self.student()
        else:
            messagebox.showinfo('Login failed',f'INCORRECT PASSWORD')
            self.back_to_main()
        

    def Admin(self):
        self.War_u = self.War_u_entry.get()
        self.War_p = self.entry_p.get()
        cursor.execute('select * from war_details;')
        self.data = cursor.fetchall()
        self.names = [name[0] for name in self.data]
        if self.War_u in self.names:
            cursor.execute(f"select roll from war_details where Name = '{self.War_u}'")
            self.pasw = cursor.fetchall()
            self.pasw = [passw[0] for passw in self.pasw]
        else:
            messagebox.showinfo('Login failed',f'INCORRECT USERNAME')
            return
        if self.War_p in self.pasw:
            messagebox.showinfo('Login Succesfull',f'Welcome {self.War_u}')
            self.warden()
        else:
            messagebox.showinfo('Login failed',f'INCORRECT PASSWORD')
            self.back_to_main()

    def back_to_main2(self,event):
        self.home = Home(root)
        
    def warden(self):
        self.msg_frame = Frame(self.root, width=5000, height= 1000, bd= 4, relief= 'ridge', bg= 'white')
        self.msg_frame.place(x = 0,y = 0)
        self.msg = Label(self.msg_frame, text = 'View details of a student', bg = 'white', fg = 'red', font=('Times New Roman', 20, 'bold'))
        self.msg.place(x = 630, y = 10)
        
        cursor.execute('select * from student_detail order by date desc;')
        self.data = cursor.fetchall()
        self.x1 = 10
        self.y1 = 100
        self.msg = Label(self.msg_frame, text = "STUDENTNAME"+'\t\t\t'+'HOSTEL NAME'+'\t\t\t'+'Register no'+'\t\t\t'+'phone number'+'\t\t\t'+'Problem'+'\t\t\t'+'Time',bg = 'white', fg = 'orange', font=('Times New Roman', 13, 'bold'))
        self.msg.place(x = 5, y = 60)
        for name in self.data:
            self.msg = Label(self.msg_frame, text =  name[0] +'\t\t\t\t\t'+name[2]+'\t\t\t\t\t'+name[3]+'\t\t\t\t\t'+name[1]+'\t\t\t\t'+name[4]+'\t\t\t\t'+name[5].strftime("%Y-%m-%d %H:%M:%S"), bg = 'white', fg = 'blue', font=('Times New Roman', 10, 'bold'))
            self.msg.place(x = self.x1,y= self.y1)
            self.y1 += 40         

        self.bck_lbl = Label(self.msg_frame, text = 'Back To Main Page', bg = 'white', fg = 'steel blue', font=('Courier New', 14, 'bold'), cursor = 'hand2')
        self.bck_lbl.place(x = 0, y = 720)
        self.bck_lbl.bind("<Button - 1>", self.back_to_main2)
   

    def student(self):

        font = ('Courier New', 16, 'bold')
        self.msg_frame = Frame(self.root, width=1800, height= 950, bd= 4, relief= 'ridge', bg= 'pink')
        self.msg_frame.place(x = 0,y = 0)

        image_path = "C:/Users/sathv/OneDrive/Desktop/Folders/Food Swift/plate.jpg"
        self.bg   = Image.open(image_path)
        self.bg = self.bg.resize((1700, 950))
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bg_lbl = Label(self.msg_frame, image= self.bg)
        self.bg_lbl.place(x= 0, y = 0)

        self.msg = Label(self.msg_frame, text = 'Enter your details', bg = 'white', fg = 'red', font=('Times New Roman', 20, 'bold'))
        self.msg.place(x = 500, y = 200)
        self.name_lbl = Label(self.msg_frame, text = "NAME", bg = 'white', fg = 'blue', font=('Courier New', 16, 'bold'))
        self.name_lbl.place(x = 450, y = 300)
        self.name_entry = Entry(self.msg_frame, font=font, width= 15)
        self.name_entry.place(x = 650, y = 300)

        self.regno_lbl = Label(self.msg_frame, text='Regnum', bg = 'white', fg = 'blue', font=('Courier New', 16, 'bold'))
        self.regno_lbl.place(x = 450, y = 350)
        self.regno_entry = Entry(self.msg_frame, font= font, width= 15)
        self.regno_entry.place(x = 650, y = 350)

        self.hostel_name_lbl = Label(self.msg_frame, text='HostelName',bg = 'white', fg = 'blue', font=('Courier New', 16, 'bold'))
        self.hostel_name_lbl.place(x = 450, y = 400)
        self.hostel_name_entry = Entry(self.msg_frame, font= font, width= 15)
        self.hostel_name_entry.place(x = 650, y = 400)

        self.problem_lbl = Label(self.msg_frame, text='Problem', bg = 'white', fg = 'blue', font=('Courier New', 16, 'bold'))
        self.problem_lbl.place(x = 450, y = 450)
        self.problem_entry = Entry(self.msg_frame, font= font, width= 15)
        self.problem_entry.place(x = 650, y = 450)

        self.phonenum_lbl = Label(self.msg_frame, text='Phonenum', bg = 'white', fg = 'blue', font=('Courier New', 16, 'bold'))
        self.phonenum_lbl.place(x = 450, y = 500)
        self.phonenum_entry = Entry(self.msg_frame, font= font, width= 15)
        self.phonenum_entry.place(x = 650, y = 500)

        self.btn = Button(self.msg_frame, text = 'SUBMIT',font=('Courier New', 18, 'bold'), bg = 'white', command= self.student_details, cursor = 'hand2')
        self.btn.place(x=650,y=600) 

        self.bck_lbl = Label(self.msg_frame, text = 'Back To Main Page', bg = 'white', fg = 'steel blue', font=('Courier New', 14, 'bold'), cursor = 'hand2')
        self.bck_lbl.place(x = 0, y = 720)
        self.bck_lbl.bind("<Button - 1>", self.back_to_main2)

    def student_details(self):
        self.name  = self.name_entry.get()
        self.hostel_name = self.hostel_name_entry.get() 
        self.phonenum = self.phonenum_entry.get()
        self.regno = self.regno_entry.get()
        self.prob = self.problem_entry.get()

        if len(self.phonenum) != 10 or self.name == '' or self.hostel_name == '' or self.regno == '' or self.prob == '':
            messagebox.showinfo('Invalid',f'INVALID CREDENTIALS')
            return self.student
        else:
            self.query = "insert into student_detail(name,regno , hostel_name, phonenum,prob) values(%s,%s,%s,%s,%s)"
            self.values = (self.name,self.regno,self.hostel_name, self.phonenum,self.prob)
            cursor.execute(self.query,self.values)
            conn.commit()
            messagebox.showinfo('Successfully Saved',f'Your Details are sent to the warden')
    
    def submit(self):
        self.lbl=  Label(self.msg_frame, text= 'Your details are saved Sucessfully', bg = 'white', fg = 'green', font=('Courier New', 18, 'bold'))
        self.lbl.place(x = 50, y = 250)

    
class Register:
    def __init__(self, root) -> None:
        self.root = root
        font = ('Courier New', 18, 'bold')
        self.main_frame = Frame(self.root, width= 1600, height= 950, bg = 'pink')
        self.main_frame.place(x = 0, y = 0)

        self.name_lbl = Label(self.main_frame, text = "SIGN UP", font = font, width= 10)
        self.name_lbl.place(x = 650, y = 100)

        self.name_lbl = Label(self.main_frame, text = "USER NAME", font = font, width= 10)
        self.name_lbl.place(x = 500, y = 200)
        self.name_entry = Entry(self.main_frame, font=font, width= 15)
        self.name_entry.place(x = 700, y = 200)
        
        self.pass_lbl = Label(self.main_frame, text='DEPARTMENT', font = font, width= 10)
        self.pass_lbl.place(x = 500, y = 250)
        self.pass_entry = Entry(self.main_frame, font= font, width= 15)
        self.pass_entry.place(x = 700, y = 250)

        self.roll_lbl = Label(self.main_frame, text='ROLL NO.', font = font, width= 10)
        self.roll_lbl.place(x = 500, y = 300)
        self.roll_entry = Entry(self.main_frame, font= font, width= 15)
        self.roll_entry.place(x = 700, y = 300)

        self.regno_lbl = Label(self.main_frame, text='Password', font = font, width= 10)
        self.regno_lbl.place(x = 500, y = 350)
        self.regno_entry = Entry(self.main_frame, font= font, width= 15)
        self.regno_entry.place(x = 700, y = 350)
        
        self.register_btn = Button(self.main_frame, text= 'REGISTER', font = font, width= 10, command= self.register_user)
        self.register_btn.place(x = 650, y = 550)

        self.goto_register = Label(self.main_frame, text= 'Already a member LOGIN!', bg = 'pink',font=('Courier New', 10, 'bold'))
        self.goto_register.place(x = 5, y = 720)
        self.goto_register.bind("<Button-1>", self.change_page)

    def back_to_main(self):
        self.main_frame.destroy()
        
    def register_user(self):
        self.name  = self.name_entry.get()
        self.roll = self.roll_entry.get()
        self.dept = self.pass_entry.get() 
        self.pwd = self.regno_entry.get()
        self.query = "insert into user_details(Name, Dept, Roll,pwd) values(%s,%s,%s,%s)"
        self.values = (self.name, self.dept,self.roll,self.pwd)
        cursor.execute(self.query, self.values)
        conn.commit()
        messagebox.showinfo('Account Created',f'UserName = "{self.name}"\nPassword = "{self.pwd}"')
    def change_page(self,event):
        self.main_frame.destroy()
        home = Home(root)

root = Tk()
root.title('FOOD SWIFT')
root.geometry('1700x1000+0+0')
home = Home(root)
root.mainloop()