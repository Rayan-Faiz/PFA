import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as popup
from model import Connection as Cs



ID=None
conn=Cs()
conn.connect()

#---------- controller ----------


#--this part has the methods of the app--
def searchProduct():
    global ID
    ID=search_entry_i.get()
    if ID!=None:
        products=conn.search(id=ID)
        search_entry_i.delete(0,'end')
        my_tree.delete(*my_tree.get_children())
        for product in products:
            my_tree.insert('', tk.END, text=product[0],values=(product[1],product[2],product[3],product[4],product[5]))


def addProduct():
    global ID
    ID=entry_id.get()
    n=entry_n.get()
    q=entry_q.get()
    p=entry_p.get()
    ed=entry_ed.get()
    rd=entry_rd.get()
    if ID!=None:
        print(f"add Product {ID}")
        conn.add(id=ID,name=n, quantity=q, price=p, eDate=ed, rDate=rd)
        show()
        popup.showinfo('Message','product added successfully')
        
def updateProduct():
    global ID
    ID=entry_id.get()
    n=entry_n.get()
    q=entry_q.get()
    p=entry_p.get()
    ed=entry_ed.get()
    rd=entry_rd.get()
    if ID != None:
        conn.update(id=ID, name=n, quantity=q, price=p, eDate=ed, rDate=rd)
        show()
        print(f"update Product {ID}")
        popup.showinfo('Message','product updated successfully')

def deleteProduct():
    global ID
    ID=delete_entry_i.get()
    conn.delete(ID)
    show()
    popup.showinfo('Message','product deleted successfully')

def selectItem(event):
    global ID
    seletedItem=my_tree.selection()[0]
    ID=my_tree.item(seletedItem)["text"]
    values=my_tree.item(seletedItem)["values"]

    entry_id.delete(0,'end')
    entry_id.insert(0,ID)
    entry_n.delete(0,'end')
    entry_n.insert(0,values[0])
    entry_q.delete(0,'end')
    entry_q.insert(0,values[1])
    entry_p.delete(0,'end')
    entry_p.insert(0,values[2])
    entry_ed.delete(0,'end')
    entry_ed.insert(0,values[3])
    entry_rd.delete(0,'end')
    entry_rd.insert(0,values[4])
    print(f"select {ID}")

def show():
    global ID
    entry_id.delete(0,'end')
    entry_n.delete(0,'end')
    entry_q.delete(0,'end')
    entry_p.delete(0,'end')
    entry_ed.delete(0,'end')
    entry_rd.delete(0,'end')
    ID=None
    my_tree.delete(*my_tree.get_children())
    products=conn.getAll()
    for product in products:
        my_tree.insert('', tk.END, text=product[0],values=(product[1],product[2],product[3],product[4],product[5]))


#---------- view ----------


frame=tk.Tk()
frame.geometry("900x850")
frame.title("Stock manager")


#--makes the grid--
my_tree=ttk.Treeview(frame,columns=("name","quantity","price","entry date","release date"))
my_tree.heading("#0",text="ID")
my_tree.heading("name",text="name")
my_tree.heading("quantity",text="quantity")
my_tree.heading("price",text="price")
my_tree.heading("entry date",text="entry date")
my_tree.heading("release date",text="release date")
my_tree.column("#0",width=50)
my_tree.column("name",width=200)
my_tree.column("quantity",width=70)
my_tree.column("price",width=70)
my_tree.column("entry date",width=120)
my_tree.column("release date",width=120)
my_tree.pack(side=tk.LEFT,fill=tk.BOTH,)

#--elements that interact with users (buttons, entries...)--
search_label=tk.Label(frame,text="SEARCH by ID",font=('Arial', 17, 'bold'))
search_label.pack(side=tk.TOP,padx=10,pady=10)
search_entry_i=tk.Entry(frame)
search_entry_i.pack(side=tk.TOP)
search_button=tk.Button(frame,text="Search",command=searchProduct)
search_button.pack(side=tk.TOP, padx=5, pady=5)

reset_button=tk.Button(frame,text="Reset",command=show)
reset_button.pack(side=tk.TOP, padx=5, pady=5)



label=tk.Label(frame,text="ADD or UPDATE a product",font=('Arial', 17, 'bold'))
label.pack(side=tk.TOP,padx=10,pady=10)
label_i=tk.Label(frame,text="ID")
label_i.pack()
entry_id=tk.Entry(frame)
entry_id.pack(side=tk.TOP)
label_n=tk.Label(frame,text="name")
label_n.pack()
entry_n=tk.Entry(frame)
entry_n.pack(side=tk.TOP)
label_q=tk.Label(frame,text="quantity")
label_q.pack()
entry_q=tk.Entry(frame)
entry_q.pack(side=tk.TOP)
label_p=tk.Label(frame,text="price")
label_p.pack()
entry_p=tk.Entry(frame)
entry_p.pack(side=tk.TOP)
entry_ed=tk.Label(frame,text="entry date")
entry_ed.pack()
entry_ed=tk.Entry(frame)
entry_ed.pack(side=tk.TOP)
entry_rd=tk.Label(frame,text="release date")
entry_rd.pack()
entry_rd=tk.Entry(frame)
entry_rd.pack(side=tk.TOP)
add_button=tk.Button(frame,text="Add",command=addProduct)
add_button.pack(side=tk.TOP,padx=5,pady=5)
update_button=tk.Button(frame,text="Update",command=updateProduct)
update_button.pack(side=tk.TOP, padx=5, pady=5)

delete_label=tk.Label(frame,text="DELETE by ID",font=('Arial', 17, 'bold'))
delete_label.pack(side=tk.TOP,padx=10,pady=10)
delete_entry_i=tk.Entry(frame)
delete_entry_i.pack(side=tk.TOP)
delete_button=tk.Button(frame,text="Delete",command=deleteProduct)
delete_button.pack(side=tk.TOP, padx=5, pady=5)

my_tree.bind('<ButtonRelease-1>',selectItem)
show()

frame.mainloop()
