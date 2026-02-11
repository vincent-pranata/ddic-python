from database import get_db

def create_inventory_record_table():
    conn = get_db()
    cursor = conn.cursor()
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
    conn.commit()
    cursor.close()
    conn.close()

def delete_inventory_record_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists Inventory_Records
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_inventory_record(inventory_id, qty, log_date, notes, operator):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into Inventory_Records (inventory_id, qty, log_date, notes, operator) values (%s, %s, %s, %s, %s)", (inventory_id, qty, log_date, notes, operator,))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"id": new_id, "message": "Inventory record created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_inventory_record(inventory_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT qty, DATE_FORMAT(log_date, '%d/%m/%Y') AS log_date, notes, operator FROM Inventory_Records WHERE inventory_id = %s", (inventory_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
