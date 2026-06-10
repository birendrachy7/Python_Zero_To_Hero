def square(max_value):
    current = 1
    while current <= max_value:
        yield current **2
        current+=1


for num in square(5):
    print(num)