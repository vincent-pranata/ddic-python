import hashlib, binascii, os
from app.models.client_model import Client
from app.models.user_model import User
from app.models.inventory_model import Inventory
from app.models.inventory_record_model import InventoryRecord
from app.models.recipe_model import Recipe

class MainEngine:
    connection = None
    def __init__(self, connection):
        self.connection = connection
        self.createClientTable()
        self.createUserTable()
        self.createInventoryTable()
        self.createInventoryRecordTable()
        self.createRecipeTable()
        
    def createClientTable(self):
        with Client(self.connection) as db:
            db.createClientTable()

    def createUserTable(self):
        with User(self.connection) as db:
            db.createUserTable()

    def createInventoryTable(self):
        with Inventory(self.connection) as db:
            db.createInventoryTable()

    def createInventoryRecordTable(self):
        with InventoryRecord(self.connection) as db:
            db.createInventoryRecordTable()
            
    def createRecipeTable(self):
        with Recipe(self.connection) as db:
            db.createRecipeTable()
    
    # def login(self, email, password):
    #     find = False
    #     with CustomerDatabaseUtils() as db:
    #         for cust in db.getAllCustomers():
    #             find = False
    #             if cust[4]==email and self.verify_password(cust[5], password):
    #                 find = True
    #                 break
    #     return find

    def getAllClients(self):
        with Client(self.connection) as db:
            return db.getAllClients()  
           
    def insertClient(self, client_name):
        with Client(self.connection) as db:
            db.insertClient(client_name)  
           
    def getAllUsers(self):
        with User(self.connection) as db:
            return db.getAllUsers()  

    def insertUser(self, username, password, role):
        with User(self.connection) as db:
            db.insertUser(username, password, role)

    def getClientInventory(self, client_id):
        with Inventory(self.connection) as db:
            return db.getClientInventory(client_id)

    def insertInventory(self, code, client_id, name, qty, uom, entry_date, exp_date, operator):
        success = False
        inventory_id = None
        with Inventory(self.connection) as db:
            success = db.insertInventory(code, client_id, name, qty, uom, entry_date, exp_date)
            inventory_id = db.getLastInsertId()
        
        if success:
            success = self.insertInventoryRecord(inventory_id, qty, entry_date, "Barang Masuk", operator)
        
    def getInventoryRecord(self, inventory_id):
        with InventoryRecord(self.connection) as db:
            return db.getInventoryRecord(inventory_id)
        
    def insertInventoryRecord(self, inventory_id, qty, log_date, notes, operator):
        with InventoryRecord(self.connection) as db:
            db.insertInventoryRecord(inventory_id, qty, log_date, notes, operator)
        
    def getClientRecipe(self, client_id):
        with Recipe(self.connection) as db:
            return db.getClientRecipe(client_id)                 
        
    def insertRecipe(self, client_id, name, can, volume, sterilisation):
        with Recipe(self.connection) as db:
            db.insertRecipe(client_id, name, can, volume, sterilisation)

    # def hash_password(self, password):
    #     """Hash a password for storing."""
    #     salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    #     passwordhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    #     passwordhash = binascii.hexlify(passwordhash)
    #     return (salt + passwordhash).decode('ascii')

    # def verify_password(self, stored_password, provided_password):
    #     """Verify a stored password against one provided by user"""
    #     salt = stored_password[:64]
    #     stored_password = stored_password[64:]
    #     pwdhash = hashlib.pbkdf2_hmac('sha512', 
    #                                   provided_password.encode('utf-8'), 
    #                                   salt.encode('ascii'), 
    #                                   100000)
    #     pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    #     return pwdhash == stored_password
