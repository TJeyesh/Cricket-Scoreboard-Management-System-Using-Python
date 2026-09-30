from customtkinter import * #type: ignore
import customtkinter as ctk
from tkinter import ttk #type: ignore
import tkinter as tk
from ctk_graph import *
from PIL import Image,ImageTk
ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")
from tkinter import messagebox as tkm
instantotp=12345
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',          
    user='root',                   
    passwd='root',                        
    auth_plugin = 'mysql_native_password',
    buffered=True
)
cursor=mydb.cursor()
cursor.execute('show databases')
z=cursor.fetchall()
print(z)
if ('cms',) not in z:
    while True :
            database='cms'
            cursor.execute(f"create database {'cms'}")
            mydb.commit()
            cursor.execute(f"use {database}")
            cursor.execute(f"create table accounts (username varchar(255) primary key , email varchar(255) , password varchar(255))")
            cursor.execute(f"create table fi (name varchar(255),runs int(11),balls int(11),4s int(11),6s int(11),wickets int(11),status int(11))")
            
            cursor.execute(f"create table si (name varchar(255),runs int(11),balls int(11),4s int(11),6s int(11),wickets int(11),status int(11))")
            
            cursor.execute(f"create table first (name varchar(255),runs int(11),balls int(11),4s int(11),6s int(11),wickets int(11),status int(11))")
            
            cursor.execute(f"create table second (name varchar(255),runs int(11),balls int(11),4s int(11),6s int(11),wickets int(11),status int(11))")
            
            cursor.execute(f"create table teams (name varchar(255),FORMAT varchar(255) , winst20 int(11) , winsodi int(11) , winstest int(11) , losst20 int(11) , lossodi int(11) , losstest int(11) , tiet20 int(11) , tieodi int(11) , tietest int(11))")

            cursor.execute(f"create table players (name varchar(255) , jersey varchar(255) , runst20 int(11) , runsodi int(11) , runstest int(11) , ballst20 int(11) , ballsodi int(11) , ballstest int(11) , wicketst20 int(11) , wicketsodi int(11) , wicketstest int(11) , 50st20 int(11) , 100st20 int(11) , 50sodi int(11) , 100sodi int(11) , 50stest int(11) , 100stest int(11) , team varchar(255))")
            cursor.execute(f"create table loginhistory (username varchar(255) , signintime datetime , signouttime datetime)")
            mydb.commit()
            break
else:
    database='cms'
mydb.close()

mydb=mysql.connector.connect(
    host='localhost',          
    user='root',                   
    passwd='root',
    database='cms',                        
    auth_plugin = 'mysql_native_password',
    buffered=True
)
if mydb.is_connected():
    print("Successfully connected to the database")
else:
    print("Unable to connect to the database")
    quit()
cursor=mydb.cursor()
class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cricket Management System")
        self.geometry("1000x700")
        self.resizable(False,False)
        # self.attributes('-fullscreen',True)
        self.iconbitmap('CMS_logo.ico')
        self.bg=CTkImage(dark_image=Image.open("Login.png"),size=(1000,700)) # type: ignore
        self.label=CTkLabel(self,text='hi',image=self.bg) # type: ignore
        self.label.place(x=0,y=0)
        label=CTkLabel(master=self,text='Cricket Management System',corner_radius=50,font=('sans-serf',40),text_color='blue').place(x=250,y=50)
        tabs=CTkTabview(self,width=500,height=300,corner_radius=10,segmented_button_selected_hover_color='blue')
        tabs.place(x=250,y=200)
        tabs.add('Sign In')
        tabs.add('Sign Up')

        # Sign In
        
        userentry=CTkEntry(tabs.tab('Sign In'),width=300,placeholder_text='Enter your Username',font=('sans-serf',20))
        userentry.place(x=80,y=0)
        passwdentry=CTkEntry(tabs.tab('Sign In'),width=300,placeholder_text='Enter your Password',font=('sans-serf',20))
        passwdentry.place(x=80,y=50)
        Forgotbutton=CTkButton(tabs.tab('Sign In'),width=300,text=f"Forgot Password",font=('sans-serf',20))
        Forgotbutton.place(x=80,y=100)
        button=CTkButton(tabs.tab('Sign In'),width=300,text=f"Sign In ",font=('sans-serf',20),command=lambda: signin())
        button.place(x=80,y=150)
        
        #Sign Up

        userentry1=CTkEntry(tabs.tab('Sign Up'),width=300,placeholder_text='Enter your Username',font=('sans-serf',20))
        userentry1.place(x=80,y=0)
        passwdentry1=CTkEntry(tabs.tab('Sign Up'),width=300,placeholder_text='Enter your Password',font=('sans-serf',20))
        passwdentry1.place(x=80,y=100)
        emailentry=CTkEntry(tabs.tab('Sign Up'),width=300,placeholder_text=f"Enter your email",font=('sans-serf',20))
        emailentry.place(x=80,y=50)
        button1=CTkButton(tabs.tab('Sign Up'),width=300,text=f"Sign Up ",font=('sans-serf',20),command=lambda: signup())
        button1.place(x=80,y=150)
        def signin():
            if userentry.get()=='' or passwdentry.get()=='':
                tkm.showwarning('Error','All fields are required')
            else:
                cursor.execute(f"select email from accounts where username='{userentry.get()}' and password='{passwdentry.get()}' ")
                v=cursor.fetchall()
                if len(v)!=0:
                    emailid=v[0][0] # type: ignore
                    from otp import otp_login
                    global instantotp
                    instantotp=otp_login(emailid,userentry.get())
                    if str(instantotp).isdigit():
                        otpentry=CTkEntry(tabs.tab('Sign In'),width=300,placeholder_text=f"Enter OTP send to your Email",font=('sans-serf',20))
                        otpentry.place(x=80,y=100)
                        verifybutton=CTkButton(tabs.tab('Sign In'),width=300,text=f"Verify OTP",font=('sans-serf',20),command=lambda: otp_check(otpentry.get(),userentry.get()))
                        verifybutton.place(x=80,y=150)
                    else :
                        tkm.showerror('Error','Invalid email id')
                else:
                    tkm.showerror('Error','Account not in database')
        
        def signup():
            if userentry1.get()=='' or passwdentry1.get()=='' or emailentry.get=='':
                tkm.showwarning('Error','All fields are required')
            else:
                cursor.execute(f"select * from accounts where username='{userentry1.get()}'")
                v=cursor.fetchall()
                if len(v)==0:
                    from otp import otp_login
                    global instantotp
                    instantotp=otp_login(emailentry.get(),userentry1.get())
                    if str(instantotp).isdigit():
                        otpentry=CTkEntry(tabs.tab('Sign Up'),width=300,placeholder_text=f"Enter OTP send to your Email",font=('sans-serf',20))
                        otpentry.place(x=80,y=100)
                        verifybutton=CTkButton(tabs.tab('Sign Up'),width=300,text=f"Verify OTP",font=('sans-serf',20),command=lambda: otp_check(otpentry.get(),userentry1.get(),[userentry1.get(),emailentry.get(),passwdentry1.get()]))
                        verifybutton.place(x=80,y=150)
                    else :
                        tkm.showerror('Error','Invalid email id')
                else:
                    tkm.showerror('Error','Username already taken database')
        def otp_check(otpentry,username,insert=[]):
            if otpentry==str(instantotp):
                tkm.showinfo('Welcome',f'Welcome {username}')
                if len(insert)!=0:
                    cursor.execute(f"insert into accounts values('{insert[0]}','{insert[1]}','{insert[2]}')")
                    cursor.execute(f"insert into LoginHistory values('{username}',now(),now())")
                else:
                    cursor.execute(f"insert into LoginHistory values('{username}',now(),now())")
                mydb.commit()
                Admin(self)
            else:
                tkm.showerror('Error',"OTP didn't match")
        def Admin(self):
                self.geometry("1536x864")
                self.state('zoomed')
                self.resizable(False,False)
                self.attributes('-fullscreen',True)
                Top=CTkFrame(self,width=1536,height=50,fg_color='white')
                Top.place(x=0,y=0)
                
                Left=CTkFrame(self,width=400,height=814,fg_color='aquamarine')
                Left.place(x=0,y=50)
                Right=CTkFrame(self,width=200,height=564,fg_color='lemon chiffon')
                Right.place(x=1336,y=250)
                Bottom=CTkFrame(self,width=1536,corner_radius=0,height=50,fg_color='PeachPuff3')
                Bottom.place(x=0,y=814)
                Center=CTkFrame(self,width=936,height=764,fg_color='peach puff')
                Center.place(x=400,y=50)
                copyright=CTkLabel(Bottom,text='Developed by T.Jeyesh',corner_radius=10,width=1000,font=('sans-serf',30),text_color='red')
                copyright.place(x=875,y=5)
                accountframe=CTkFrame(self,width=200,height=200,fg_color='lemon chiffon')
                accountframe.place(x=1336,y=50)
                bg=CTkImage(dark_image=Image.open("hyy.png"),size=(200,110))
                accountdetails=CTkLabel(accountframe,text='',image=bg)
                accountdetails.place(x=0,y=0)
                accountlabel=CTkLabel(accountframe,text='Jeyesh\n12107871\ntjeyesh@bspsss10.edu.in')
                accountlabel.place(x=30,y=140)
                CTkLabel(Left,width=400,height=30,text='Press your choice',font=('sans-serf',30)).place(x=0,y=0)
                L1bg=CTkImage(dark_image=Image.open("L1.png"),size=(200,100))
                L2bg=CTkImage(dark_image=Image.open("L2.png"),size=(200,100))
                L3bg=CTkImage(dark_image=Image.open("L3.png"),size=(200,100))
                L4bg=CTkImage(dark_image=Image.open("L4.png"),size=(200,100))
                L5bg=CTkImage(dark_image=Image.open("L5.png"),size=(200,100))
                L6bg=CTkImage(dark_image=Image.open("L6.png"),size=(200,100))
                R1bg=CTkImage(dark_image=Image.open("R1.png"),size=(200,100))
                R2bg=CTkImage(dark_image=Image.open("R2.png"),size=(200,100))
                R3bg=CTkImage(dark_image=Image.open("R3.png"),size=(200,100))

                L1=CTkButton(Left,text='  Update/Register Players  ',image=L1bg,width=400,height=50,command=lambda: L1fun(self))
                L1.place(x=0,y=40)
                L2=CTkButton(Left,text='  Update/Register Teams   ',image=L2bg,width=400,height=50,command=lambda: L2fun(self))
                L2.place(x=0,y=160)
                L3=CTkButton(Left,text=' Registered Players  ',image=L3bg,width=400,height=50,command=lambda: L3fun_welcome(self))
                L3.place(x=0,y=280)
                L4=CTkButton(Left,text='  Registered Teams   ',image=L4bg,width=400,height=50,command=lambda: L4fun_welcome(self))
                L4.place(x=0,y=400)
                L5=CTkButton(Left,text='  Start a Standard Match  ',image=L5bg,width=400,height=50,command=lambda: L5fun(self))
                L5.place(x=0,y=520)
                L6=CTkButton(Left,text='Start a Non Standard Match',image=L6bg,width=400,height=50,command=lambda: L6fun(self))
                L6.place(x=0,y=640)
                R1=CTkButton(Right,text='',image=R1bg,width=200,height=50,command=lambda: R1fun(self))
                R1.place(x=0,y=0)
                R2=CTkButton(Right,text='',image=R2bg,width=200,height=50,command=lambda: R2fun(self))
                R2.place(x=0,y=110)
                R3=CTkButton(Right,text='',image=R3bg,width=200,height=50,command=lambda: R3fun(self))
                R3.place(x=0,y=220)
                exitbutton=CTkButton(Top,text='X',bg_color='red',fg_color='red',hover_color=('red','red'),width=50,height=50,command=lambda: self.destroy())
                exitbutton.place(x=1486,y=0)
                label=CTkLabel(Top,text='Cricket Management System',corner_radius=50,font=('sans-serf',40),text_color='blue4').place(x=500,y=0)
        
        
        def L1fun(self):
                        Center=CTkFrame(self,width=736,height=714,fg_color='peach puff')
                        Center.place(x=400,y=50)
                        tabs=CTkTabview(Center,fg_color='white',width=500,height=500,corner_radius=10,segmented_button_selected_hover_color='blue')
                        tabs.place(x=200,y=0)
                        tabs.add('Update Players')
                        
                        L1Playername=CTkEntry(tabs.tab('Update Players'),width=300,placeholder_text='Enter Player Name',font=('sans-serf',20))
                        L1Playername.place(x=100,y=0)
                        L1Playerjersey=CTkEntry(tabs.tab('Update Players'),width=300,placeholder_text='Enter Player Jersey',font=('sans-serf',20))
                        L1Playerjersey.place(x=100,y=50)
                        cursor.execute('select name from teams')
                        L1tempvar=[]
                        for i in cursor.fetchall():
                               L1tempvar.append(i[0]) # type: ignore
                        def combobox_callback(choice):
                                print("combobox dropdown clicked:", choice)

                        combobox_var = StringVar()
                        combobox =CTkComboBox(tabs.tab('Update Players'), values=L1tempvar,command=combobox_callback, variable=combobox_var,width=300)
                        combobox.set(f"{L1tempvar[0]}")
                        combobox.place(x=100,y=100)
                        button=CTkButton(tabs.tab('Update Players'),width=300,text=f"Submit",font=('sans-serf',20),command=lambda: L1button_check())
                        button.place(x=100,y=150)
                        def L1button_check():
                                if L1Playerjersey.get()=='' or L1Playername.get()=='':
                                      tkm.showwarning('Error','All fields are required')
                                else:
                                       cursor.execute(f"insert into players values ('{L1Playername.get()}','{L1Playerjersey.get()}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'{combobox_var.get()}')")
                                       tkm.showinfo(f"Updation Successfull','Successfully added {L1Playername}")
                                       mydb.commit()

        def L2fun(self):
                        Center=CTkFrame(self,width=736,height=714,fg_color='peach puff')
                        Center.place(x=400,y=50)
                        tabs=CTkTabview(Center,fg_color='white',width=500,height=500,corner_radius=10,segmented_button_selected_hover_color='blue')
                        tabs.place(x=200,y=0)
                        tabs.add('Update Teams')
                        
                        L2Teamname=CTkEntry(tabs.tab('Update Teams'),width=300,placeholder_text='Enter Team Name',font=('sans-serf',20))
                        L2Teamname.place(x=100,y=0)
                        check_var1 = ctk.IntVar()
                        checkbox1 = CTkCheckBox(tabs.tab('Update Teams'), text='T20', variable=check_var1)
                        checkbox1.place(x=100,y=50)
                        check_var2= ctk.IntVar()
                        checkbox2 = CTkCheckBox(tabs.tab('Update Teams'), text='ODI', variable=check_var2)
                        checkbox2.place(x=200,y=50)
                        check_var3 = ctk.IntVar()
                        checkbox3 = CTkCheckBox(tabs.tab('Update Teams'), text='TEST', variable=check_var3)
                        checkbox3.place(x=300,y=50)
                        cursor.execute('select name from teams')
                        L2tempvar=[]
                        for i in cursor.fetchall():
                               L2tempvar.append(i[0]) # type: ignore
                        button=CTkButton(tabs.tab('Update Teams'),width=300,text=f"Submit",font=('sans-serf',20),command=lambda: L2button_check())
                        button.place(x=100,y=100)
                        def L2button_check():
                                if L2Teamname!='' and L2Teamname.get().upper() not in L2tempvar:
                                      if L2Teamname.get()=='':
                                                tkm.showwarning('Error','All fields are required')   
                                      else:
                                        print(L2Teamname.get().upper())
                                        print(check_var1.get(),check_var2.get(),check_var3.get())
                                        if check_var1.get()==1 or check_var2.get()==1 or check_var3.get()==1:
                                                var1=['','T20']
                                                var2=['','ODI']
                                                var3=['','TEST']
                                                var=f"{var1[check_var1.get()]}/{var2[check_var2.get()]}/{var3[check_var3.get()]}"
                                                print(var)
                                                cursor.execute(f"insert into teams values ('{L2Teamname.get().upper()}','h',0,0,0,0,0,0,0,0,0)")
                                                tkm.showinfo('Updation Successfull',f"Successfully added {L2Teamname.get().upper()}")
                                                mydb.commit()
                                        else:
                                                tkm.showwarning('Error','Any One of T20/ODI/TEST should be checked')   
                                else:
                                       tkm.showwarning('Error','All fields are required')

        def L3fun_welcome(self):
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color="black")
                Starting_Frame.place(x=0,y=0)
                WELCOME=CTkLabel(Starting_Frame,text_color='white',text="Registerd Players",corner_radius=50,font=('sans-serf',40))
                WELCOME.place(x=50,y=400)
                self.bg=CTkImage(dark_image=Image.open("L3.png"),size=(1000,864)) # type: ignore
                self.label=CTkLabel(Starting_Frame,text='',image=self.bg) # type: ignore
                self.label.place(x=536,y=0)
                button=CTkButton(Starting_Frame,width=200,text="Start",command=lambda: L3fun(self))
                button.place(x=100,y=500)

        def L3fun(self):
                        Center=CTkFrame(self,width=1536,height=864,fg_color='peach puff')
                        Center.place(x=0,y=0)
                        table =ttk.Treeview(Center)
                        table['columns'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14')
                        table.column('#0', width=0, stretch=tk.NO)
                        table.column('1',anchor=tk.CENTER ,width=60)
                        table.column('2', anchor=tk.CENTER, width=150)
                        table.column('3', anchor=tk.CENTER, width=70)
                        
                        table.column('4',anchor=tk.CENTER ,width=110)
                        table.column('5', anchor=tk.CENTER, width=170)
                        table.column('6', anchor=tk.CENTER, width=170)
                        
                        table.column('7',anchor=tk.CENTER ,width=180)
                        table.column('8', anchor=tk.CENTER, width=200)
                        table.column('9', anchor=tk.CENTER, width=150)
                        
                        table.column('10',anchor=tk.CENTER ,width=150)
                        table.column('11', anchor=tk.CENTER, width=150)
                        table.column('12', anchor=tk.CENTER, width=170)
                        table.column('13', anchor=tk.CENTER, width=170)
                        table.column('14', anchor=tk.CENTER, width=180)
                        style = ttk.Style()
                        style.configure("Treeview.Heading", font=(None,15))
                        style.configure('Treeview', rowheight=50)
                        table.heading('#0', text='', anchor=tk.CENTER)
                        table.heading('1', text='Sr No', anchor=tk.CENTER)
                        table.heading('2', text='Player Name', anchor=tk.CENTER)
                        table.heading('3', text='Jersey', anchor=tk.CENTER)
                        table.heading('4', text='Team', anchor=tk.CENTER)
                        table.heading('5', text='Runs/Balls in T20', anchor=tk.CENTER)
                        table.heading('6', text='Runs/Balls in ODI', anchor=tk.CENTER)
                        table.heading('7', text='Runs/Balls in TEST', anchor=tk.CENTER)
                        table.heading('8', text='Wickets in T20/ODI/TEST', anchor=tk.CENTER)
                        table.heading('9', text='50s/100s in T20', anchor=tk.CENTER)
                        table.heading('10', text='50s/100s in ODI', anchor=tk.CENTER)
                        table.heading('11', text='50s/100s in TEST', anchor=tk.CENTER)
                        table.heading('12', text='Strike Rate in T20', anchor=tk.CENTER)
                        table.heading('13', text='Strike Rate in ODI', anchor=tk.CENTER)
                        table.heading('14', text='Strike Rate in TEST', anchor=tk.CENTER)
                        cursor.execute("select name,jersey,team,runst20,ballst20,runsodi,ballsodi,runstest,ballstest,wicketst20,wicketsodi,wicketstest,50st20,100st20,50sodi,100sodi,50stest,100stest,runst20*100/ballst20,runsodi*100/ballsodi,runstest*100/ballstest from players")
                        data=cursor.fetchall()
                        j=1
                        for z in data:
                                v=[j,*z[0:3],f"{z[3]} / {z[4]}",f"{z[5]} / {z[6]}",f"{z[7]} / {z[8]}",f"{z[9]} / {z[10]} / {z[11]}",f"{z[12]} / {z[13]}",f"{z[14]} / {z[15]}",f"{z[16]} / {z[17]}",*z[18:21]] # type: ignore
                                table.insert(parent='', index='end', iid=j, text='', values=v)
                                table.place(x=0,y=0)
                                j+=1
                        CTkButton(Center,width=200,text='Go Back to Admin Page',height=50,command=lambda: Admin(self)).place(x=300,y=564)

        def L4fun_welcome(self):
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color="black")
                Starting_Frame.place(x=0,y=0)
                WELCOME=CTkLabel(Starting_Frame,text_color='white',text="Registerd Teams",corner_radius=50,font=('sans-serf',40))
                WELCOME.place(x=50,y=400)
                self.bg=CTkImage(dark_image=Image.open("L4.png"),size=(1000,864)) # type: ignore
                self.label=CTkLabel(Starting_Frame,text='',image=self.bg) # type: ignore
                self.label.place(x=536,y=0)
                button=CTkButton(Starting_Frame,width=200,text="Start",command=lambda: L4fun(self))
                button.place(x=100,y=500)

        def L4fun(self):
                        Center=CTkFrame(self,width=1536,height=864,fg_color='peach puff')
                        Center.place(x=30,y=0)
                        table =ttk.Treeview(Center)
                        table['columns'] = ('1','2','3','4','5','6')
                        table.column('#0', width=0, stretch=tk.NO)
                        table.column('1',anchor=tk.CENTER ,width=70)
                        table.column('2', anchor=tk.CENTER, width=150)
                        table.column('3', anchor=tk.CENTER, width=70)
                        
                        table.column('4',anchor=tk.CENTER ,width=250)
                        table.column('5', anchor=tk.CENTER, width=250)
                        table.column('6', anchor=tk.CENTER, width=250)
                        style = ttk.Style()
                        style.configure("Treeview.Heading", font=(None,15))
                        style.configure('Treeview', rowheight=50)
                        table.heading('#0', text='', anchor=tk.CENTER)
                        table.heading('1', text='Sr No', anchor=tk.CENTER)
                        table.heading('2', text='Team Name', anchor=tk.CENTER)
                        table.heading('3', text='Format', anchor=tk.CENTER)
                        table.heading('4', text='Wins/Loss/Tie T20', anchor=tk.CENTER)
                        table.heading('5', text='Wins/Loss/Tie ODI', anchor=tk.CENTER)
                        table.heading('6', text='Wins/Loss/Tie TEST', anchor=tk.CENTER)
                        cursor.execute("select name,Format,winst20,losst20,tiet20,winsodi,lossodi,tieodi,winstest,losstest,tietest from teams")
                        data=cursor.fetchall()
                        j=1
                        for z in data:
                                v=[j,*z[0:2],f"{z[2]} / {z[3]} / {z[4]}",f"{z[5]} / {z[6]} / {z[7]}",f"{z[8]} / {z[9]} / {z[10]}"] # type: ignore
                                table.insert(parent='', index='end', iid=j, text='', values=v)
                                table.place(x=0,y=0)
                                j+=1
                        CTkButton(Center,width=200,text='Go Back to Admin Page',height=50,command=lambda: Admin(self)).place(x=300,y=564)

        def L5fun(self):
                        Center=CTkFrame(self,width=736,height=714,fg_color='peach puff')
                        Center.place(x=400,y=50)
                        tabs=CTkTabview(Center,fg_color='white',width=500,height=500,corner_radius=10,segmented_button_selected_hover_color='blue')
                        tabs.place(x=200,y=0)
                        tabs.add('Select teams')
                        cursor.execute('select name from teams')
                        L5tempvar=[]
                        for i in cursor.fetchall():
                               L5tempvar.append(i[0]) # type: ignore
                        def combobox_callback(choice):
                                print("combobox dropdown clicked:", choice)
                        
                        L5Team1ComboBox = StringVar()
                        L5Team1=CTkComboBox(tabs.tab('Select teams'),values=L5tempvar,command=combobox_callback, variable=L5Team1ComboBox,width=300)
                        L5Team1ComboBox.set(f"{L5tempvar[0]}")
                        L5Team1.place(x=100,y=0)
                        
                        L5Team2ComboBox = StringVar()
                        L5Team2=CTkComboBox(tabs.tab('Select teams'),values=L5tempvar,command=combobox_callback, variable=L5Team2ComboBox,width=300)
                        L5Team2ComboBox.set(f"{L5tempvar[1]}")
                        L5Team2.place(x=100,y=50)
                        

                        button=CTkButton(tabs.tab('Select teams'),width=300,text=f"Submit",font=('sans-serf',20),command=lambda: L5button_check())
                        button.place(x=100,y=150)
                        def L5button_check():
                                if L5Team1ComboBox.get() == L5Team2ComboBox.get():
                                       tkm.showwarning('Error',"Both teams cannot be same")
                                else:
                                       T20.selectingplayers(self,L5Team1ComboBox.get(),L5Team2ComboBox.get())
                        
        def L6fun(self):
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color="black")
                Starting_Frame.place(x=0,y=0)
                WELCOME=CTkLabel(Starting_Frame,text_color='white',text="THIS PAGE IS COMING SOON",corner_radius=50,font=('sans-serf',35))
                WELCOME.place(x=0,y=400)
                self.bg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1000,864)) # type: ignore
                self.label=CTkLabel(Starting_Frame,text='',image=self.bg) # type: ignore
                self.label.place(x=536,y=0)
                button=CTkButton(Starting_Frame,width=200,text="Go Back to Admin Page",command=lambda: Admin(self))
                button.place(x=150,y=490)

        def R1fun(self):# Function body
                        self.destroy()
        def R2fun(self):# Function body
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color="black")
                Starting_Frame.place(x=0,y=0)
                WELCOME=CTkLabel(Starting_Frame,text_color='white',text="THIS PAGE IS COMING SOON",corner_radius=50,font=('sans-serf',35))
                WELCOME.place(x=0,y=400)
                self.bg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1000,864)) # type: ignore
                self.label=CTkLabel(Starting_Frame,text='',image=self.bg) # type: ignore
                self.label.place(x=536,y=0)
                button=CTkButton(Starting_Frame,width=200,text="Go Back to Admin Page",command=lambda: Admin(self))
                button.place(x=150,y=490)   
        def R3fun(self):# Function body
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color="black")
                Starting_Frame.place(x=0,y=0)
                WELCOME=CTkLabel(Starting_Frame,text_color='white',text="THIS PAGE IS COMING SOON",corner_radius=50,font=('sans-serf',35))
                WELCOME.place(x=0,y=400)
                self.bg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1000,864)) # type: ignore
                self.label=CTkLabel(Starting_Frame,text='',image=self.bg) # type: ignore
                self.label.place(x=536,y=0)
                button=CTkButton(Starting_Frame,width=200,text="Go Back to Admin Page",command=lambda: Admin(self))
                button.place(x=150,y=490)   


class T20():
        def selectingplayers(self,team1,team2):
                Center=CTkFrame(self,width=736,height=714,fg_color='peach puff')
                Center.place(x=400,y=50)
                tabs=CTkTabview(Center,fg_color='white',width=500,height=500,corner_radius=10,segmented_button_selected_hover_color='blue')
                tabs.place(x=200,y=0)
                tabs.add(f"{team1}'s 11")
                tabs.add(f"{team2}'s 11")             
                team1_11=[]
                team2_11=[]
                team1_11r,team2_11r=[],[]
                cursor.execute(f"select name from Players where team='{team1}'")
                for i in cursor.fetchall():
                        team1_11.append(i[0]) # type: ignore # type: ignore
                        team1_11r.append(i[0]) # type: ignore
                cursor.execute(f"select name from Players where team='{team2}'")
                for i in cursor.fetchall():
                        team2_11.append(i[0]) # type: ignore # type: ignore
                        team2_11r.append(i[0]) # type: ignore

                def combobox_callback1():
                        if len(Team1ComboBox.get())!=0:
                            cursor.execute(f"insert into first values ('{Team1ComboBox.get()}',0,0,0,0,-1,'Yet to Bat')") 

                            team1_11.remove(Team1ComboBox.get())
                            Team1.configure(values=team1_11)
                            Team1ComboBox.set('')
                            tkm.showinfo('Successfully selected',f"Successfully selected {Team1ComboBox.get()}")
                        if len([*team1_11,*team2_11])==0:
                               mydb.commit()
                               tkm.showinfo('Successfully selected',f"Successfully selected the teams")
                               Scoreboard.Starting_First_Innings(self,team1,team2,60,11)  # type: ignore
                def combobox_callback2():
                        if len(Team2ComboBox.get())!=0:    
                            cursor.execute(f"insert into second values ('{Team2ComboBox.get()}',0,0,0,0,-1,'Yet to Bat')")
                            team2_11.remove(Team2ComboBox.get())
                            Team2.configure(values=team2_11)
                            Team2ComboBox.set('')
                            tkm.showinfo('Successfully selected',f"Successfully selected {Team2ComboBox.get()}")
                        if len([*team1_11,*team2_11])==0:
                               mydb.commit()
                               tkm.showinfo('Successfully selected',f"Successfully selected the teams")
                               Scoreboard.Starting_First_Innings(self,team1,team2,60,11)  # type: ignore
                
                Team1ComboBox = StringVar()
                Team1=CTkComboBox(tabs.tab(f"{team1}'s 11"),values=team1_11, variable=Team1ComboBox,width=300,height=70)
                Team1ComboBox.set(f"{team1_11[0]}")
                Team1.place(x=100,y=30)
                        
                Team2ComboBox = StringVar()
                Team2=CTkComboBox(tabs.tab(f"{team2}'s 11"),values=team2_11, variable=Team2ComboBox,width=300,height=70)
                Team2ComboBox.set(f"{team2_11[1]}")
                Team2.place(x=100,y=30)
                
                def Select_Random():
                        mydb.rollback()
                        for i in range(11):
                                cursor.execute(f"insert into first values ('{team1_11r[i]}',0,0,0,0,-1,'Yet to Bat')")  
                        for i in range(11):         
                               cursor.execute(f"insert into second values ('{team2_11r[i]}',0,0,0,0,-1,'Yet to Bat')")
                        mydb.commit()
                        tkm.showinfo('Successfully selected',f"Successfully selected the teams")
                        Scoreboard.Starting_First_Innings(self,team1,team2,60,11) # type: ignore

                Random1=CTkButton(tabs.tab(f"{team1}'s 11"),width=300,text=f"Select First 11",font=('sans-serf',20),command=Select_Random)
                Random1.place(x=100,y=200)
                Random2=CTkButton(tabs.tab(f"{team2}'s 11"),width=300,text=f"Select First 11",font=('sans-serf',20),command=Select_Random)
                Random2.place(x=100,y=200)

                selection_team1=CTkButton(tabs.tab(f"{team1}'s 11"),width=300,text=f"Submit",font=('sans-serf',20),command=combobox_callback1)
                selection_team1.place(x=100,y=300)
                selection_team2=CTkButton(tabs.tab(f"{team2}'s 11"),width=300,text=f"Submit",font=('sans-serf',20),command=combobox_callback2)
                selection_team2.place(x=100,y=300)

        


class Scoreboard():
        def Starting_First_Innings(self,team1,team2,Balls,Wickets):
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color="black")
                Starting_Frame.place(x=0,y=0)
                WELCOME=CTkLabel(Starting_Frame,text_color='white',text="FIRST INNINGS",corner_radius=50,font=('sans-serf',40))
                WELCOME.place(x=50,y=400)
                self.bg=CTkImage(dark_image=Image.open("T20.png"),size=(1000,864)) # type: ignore
                self.label=CTkLabel(Starting_Frame,text='',image=self.bg) # type: ignore
                self.label.place(x=536,y=0)
                button=CTkButton(Starting_Frame,width=200,text="Start",command=lambda: Scoreboard.Target(self,team1,team2,Balls,Wickets))
                button.place(x=100,y=500)
        def Starting_Second_Innings(self,team1,team2,Balls,Wickets):
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color="black")
                Starting_Frame.place(x=0,y=0)
                WELCOME=CTkLabel(Starting_Frame,text_color='white',text="SECOND INNINGS",corner_radius=50,font=('sans-serf',40))
                WELCOME.place(x=50,y=400)
                self.bg=CTkImage(dark_image=Image.open("T20.png"),size=(1000,864)) # type: ignore
                self.label=CTkLabel(Starting_Frame,text='',image=self.bg) # type: ignore
                self.label.place(x=536,y=0)
                button=CTkButton(Starting_Frame,width=200,text="Start",command=lambda: Scoreboard.Chase(self,team1,team2,Balls,Wickets))
                button.place(x=100,y=500)
        
        def Target(self,team1,team2,balls,wickets):
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color='thistle1')
                Starting_Frame.place(x=0,y=0)
                Head_Frame=CTkLabel(Starting_Frame,fg_color='thistle3',width=1536,height=64,text_color='red',text=f"{team1} VS {team2}",font=('sans-serf',40))
                Head_Frame.place(x=0,y=0)
                exitbutton=CTkButton(Head_Frame,text='X',bg_color='red',fg_color='red',hover_color=('red','red'),width=50,height=50,command=lambda: self.destroy()) # type: ignore
                exitbutton.place(x=1486,y=0)
                Commentatory=CTkTabview(Starting_Frame,fg_color='thistle2',width=768,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
                Commentatory.place(x=0,y=454)
                Commentatory.add("Commentatory")
                NB_Commentatory=CTkTextbox(Commentatory.tab("Commentatory"),fg_color='thistle2',text_color='blue',width=768,height=330)
                NB_Commentatory.place(x=0,y=0)
                NB_Commentatory_Submit=CTkButton(Commentatory.tab("Commentatory"),fg_color='thistle2',width=200,text='Submit').place(x=250,y=310)


                entrytabs=CTkTabview(Starting_Frame,fg_color='thistle2',width=768,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
                entrytabs.place(x=0,y=64)
                entrytabs.add('Normal ball')
                entrytabs.add('Wide ball')
                entrytabs.add('Leg By')
                entrytabs.add('No ball')
                entrytabs.add('Wicket ball')
                team1_11=[]
                team2_11=[]
                cursor.execute(f"select name from First")
                for i in cursor.fetchall():
                        team1_11.append(i[0]) # type: ignore # type: ignore
                cursor.execute(f"select name from second")
                for i in cursor.fetchall():
                        team2_11.append(i[0]) # type: ignore

            # Normal Ball
                

                NB_L1=CTkLabel(entrytabs.tab('Normal ball'),text='ON Strike Batter',font=('sans-serf',20)).place(x=100,y=0)
                NB_L2=CTkLabel(entrytabs.tab('Normal ball'),text='OFF Strike Batter',font=('sans-serf',20)).place(x=450,y=0)
                NB_L3=CTkLabel(entrytabs.tab('Normal ball'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                NB_L4=CTkLabel(entrytabs.tab('Normal ball'),text='Select runs',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter1 = StringVar()
                NB_ON_Batter = CTkComboBox(entrytabs.tab('Normal ball'),values=team1_11, variable=ON_Batter1,width=300,height=50)
                NB_ON_Batter.place(x=50,y=30)
                OFF_Batter1 = StringVar()
                NB_OFF_Batter = CTkComboBox(entrytabs.tab('Normal ball'),values=team1_11, variable=OFF_Batter1,width=300,height=50)
                NB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller1 = StringVar()
                NB_ON_Baller = CTkComboBox(entrytabs.tab('Normal ball'),values=team2_11, variable=ON_Baller1,width=300,height=50)
                NB_ON_Baller.place(x=400,y=100)

                NB_run_V = StringVar()
                NB_run=CTkComboBox(entrytabs.tab('Normal ball'),values=['0','1','2','3','4','6'], variable=NB_run_V,width=300,height=20)
                NB_run.place(x=50,y=110)

                NB_Commentatory=CTkTextbox(entrytabs.tab('Normal ball'),text_color='blue',width=700,height=160)
                NB_Commentatory.place(x=20,y=150)
                NB_Commentatory.insert("0.10","Enter Commentatory\n")
                NB_Submit = CTkButton(entrytabs.tab('Normal ball'),width=200,text='Submit',command=lambda: N_Submitfun(self)).place(x=250,y=310)
                def N_Submitfun(self):
                        if ON_Batter1.get()=='' or OFF_Batter1.get()=='' or ON_Baller1.get()=='' or NB_run_V.get()=='':
                                tkm.showerror('Error',"All fields are neccessary")
                        elif ON_Batter1.get() == OFF_Batter1.get():
                                tkm.showerror('Error',"ON Strike Batter and OFF Strike Batter can't be same")
                        else:   
                                cursor.execute(f"select name from fi where name='{ON_Batter1.get()}'")
                                four=int(NB_run_V.get())//4
                                six=int(NB_run_V.get())//6
                                if six==1:
                                        four=0
                                if len(cursor.fetchall())==0:
                                        cursor.execute(f"insert into fi values ('{ON_Batter1.get()}',{int(NB_run_V.get())},1,{four},{six},-1,'None')")
                                else:
                                        cursor.execute(f"update fi set runs=runs+{int(NB_run_V.get())},balls=balls+1,4s=4s+{four},6s=6s+{six} where name='{ON_Batter1.get()}'")
                                cursor.execute(f"update first set runs=runs+{int(NB_run_V.get())},balls=balls+1,4s=4s+{four},6s=6s+{six},status='Batting' where name='{ON_Batter1.get()}'")
                                if int(NB_run_V.get())%2!=0:
                                        var=ON_Batter1.get()
                                        ON_Batter1.set(OFF_Batter1.get())
                                        OFF_Batter1.set(var)
                                mydb.commit()
                                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                        cursor.execute(f"select sum(balls) from fi")
                        if balls==int(cursor.fetchall()[0][0]): # type: ignore
                                tkm.showinfo('First Innings','First Innings completed')
                                Scoreboard.Starting_Second_Innings(self,team1,team2,balls,wickets)
                                # Scoreboard.Chase(self,balls,wickets)
                        else:
                                cursor.execute(f"select name from first where wickets!=-1")
                                if len(cursor.fetchall())==1:
                                        tkm.showinfo('First Innings','First Innings completed')
                                        Scoreboard.Starting_Second_Innings(self,team1,team2,balls,wickets)


                                


            # Wide ball
                
                WB_Commentatory=CTkTextbox(entrytabs.tab('Wide ball'),text_color='blue',width=700,height=260)
                WB_Commentatory.place(x=20,y=20)
                WB_Commentatory.insert("0.10","Enter Commentatory About Wide Ball\n")
                WB_Submit = CTkButton(entrytabs.tab('Wide ball'),width=200,text='Submit',command=lambda: W_Submitfun(self)).place(x=250,y=300)
                def W_Submitfun(self):
                        cursor.execute(f"select name from fi where name='Extra'")
                        if len(cursor.fetchall())==0:
                                cursor.execute(f"insert into fi (name,runs) values('Extra',1)")
                        else:
                                cursor.execute(f"update fi set runs=runs+1 where name='Extra'")        
                        mydb.commit()
                        Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                
            # Leg By

                LB_L1=CTkLabel(entrytabs.tab('Leg By'),text='ON Strike Batter',font=('sans-serf',20)).place(x=100,y=0)
                LB_L2=CTkLabel(entrytabs.tab('Leg By'),text='OFF Strike Batter',font=('sans-serf',20)).place(x=450,y=0)
                LB_L3=CTkLabel(entrytabs.tab('Leg By'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                LB_L4=CTkLabel(entrytabs.tab('Leg By'),text='Select runs',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter2 = StringVar()
                LB_ON_Batter = CTkComboBox(entrytabs.tab('Leg By'),values=team1_11, variable=ON_Batter2,width=300,height=50)
                LB_ON_Batter.place(x=50,y=30)
                OFF_Batter2 = StringVar()
                LB_OFF_Batter = CTkComboBox(entrytabs.tab('Leg By'),values=team1_11, variable=OFF_Batter2,width=300,height=50)
                LB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller2 = StringVar()
                LB_ON_Baller = CTkComboBox(entrytabs.tab('Leg By'),values=team2_11, variable=ON_Baller2,width=300,height=50)
                LB_ON_Baller.place(x=400,y=100)

                LB_run_V = StringVar()
                LB_run=CTkComboBox(entrytabs.tab('Leg By'),values=['0','1','2','3'], variable=LB_run_V,width=300,height=20)
                LB_run.place(x=50,y=110)
                
                LB_Commentatory=CTkTextbox(entrytabs.tab('Leg By'),text_color='blue',width=700,height=160)
                LB_Commentatory.place(x=20,y=150)
                LB_Commentatory.insert("0.10","Enter Commentatory About Leg By\n")

                LB_Submit = CTkButton(entrytabs.tab('Leg By'),width=200,text='Submit',command=lambda: L_Submitfun(self)).place(x=250,y=310)
                def L_Submitfun(self):
                        if ON_Batter2.get()=='' or OFF_Batter2.get()=='' or ON_Baller2.get()=='' or LB_run_V.get()=='':
                                tkm.showerror('Error',"All fields are neccessary")
                        elif ON_Batter2.get() == OFF_Batter2.get():
                                tkm.showerror('Error',"ON Strike Batter and OFF Strike Batter can't be same")
                        else:   
                                cursor.execute(f"select name from fi where name='{ON_Batter2.get()}'")
                                if len(cursor.fetchall())==0:
                                        cursor.execute(f"insert into fi values ('{ON_Batter2.get()}',{int(LB_run_V.get())},1,0,0,-1,'None')")
                                else:
                                        cursor.execute(f"update fi set runs=runs+{int(LB_run_V.get())},balls=balls+1 where name='{ON_Batter2.get()}'")
                                if int(LB_run_V.get())%2!=0:
                                        var=ON_Batter2.get()
                                        ON_Batter2.set(OFF_Batter2.get())
                                        OFF_Batter2.set(var)
                                mydb.commit()
                                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                        if balls==int(cursor.fetchall()[0][0]): # type: ignore
                                tkm.showinfo('First Innings','First Innings completed')
                                Scoreboard.Starting_Second_Innings(self,team1,team2,balls,wickets)
                                # Scoreboard.Chase(self,balls,wickets)
                        else:
                                cursor.execute(f"select name from first where wickets!=-1")
                                if len(cursor.fetchall())==1:
                                        tkm.showinfo('First Innings','First Innings completed')
                                        Scoreboard.Starting_Second_Innings(self,team1,team2,balls,wickets)
                                        # Scoreboard.Chase(self,balls,wickets)
            # No ball

                NB_L1=CTkLabel(entrytabs.tab('No ball'),text='ON Strike Batter',font=('sans-serf',20)).place(x=100,y=0)
                NB_L2=CTkLabel(entrytabs.tab('No ball'),text='OFF Strike Batter',font=('sans-serf',20)).place(x=450,y=0)
                NB_L3=CTkLabel(entrytabs.tab('No ball'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                NB_L4=CTkLabel(entrytabs.tab('No ball'),text='Select runs',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter3 = StringVar()
                NB_ON_Batter = CTkComboBox(entrytabs.tab('No ball'),values=team1_11, variable=ON_Batter3,width=300,height=50)
                NB_ON_Batter.place(x=50,y=30)
                OFF_Batter3 = StringVar()
                NB_OFF_Batter = CTkComboBox(entrytabs.tab('No ball'),values=team1_11, variable=OFF_Batter3,width=300,height=50)
                NB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller3 = StringVar()
                NB_ON_Baller = CTkComboBox(entrytabs.tab('No ball'),values=team2_11, variable=ON_Baller3,width=300,height=50)
                NB_ON_Baller.place(x=400,y=100)

                NOB_run_V = StringVar()
                NOB_run=CTkComboBox(entrytabs.tab('No ball'),values=['0','1','2','3','4','6'] , variable=NOB_run_V,width=300,height=20)
                NOB_run.place(x=50,y=110)
                
                NOB_Commentatory=CTkTextbox(entrytabs.tab('No ball'),text_color='blue',width=700,height=160)
                NOB_Commentatory.place(x=20,y=150)
                NOB_Commentatory.insert("0.10","Enter Commentatory About No Ball\n")

                NOB_Submit = CTkButton(entrytabs.tab('No ball'),width=200,text='Submit',command=lambda: NOB_Submitfun(self)).place(x=250,y=310)
                def NOB_Submitfun(self):
                        cursor.execute(f"select name from fi where name='Extra'")
                        if len(cursor.fetchall())==0:
                                cursor.execute(f"insert into fi (name,runs) values('Extra',1+{int('0'+NOB_run_V.get())})")
                        else:
                                cursor.execute(f"update fi set runs=runs+1+{int('0'+NOB_run_V.get())} where name='Extra'")        
                        mydb.commit()
                        Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)

            # Wicket ball
                
                # wicketstabs=CTkTabview(entrytabs.tab('Wicket ball'),fg_color='thistle1',width=768,height=380,corner_radius=10)
                # wicketstabs.place(x=0,y=0)
                # wicketstabs.add('BOLD')
                # wicketstabs.add('CATCH')
                # wicketstabs.add('LBW')
                # wicketstabs.add('RUN OUT')
                # wicketstabs.add('HIT WICKET')

                # B_Submit = CTkButton(wicketstabs.tab('BOLD'),width=200,text='Submit',command=lambda: Scoreboard.B_Submitfun(self)).place(x=250,y=280)
                # C_Submit = CTkButton(wicketstabs.tab('CATCH'),width=200,text='Submit',command=lambda: Scoreboard.C_Submitfun(self)).place(x=250,y=280)
                # LBW_Submit = CTkButton(wicketstabs.tab('LBW'),width=200,text='Submit',command=lambda: Scoreboard.LBW_Submitfun(self)).place(x=250,y=280)
                # RO_Submit = CTkButton(wicketstabs.tab('RUN OUT'),width=200,text='Submit',command=lambda: Scoreboard.RO_Submitfun(self)).place(x=250,y=280)
                # HW_Submit = CTkButton(wicketstabs.tab('HIT WICKET'),width=200,text='Submit',command=lambda: Scoreboard.HW_Submitfun(self)).place(x=250,y=280)

                # if cursor
                WiB_L1=CTkLabel(entrytabs.tab('Wicket ball'),text='Batter got out',font=('sans-serf',20)).place(x=100,y=0)
                WiB_L2=CTkLabel(entrytabs.tab('Wicket ball'),text='Fielder who made out',font=('sans-serf',20)).place(x=450,y=0)
                WiB_L3=CTkLabel(entrytabs.tab('Wicket ball'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                WiB_L4=CTkLabel(entrytabs.tab('Wicket ball'),text='Select Out type',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter4 = StringVar()
                WiB_ON_Batter = CTkComboBox(entrytabs.tab('Wicket ball'),values=team1_11, variable=ON_Batter4,width=300,height=50)
                WiB_ON_Batter.place(x=50,y=30)
                OFF_Batter4 = StringVar()
                WiB_OFF_Batter = CTkComboBox(entrytabs.tab('Wicket ball'),values=team2_11, variable=OFF_Batter4,width=300,height=50)
                WiB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller4 = StringVar()
                WiB_ON_Baller = CTkComboBox(entrytabs.tab('Wicket ball'),values=team2_11, variable=ON_Baller4,width=300,height=50)
                WiB_ON_Baller.place(x=400,y=100)

                WiB_outtype_V = StringVar()
                WiB_outtype=CTkComboBox(entrytabs.tab('Wicket ball'),values=['BOLD','CATCH','LBW','RUN OUT','HIT WICKET'], variable=WiB_outtype_V,width=300,height=20)
                WiB_outtype.place(x=50,y=110)
                
                WiB_Commentatory=CTkTextbox(entrytabs.tab('Wicket ball'),text_color='blue',width=700,height=160)
                WiB_Commentatory.place(x=20,y=150)
                WiB_Commentatory.insert("0.10","Enter Commentatory About Wicket ball\n")

                WiB_Submit = CTkButton(entrytabs.tab('Wicket ball'),width=200,text='Submit',command=lambda: WiB_Submitfun(self)).place(x=250,y=310)
                def WiB_Submitfun(self):
                        if ON_Baller4.get()=='' or WiB_outtype.get()=='':
                                tkm.showwarning('Invalid Submit',"Baller and Out type can't be void")
                        elif WiB_outtype.get() in ['RUN OUT','CATCH'] and OFF_Batter4.get()=='':
                                tkm.showwarning('Invalid Submit',"For RUN OUT,CATCH OUT\nFielder who made out can't be void")
                        else:
                                cursor.execute(f"select name from fi where status= 'None'")
                                if (ON_Batter4.get(),) not in cursor.fetchall():
                                        cursor.execute(f"insert into fi values ('{ON_Batter4}',0,0,0,0,0,'None')")
                                if WiB_outtype.get()=='BOLD':
                                        cursor.execute(f"update fi set status='bold {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update first set status='bold {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                elif WiB_outtype.get()=='CATCH':
                                        cursor.execute(f"update fi set status='c {OFF_Batter4.get()} b {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update first set status='c {OFF_Batter4.get()} b {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                elif  WiB_outtype.get()=='RUN OUT':
                                        cursor.execute(f"update fi set status='run out {OFF_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update first set status='run out {OFF_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                elif WiB_outtype.get()=='LBW':
                                        cursor.execute(f"update fi set status='lbw {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update first set status='lbw {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                else:
                                        cursor.execute(f"update fi set status='Hit Wicket {ON_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update first set status='Hit Wicket {ON_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                mydb.commit()
                                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                                if balls==int(cursor.fetchall()[0][0]): # type: ignore
                                        tkm.showinfo('First Innings','First Innings completed')
                                        Scoreboard.Starting_Second_Innings(self,team1,team2,balls,wickets)
                                        # Scoreboard.Chase(self,balls,wickets)
                                else:
                                        cursor.execute(f"select name from first where wickets!=-1")
                                        if len(cursor.fetchall())==1:
                                                tkm.showinfo('First Innings','First Innings completed')
                                                Scoreboard.Starting_Second_Innings(self,team1,team2,balls,wickets)
                                                # Scoreboard.Chase(self,balls,wickets) 



            #############################################################################################################            

                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)


                


                values = [49, 76, 61, 65, 510, 24, 9, 29, 53, 24]

                Graph=CTkGraph(Starting_Frame, values, width=300, height=300, fg_color='white', graph_color='white',graph_line_color='black',graph_axis_color='black',
                        graph_fg_color="white",title_text_color='black', title="Worm Graph\nScoring Comparison", title_font_size=30, corner_radius=20)
                Graph.place(x=1230,y=84)

                # Summary=CTkTabview(Starting_Frame,fg_color='thistle2',width=455,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
                # Summary.place(x=773,y=64)
                # Summary.add("STATS")
                # Stat1=CTkLabel(Summary.tab("STATS"),text=f"{team1}{'  '*10}0/0(0.0)",font=('sans-serf',30)).place(x=0,y=0)
                # Stat2=CTkLabel(Summary.tab("STATS"),text=f"{team2}{'  '*5}0/0(0.0)",font=('sans-serf',30)).place(x=0,y=50)

                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(455,400))
                Summary=CTkLabel(Starting_Frame,image=self.lbg,fg_color='thistle2',width=455,height=400)
                Summary.place(x=773,y=64)

        def Chase(self,team1,team2,balls,wickets):
                Starting_Frame = CTkFrame(self,width=1536,height=864,fg_color='thistle1')
                Starting_Frame.place(x=0,y=0)
                Head_Frame=CTkLabel(Starting_Frame,fg_color='thistle3',width=1536,height=64,text_color='red',text=f"{team1} VS {team2}",font=('sans-serf',40))
                Head_Frame.place(x=0,y=0)
                exitbutton=CTkButton(Head_Frame,text='X',bg_color='red',fg_color='red',hover_color=('red','red'),width=50,height=50,command=lambda: self.destroy()) # type: ignore
                exitbutton.place(x=1486,y=0)
                Commentatory=CTkTabview(Starting_Frame,fg_color='thistle2',width=768,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
                Commentatory.place(x=0,y=454)
                Commentatory.add("Commentatory")
                NB_Commentatory=CTkTextbox(Commentatory.tab("Commentatory"),fg_color='thistle2',text_color='blue',width=768,height=330)
                NB_Commentatory.place(x=0,y=0)
                NB_Commentatory_Submit=CTkButton(Commentatory.tab("Commentatory"),fg_color='thistle2',width=200,text='Submit').place(x=250,y=310)


                entrytabs=CTkTabview(Starting_Frame,fg_color='thistle2',width=768,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
                entrytabs.place(x=0,y=64)
                entrytabs.add('Normal ball')
                entrytabs.add('Wide ball')
                entrytabs.add('Leg By')
                entrytabs.add('No ball')
                entrytabs.add('Wicket ball')
                team1_11=[]
                team2_11=[]
                cursor.execute(f"select name from First")
                for i in cursor.fetchall():
                        team2_11.append(i[0]) # type: ignore # type: ignore # type: ignore
                cursor.execute(f"select name from second")
                for i in cursor.fetchall():
                        team1_11.append(i[0]) # type: ignore

            # Normal Ball
                

                NB_L1=CTkLabel(entrytabs.tab('Normal ball'),text='ON Strike Batter',font=('sans-serf',20)).place(x=100,y=0)
                NB_L2=CTkLabel(entrytabs.tab('Normal ball'),text='OFF Strike Batter',font=('sans-serf',20)).place(x=450,y=0)
                NB_L3=CTkLabel(entrytabs.tab('Normal ball'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                NB_L4=CTkLabel(entrytabs.tab('Normal ball'),text='Select runs',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter1 = StringVar()
                NB_ON_Batter = CTkComboBox(entrytabs.tab('Normal ball'),values=team1_11, variable=ON_Batter1,width=300,height=50)
                NB_ON_Batter.place(x=50,y=30)
                OFF_Batter1 = StringVar()
                NB_OFF_Batter = CTkComboBox(entrytabs.tab('Normal ball'),values=team1_11, variable=OFF_Batter1,width=300,height=50)
                NB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller1 = StringVar()
                NB_ON_Baller = CTkComboBox(entrytabs.tab('Normal ball'),values=team2_11, variable=ON_Baller1,width=300,height=50)
                NB_ON_Baller.place(x=400,y=100)

                NB_run_V = StringVar()
                NB_run=CTkComboBox(entrytabs.tab('Normal ball'),values=['0','1','2','3','4','6'], variable=NB_run_V,width=300,height=20)
                NB_run.place(x=50,y=110)

                NB_Commentatory=CTkTextbox(entrytabs.tab('Normal ball'),text_color='blue',width=700,height=160)
                NB_Commentatory.place(x=20,y=150)
                NB_Commentatory.insert("0.10","Enter Commentatory\n")
                NB_Submit = CTkButton(entrytabs.tab('Normal ball'),width=200,text='Submit',command=lambda: N_Submitfun(self)).place(x=250,y=310)
                def N_Submitfun(self):
                        if ON_Batter1.get()=='' or OFF_Batter1.get()=='' or ON_Baller1.get()=='' or NB_run_V.get()=='':
                                tkm.showerror('Error',"All fields are neccessary")
                        elif ON_Batter1.get() == OFF_Batter1.get():
                                tkm.showerror('Error',"ON Strike Batter and OFF Strike Batter can't be same")
                        else:   
                                cursor.execute(f"select name from si where name='{ON_Batter1.get()}'")
                                four=int(NB_run_V.get())//4
                                six=int(NB_run_V.get())//6
                                if six==1:
                                        four=0
                                if len(cursor.fetchall())==0:
                                        cursor.execute(f"insert into si values ('{ON_Batter1.get()}',{int(NB_run_V.get())},1,{four},{six},-1,'None')")
                                else:
                                        cursor.execute(f"update si set runs=runs+{int(NB_run_V.get())},balls=balls+1,4s=4s+{four},6s=6s+{six} where name='{ON_Batter1.get()}'")
                                cursor.execute(f"update second set runs=runs+{int(NB_run_V.get())},balls=balls+1,4s=4s+{four},6s=6s+{six},status='Batting' where name='{ON_Batter1.get()}'")
                                if int(NB_run_V.get())%2!=0:
                                        var=ON_Batter1.get()
                                        ON_Batter1.set(OFF_Batter1.get())
                                        OFF_Batter1.set(var)
                                mydb.commit()
                                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                                cursor.execute("select sum(runs) from  first")
                                target=int(cursor.fetchall()[0][0])+1# type: ignore
                                cursor.execute("select sum(runs) from second")
                                chased=int(cursor.fetchall()[0][0]) # type: ignore
                                if target<chased:
                                        tkm.showinfo('Summary',f"{team2} won")
                                        cursor.execute(f"truncate fi")
                                        cursor.execute(f"truncate si")
                                        cursor.execute(f"truncate first")
                                        cursor.execute(f"truncate second")
                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                        Summary.place(x=0,y=0)

                                elif target>chased:
                                        cursor.execute("select name from si where status!='Yet to Bat'")
                                        if len(cursor.fetchall()) in range(0,11):
                                                cursor.execute("select sum(balls) from si")
                                                if int(cursor.fetchall()[0][0])==balls: # type: ignore
                                                        tkm.showinfo('Summary',f"{team1} won")
                                                        cursor.execute(f"truncate fi")
                                                        cursor.execute(f"truncate si")
                                                        cursor.execute(f"truncate first")
                                                        cursor.execute(f"truncate second")
                                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                                        Summary.place(x=0,y=0)  
                                else:
                                        tkm.showinfo('Summary',f"It's a Tie")
                                        cursor.execute(f"truncate fi")
                                        cursor.execute(f"truncate si")
                                        cursor.execute(f"truncate first")
                                        cursor.execute(f"truncate second")
                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                        Summary.place(x=0,y=0)
                                


            # Wide ball
                
                WB_Commentatory=CTkTextbox(entrytabs.tab('Wide ball'),text_color='blue',width=700,height=260)
                WB_Commentatory.place(x=20,y=20)
                WB_Commentatory.insert("0.10","Enter Commentatory About Wide Ball\n")
                WB_Submit = CTkButton(entrytabs.tab('Wide ball'),width=200,text='Submit',command=lambda: W_Submitfun(self)).place(x=250,y=300)
                def W_Submitfun(self):
                        cursor.execute(f"select name from si where name='Extra'")
                        if len(cursor.fetchall())==0:
                                cursor.execute(f"insert into si (name,runs) values('Extra',1)")
                        else:
                                cursor.execute(f"update si set runs=runs+1 where name='Extra'")        
                        mydb.commit()
                        Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                        cursor.execute("select sum(runs) from  first")
                        target=int(cursor.fetchall()[0][0]) +1# type: ignore
                        cursor.execute("select sum(runs) from second")
                        chased=int(cursor.fetchall()[0][0]) # type: ignore
                        if target<chased:
                                tkm.showinfo('Summary',f"{team2} won")
                                cursor.execute(f"truncate fi")
                                cursor.execute(f"truncate si")
                                cursor.execute(f"truncate first")
                                cursor.execute(f"truncate second")
                                z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                Summary.place(x=0,y=0)
                        elif target>chased:
                                cursor.execute("select name from si where status!='Yet to Bat'")
                                if len(cursor.fetchall()) in range(0,11):
                                        cursor.execute("select sum(balls) from si")
                                        if int(cursor.fetchall()[0][0])==balls: # type: ignore
                                                tkm.showinfo('Summary',f"{team1} won")  
                                                cursor.execute(f"truncate fi")
                                                cursor.execute(f"truncate si")
                                                cursor.execute(f"truncate first")
                                                cursor.execute(f"truncate second")
                                                z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                                Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                                Summary.place(x=0,y=0)
                        else:
                                tkm.showinfo('Summary',f"It's a Tie")
                                cursor.execute(f"truncate fi")
                                cursor.execute(f"truncate si")
                                cursor.execute(f"truncate first")
                                cursor.execute(f"truncate second")
                                z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                Summary.place(x=0,y=0)
                
            # Leg By

                LB_L1=CTkLabel(entrytabs.tab('Leg By'),text='ON Strike Batter',font=('sans-serf',20)).place(x=100,y=0)
                LB_L2=CTkLabel(entrytabs.tab('Leg By'),text='OFF Strike Batter',font=('sans-serf',20)).place(x=450,y=0)
                LB_L3=CTkLabel(entrytabs.tab('Leg By'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                LB_L4=CTkLabel(entrytabs.tab('Leg By'),text='Select runs',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter2 = StringVar()
                LB_ON_Batter = CTkComboBox(entrytabs.tab('Leg By'),values=team1_11, variable=ON_Batter2,width=300,height=50)
                LB_ON_Batter.place(x=50,y=30)
                OFF_Batter2 = StringVar()
                LB_OFF_Batter = CTkComboBox(entrytabs.tab('Leg By'),values=team1_11, variable=OFF_Batter2,width=300,height=50)
                LB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller2 = StringVar()
                LB_ON_Baller = CTkComboBox(entrytabs.tab('Leg By'),values=team2_11, variable=ON_Baller2,width=300,height=50)
                LB_ON_Baller.place(x=400,y=100)

                LB_run_V = StringVar()
                LB_run=CTkComboBox(entrytabs.tab('Leg By'),values=['0','1','2','3'], variable=LB_run_V,width=300,height=20)
                LB_run.place(x=50,y=110)
                
                LB_Commentatory=CTkTextbox(entrytabs.tab('Leg By'),text_color='blue',width=700,height=160)
                LB_Commentatory.place(x=20,y=150)
                LB_Commentatory.insert("0.10","Enter Commentatory About Leg By\n")

                LB_Submit = CTkButton(entrytabs.tab('Leg By'),width=200,text='Submit',command=lambda: L_Submitfun(self)).place(x=250,y=310)
                def L_Submitfun(self):
                        if ON_Batter2.get()=='' or OFF_Batter2.get()=='' or ON_Baller2.get()=='' or LB_run_V.get()=='':
                                tkm.showerror('Error',"All fields are neccessary")
                        elif ON_Batter2.get() == OFF_Batter2.get():
                                tkm.showerror('Error',"ON Strike Batter and OFF Strike Batter can't be same")
                        else:   
                                cursor.execute(f"select name from si where name='{ON_Batter2.get()}'")
                                if len(cursor.fetchall())==0:
                                        cursor.execute(f"insert into si values ('{ON_Batter2.get()}',{int(LB_run_V.get())},1,0,0,-1,'None')")
                                else:
                                        cursor.execute(f"update si set runs=runs+{int(LB_run_V.get())},balls=balls+1 where name='{ON_Batter2.get()}'")
                                cursor.execute(f"update second set runs=runs+{int(LB_run_V.get())},balls=balls+1 where name='{ON_Batter2.get()}'")
                                if int(LB_run_V.get())%2!=0:
                                        var=ON_Batter2.get()
                                        ON_Batter2.set(OFF_Batter2.get())
                                        OFF_Batter2.set(var)
                                mydb.commit()
                                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                                cursor.execute("select sum(runs) from  first")
                                target=int(cursor.fetchall()[0][0])+1 # type: ignore
                                cursor.execute("select sum(runs) from second")
                                chased=int(cursor.fetchall()[0][0]) # type: ignore
                                if target<chased:
                                        tkm.showinfo('Summary',f"{team2} won")
                                        cursor.execute(f"truncate fi")
                                        cursor.execute(f"truncate si")
                                        cursor.execute(f"truncate first")
                                        cursor.execute(f"truncate second")
                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                        Summary.place(x=0,y=0)
                                elif target>chased:
                                        cursor.execute("select name from si where status!='Yet to Bat'")
                                        if len(cursor.fetchall()) in range(0,11):
                                                cursor.execute("select sum(balls) from si")
                                                if int(cursor.fetchall()[0][0])==balls: # type: ignore
                                                        tkm.showinfo('Summary',f"{team1} won")  
                                                        cursor.execute(f"truncate fi")
                                                        cursor.execute(f"truncate si")
                                                        cursor.execute(f"truncate first")
                                                        cursor.execute(f"truncate second")
                                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                                        Summary.place(x=0,y=0)
                                else:
                                        tkm.showinfo('Summary',f"It's a Tie")
                                        cursor.execute(f"truncate fi")
                                        cursor.execute(f"truncate si")
                                        cursor.execute(f"truncate first")
                                        cursor.execute(f"truncate second")
                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                        Summary.place(x=0,y=0)

            # No ball

                NB_L1=CTkLabel(entrytabs.tab('No ball'),text='ON Strike Batter',font=('sans-serf',20)).place(x=100,y=0)
                NB_L2=CTkLabel(entrytabs.tab('No ball'),text='OFF Strike Batter',font=('sans-serf',20)).place(x=450,y=0)
                NB_L3=CTkLabel(entrytabs.tab('No ball'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                NB_L4=CTkLabel(entrytabs.tab('No ball'),text='Select runs',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter3 = StringVar()
                NB_ON_Batter = CTkComboBox(entrytabs.tab('No ball'),values=team1_11, variable=ON_Batter3,width=300,height=50)
                NB_ON_Batter.place(x=50,y=30)
                OFF_Batter3 = StringVar()
                NB_OFF_Batter = CTkComboBox(entrytabs.tab('No ball'),values=team1_11, variable=OFF_Batter3,width=300,height=50)
                NB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller3 = StringVar()
                NB_ON_Baller = CTkComboBox(entrytabs.tab('No ball'),values=team2_11, variable=ON_Baller3,width=300,height=50)
                NB_ON_Baller.place(x=400,y=100)

                NOB_run_V = StringVar()
                NOB_run=CTkComboBox(entrytabs.tab('No ball'),values=['0','1','2','3','4','6'] , variable=NOB_run_V,width=300,height=20)
                NOB_run.place(x=50,y=110)
                
                NOB_Commentatory=CTkTextbox(entrytabs.tab('No ball'),text_color='blue',width=700,height=160)
                NOB_Commentatory.place(x=20,y=150)
                NOB_Commentatory.insert("0.10","Enter Commentatory About No Ball\n")

                NOB_Submit = CTkButton(entrytabs.tab('No ball'),width=200,text='Submit',command=lambda: NOB_Submitfun(self)).place(x=250,y=310)
                def NOB_Submitfun(self):
                        cursor.execute(f"select name from si where name='Extra'")
                        if len(cursor.fetchall())==0:
                                cursor.execute(f"insert into si (name,runs) values('Extra',1+{int('0'+NOB_run_V.get())})")
                        else:
                                cursor.execute(f"update si set runs=runs+1+{int('0'+NOB_run_V.get())} where name='Extra'")        
                        mydb.commit()
                        Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                        cursor.execute("select sum(runs) from  first")
                        target=int(cursor.fetchall()[0][0]) + 1 # type: ignore
                        cursor.execute("select sum(runs) from second")
                        chased=int(cursor.fetchall()[0][0]) # type: ignore
                        if target<chased:
                                tkm.showinfo('Summary',f"{team2} won")
                                cursor.execute(f"truncate fi")
                                cursor.execute(f"truncate si")
                                cursor.execute(f"truncate first")
                                cursor.execute(f"truncate second")
                                z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                Summary.place(x=0,y=0) 
                        elif target>chased:
                                cursor.execute("select name from si where status!='Yet to Bat'")
                                if len(cursor.fetchall()) in range(0,11):
                                        cursor.execute("select sum(balls) from si")
                                        if int(cursor.fetchall()[0][0])==balls: # type: ignore
                                                tkm.showinfo('Summary',f"{team1} won")
                                                cursor.execute(f"truncate fi")
                                                cursor.execute(f"truncate si")
                                                cursor.execute(f"truncate first")
                                                cursor.execute(f"truncate second")
                                                z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                                Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                                Summary.place(x=0,y=0) 
                                 
                        else:
                                tkm.showinfo('Summary',f"It's a Tie")
                                cursor.execute(f"truncate fi")
                                cursor.execute(f"truncate si")
                                cursor.execute(f"truncate first")
                                cursor.execute(f"truncate second")
                                z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                Summary.place(x=0,y=0) 


            # Wicket ball
                
                # wicketstabs=CTkTabview(entrytabs.tab('Wicket ball'),fg_color='thistle1',width=768,height=380,corner_radius=10)
                # wicketstabs.place(x=0,y=0)
                # wicketstabs.add('BOLD')
                # wicketstabs.add('CATCH')
                # wicketstabs.add('LBW')
                # wicketstabs.add('RUN OUT')
                # wicketstabs.add('HIT WICKET')

                # B_Submit = CTkButton(wicketstabs.tab('BOLD'),width=200,text='Submit',command=lambda: Scoreboard.B_Submitfun(self)).place(x=250,y=280)
                # C_Submit = CTkButton(wicketstabs.tab('CATCH'),width=200,text='Submit',command=lambda: Scoreboard.C_Submitfun(self)).place(x=250,y=280)
                # LBW_Submit = CTkButton(wicketstabs.tab('LBW'),width=200,text='Submit',command=lambda: Scoreboard.LBW_Submitfun(self)).place(x=250,y=280)
                # RO_Submit = CTkButton(wicketstabs.tab('RUN OUT'),width=200,text='Submit',command=lambda: Scoreboard.RO_Submitfun(self)).place(x=250,y=280)
                # HW_Submit = CTkButton(wicketstabs.tab('HIT WICKET'),width=200,text='Submit',command=lambda: Scoreboard.HW_Submitfun(self)).place(x=250,y=280)

                # if cursor
                WiB_L1=CTkLabel(entrytabs.tab('Wicket ball'),text='Batter got out',font=('sans-serf',20)).place(x=100,y=0)
                WiB_L2=CTkLabel(entrytabs.tab('Wicket ball'),text='Fielder who made out',font=('sans-serf',20)).place(x=450,y=0)
                WiB_L3=CTkLabel(entrytabs.tab('Wicket ball'),text='Current Baller',font=('sans-serf',20)).place(x=450,y=80)
                WiB_L4=CTkLabel(entrytabs.tab('Wicket ball'),text='Select Out type',font=('sans-serf',20)).place(x=100,y=80)

                ON_Batter4 = StringVar()
                WiB_ON_Batter = CTkComboBox(entrytabs.tab('Wicket ball'),values=team1_11, variable=ON_Batter4,width=300,height=50)
                WiB_ON_Batter.place(x=50,y=30)
                OFF_Batter4 = StringVar()
                WiB_OFF_Batter = CTkComboBox(entrytabs.tab('Wicket ball'),values=team2_11, variable=OFF_Batter4,width=300,height=50)
                WiB_OFF_Batter.place(x=400,y=30)
                
                ON_Baller4 = StringVar()
                WiB_ON_Baller = CTkComboBox(entrytabs.tab('Wicket ball'),values=team2_11, variable=ON_Baller4,width=300,height=50)
                WiB_ON_Baller.place(x=400,y=100)

                WiB_outtype_V = StringVar()
                WiB_outtype=CTkComboBox(entrytabs.tab('Wicket ball'),values=['BOLD','CATCH','LBW','RUN OUT','HIT WICKET'], variable=WiB_outtype_V,width=300,height=20)
                WiB_outtype.place(x=50,y=110)
                
                WiB_Commentatory=CTkTextbox(entrytabs.tab('Wicket ball'),text_color='blue',width=700,height=160)
                WiB_Commentatory.place(x=20,y=150)
                WiB_Commentatory.insert("0.10","Enter Commentatory About Wicket ball\n")

                WiB_Submit = CTkButton(entrytabs.tab('Wicket ball'),width=200,text='Submit',command=lambda: WiB_Submitfun(self)).place(x=250,y=310)
                def WiB_Submitfun(self):
                        if ON_Baller4.get()=='' or WiB_outtype.get()=='':
                                tkm.showwarning('Invalid Submit',"Baller and Out type can't be void")
                        elif WiB_outtype.get() in ['RUN OUT','CATCH'] and OFF_Batter4.get()=='':
                                tkm.showwarning('Invalid Submit',"For RUN OUT,CATCH OUT\nFielder who made out can't be void")
                        else:
                                cursor.execute(f"select name from fi where status= 'None'")
                                if (ON_Batter4.get(),) not in cursor.fetchall():
                                        cursor.execute(f"insert into si values ('{ON_Batter4}',0,0,0,0,0,'None')")
                                if WiB_outtype.get()=='BOLD':
                                        cursor.execute(f"update si set status='bold {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update second set status='bold {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                elif WiB_outtype.get()=='CATCH':
                                        cursor.execute(f"update si set status='c {OFF_Batter4.get()} b {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update second set status='c {OFF_Batter4.get()} b {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                elif  WiB_outtype.get()=='RUN OUT':
                                        cursor.execute(f"update si set status='run out {OFF_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update second set status='run out {OFF_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                elif WiB_outtype.get()=='LBW':
                                        cursor.execute(f"update si set status='lbw {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update second set status='lbw {ON_Baller4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                else:
                                        cursor.execute(f"update si set status='Hit Wicket {ON_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                        cursor.execute(f"update second set status='Hit Wicket {ON_Batter4.get()}',balls=balls+1 where name='{ON_Batter4.get()}'")
                                mydb.commit()
                                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)
                                cursor.execute("select sum(runs) from  first")
                                target=int(cursor.fetchall()[0][0]) + 1 # type: ignore
                                cursor.execute("select sum(runs) from second")
                                chased=int(cursor.fetchall()[0][0]) # type: ignore
                                if target<chased:
                                        tkm.showinfo('Summary',f"{team2} won")
                                        cursor.execute(f"truncate fi")
                                        cursor.execute(f"truncate si")
                                        cursor.execute(f"truncate first")
                                        cursor.execute(f"truncate second")
                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                        Summary.place(x=0,y=0)
                                elif target>chased:
                                        cursor.execute("select name from si where status!='Yet to Bat'")
                                        if len(cursor.fetchall()) in range(0,11):
                                                cursor.execute("select sum(balls) from si")
                                                if int(cursor.fetchall()[0][0])==balls: # type: ignore
                                                        tkm.showinfo('Summary',f"{team1} won")
                                                        cursor.execute(f"truncate fi")
                                                        cursor.execute(f"truncate si")
                                                        cursor.execute(f"truncate first")
                                                        cursor.execute(f"truncate second")
                                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                                        Summary.place(x=0,y=0) 
                                        
                                else:
                                        tkm.showinfo('Summary',f"It's a Tie")
                                        cursor.execute(f"truncate fi")
                                        cursor.execute(f"truncate si")
                                        cursor.execute(f"truncate first")
                                        cursor.execute(f"truncate second")
                                        z=CTkLabel(self,width=1536,height=814,fg_color='black').place(x=0,y=0)
                                        self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(1536,814))
                                        Summary=CTkLabel(z,image=self.lbg,fg_color='thistle2',width=1536,height=814)
                                        Summary.place(x=0,y=0) 



            #############################################################################################################            

                Scoreboard.updatescorecard(self,team1,team2,Starting_Frame)


                


                values = [49, 76, 61, 65, 510, 24, 9, 29, 53, 24]

                Graph=CTkGraph(Starting_Frame, values, width=300, height=300, fg_color='white', graph_color='white',graph_line_color='black',graph_axis_color='black',
                        graph_fg_color="white",title_text_color='black', title="Worm Graph\nScoring Comparison", title_font_size=30, corner_radius=20)
                Graph.place(x=1230,y=84)
                self.lbg=CTkImage(dark_image=Image.open("CMS_logo.jpg"),size=(455,400))
                Summary=CTkLabel(Starting_Frame,image=self.lbg,fg_color='thistle2',width=455,height=400)
                Summary.place(x=773,y=64)
                # Summary.add(f"STATS")
                # Stat1=CTkLabel(Summary.tab("STATS"),text=f"{team1}{'  '*10}0/0(0.0)",font=('sans-serf',30)).place(x=0,y=0)
                # Stat2=CTkLabel(Summary.tab("STATS"),text=f"{team2}{'  '*5}0/0(0.0)",font=('sans-serf',30)).place(x=0,y=50)



        def updatescorecard(self,team1,team2,frame):
                tabs=CTkTabview(frame,fg_color='white',width=768,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
                tabs.place(x=768,y=454)
                tabs.add("Scorecard")
                scoreboardtabs=CTkTabview(tabs.tab("Scorecard"),fg_color='white',width=768,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
                scoreboardtabs.place(x=0,y=0)
                scoreboardtabs.add(f"{team1}'s innings")
                scoreboardtabs.add(f"{team2}'s innings")
                t=[scoreboardtabs.tab(f"{team1}'s innings"),scoreboardtabs.tab(f"{team2}'s innings")]
                for i in range (2):
                        if i==0:
                                cursor.execute(f"select name,runs,balls,Status,4s,6s,runs*100/balls from first ")
                        else:
                                cursor.execute(f"select name,runs,balls,Status,4s,6s,runs*100/balls from second ")   
                        table =ttk.Treeview(t[i])
                        table['columns'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14')
                        table.column('#0', width=0, stretch=tk.NO)
                        table.column('1',anchor=tk.CENTER ,width=200)
                        table.column('2', anchor=tk.CENTER, width=100)
                        table.column('3', anchor=tk.CENTER, width=100)
                        
                        table.column('4',anchor=tk.CENTER ,width=200)
                        table.column('5', anchor=tk.CENTER, width=100)
                        table.column('6', anchor=tk.CENTER, width=100)
                        table.column('7', anchor=tk.CENTER, width=100)
                        style = ttk.Style()
                        style.configure("Treeview.Heading", font=('sans-serf',15))
                        style.configure("Treeview.Insert", font=('sans-serf',15))
                        style.configure('Treeview', rowheight=50)
                        table.heading('#0', text='', anchor=tk.CENTER)
                        table.heading('1', text='Player Name', anchor=tk.CENTER)
                        table.heading('2', text='Runs', anchor=tk.CENTER)
                        table.heading('3', text='Balls', anchor=tk.CENTER)
                        table.heading('4', text='Status', anchor=tk.CENTER)
                        table.heading('5', text='4s', anchor=tk.CENTER)
                        table.heading('6', text='6s', anchor=tk.CENTER)
                        table.heading('7', text='SR', anchor=tk.CENTER)
                        va=cursor.fetchall()
                        for i in range(len(va)):
                                table.insert(parent='', index='end', iid=i, text='', values=[*va[i]])

                        table.place(x=0,y=0)
        

        # def stat(self,team1,team2,frame):
        #         Summary=CTkTabview(frame,fg_color='thistle2',width=455,height=400,corner_radius=10,segmented_button_selected_hover_color='blue')
        #         Summary.place(x=773,y=64)
        #         Summary.add("STATS")
        #         cursor.execute("select sum(runs) from fi")
        #         t1r=int(cursor.fetchall()[0][0]) # type: ignore
        #         cursor.execute("select sum(runs) from si")
        #         t2r=int(cursor.fetchall()[0][0]) # type: ignore
        #         cursor.execute("select name from fi where status!='Batting'")
        #         t1w=int(cursor.fetchall()[0][0]) # type: ignore
        #         cursor.execute("select name from si where status!='Batting'")
        #         t2w=int(cursor.fetchall()[0][0]) # type: ignore
        #         Stat1=CTkLabel(Summary.tab("STATS"),text=f"{team1}{'  '*10}{t1r}/{t1w}(0.0)",font=('sans-serf',30)).place(x=0,y=0)
        #         Stat2=CTkLabel(Summary.tab("STATS"),text=f"{team2}{'  '*5}{t2r}/{t2w}(0.0)",font=('sans-serf',30)).place(x=0,y=50)



if __name__=='__main__':
    app=Login()
    app.mainloop()
