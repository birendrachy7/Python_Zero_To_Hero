# reduce() function applies a function cumulatively to the elements of an iterable and returns a single final value. 
# It processes elements step-by-step, combining two elements at a time until only one result remains

from functools import reduce
a = [2, 4, 6, 8]
r = reduce(lambda x, y: x + y, a)
print(r)

print("----------------")
ab = [5, 9, 3, 12, 7]
rb = reduce(lambda x, y: x if x > y else y, ab)
print(rb)