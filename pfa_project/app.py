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
            my_tree.insert('', tk.END, text=product[0],values=(product[1],product[2],product[3]))


def addProduct():
    global ID
    ID=add_entry_id.get()
    n=add_entry_n.get()
    q=add_entry_q.get()
    p=add_entry_p.get()
    if ID!=None:
        print(f"add Product {ID}")
        conn.add(id=ID,name=n, quantity=q, price=p)
        show()
        popup.showinfo('Message','product added successfully')
        
def updateProduct():
    global ID
    ID=update_entry_id.get()
    n=update_entry_n.get()
    q=update_entry_q.get()
    p=update_entry_p.get()
    if ID != None:
        conn.update(id=ID, name=n, quantity=q, price=p)
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

    update_entry_id.delete(0,'end')
    update_entry_id.insert(0,ID)
    update_entry_n.delete(0,'end')
    update_entry_n.insert(0,values[0])
    update_entry_q.delete(0,'end')
    update_entry_q.insert(0,values[1])
    update_entry_p.delete(0,'end')
    update_entry_p.insert(0,values[2])
    print(f"select {ID}")

def show():
    global ID
    search_entry_i.delete(0,'end')
    add_entry_id.delete(0,'end')
    add_entry_n.delete(0,'end')
    add_entry_q.delete(0,'end')
    add_entry_p.delete(0,'end')
    update_entry_id.delete(0,'end')
    update_entry_n.delete(0,'end')
    update_entry_q.delete(0,'end')
    update_entry_p.delete(0,'end')
    delete_entry_i.delete(0,'end')
    ID=None
    my_tree.delete(*my_tree.get_children())
    products=conn.getAll()
    for product in products:
        my_tree.insert('', tk.END, text=product[0],values=(product[1],product[2],product[3]))


#---------- view ----------


frame=tk.Tk()
frame.geometry("670x870")
frame.title("Stock manager")


#--makes the grid--
my_tree=ttk.Treeview(frame,columns=("name","quantity","price"))
my_tree.heading("#0",text="ID")
my_tree.heading("name",text="name")
my_tree.heading("quantity",text="quantity")
my_tree.heading("price",text="price")
my_tree.column("#0",width=50)
my_tree.column("name",width=200)
my_tree.column("quantity",width=70)
my_tree.column("price",width=70)
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

add_label=tk.Label(frame,text="ADD new product",font=('Arial', 17, 'bold'))
add_label.pack(side=tk.TOP,padx=10,pady=10)
add_label_id = tk.Label(frame, text="ID")
add_label_id.pack()
add_entry_id=tk.Entry(frame)
add_entry_id.pack(side=tk.TOP)
add_label_n = tk.Label(frame, text="name")
add_label_n.pack()
add_entry_n=tk.Entry(frame)
add_entry_n.pack(side=tk.TOP)
add_label_q = tk.Label(frame, text="quantity")
add_label_q.pack()
add_entry_q = tk.Entry(frame)
add_entry_q.pack()
add_label_p = tk.Label(frame, text="price")
add_label_p.pack()
add_entry_p = tk.Entry(frame)
add_entry_p.pack()
add_button=tk.Button(frame,text="Add",command=addProduct)
add_button.pack(side=tk.TOP,padx=5,pady=5)

update_label=tk.Label(frame,text="UPDATE a product",font=('Arial', 17, 'bold'))
update_label.pack(side=tk.TOP,padx=10,pady=10)
update_label_i=tk.Label(frame,text="Choose ID to update")
update_label_i.pack()
update_entry_id=tk.Entry(frame)
update_entry_id.pack(side=tk.TOP)
update_label_n=tk.Label(frame,text="Update name")
update_label_n.pack()
update_entry_n=tk.Entry(frame)
update_entry_n.pack(side=tk.TOP)
update_label_q=tk.Label(frame,text="Update quantity")
update_label_q.pack()
update_entry_q=tk.Entry(frame)
update_entry_q.pack(side=tk.TOP)
update_label_p=tk.Label(frame,text="Update price")
update_label_p.pack()
update_entry_p=tk.Entry(frame)
update_entry_p.pack(side=tk.TOP)
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