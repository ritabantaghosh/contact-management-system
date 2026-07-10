import csv
import tabulate

def main():
    print("Welcome to Contact Management System.")
    while True:
        print("You can type 'Add' to add contacts, 'Delete' to delete any contact, 'Search' to search any contact, 'Display' to display all contacts, or 'Quit' to exit the system.")
        choice = input("Enter your choice: ").lower().strip()
        if choice == "add":
            lists = add_contacts()
        elif choice == "delete":
            delete_contact()
        elif choice == "search":
            search_contacts()
        elif choice == "display":
            display_contacts()
        elif choice == "quit":
            break
        else:
            print("Invalid choice.")

def add_contacts():
    name = input("Enter the name of contact: ")
    number = input("Enter the number of contact: ")
    while (not name or not number or number.isdigit() == False):
        if name == "":
            name = input("Enter the name of contact: ")
        if number == "" or number.isdigit() == False:
            number = input("Enter the number of contact: ")
    email = input("Enter the email of contact(optional): ")
    with open("contacts.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["NAME", "NUMBER", "EMAIL"])
        writer.writerow({"NAME": name, "NUMBER": number, "EMAIL": email})


def delete_contact():
    lists = []
    with open("contacts.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lists.append(row)
    for i, l in enumerate(lists):
        print(i + 1, ".", lists[i]["NAME"], "|", lists[i]["NUMBER"], "|", lists[i]["EMAIL"])
    number = input("Which one of these would you like to remove? ")
    while True:
        if number.isdigit():
            if int(number) <= 0 or int(number) > len(lists):
                number = input("Which one of these would you like to remove? ")
            else:
                break
        else:
            number = input("Which one of these would you like to remove? ")
            continue
    
    with open("contacts.csv") as file:
        lines = file.readlines()
    del lines[int(number)]
    with open("contacts.csv", "w") as file:
        file.writelines(lines)
        
def search_contacts():
    print("How would you like to search?")
    print("Enter 1 to search by name.")
    print("Enter 2 to search by number.")
    print("Enter 3 to search by email.")
    number = input("Enter: ")
    while True:
        if number.isdigit() and 1 <= int(number) <= 3:
            break
        else:
            number = input("Enter: ")
            continue
    number = int(number)
    search = []
    with open("contacts.csv") as file:
        rows = csv.reader(file)
        for row in rows:
            search.append(row)
    try:
        if number == 1:
            name = input("Enter name: ").lower().strip()
            for s in search:
                if s[0].lower() == name:
                    matches = s
            if len(matches) == 2:
                print(matches[0], matches[1])
            elif len(matches) == 3:
                print(matches[0], matches[1], matches[2])
    except:
        print("Name not found.")
    try:
        if number == 2:
            num = input("Enter number: ").strip()
            for s in search:
                if s[1] == num:
                    matches = s
            if len(matches) == 2:
                print(matches[0], matches[1])
            elif len(matches) == 3:
                print(matches[0], matches[1], matches[2])
    except:
        print("Number not found.")
    try:
        if number == 3:
            email = input("Enter email: ").lower().strip()
            for s in search:
                if s[2].lower() == email:
                    matches = s
            print(matches[0], matches[1], matches[2])
    except:
        print("Email not found.")

def display_contacts():
    lists = []
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            lists.append(row)
    headers = lists[0]
    table = []
    for i in range(len(lists)):
        if i <= len(lists) - 2:
            table.append(lists[i + 1])
    print(tabulate.tabulate(table, headers, tablefmt="grid"))



if __name__ == "__main__":
    main()
