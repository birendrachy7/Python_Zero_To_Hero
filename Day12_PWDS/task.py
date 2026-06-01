# Create a function name fizzbuzz that takes a number as an argument and returns:
# "Fizz" if the number is divisible by 3,
# "Buzz" if the number is divisible by 5,
# "FizzBuzz" if the number is divisible by both 3 and 5,
# and the number itself if it is divisible by neither 3 nor 5.
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
# Example usage:
print(fizzbuzz(3))   # Output: Fizz
print(fizzbuzz(5))   # Output: Buzz
print(fizzbuzz(15))  # Output: FizzBuzz


#user input
number = int(input("Enter a number: ")) 
print(fizzbuzz(number))  # Output: The result based on the input number