
import sqlite3

DB_NAME = "users.db"


# Database

def init_db():
    """Create database and users table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect(DB_NAME)


# adding users details

def add_user():
    print("\n--- Add New User ---")

    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    age_str = input("Enter Age: ").strip()

    if not name or not email or not age_str:
        print("All fields are required!")
        return

    try:
        age = int(age_str)

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Age must be a valid number.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )

        conn.commit()
        conn.close()

        print("User added successfully!")

    except sqlite3.IntegrityError:
        print("Email already exists.")


#reading  users details

def show_all_users():
    print("\n--- User List ---")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    if not users:
        print("No users found.")
        return

    print("-" * 60)
    print(f"{'ID':<5}{'NAME':<20}{'EMAIL':<25}{'AGE':<5}")
    print("-" * 60)

    for user in users:
        print(
            f"{user[0]:<5}"
            f"{user[1]:<20}"
            f"{user[2]:<25}"
            f"{user[3]:<5}"
        )


# update users details

def update_user():
    print("\n--- Update User ---")

    show_all_users()

    user_id = input("\nEnter User ID to Update: ").strip()

    try:
        user_id = int(user_id)

    except ValueError:
        print("Invalid ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        print("User not found.")
        conn.close()
        return

    print("\nLeave blank to keep existing value.")

    name = input(f"New Name ({user[1]}): ").strip()
    email = input(f"New Email ({user[2]}): ").strip()
    age = input(f"New Age ({user[3]}): ").strip()

    if not name:
        name = user[1]

    if not email:
        email = user[2]

    if not age:
        age = user[3]
    else:
        try:
            age = int(age)

            if age <= 0:
                print("Age must be positive.")
                conn.close()
                return

        except ValueError:
            print("Invalid age.")
            conn.close()
            return

    try:
        cursor.execute(
            """
            UPDATE users
            SET name = ?, email = ?, age = ?
            WHERE id = ?
            """,
            (name, email, age, user_id)
        )

        conn.commit()
        print("User updated successfully!")

    except sqlite3.IntegrityError:
        print("Email already exists.")

    conn.close()


# deleting users details

def delete_user():
    print("\n--- Delete User ---")

    show_all_users()

    user_id = input("\nEnter User ID to Delete: ").strip()

    try:
        user_id = int(user_id)

    except ValueError:
        print("Invalid ID.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        print("User not found.")
        conn.close()
        return

    confirm = input(
        f"Delete {user[1]}? (y/n): "
    ).lower()

    if confirm == "y":
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        conn.commit()
        print("User deleted successfully!")

    else:
        print("Deletion cancelled.")

    conn.close()


# menu 

def print_menu():
    print("\n" + "=" * 40)
    print("        SIMPLE CRUD APPLICATION")
    print("=" * 40)
    print("1. Add User")
    print("2. Show All Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    print("=" * 40)


def menu_choice(choice):

    if choice == "1":
        add_user()

    elif choice == "2":
        show_all_users()

    elif choice == "3":
        update_user()

    elif choice == "4":
        delete_user()

    elif choice == "5":
        return False

    else:
        print("Invalid choice. Please select 1-5.")

    return True


# ---------------- MAIN ----------------

def main():

    print("Welcome to Simple CRUD App")

    init_db()

    choose = True

    while choose:

        print_menu()

        choice = input("Enter your choice: ").strip()

        choose = menu_choice(choice)

        if choose:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()