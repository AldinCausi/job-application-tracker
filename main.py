import database
import sys

if __name__ == "__main__":

    # Das hier erlaubt es dem Nutzer mit einer leeren database zu starten
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        if argument == "1":
            database.delete_table()


    database.create_table()
    default_status = "pending"


    while True:
        print("\n1. Bewerbung hinzufügen")
        print("2. Bewerbungen anzeigen")
        print("3. Status einer Bewerbung ändern")
        print("4. Bewerbung löschen")
        print("5. Beenden")

        choice = input("> ")

        if choice == "1":
            database.create_table()
            company = input("> Company: ")
            role = input("> Role: ")
            status = default_status
            database.add_application(company, role, status)

        elif choice == "2":

            database.show_applications()

        elif choice == "3":

            status_id = int(input("> ID: "))
            new_status = input("> Neuer Status: ")
            database.update_status(new_status, status_id)

        elif choice == "4":

            while True:
                
                print("\n1. Lösche mit spezifischer ID")
                print("2. Lösche alle einer Company")
                print("3. Lösche alle eines Jobs")
                print("4. Zurück")

                del_choice = input("> ")

                if del_choice == "1":
                    
                    application_id = int(input("> ID: "))
                    database.delete_byID(application_id)
                    break

                elif del_choice == "2":

                    company_del = input("> Company: ")
                    database.delete_by_company(company_del)
                    break

                elif del_choice == "3":

                    role_del = input("> Role: ")
                    database.delete_by_role(role_del)
                    break

                elif del_choice == "4":
                    database.create_table()
                    break
                
                else:
                    print("Gib eine Zahl von 1-4 ein.")
                    continue

        elif choice == "5":
            database.conn.close()
            break
        
        else:
            print("Gib eine Zahl von 1-4 ein.")
            continue