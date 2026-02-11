from database import get_db

def create_batch_record_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists Batch_Records (
                id int not null auto_increment,
                batch_id int not null,
                qty double not null,
                division text not null,
                log_date date not null,
                notes text,
                operator text not null,
                constraint PK_Batch_Records primary key (id)
            )""")
    conn.commit()
    cursor.close()
    conn.close()

def delete_batch_record_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists Batch_Records
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_batch_record(batch_id, qty, division, log_date, notes, operator):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into Batch_Records (batch_id, qty, division, log_date, notes, operator) values (%s, %s, %s, %s, %s, %s)", (batch_id, qty, division, log_date, notes, operator,))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"id": new_id, "message": "Batch record created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_batch_record(batch_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT qty, division, DATE_FORMAT(log_date, '%d/%m/%Y') AS formatted_log_date, notes, operator FROM Batch_Records WHERE batch_id = %s", (batch_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
