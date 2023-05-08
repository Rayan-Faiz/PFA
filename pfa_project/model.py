import mysql.connector as mc

class Connection:
    def __init__(self):
        self.host="localhost"
        self.database="database"
        self.user="root"
        self.password="root"
        self.port=8889
        self.conn=None
        self.cursor=None
        self.table="products"

    #--to connect app.py with database--
    def connect(self):
        try:
            self.conn=mc.connect(host=self.host, database=self.database, user=self.user, password=self.password, port=self.port)
            print("connect to database")
        except mc.Error as err:
            print(err)
        self.cursor=self.conn.cursor()

    #--to disconnect--
    def disconnect(self):
        if self.cursor:
            self.cursor.close
        if self.conn:
            self.conn.close

    def getAll(self):
        req=f"select * from {self.table}"
        self.cursor.execute(req)
        products=self.cursor.fetchall()
        return products
    
    def search(self,id):
        req=f"select * from {self.table} where id=%s"
        values=(id,)
        self.cursor.execute(req,values)
        products=self.cursor.fetchall()
        return products

    def add(self,id, name, quantity, price, eDate, rDate):
        req=f"insert into {self.table} (id, name, quantity, price, entry_Date, release_Date)values(%s, %s, %s, %s, %s, %s)"
        values=(id, name, quantity, price, eDate, rDate)
        self.cursor.execute(req,values)
        self.conn.commit()

    def update(self, name, quantity, price, eDate, rDate, id):
        req=f"update {self.table} set name=%s, quantity=%s, price=%s, entry_Date=%s, release_Date=%s where id=%s"
        values=(name, quantity, price, eDate, rDate, id)
        self.cursor.execute(req,values)
        self.conn.commit()

    def delete(self,id):
        req=f"delete from {self.table} where id=%s"
        values=(id,)
        self.cursor.execute(req,values)
        self.conn.commit()
