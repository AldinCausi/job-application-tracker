import sqlite3
import utils

class Database:
    def __init__(self, db_name="bewerbungen.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS bewerbungen (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT,
                    role TEXT,
                    status TEXT)
                    """)

    def add_application(self, company, role, status):
        self.cursor.execute(
            "INSERT INTO bewerbungen(company, role, status) VALUES (?,?,?)", (company, role, status)
            )
        self.conn.commit()

    def show_applications(self):
        utils.clear_screen()
        self.cursor.execute("SELECT * FROM bewerbungen")
        result = self.cursor.fetchall()

        if result == []:
            print("\nKeine Bewerbungen\n")
        
        for row in result:
            print("-" * 20)
            print(f"ID: {row[0]}")
            print(f"Company: {row[1]}")
            print(f"Role: {row[2]}")
            print(f"Status: {row[3]}")

    def delete_byID(self, id):
        self.cursor.execute("DELETE FROM bewerbungen WHERE id = ?", (id,))
        self.conn.commit()

    def delete_by_company(self, company):
        self.cursor.execute("DELETE FROM bewerbungen WHERE company = ?", (company, ))
        self.conn.commit()

    def delete_by_role(self, role):
        self.cursor.execute("DELETE FROM bewerbungen WHERE role = ?", (role, ))
        self.conn.commit()

    def update_status(self, status, id):
        self.cursor.execute("UPDATE bewerbungen SET status = ? WHERE id = ?", (status, id))
        self.conn.commit()

    def show_with_status(self, status):
        utils.clear_screen()
        self.cursor.execute("SELECT * FROM bewerbungen WHERE status = ?", (status, ))
        result = self.cursor.fetchall()

        if result == []:
            print(f"Keine Bewerbungen mit status={status}\n")
        
        for row in result:
            print("-" * 20)
            print(f"ID: {row[0]}")
            print(f"Company: {row[1]}")
            print(f"Role: {row[2]}")
            print(f"Status: {row[3]}")
