from tkinter import *
from tkinter import messagebox
import mysql.connector


def connect_db():
    if login.get()=='' or passw.get()=='':
        messagebox.showerror('Erreur','Veuillez remplire tous les inputs')
    elif passw.get()!=passwch.get():
        messagebox.showerror(0,'Passwords dont match')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='database',port='3306')
            cursor=conn.cursor()
        except:
            messagebox.showerror('erreur', 'connexion non etabli')
    us=login.get()
    iss=passw.get()
    values = (us,iss)
    query="INSERT INTO info (email,password) VALUES (%s,%s)"
    try:
        cursor.execute(query, values)
        conn.commit()
    except:
        messagebox.showerror(0,'erreur')
    root.destroy()
    import loginin



def login_form():
    root.destroy()
    import loginin

root=Tk()
root.title('register')
root.geometry('650x750+300+200')
root.configure(bg='#fff')
root.resizable(False,False)


frame2=Frame(root,width=350,height=50,bg='white')
frame=Frame(root,width=350,height=500,bg='white')
frame.place(x=150,y=200)
frame2.place(x=150,y=70)
head=Label(frame2,text='Inscription',bg='white',fg='black', font=('Comic Sans',23,'bold'))
head.place(x=70,y=0)
#############################
email=Label(frame,text='E-mail',bg='white',fg='black', font=('Comic Sans',10,'bold'))
email.place(x=50,y=0)
###########################
def on_enter(e):
    login.delete(0,'end')

def on_leave(e):
    name=login.get()
    if name=='':
        login.insert(0,'votremail@****.***')


login=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Comic Sans',11))
login.insert(0,'votremail@****.***')
login.place(x=50,y=50)
login.bind('<FocusIn>', on_enter)
login.bind('<FocusOut>', on_leave)
#########################
mdp=Label(frame,text='Mot de Passe',bg='white',fg='black', font=('Comic Sans',10,'bold'))
mdp.place(x=50,y=100)
#########################


def on_enter(e):
    passw.delete(0,'end')

def on_leave(e):
    name=passw.get()
    if name=='':
        passw.insert(0,'***********')


passw=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Comic Sans',10))
passw.insert(0,'***********')
passw.place(x=50,y=150)
passw.bind('<FocusIn>', on_enter)
passw.bind('<FocusOut>', on_leave)
#########################
mdpc=Label(frame,text='Confirmer Mot de Passe',bg='white',fg='black', font=('Comic Sans',10,'bold'))
mdpc.place(x=50,y=200)
#########################


def on_enter(e):
    passwch.delete(0,'end')

def on_leave(e):
    name1=passwch.get()
    if name1=='':
        passwch.insert(0,'***********')


passwch=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Comic Sans',10))
passwch.insert(0,'***********')
passwch.place(x=50,y=250)
passwch.bind('<FocusIn>', on_enter)
passwch.bind('<FocusOut>', on_leave)
##########################
Button(frame,width=39,pady=7,text="S'inscrire",bg='gray',fg='black',border=5,command=connect_db).place(x=27,y=290)
Button(frame,width=39,pady=7,text='Page de connexion',bg='gray',fg='black',border=5,command=login_form).place(x=27,y=340)

root.mainloop()