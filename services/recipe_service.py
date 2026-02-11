from database import get_db

def create_recipe_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists Recipes (
                    recipe_id int not null auto_increment,
                    client_id int not null,
                    name text not null,
                    can_type text not null,
                    volume double not null,
                    sterilisation text not null,
                    parameters json,
                    materials json,
                    constraint PK_Recipe primary key (recipe_id)
                )""")
    conn.commit()
    cursor.close()
    conn.close()

def delete_recipe_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        drop table if exists Recipes
            """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_recipe(client_id, name, can_type, volume, sterilisation,):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("insert into Recipes (client_id, name, can_type, volume, sterilisation, parameters, materials) values (%s,%s,%s,%s,%s, %s, %s)", (client_id, name, can_type, volume, sterilisation, '{"parameters": {}}', '{"materials": []}', ))
        conn.commit()
        new_id = cursor.lastrowid
        return  {"recipe_id": new_id, "message": "Recipe created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def get_client_recipes(client_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT recipe_id, name, can_type, volume, sterilisation FROM Recipes WHERE client_id = %s", (client_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_client_recipes_details(client_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT recipe_id, name FROM Recipes WHERE client_id = %s", (client_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_recipe_materials(recipe_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT materials FROM Recipes WHERE recipe_id = %s", (recipe_id,))
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    return results

def get_recipe_parameters(recipe_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT parameters FROM Recipes WHERE recipe_id = %s", (recipe_id,))
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    return results

def update_materials(recipe_id, materials):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Recipes SET materials = %s WHERE recipe_id = %s", (materials, recipe_id,))
        conn.commit()
        return  {"recipe_id": recipe_id, "message": "Materials updated successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

def update_parameters(recipe_id, parameters):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Recipes SET parameters = %s WHERE recipe_id = %s", (parameters, recipe_id,))
        conn.commit()
        return  {"recipe_id": recipe_id, "message": "Parameters updated successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()
