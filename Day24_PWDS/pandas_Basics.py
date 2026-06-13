import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

print('*'*20)
data = {
    "Name": ["Ram", "Biru", "Hari"],
    "Age": [25, 21, 23],
    "Salary": [50000, 70000, 60000]
}


print('*'*20)

df = pd.DataFrame(data)
print(df)

print('*'*20)

# converting the above data into csv file
df.to_csv("employees.csv", index= False)

df = pd.read_csv("employees.csv")
print(df)


print('*'*20)
print(df.head(2))



print('*'*20)
print(df.tail(2))

print('*'*20)

# # convert the above data into excel files
# df.to_excel("employees.xlsx",index=False)
# df = pd.read_excel("employees.xlsx")

# print(df)



print('*'*20)

print(f"The shape of Dataset is:{df.shape}")


print('*'*20)
print(f"The size of Dataset is:{df.size}")


print('*'*20)

print(df.info())


print('*'*20)

print(df.columns)

print('*'*20)

print(df.describe())



print('*'*20)

# Select columns
print(df[['Name',"Salary"]])

print('*'*20)

print("Filter rows")
print(df[df["Salary"]>55000])

print('*'*20)
print("Add Bonus COlumns")
df["Bonus"]=df["Salary"]*0.10
print(df)

print('*'*20)
print("Sort by salary descending")
df.sort_values("Salary", ascending=False)
print(df)

print('*'*20)
print("HAndle missing values")
print(df.fillna(0))

print('*'*20)
print("Updated employee.csv")
df.to_csv("updated_employees.csv",index=False)
print('*'*20)
print("updated employees with bonus")
df= pd.read_csv("updated_employees.csv")
print(df)


print('*'*20)

#6. Data Visualization with Matplotlib

plt.figure(figsize=(6,4))
plt.bar(df["Name"],df['Salary'])
plt.xlabel("Name")
plt.ylabel("Salary")
plt.title("Salary of Employee")
plt.show()

#8. Data Visulization wtih seaborn
print('*'*20)

plt.figure(figsize=(6,4))

sns.barplot(data=df,x="Name",y="Salary")
plt.show()


#9. Data Visualization wiht plotly
fig=px.bar(df,x="Name",y="Salary",title="Salary of Emplyee")
fig.show()