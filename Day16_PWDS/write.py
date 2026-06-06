student_list=["Bibek","Birendra","Lochan","Sujan","Suman","Sushil","YOYO"]


# with open ("students.txt","w") as file:
#     for student in student_list:
#         file.write(student + "\n")
        
        
        
# .writelines() method can be used to write a list of strings to a file. Each string in the list will be written as a separate line in the file. Here's how you can use it: 
with open("students.txt", "w") as file:
    file.writelines(student + "\n" for student in student_list) 
    