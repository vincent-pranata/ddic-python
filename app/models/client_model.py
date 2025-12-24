import mysql.connector
from dotenv import load_dotenv
import os
class Client:
   
    connection = None
    # Default to 'local' if APP_ENV is not set in the host environment
    environment = os.getenv("APP_ENV", "local")
    
    # Construct the filename, e.g., ".env.development"
    env_file_path = f".env.{environment}"

    # Load variables from the specific environment file
    load_dotenv(dotenv_path=env_file_path)

    def __init__(self, connection = None):
        db_user = os.getenv('SQL_USERNAME')
        db_password = os.getenv('SQL_PASSWORD')
        db_name = os.getenv('DBNAME')
        db_connection_name = os.getenv('SQL_URL')
        connection = mysql.connector.connect(user=db_user, password=db_password,
                            host=db_connection_name, db=db_name)        
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
            drop table if exists Clients
                """)
        self.connection.commit()

    def createClientTable(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            create table if not exists Clients (
                    client_id int not null auto_increment,
                    name text not null,
                    constraint PK_Client primary key (client_id)
                )""")
        self.connection.commit()

    def insertClient(self, name):
        cursor = self.connection.cursor()
        cursor.execute("insert into Clients (name) values (%s)", (name, ))
            
        self.connection.commit()

        return cursor.rowcount == 1

    def getAllClients(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Clients")
        return cursor.fetchall()

    def getClientByName(self, name):
        cursor = self.connection.cursor()
        cursor.execute("select * from Clients WHERE name like %s", (name,))
        return cursor.fetchall()

    def deleteClient(self, client_id):
        cursor = self.connection.cursor()
        cursor.execute("delete from Clients where client_id = %s", (client_id,))
        self.connection.commit()
