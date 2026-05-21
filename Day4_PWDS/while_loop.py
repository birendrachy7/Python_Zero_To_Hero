# While Loop
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
# The while loop can be thought of as a repeating if statement.
# Syntax of while loop:
# while condition:
#     # code to be executed
# The condition is evaluated before the execution of the loop's body. If the condition is true, the code block inside the loop is executed.
# Example of while loop:

"""
num = 1
while num <= 10:
    print(3*num)
   # print(f"{3}*{num} = {num * 3}")
    num = num + 1


print("#------------------------------------------------------# ")

mul = 3
while mul <= 30:
    print(mul)
    mul = mul + 3
    
    
print("#------------------------------------------------------# ")


prod=3
while prod <=30:
    print(prod)
    prod +=3


"""
print("#-------------------------------------------------------#")

#break using while loop

count = 1   # Initialize count to 1
while True:  # Infinite loop, will run until break is encountered
    print(count) # Print the current value of count
    count += 1   # Increment count by 1
    if count > 5:   # Check if count exceeds 5
        break    # Exit when count exceeds 5