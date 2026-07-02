from admin import Admin


def main():
    admin = Admin()

    while True:
        print("\n===== Student Marks Tracker =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Marks")
        print("4. Search Student")
        print("5. View Students")
        print("6. Average Marks")
        print("7. Save")
        print("8. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Name of the student : ")
            marks = int(input("Marks of that student : "))
            try:
                admin.add_student(name, marks)
                print(f"Added {name} with marks {marks} succsessfuly")
            except Exception as e:
                print(e)

        elif choice == "2":
            name = input("Name the student you want to remove : ")
            try:
                admin.remove_student(name)
            except Exception as e:
                print(e)

        elif choice == "3":
            name = input("Name of the student : ")
            new_marks = int(input("New Marks : "))

            admin.update_marks(name, new_marks)

        elif choice == "4":
            name = input("Name of the Student : ")

            name, marks = admin.search_student(name)
            print(name, " : ", marks)

        elif choice == "5":
            admin.view_all_students()

        elif choice == "6":
            avg_marks = admin.average_marks
            print("Average Marks is : ", avg_marks)

        elif choice == "7":
            admin.save_data()
            print("Data saved successfully.")

        elif choice == "8":
            admin.save_data()
            print("Data saved successfully.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
