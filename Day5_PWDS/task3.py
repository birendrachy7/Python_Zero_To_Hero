# Take a number frome the user and print it in reverser order using for loop 
num = int(input("Enter a number: "))  # Take input from the user and convert it to an integer
num_str = str(num)  # Convert the number to a string to access each digit
reversed_num_str = num_str[::-1]  # Reverse the string using slicing
print("Reversed number:", reversed_num_str)  # Print the reversed number




#Print the right angle triangle pattern using "*" using for loop
rows = int(input("Enter the number of rows for the triangle: "))  # Take input for the number of rows
for i in range(1, rows + 1):  # Loop from 1 to the number of rows
    print("*" * i)  # Print "*" repeated i times to form the triangle pattern   
    


#Take a input from user and print the reversed right angle triangle pattern using "*" using for loop
rows = int(input("Enter the number of rows for the triangle: "))  # Take input for the number of rows
for i in range(rows, 0, -1):  # Loop from the number of rows down to 1
    print("*" * i)  # Print "*" repeated i times to form the reversed triangle pattern  
    
