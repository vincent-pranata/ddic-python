from database import get_db

def delete_client_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists Clients
            """)
    conn.commit()
    cursor.close()
    conn.close()

def create_client_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists Clients (
                client_id int not null auto_increment,
                name text not null,
                    constraint PK_Client primary key (client_id)
                )""")
    conn.commit()
    cursor.close()
    conn.close()

def insert_client(name):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into Clients (name) values (%s)", (name, ))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"client_id": new_id, "name": name, "message": "Client created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_all_clients():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select * from Clients order by name asc")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
