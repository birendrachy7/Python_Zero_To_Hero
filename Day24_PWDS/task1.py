import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Sales": [100, 150, 80, 60],
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


#  Convert DataFrame to CSV

df.to_csv("sales.csv", index=False)

print("\n'sales.csv' created successfully.")


# Read the CSV file

sales_df = pd.read_csv("sales.csv")

print("\nData read from CSV:")
print(sales_df)


print("\nSummary Statistics:")
print(sales_df.describe())


highest_product = sales_df.loc[sales_df["Sales"].idxmax()]

print("\nHighest-Selling Product:")
print(f"Product: {highest_product['Product']}")
print(f"Sales: {highest_product['Sales']}")


sales_df["Growth_10%"] = sales_df["Sales"] * 1.10

print("\nAfter Adding Growth Column:")
print(sales_df)


sales_df.to_csv("sales_updated.csv", index=False)

print("\n'sales_updated.csv' saved successfully.")


plt.figure(figsize=(6, 4))
plt.bar(df["Product"], df["Sales"])
plt.title("Sales by Product (Matplotlib)")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()


plt.figure(figsize=(6, 4))
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales by Product (Seaborn)")
plt.show()

fig = px.bar(
    df, x="Product", y="Sales", title="Sales by Product (Plotly)", text="Sales"
)

fig.show()
