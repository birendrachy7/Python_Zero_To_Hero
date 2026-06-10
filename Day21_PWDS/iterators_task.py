class SquareIterator:
    def __init__(self,max_num):
        self.max_num = max_num
        self.current =0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_num:
            self.current +=1
            return self.current**2
        else:
            raise StopIteration
    
num = int(input("Enter any number"))

square_obj = SquareIterator(num)
for squ in square_obj:
    print(squ)
    