from database import Database
import sys


if __name__ == "__main__":

    db = Database()

    if len(sys.argv) > 1 and sys.argv[1] == "1":
        db.cursor.execute("DROP TABLE bewerbungen")
        db.conn.commit()
        db.conn.close()
        sys.exit(0)

    
    default_status = "applied"

    while True:
        print("\n1. Bewerbung hinzufügen")
        print("2. Bewerbungen anzeigen")
        print("3. Status ändern")
        print("4. Bewerbung löschen")
        print("5. Filter nach Status")
        print("6. Beenden")

        choice = input("> ")

        if choice == "1":
            company = input("> Company: ")
            role = input("> Role: ")
            db.add_application(company, role, default_status)

        elif choice == "2":
            db.show_applications()

        elif choice == "3":
            id = int(input("> ID: "))
            status = input("> Neuer Status: ")
            db.update_status(status, id)

        elif choice == "4":
            while True:
                
                print("\n1. Lösche mit spezifischer ID")
                print("2. Lösche alle einer Company")
                print("3. Lösche alle eines Jobs")
                print("4. Zurück")

                del_choice = input("> ")

                if del_choice == "1":
                    
                    application_id = int(input("> ID: "))
                    db.delete_byID(application_id)
                    break

                elif del_choice == "2":

                    company_del = input("> Company: ")
                    db.delete_by_company(company_del)
                    break

                elif del_choice == "3":

                    role_del = input("> Role: ")
                    db.delete_by_role(role_del)
                    break

                elif del_choice == "4":
                    db.create_table()
                    break
                
                else:
                    print("Gib eine Zahl von 1-4 ein.")
                    continue

        elif choice == "5":
            status = input("> Status: ")
            db.show_with_status(status)

        elif choice == "6":
            db.conn.close()
            break
