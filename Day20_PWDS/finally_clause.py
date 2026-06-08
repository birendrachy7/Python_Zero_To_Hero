try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing resources.")
    try:
        file.close()
    except NameError:
        pass