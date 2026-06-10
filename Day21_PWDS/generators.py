# A generator function is a special type of function that returns an iterator object. 
# Instead of using return to send back a single value, 
# generator functions use yield to produce a series of results over time.

def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt   #Yield is used in generator functions to provide a sequence of values over time.
        cnt += 1
                    # Return: is used to exit a function and return a final value.
ctr = fun(5)
for n in ctr:
    print(n)
    
    
# Explanation: This generator function fun yields numbers from 1 up to a specified max. 
# Each call to next() on the generator object resumes execution right after the yield statement, where it last left off.

# Why Do We Need Generators?
    # Memory Efficient : Handle large or infinite data without loading everything into memory.
    # No List Overhead : Yield items one by one, avoiding full list creation.
    # Lazy Evaluation : Compute values only when needed, improving performance.
    # Support Infinite Sequences : Ideal for generating unbounded data like Fibonacci series.
    # Pipeline Processing : Chain generators to process data in stages efficiently.
    