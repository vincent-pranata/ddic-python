from database import get_db

def create_preorder_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists PreOrders (
                preorder_id int not null auto_increment,
                code text not null,
                client_id int not null,
                recipe_id int not null,
                qty int not null,
                create_date date not null,
                status text not null,
                constraint PK_PreOrders primary key (preorder_id)
            )""")
    conn.commit()
    cursor.close()
    conn.close()

def delete_preorder_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists PreOrders
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_preorder(code, client_id, recipe_id, qty, create_date, status):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into PreOrders (code, client_id, recipe_id, qty, create_date, status) values (%s, %s, %s, %s, %s, %s)", (code, client_id, recipe_id, qty, create_date, status,))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"preorder_id": new_id, "message": "Preorder created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def update_preorder_status(preorder_id):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE PreOrders SET status = %s WHERE preorder_id = %s", ('COMPLETE', preorder_id,))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"preorder_id": new_id, "message": "PreOrders successfully completed"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_client_preorders(client_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT p.preorder_id, p.code, r.name, p.qty, DATE_FORMAT(p.create_date, '%d/%m/%Y') AS create_date, p.status FROM PreOrders AS p INNER JOIN Recipes AS r ON p.recipe_id = r.recipe_id WHERE p.client_id = %s", (client_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
