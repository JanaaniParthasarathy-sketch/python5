# Contact Book

contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone
        print("Contact Saved!")

    elif choice == "2":
        if not contacts:
            print("No Contacts Found")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
