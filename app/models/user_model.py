class User:
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
        cursor = self.connection.cursor()
        cursor.execute("""
            drop table if exists Users
                """)
        self.connection.commit()

    def createUserTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Users (
                    user_id int not null auto_increment,
                    username text not null,
                    password text not null,
                    role text not null,
                    constraint PK_User primary key (user_id)
                )""")
        self.connection.commit()

    def insertUser(self, username, password, role):
        cursor = self.connection.cursor()
        cursor.execute("insert into Users (username, password, role) values (%s)", (username, password, role, ))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getAllUsers(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Users")
        return cursor.fetchall()

    def getUserByName(self, username):
        cursor = self.connection.cursor()
        cursor.execute("select * from Users WHERE username like %s", (username,))
        return cursor.fetchall()

    def deleteUser(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("delete from Users where user_id = %s", (user_id,))
        self.connection.commit()
