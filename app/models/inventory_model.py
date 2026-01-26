class Inventory:
    connection = None
    def __init__(self, connection): 
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def deleteTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            drop table if exists Inventories
                """)
        self.connection.commit()

    def createInventoryTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Inventories (
                    inventory_id int not null auto_increment,
                    code text not null,
                    client_id int not null,
                    name text not null,
                    qty float not null,
                    uom text not null,
                    entry_date date not null,
                    exp_date date not null,
                    constraint PK_Inventory primary key (inventory_id)
                )""")
        self.connection.commit()

    def insertInventory(self, code, client_id, name, qty, uom, entry_date, exp_date):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("insert into Inventories (code, client_id, name, qty, uom, entry_date, exp_date) values (%s, %s, %s, %s, %s, %s, %s)", (code, client_id, name, qty, uom, entry_date, exp_date))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getClientInventory(self, client_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT inventory_id, code, name, qty, uom, DATE_FORMAT(entry_date, '%d/%m/%Y') AS formatted_entry_date, DATE_FORMAT(exp_date, '%d/%m/%Y') AS formatted_exp_date FROM Inventories WHERE client_id = %s", (client_id,))
        return cursor.fetchall()

    def getInventoryByName(self, username):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("select * from Inventories WHERE username like %s", (username,))
        return cursor.fetchall()

    def deleteInventory(self, inventory_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("delete from Inventories where inventory_id = %s", (inventory_id,))
        self.connection.commit()

    def getLastInsertId(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT LAST_INSERT_ID()")
        result = cursor.fetchone()
        return result[0] if result else None