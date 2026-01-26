class PreOrder:
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
            drop table if exists PreOrders
                """)
        self.connection.commit()

    def createPreOrderTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists PreOrders (
                    batch_id text not null,
                    recipe_id int not null,
                    work_order_id int not null,
                    qty float not null,
                    target_date date not null,
                    constraint PK_PreOrder primary key (batch_id)
                )""")
        self.connection.commit()

    def insertPreOrder(self, batch_id, recipe_id, work_order_id, qty, target_date):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("insert into PreOrders (batch_id, recipe_id, work_order_id, qty, target_date) values (%s, %s, %s, %s, %s)", (batch_id, recipe_id, work_order_id, qty, target_date))

        self.connection.commit()

        return cursor.rowcount == 1

    def getClientPreOrder(self, client_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT b.batch_id, r.name, b.qty, DATE_FORMAT(b.target_date, '%d/%m/%Y') AS formatted_target_date FROM PreOrders INNER JOIN recipe AS r WHERE r.recipe_id = b.recipe_id AND r.client_id = %s", (client_id,))
        return cursor.fetchall()
