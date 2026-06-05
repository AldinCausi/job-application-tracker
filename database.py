import sqlite3
import utils

conn  = sqlite3.connect("bewerbungen.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS bewerbungen (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   company TEXT,
                   role TEXT,
                   status TEXT)
                """)

def add_application(company, role, status):
    cursor.execute(
        "INSERT INTO bewerbungen(company, role, status) VALUES (?,?,?)", (company, role, status)
        )
    conn.commit()

def show_applications():
    utils.clear_screen()
    cursor.execute("SELECT * FROM bewerbungen")
    result = cursor.fetchall()

    if result == []:
        print("\nKeine Bewerbungen\n")
    
    for row in result:
        print("-" * 20)
        print(f"ID: {row[0]}")
        print(f"Company: {row[1]}")
        print(f"Role: {row[2]}")
        print(f"Status: {row[3]}")

def delete_byID(id):
    cursor.execute("DELETE FROM bewerbungen WHERE id = ?", (id,))
    conn.commit()

def delete_by_company(company):
    cursor.execute("DELETE FROM bewerbungen WHERE company = ?", (company, ))
    conn.commit()

def delete_by_role(role):
    cursor.execute("DELETE FROM bewerbungen WHERE role = ?", (role, ))
    conn.commit()

def update_status(status, id):
    cursor.execute("UPDATE bewerbungen SET status = ? WHERE id = ?", (status, id))
    conn.commit()