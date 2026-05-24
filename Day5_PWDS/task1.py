# WAP to ask the user to take a number. Count up from 1 to that number, but apply these two rule using continue and break:
# If the number is a multiple of 3, skip it and continue counting.
# If the number is greater than or equal to , stop loop entirely using the break statement.

num = int(input("Enter a number: "))  # Take input from the user and convert it to an integer
count = 1  # Initialize count to 1
while count <= num:  # Loop until count is less than or equal to the user input
    if count % 3 == 0:  # Check if count is a multiple of 3
        count += 1  # Increment count by 1 to skip the current number
        continue  # Skip the rest of the loop and continue with the next iteration
    print(count)  # Print the current value of count
    count += 1  # Increment count by 1 for the next iteration
    if count >= num:  # Check if count is greater than or equal to the user input
        break  # Exit the loop if count exceeds or equals the user input



# anlysis: the same code by for loop
num = int(input("Enter a number: "))  # Take input from the user and convert it to an integer   
for count in range(1, num + 1):  # Loop from 1 to the user input
    if count % 3 == 0:  # Check if count is a multiple of 3
        continue  # Skip the rest of the loop and continue with the next iteration
    print(count)  # Print the current value of count
    if count >= num:  # Check if count is greater than or equal to the user input
        break  # Exit the loop if count exceeds or equals the user input
    
