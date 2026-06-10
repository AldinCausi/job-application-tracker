from database import Database
import utils
import sys
from enum import Enum

def add_application(db, status):
    company = input("> Company: ")
    role = input("> Role: ")
    db.add_application(company, role, status)

def update_status(db):
    bewerbungen = db.show_applications()
    if not bewerbungen:
        return
    
    print("Gebe 'b' ein, um zurück zu gehen")
    application_id = input("> ID: ")

    if application_id == "b":
        utils.clear_screen()
        return  

    if not application_id.isdigit():
        print("Ungültige ID.")
        return
    
    if not db.check_if_ID_exists(int(application_id)):
        print("Diese ID gehört zu keinem Eintrag.")
        return
    
    current_status = Status[db.get_status(int(application_id))]
    allowed_status_changes = list(current_status.transitions())

    if not allowed_status_changes:
        print("Dieser Status kann nicht verändert werden.\n")
        return
    
    print("Mögliche Statuswechsel: ")
    for i, status in enumerate(allowed_status_changes, start=1):
        print(f"{i}. {status.name}")
    print(f"{i+1}. Zurück")
    while True:
        status_choice = input("> ")

        if not status_choice.isdigit():
            continue

        status_choice = int(status_choice)

        if status_choice == len(allowed_status_changes)+1:
            utils.clear_screen()
            return
        if 1 <= status_choice <= len(allowed_status_changes):
            new_status = allowed_status_changes[status_choice-1]
            db.update_status(new_status.name, application_id)
            return
        else:
            print(f"Gebe eine zahl von 1-{len(allowed_status_changes)+1} ein")

def filter_show_by_status(db):
    if not db.if_any_status_exists():
        print("Es gibt gerade keine Bewerbungen. Füge erstmal welche hinzu")
        return
    
    existing_status = db.get_distinct_status()

    print("Vergebene Status: ")
    for i, status in enumerate(existing_status, start=1):
        print(f"{i}. {status}")
    print(f"{i+1}. Zurück")
    while True:
        status_choice  = input("> ")
        if not status_choice.isdigit():
            continue

        status_choice = int(status_choice)

        if status_choice == len(existing_status)+1:
            utils.clear_screen()
            return
        if 1 <= status_choice <= len(existing_status):
            chosen_status = existing_status[status_choice-1]
            db.show_with_status(chosen_status)
            return
        else:
            print(f"Gebe eine Zahl von 1-{len(existing_status)+1} ein")
            continue

def delete_application(db):
    bewerbungen = db.show_applications()
    if not bewerbungen:
        return

    while True:
        print("\n1. Lösche mit spezifischer ID")
        print("2. Lösche alle einer Company")
        print("3. Lösche alle eines Jobs")
        print("4. Zurück")

        del_choice = input("> ")

        if del_choice == "1":
            delete_byID(db)
            return
        elif del_choice == "2":
            delete_by_company(db)
            return
        elif del_choice == "3":
            delete_by_role(db)
            return
        elif del_choice == "4":
            utils.clear_screen()
            return
        else:
            print("Gib eine Zahl von 1-4 ein.")
            continue

def delete_byID(db):
    print("Gebe 'b' ein, um zurück zu gehen")
    id_to_delete = input("> ID: ")
    if id_to_delete == "b":
        utils.clear_screen()
        return
    if not id_to_delete.isdigit():
        print("Ungültige ID.")
        return
    if not db.id_exists(id_to_delete):
        print("Es existiert kein Job mit dieser ID in der Datenbank.")
        return
    id_to_delete = int(id_to_delete)
    db.delete_byID(id_to_delete)

def delete_by_company(db):
    print("Gebe 'b' ein, um zurück zu gehen")
    company_to_delete = input("> Company: ")
    if company_to_delete == "b":
        utils.clear_screen()
        return
    if not db.company_exists(company_to_delete):
        print("Diese company existiert nicht in der Datenbank.")
        return
    db.delete_by_company(company_to_delete)

def delete_by_role(db):
    print("Gebe 'b' ein, um zurück zu gehen")
    role_to_delete = input("> Role: ")
    if role_to_delete == "b":
        utils.clear_screen()
        return
    if not db.role_exists(role_to_delete):
        print("Dieser Job existiert nicht in der Datenbank")
        return
    db.delete_by_role(role_to_delete)


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
    print("4. Filter nach Status")
    print("5. Bewerbung löschen")
    print("6. Beenden")

    choice = input("> ")

    if choice == "1":
        add_application(db, status)

    elif choice == "2":
        db.show_applications()

    elif choice == "3":
        update_status(db)
    
    elif choice == "4":
        filter_show_by_status(db)

    elif choice == "5":
        delete_application(db)

    elif choice == "6":
        db.conn.close()
        break
