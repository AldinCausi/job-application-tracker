import sqlite3
import os

def clear_screen():
    os.system("clear")


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
    clear_screen()
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

if __name__ == "__main__":
    create_table()
    default_status = "pending"


    while True:
        print("\n1. Bewerbung hinzufügen")
        print("2. Bewerbungen anzeigen")
        print("3. Status einer Bewerbung ändern")
        print("4. Bewerbung löschen")
        print("5. Beenden")

        choice = input("> ")

        if choice == "1":
            clear_screen()
            company = input("> Company: ")
            role = input("> Role: ")
            status = default_status
            add_application(company, role, status)

        elif choice == "2":

            show_applications()

        elif choice == "3":

            status_id = int(input("> ID: "))
            new_status = input("> Neuer Status: ")
            update_status(new_status, status_id)

        elif choice == "4":

            while True:
                
                print("\n1. Lösche mit spezifischer ID")
                print("2. Lösche alle einer Company")
                print("3. Lösche alle eines Jobs")
                print("4. Zurück")

                del_choice = input("> ")

                if del_choice == "1":
                    
                    application_id = int(input("> ID: "))
                    delete_byID(application_id)
                    break

                elif del_choice == "2":

                    company_del = input("> Company: ")
                    delete_by_company(company_del)
                    break

                elif del_choice == "3":

                    role_del = input("> Role: ")
                    delete_by_role(role_del)
                    break

                elif del_choice == "4":
                    clear_screen()
                    break
                
                else:
                    print("Gib eine Zahl von 1-4 ein.")
                    continue

        elif choice == "5":
            conn.close()
            break
        
        else:
            print("Gib eine Zahl von 1-4 ein.")
            continue

