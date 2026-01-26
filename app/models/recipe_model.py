class Recipe:
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
            drop table if exists Recipes
                """)
        self.connection.commit()

    def createRecipeTable(self):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Recipes (
                    recipe_id int not null auto_increment,
                    client_id int not null,
                    name text not null,
                    can_type text not null,
                    volume float not null,
                    sterilisation text not null,
                    parameters json,
                    materials json,
                    constraint PK_Recipe primary key (recipe_id)
                )""")
        self.connection.commit()

    def insertRecipe(self, client_id, name, can_type, volume, sterilisation):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("insert into Recipes (client_id, name, can_type, volume, sterilisation) values (%s, %s, %s, %s, %s)", (client_id, name, can_type, volume, sterilisation,))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getClientRecipe(self, client_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT recipe_id, name, can_type, volume, sterilisation FROM Recipes WHERE client_id = %s", (client_id,))
        return cursor.fetchall()

    def getRecipeByName(self, username):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("select * from Recipes WHERE username like %s", (username,))
        return cursor.fetchall()

    def deleteRecipe(self, recipe_id):
        self.connection.reconnect()
        cursor = self.connection.cursor()
        cursor.execute("delete from Recipes where recipe_id = %s", (recipe_id,))
        self.connection.commit()
