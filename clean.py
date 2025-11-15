import pandas as pd

data_frame = pd.read_csv("Reliance Trends Fashion.csv")

# print(data_frame.head())

# print(data_frame.isnull().sum())

# print(data_frame.duplicated().sum())

data_frame.drop_duplicates(inplace=True)

print(data_frame.columns)

data_frame = data_frame.drop(columns=["Image_URL", "Product_URL"])

data_frame.reset_index(drop=True, inplace=True)
# print(data_frame.duplicated().sum())

print(data_frame.columns)