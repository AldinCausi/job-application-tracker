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

    def get_status(self, id):
        self.cursor.execute("SELECT status FROM bewerbungen WHERE id = ?", (id, ))
        result = self.cursor.fetchone()
        return result[0]

    def update_status(self, status, id):
        self.cursor.execute("UPDATE bewerbungen SET status = ? WHERE id = ?", (status, id))
        self.conn.commit()

    # Muss das ändern damit der Nutzer den Status nicht komplett selber eintippen muss
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

    def get_distinct_status(self):
        self.cursor.execute("SELECT status, COUNT(*) AS anzahl FROM bewerbungen GROUP BY status ORDER BY status")
        result = self.cursor.fetchall()
        return [row[0] for row in result]

    def if_any_status_exists(self):
        existing_status = self.get_distinct_status()
        if not existing_status:
            return False
        else:
            return True

    def get_all_IDs(self):
        self.cursor.execute("SELECT id FROM bewerbungen")
        result = self.cursor.fetchall()
        return [row[0] for row in result]

    def check_if_ID_exists(self, id):
        all_ids = self.get_all_IDs()
        if id not in all_ids:
            return False
        else:
            return True
