# Das hier ist eine Job application tracker software. Start 24.05.2026 17:23
import json

# Menu darstellen
def menu():
    while True:
        print("1. Bewerbung hinzufügen\n")
        print("2. Bewerbungen ansehen\n")
        print("Gebe 'q' ein, um das Programm zu beenden.\n")
        userInput = input("> ")
        if userInput == 'q':
            break
        if int(userInput) == 1:
            add_application()
        if int(userInput) == 2:
            show_applications()



#Bewerbung hinzufügen
def add_application():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e: 
        data = {}

    name = input("Gebe den Namen der Firma ein\n> ")
    job = input("Gebe die Jobbezeichnung ein\n> ")

    data[name] = {
        "Status": "Wartet",
        "Job": job
    }

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    with open("data.json", "r") as f:
        data = json.load(f)

    with open("Bewerbungen.txt", "w") as f:
        for key, info in data.items():
            f.write(f"{key}\n")
            f.write(f"\t\tSTATUS: {info["Status"]}\n")
            f.write(f"\t\tJob: {info["Job"]}\n")

# Bewerbungen ansehen
def show_applications():
    with open("Bewerbungen.txt", "r") as f:
        content = f.read()
    print(content)


menU()
