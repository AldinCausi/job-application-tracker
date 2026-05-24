# Das hier ist eine Job application tracker software. Start 24.05.2026 17:23


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



#Bewerbung hinzufügen
def add_application():

    dict_applications = {}

    status_default = "Wartet auf Rückmeldung"

    print("Gebe den Namen der Firma\n")
    comp_name = input("> ")

    print("Gebe die Jobbezeichnung ein\n")
    job_name = input("> ")

    dict_applications.update(
        {
            comp_name: {
            "Job": job_name, 
            "Status": status_default
            }
        }
    )

    with open("Bewerbungen.txt", "w") as f:
        for key, info in dict_applications.items():
            f.write(f"{key}\n")
            f.write(f"\t\tStatus: {info["Status"]}\n")
            f.write(f"\t\tJob: {info["Job"]}\n")

# Hier werden Dinge an Beispielen ausprobiert
def test():
    test_dict = {
            "Bewerbung_1": {
            "Firma": "Thyssenkrupp",
            "Job": "Softwarewntwickler",
            "Status": "Wartet auf Rückmeldung"
        }
    }


    with open("test.txt", "a") as f:
        for key, info in test_dict.items():
            f.write(f"{key}: ")
            f.write(f"{info["Status"]}\n")
            f.write(f"\tJob: {info["Job"]}\n")
            f.write(f"\tFirma: {info["Firma"]}")

print("1. Test\n")
print("2. Tracker\n")
input_test = input("> ")
if input_test == "1":
    test()
if input_test == "2":
    menu()


