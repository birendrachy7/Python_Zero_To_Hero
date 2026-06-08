try:
    num=int(input("Enter a number"))
    result = 100 /num
except ValueError:
    print("You must enter a valid number")
except ZeroDivisionError:
    print("You cannot divided by zero")
else:
    print(f"100 divided by {num} is {result}")
    print("No exceptions occurred!!")
finally:
    print("You are at the end of the this program")
    