#Importing required necessities
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as scrolledtext
import random
import sqlite3
from sqlite3 import Error

#Declaring functions for Everything...
def homepage():
	global e1
	remove()
	lab1 = tk.Label(frame_1,text='PASSWORD MANAGER',fg='White' if brightness < 120 else 'Black',bg=bg_colour,font=font_)
	lab1.place(width=150,height=30,relx='0.35',rely='0.15')
	lab2 = tk.Label(frame_1,text='Enter MASTER key to continue...|:)|',fg='White' if brightness < 120 else 'Black',bg=bg_colour)
	lab2.place(x=20,y=150,width=450,height=30)
	lab3 = tk.Button(frame_1,text='Password Correct...')
	enter_ = tk.Label(frame_1,text="ENTER PASSWORD ===>>>")
	enter_.place(x=70,y=230,width=150,height=30)
	e1 = tk.Entry(frame_1,show="*",relief='groove') 
	e1.bind("<Return>", (lambda event: login()))
	e1.place(x=250,y=230,width=130,height=30)
	but_1 = tk.Button(frame_1,text='login',fg='White' if brightness < 120 else 'Black',bg=bg_colour,command=login)
	but_1.place(x=185,y=280,width=70,height=30)

def homepage_logged_in():
	random_color()
	homepage()
	enter_or_display_button()

#Used to change colour of ui each time it is opened
def random_color():
	global brightness,bg_colour
	ct = [random.randrange(256) for x in range(3)]
	brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
	ct_hex = "%02x%02x%02x" % tuple(ct)
	bg_colour = '#' + "".join(ct_hex)

# Remove all widgets in Frame
def remove():
		for widget in frame_1.winfo_children():
			widget.destroy()

def enter_or_display_button():
	enter_button = tk.Button(frame_1,text='Enter Credentials ',fg='White' if brightness < 120 else 'Black',bg=bg_colour,command=enter_credentials)
	enter_button.place(x=70,y=370,width=100,height=30)
	Display_buton =tk.Button(frame_1,text='Display Credentials ',fg='White' if brightness < 120 else 'Black',bg=bg_colour,command=display_from_db)
	Display_buton.place(x=230,y=370,width=120,height=30)
		
def login():	
	login_password = #ENTER YOUR PASSWORD HERE....
	if e1.get() == login_password :
		enter_or_display_button()
		print('welcome')
	else:
		print('password Incorrect...Try again...')
		lab4 = tk.Label(frame_1,text='INCORRECT PASSWORD. TRY AGAIN...',fg='White' if brightness < 120 else 'Black',bg=bg_colour,font=font_)
		lab4.place(x=117,y=330,width=230,height=15)

def enter_credentials():
	global username, password, website, var_u, var_p, var_w
	remove()
	username_label = tk.Label(frame_1,text='Enter your Username >')
	password_label = tk.Label(frame_1,text='Enter your Password >')
	website_label = tk.Label(frame_1,text='Enter the Website >')
	username = tk.Entry(frame_1)
	password = tk.Entry(frame_1)
	website = tk.Entry(frame_1)
	var_u=username.get()
	var_p=password.get() 
	var_w=website.get() 
	save_info = tk.Button(frame_1,text='Save Info',fg='White' if brightness < 120 else 'Black',bg=bg_colour,command=insert_to_db)
	gohome_label = tk.Button(frame_1,text='Go Home',fg='White' if brightness < 120 else 'Black',bg=bg_colour, command = homepage_logged_in)

	username_label.place(x=70,y=100,width=150,height=30)
	password_label.place(x=70,y=150,width=150,height=30)
	website_label.place(x=70,y=200,width=150,height=30)
	username.place(x=230,y=100,width=130,height=30)
	password.place(x=230,y=150,width=130,height=30)
	website.place(x=230,y=200,width=130,height=30)
	save_info.place(x=180,y=250,width=130,height=30)
	gohome_label.place(x=180,y=290,width=130,height=30)

# Inserting entered data to database...
def insert_to_db():
	# Create a database connection to a disk file based database
	connectionObject    = sqlite3.connect("Path to database....")# insert path to db here....
	# Obtain a cursor object
	cursorObject        = connectionObject.cursor()
	try:
		#creating table
		createTable = "CREATE TABLE IF NOT EXISTS user(website char, username char, password char)"
		cursorObject.execute(createTable)
		cursorObject.execute("INSERT INTO user (website, username, password) VALUES(?, ?, ?)",( website.get(), username.get(), password.get()))
		print(var_w)
		print(var_u)
		print(var_p)
	except sqlite3.Error as error:
		print("Error while creating a sqlite table", error)
	#saving
	finally:
		connectionObject.commit()
		cursorObject.close()
		connectionObject.close()

# Displaying data from database...
def display_from_db():
	remove()
	gohome_but = tk.Button(frame_1,text='Go Home',fg='White' if brightness < 120 else 'Black',bg=bg_colour, command = homepage_logged_in)
	gohome_but.pack()
	txt = scrolledtext.ScrolledText(frame_1, undo=True)
	txt['font'] = ('comicsans', '12')
	txt.pack(expand=True)
	try:
		sqliteConnection = sqlite3.connect(Path to database....)# insert path to db here....
		cursor = sqliteConnection.cursor()
		cursor.execute('''SELECT * FROM user;''')
		table_data = cursor.fetchall()
		txt.insert(tk.INSERT,"Website | Username | Password\n")
		for row in table_data :
			for i in row:
				txt.insert(tk.INSERT,i+' | ')
			txt.insert(tk.END,'\n')
	except sqlite3.Error as error:
		print("Error while creating a sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()

root= tk.Tk()
root.geometry("500x500+400+175")
root.title('PASS/WORD MANAGER v0.1')
frame_1 = tk.Frame(root,padx=10,pady=10,width=600,height=600,takefocus=True,bg = 'white',relief = 'groove',highlightbackground= 'white')
frame_1.place(x=10,y=10,width=480,height=500)
font_ =("Trebuchet MS", "10", "underline")

random_color()
homepage()


root.mainloop()