# Reading the binary file (like an image)
with open("naruto.jpg","rb") as file:
    binary_data = file.read()
    print(f"Read {len(binary_data)} bytes")
    
# writing binary data
with open("naruto-copy.jpg","wb") as file:
    file.write(binary_data)
    
# Copying a binary file
#def 