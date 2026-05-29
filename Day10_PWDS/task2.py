products={
    "Laptop": 70000,
    "Mouse":500,
    "keyboard": 1200,
    "monitor": 15000
}

count=0

for key, values in products.items():
    if values>1000:
        count +=1

print(f"There are {count} products whose cost is more than 1000")





#Same 

count=0
less=0
for i in products:
  if products[i]>1000:
    count+=1
  else:
    less+=1
print(f"There are {count} product whose cost is more than 1000")
print(f"There are {less} product whose cost is less than 1000")
