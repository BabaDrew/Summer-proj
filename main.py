from Users import User
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
def main():
    me = User(input("Enter your name: "))
    # return "<h1>Trying heading</h1>Regular text"

    while True:
        print("\nMENU:")
        print("0. Exit")
        print("1. Add a new course")
        print("2. Edit the grade distribution for a course")
        print("3. View all courses and their respective values")
        print("4. View a course's grade distribution")

        choice = input("Enter your choice (0-4): ")

        if choice == '1':
            me.add_course()
        elif choice == '2':
            me.edit_course()
        elif choice == '3':
            me.view_courses()
        elif choice == '4':
            me.view_courses(False)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
    print("\nHave a nice day!")


if __name__ == "__main__":
    # app.run()
    main()
