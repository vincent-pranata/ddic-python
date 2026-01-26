class InventoryRecord:
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
            drop table if exists Inventory_Records
                """)
        self.connection.commit()

    def createInventoryRecordTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Inventory_Records (
                    id int not null auto_increment,
                    inventory_id int not null,
                    qty double not null,
                    log_date date not null,
                    notes text,
                    operator text not null,
                    constraint PK_Inventory_Records primary key (id)
                )""")
        self.connection.commit()

    def insertInventoryRecord(self, inventory_id, qty, log_date, notes, operator):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("insert into Inventory_Records (inventory_id, qty, log_date, notes, operator) values (%s, %s, %s, %s, %s)", (inventory_id, qty, log_date, notes, operator))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getInventoryRecord(self, inventory_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT qty, DATE_FORMAT(log_date, '%d/%m/%Y') AS formatted_log_date, notes, operator FROM Inventory_Records WHERE inventory_id = %s", (inventory_id,))
        return cursor.fetchall()

    def getInventoryByName(self, username):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("select * from Inventory_Records WHERE username like %s", (username,))
        return cursor.fetchall()

    def deleteInventory(self, inventory_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("delete from Inventory_Records where inventory_id = %s", (inventory_id,))
        self.connection.commit()
