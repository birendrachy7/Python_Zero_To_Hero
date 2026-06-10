# Python Random module generates random numbers in Python. 
# It introduce randomness into programs. It offers functions that support randomization operations, 
# making it easier to work with unpredictable or varied outputs in different programming scenarios.

# Why do we need Random module?
# Helps generate random numbers for simulations, testing and games.
# Allows shuffling, sampling and selecting random elements from lists or sequences.
# Useful in creating random passwords, OTPs or mock data.
# Supports both integer and floating-point random generation.
# Essential for data sampling, machine learning and statistical modeling.

import random

# ==========================
# Basic Random Functions
# ==========================

print(random.random())      
# Random float between 0.0 and 1.0

print(random.uniform(1, 10))
# Random float between 1 and 10

print(random.randint(1, 10))
# Random integer between 1 and 10 (inclusive)

print(random.randrange(1, 10))
# Random integer from 1 to 9 (10 excluded)

print(random.randrange(0, 20, 2))
# Random even number between 0 and 18


# ==========================
# Random Choice Functions
# ==========================

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(random.choice(fruits))
# Returns one random element from the list

print(random.choices(fruits, k=3))
# Returns k random elements WITH replacement

print(random.sample(fruits, 2))
# Returns 2 unique random elements WITHOUT replacement


# ==========================
# Shuffle Functions
# ==========================

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)
# Shuffles the original list in-place

print(numbers)


# ==========================
# Probability Functions
# ==========================

colors = ["Red", "Blue", "Green"]

print(random.choices(colors,
                     weights=[70, 20, 10],
                     k=5))
# Weighted random selection
# Red has 70% chance, Blue 20%, Green 10%


# ==========================
# Seed Function
# ==========================

random.seed(42)
# Sets the seed value for reproducible results

print(random.randint(1, 100))
# Same output every time seed=42 is used


# ==========================
# Random Bytes
# ==========================

print(random.randbytes(5))
# Generates 5 random bytes
# Available in Python 3.9+


# ==========================
# Gaussian Distribution
# ==========================

print(random.gauss(0, 1))
# Random number from Normal Distribution
# mean=0, standard deviation=1

print(random.normalvariate(0, 1))
# Similar to gauss()


# ==========================
# Other Distributions
# ==========================

print(random.expovariate(1))
# Exponential distribution

print(random.betavariate(2, 5))
# Beta distribution

print(random.gammavariate(2, 2))
# Gamma distribution

print(random.lognormvariate(0, 1))
# Log-normal distribution

print(random.triangular(1, 10, 5))
# Triangular distribution
# low=1, high=10, mode=5

print(random.vonmisesvariate(0, 1))
# Circular distribution (angles)

print(random.paretovariate(3))
# Pareto distribution

print(random.weibullvariate(1, 2))
# Weibull distribution