#task1:
table_of_3=[x*3 for x in range(1,11)]
print(table_of_3)

#Task 2:
dict_table={}
for x in range(1,11):
    dict_table[x]=x*3
print(dict_table)

#task 3 (Dictionary comprehension):

dict_table_comp={x:x*3 for x in range(1,11)}
print(dict_table_comp)


#task 4:
dict_cuber={x:x**3 for x in range(1,11) if x !=6}
print(dict_cuber)