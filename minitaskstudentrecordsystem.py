# Student Record System

students = {}

while True:
    print("\n----- Student Record Menu -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students[roll] = {
            "Name": name,
            "Marks": marks
        }

        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Records Found")
        else:
            print("\nStudent Records:")
            for roll, details in students.items():
                print("Roll No:", roll)
                print("Name:", details["Name"])
                print("Marks:", details["Marks"])
                print("-" * 20)

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            print("Student Found:")
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student Not Found")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
