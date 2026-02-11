from database import get_db

def create_batch_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists Batches (
                batch_id text not null,
                recipe_id int not null,
                work_order_id int not null,
                qty double not null,
                target_date date not null,
                constraint PK_Batch primary key (batch_id)
            )""")
    conn.commit()
    cursor.close()
    conn.close()

def delete_batch_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists Batches
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_batch(batch_id, recipe_id, work_order_id, qty, target_date):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into Batches (batch_id, recipe_id, work_order_id, qty, target_date) values (%s, %s, %s, %s, %s)", (batch_id, recipe_id, work_order_id, qty, target_date,))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"batch_id": new_id, "message": "Batch created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_client_batch(client_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT b.batch_id, r.name, b.qty, DATE_FORMAT(b.target_date, '%d/%m/%Y') AS formatted_target_date FROM Batches INNER JOIN recipe AS r WHERE r.recipe_id = b.recipe_id AND r.client_id = %s", (client_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
