class Client:
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
            drop table if exists Clients
                """)
        self.connection.commit()

    def createClientTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Clients (
                    client_id int not null auto_increment,
                    name text not null,
                    constraint PK_Client primary key (client_id)
                )""")
        self.connection.commit()

    def insertClient(self, name):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("insert into Clients (name) values (%s)", (name, ))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getAllClients(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("select * from Clients order by name asc")
        return cursor.fetchall()

    def getClientByName(self, name):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("select * from Clients WHERE name like %s", (name,))
        return cursor.fetchall()

    def deleteClient(self, client_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("delete from Clients where client_id = %s", (client_id,))
        self.connection.commit()
