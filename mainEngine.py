import hashlib, binascii, os
from datetime import date, datetime
from app.models.client_model import Client

class MainEngine:
    def __init__(self):
        self.createClientTable()
        
    def createClientTable(self):
        with Client() as db:
            db.createClientTable()

    # def login(self, email, password):
    #     find = False
    #     with CustomerDatabaseUtils() as db:
    #         for cust in db.getAllCustomers():
    #             find = False
    #             if cust[4]==email and self.verify_password(cust[5], password):
    #                 find = True
    #                 break
    #     return find

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        passwordhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        passwordhash = binascii.hexlify(passwordhash)
        return (salt + passwordhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                      provided_password.encode('utf-8'), 
                                      salt.encode('ascii'), 
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
