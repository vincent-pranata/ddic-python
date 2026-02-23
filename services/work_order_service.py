from database import get_db

def create_workorder_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists WorkOrders (
                workorder_id int not null auto_increment,
                preorder_id int not null,
                client_id int not null,
                code text not null,
                cartoning int not null,
                start_date date not null,
                end_date date,
                ship_date date,
                operator text not null,
                constraint PK_WorkOrders primary key (workorder_id)
            )""")
    conn.commit()
    cursor.close()
    conn.close()

def delete_workorder_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists WorkOrders
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_workorder(preorder_id, client_id, code, cartoning, start_date, operator):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into WorkOrders (preorder_id, client_id, code, cartoning, start_date, operator) values (%s, %s, %s, %s, %s, %s)", (preorder_id, client_id, code, cartoning, start_date, operator))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"workorder_id": new_id, "message": "Workorder created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()


def get_client_workorders(client_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT w.workorder_id, w.code AS workorder_code, p.code AS preorder_code, r.name, w.cartoning, DATE_FORMAT(w.start_date, '%d/%m/%Y') AS start_date, DATE_FORMAT(w.end_date, '%d/%m/%Y') AS end_date, DATE_FORMAT(w.ship_date, '%d/%m/%Y') AS ship_date, w.operator FROM WorkOrders AS w INNER JOIN PreOrders AS p ON w.preorder_id = p.preorder_id INNER JOIN Recipes AS r ON p.recipe_id = r.recipe_id WHERE w.client_id = %s", (client_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
