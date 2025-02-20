import pandas as pd
file_path ='data.csv'
data = pd.read_csv(file_path)
print("First 5 rows of the dataset:")
print(data.head())
print("\nDataset Information:")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())
if 'category' in data.columns:
    print("\nUnique values in 'category' column:")
    print(data["categoery"].value_counts())