from database import Database
import sys
from enum import Enum


if __name__ == "__main__":

    db = Database()

    if len(sys.argv) > 1 and sys.argv[1] == "1":
        db.cursor.execute("DROP TABLE bewerbungen")
        db.conn.commit()
        db.conn.close()
        sys.exit(0)


    class Status(Enum):
        APPLIED = 1
        INTERVIEWED = 2
        REJECTED = 3
        ACCEPTED = 4

        def transitions(self):
             return {
                Status.APPLIED: {
                    Status.INTERVIEWED,
                    Status.REJECTED 
                    },
                Status.INTERVIEWED: {
                    Status.ACCEPTED,
                    Status.REJECTED
                },
                Status.REJECTED: set(),
                Status.ACCEPTED: set(),
            }[self]

    status = Status.APPLIED.name

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
            db.add_application(company, role, status)

        elif choice == "2":
            db.show_applications()

        elif choice == "3":
            db.show_applications()

            application_id = int(input("> ID: "))

            if db.check_if_ID_exists(application_id):

                current_status = Status[db.get_status(application_id)]

                allowed_status_changes = list(current_status.transitions())

                if not allowed_status_changes:
                    print("Dieser Status kann nicht verändert werden.\n")
                    continue
                print("Mögliche Statuswechsel: ")
                for i, status in enumerate(allowed_status_changes, start=1):
                    print(f"{i}. {status.name}")

                status_choice = int(input("> "))

                new_status = allowed_status_changes[status_choice-1]

                db.update_status(new_status.name, application_id)
            else:
                print("Diese ID gehört zu keinem Eintrag.")
                continue

        elif choice == "4":
            db.show_applications()
            
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
