def my_decorator(funn):
  def wrapper(*args, **kwargs):
    print(f"Argument: {args} , keyword: {kwargs}")
    result= funn(*args,**kwargs)
    print("Function execution completed: ")
    return result
  return wrapper


@my_decorator
def add(a,b,c):
  return a+b+c

@my_decorator
def mul(a,b,c):
    return a*b*c


@my_decorator
def gre(name, age):
  return f"HI {name} and I am {age} years old"

print(add(1,2,c=4))
print(mul(2,2,c=4))  
print(gre("Birendra", age=21))

