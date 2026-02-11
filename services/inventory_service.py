from database import get_db

def create_inventory_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists Inventories (
                inventory_id int not null auto_increment,
                code text not null,
                client_id int not null,
                name text not null,
                qty double not null,
                uom text not null,
                entry_date date not null,
                exp_date date not null,
                constraint PK_Inventory primary key (inventory_id)
            )""")
    conn.commit()
    cursor.close()
    conn.close()

def delete_inventory_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists Inventories
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_inventory(code, client_id, name, qty, uom, entry_date, exp_date):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into Inventories (code, client_id, name, qty, uom, entry_date, exp_date) values (%s, %s, %s, %s, %s, %s, %s)", (code, client_id, name, qty, uom, entry_date, exp_date,))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"inventory_id": new_id, "message": "Inventory created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def update_inventory_qty(inventory_id, qty):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Inventories SET qty = %s WHERE inventory_id = %s", (qty, inventory_id,))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"inventory_id": new_id, "message": "Inventory updated successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_inventory_qty(inventory_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT qty FROM Inventories WHERE inventory_id = %s", (inventory_id,))
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    return results

def get_client_inventory(client_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT inventory_id, code, name, qty, uom, DATE_FORMAT(entry_date, '%d/%m/%Y') AS entry_date, DATE_FORMAT(exp_date, '%d/%m/%Y') AS exp_date FROM Inventories WHERE client_id = %s", (client_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
