import Classes

def main():
    me = Classes.User(input("Enter your name: "))
    while True:
        print("\nMENU:")
        print("1. Add a new course")
        print("2. Edit the grade distribution for a course")
        print("3. View all courses and their respective grades")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            me.add_course()
        elif choice == '2':
            print("Currently Under Development")
        elif choice == '3':
            me.view_courses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
    print("\nHave a nice day!")


if __name__ == "__main__":
    main()
