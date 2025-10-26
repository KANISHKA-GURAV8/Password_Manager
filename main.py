from tkinter import *
from tkinter import Label
from tkinter import END
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

def password_generator():
     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
     symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
     # print("welcome to my password generator")
     n_letters = random.randint(8,10)
     n_numbers = random.randint(2,4)
     n_symbols = random.randint(2,4)

     password=[random.choice(letters) for _ in range(n_letters)] +  [random.choice(numbers) for _ in range( n_numbers) ]+[random.choice(symbols) for _ in range( n_symbols) ]
     random.shuffle(password)
     password1=''.join(password)

     # print(password1)
     password_entry.insert(0,password1)
     pyperclip.copy(password1)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=web_entry.get()
    email1=email_entry.get()
    password1=password_entry.get()
    new_data={website:{
        "email":email1,
        "password":password1
    }
    }


    if not website or not password1:
       messagebox.showerror(title='Oops',message='Please dont leave any fields empty')
    else:
       #messagebox.askokcancel(title=website,message=f"These are the details entered : \n Email:{email1}" f"\nPassword: {password1} \nIs it ok to save ")
       try:
         with open('data.json','r') as data_file:
           # json.dump(new_data,data_file,indent=4)
           data=json.load(data_file)
           # print(data)
       except FileNotFoundError:
          with open('data.json', 'w') as data_file:
             json.dump(new_data,data_file,indent=4)
       else:
           data.update(new_data)

           with open('data.json', 'w') as data_file:
              json.dump(data, data_file, indent=4)

       finally:
              web_entry.delete(0,END)
              password_entry.delete(0,END)

#---------find password-----------#
def find_password():
    website=web_entry.get()
    try:
      with open('data.json') as data_file:
        data=json.load(data_file)
    except FileNotFoundError:
      messagebox.showinfo(title='Error', message="file not found error")
    else:
        if website in data:
            email1=data[website]['email']
            password1=data[website]['password']
            messagebox.showinfo(title=website,message=f"Email:{email1}\n Password:{password1}")
            password_entry.insert(0, password1)
            email_entry.insert(0,email1)
            pyperclip.copy(password1)
            # pyperclip.copy(email1)
        else:
            messagebox.showinfo(title='Error',message=f"no details for {website} exists ")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50,bg='white')

canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file='logo.png')
# image=Label(bg='white')
# image.grid(row=0,column=1)

canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

web=Label(text='Website : ',fg='black',bg='white')
web.grid(row=1,column=0)

web_entry=Entry(width=21)
web_entry.grid(row=1,column=1)
web_entry.focus()

email=Label(text='Email/Username :',bg='white' )
email.grid(row=2,column=0)

email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,'abc@gmail.com')


password=Label(text='Password :',bg='white',fg='black')
password.grid(row=3,column=0)

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


generate_b=Button(text='Generate Password',highlightthickness=0,bg='white',command=password_generator)
generate_b.grid(row=3,column=2,padx=2)

add_b=Button(text='Add',highlightthickness=0,width=34,bg='white',command=save)
add_b.grid(row=4,column=1,columnspan=2,padx=2)
# label=Label(text='TIMER',font=(FONT_NAME,35),fg=GREEN,bg=YELLOW)
# label.grid(column=1,row=0,pady=15)

search=Button(text='   Search   ',highlightthickness=0,bg='white',width=13,command=find_password)
search.grid(row=1,column=2,pady=2)

window.mainloop()