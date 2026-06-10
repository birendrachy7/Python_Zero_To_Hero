# The math module in Python is a built-in library that contains a collection of mathematical functions and constants. 
# It is commonly used to perform standard math operations such as rounding, trigonometry, logarithms and more, 
# all with precise and reliable results.

# Why do we need Math module ?
# Provides built-in functions for complex math operations like square root, power and trigonometry.
# Offers constants like pi and e, useful in scientific and engineering calculations.
# Improves accuracy and performance over manual calculations or custom functions.
# Helps in performing logarithmic and exponential operations easily.
# Supports real-world applications like physics, statistics, geometry and finance.



# Importing math module

import math

# Euler's number
print(math.e)

# Pi
print (math.pi)



# Numeric Functions in Math Module

# 1. Finding the ceiling and the floor value

# Ceil value means the smallest integral value greater than the number 
# the floor value means the greatest integral value smaller than the number. 
# This can be easily calculated using the ceil() and floor() method respectively.
a = 2.3
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 
print ("The floor of 2.3 is : ", end="") 
print (math.floor(a))

# 2. Finding the factorial of the number

b = 5
print("The factorial of 5 is : ", end="")
print(math.factorial(b))