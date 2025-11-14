import pandas as pd
import numpy as np

data = {
    'product_name' : ['Laptop', 'Mouse', 'Keyboards'],
    'category' : ['Electronics', 'Accessories', 'Gadgets'],
    'price' : [70000, 500, 2000],
    'quantity' : [1, 2, 1],
    'discount (%)' : [10, 5, 5]
}

data_frame = pd.DataFrame(data)

# print(data_frame.info)

data_frame['Revenue'] = data_frame['price'] * data_frame['quantity'] * (1 - data_frame['discount (%)']/100)
# print(data_frame.head())

# data_frame.to_csv("data.csv", index=False)

sales = pd.read_csv("data.csv")
sales.head()

# data_frame.tail() # bottom 5
# data_frame.head() # top 5

# print(sales.describe())

# Selecting, Indexing and Filtering
# print(data_frame['product_name'] == 'Laptop')


df = pd.read_csv("zomato.csv", encoding="latin-1")

df1 = pd.read_excel("Country-Code.xlsx")

# print(df.info())
# print("Rows : ", df.shape[0])
# print("Columns : ", df.shape[1])

# print(df.columns)

df_new = pd.merge(df, df1, how="left")

# print(df1['Country Code'].unique()) # prints unique columns

# print(df1['Country'].nunique())

# 1 load data
# 2 analyze the data
    # rows / columns
    # Na
    # NaN  
    # Na and NaN h toh random data fill karde, lekin zyada hai toh drop krde

    # duplicate - if duplicate then drop

# print(df_new['Country'] == 'India')

# print(df[df['City'] == 'New Delhi'])

# print(df[(df['City'] == 'Ghaziabad') & (df['Rating text'] == 'Poor')])

# print(df[df[df['City'] == 'Ghaziabad'] == 'Rating text'] == 'Poor')

import matplotlib.pyplot as plt
import seaborn as sns

new_data = {
    'Category' : ['Electronics', 'Clothing', 'Groceries', 'Toys', 'Furniture'],
    'Revenue' : [55000, 32000, 21000, 15000, 40000],
    'Profit' : [12000, 7000, 5000, 2000, 9000],
    'Quantity' : [120, 230, 300, 150, 100]
}

# Line Plot - To visualize trend over time or continuous data.
# Why : shows how values change squentially

# plt.figure(figsize=(6,4))
# # print(plt.plot(new_data['Category'], new_data['Revenue']))

# # plt.show()

# sns.barplot(x='Category', y='Revenue', data=new_data)
# plt.title("Seaborn Bar Plot - Revenue by Category")

# print(plt.show())

# Histogram
# plt.figure(figsize=(6,4))
# plt.hist(new_data['Revenue'], bins=10, color='orange', edgecolor='black')
# plt.title("Histogram")
# plt.xlabel('Revenue')
# plt.ylabel('Frequency')
# print(plt.show())


# Area Plot

x = np.arange(1,6)
y1 = np.array([10,20,30,25,15])
y2 = np.array([5,15,25,20,10])

plt.figure(figsize=(6,4))
plt.stackplot(x, y1, y2, labels=['Product A', 'Product B'])
plt.legend(loc='upper left')
print(plt.show())
