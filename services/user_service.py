from database import get_db

def create_user_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists Users (
                user_id int not null auto_increment,
                username text not null,
                password text not null,
                role text not null,
                constraint PK_User primary key (user_id)
            )""")
    conn.commit()
    cursor.close()
    conn.close()

def delete_user_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists Users
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_user(username, password, role):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into Users (username, password, role) values (%s,%s,%s)", (username, password, role, ))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"user_id": new_id, "username": username, "role": role, "message": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()
    
def get_all_users():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT user_id, username, role FROM Users")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
