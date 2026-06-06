# Note-Taking App using File Handling

FILE_NAME = "notes.txt" # 

while True:
    print("\nNote-Taking App")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Clear all notes")
    print("4. Exit")

# 
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        note = input("Enter your note: ")

        with open(FILE_NAME, "a") as file:
            file.write(note + "\n")

        print("Note added!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                notes = file.readlines()

            if len(notes) == 0:
                print("No notes available.")
            else:
                print("\nYour Notes:")
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")

        except FileNotFoundError:
            print("No notes file found.")

    elif choice == "3":
        with open(FILE_NAME, "w") as file:
            pass  # Clears the file

        print("All notes cleared!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")