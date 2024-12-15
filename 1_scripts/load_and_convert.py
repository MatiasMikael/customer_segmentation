import pandas as pd

# Use absolute path for the file
file_path = 'C:/Users/Matias/Desktop/customer_segmentation/2_data/online_retail.xlsx'

# Load the Excel file
data = pd.read_excel(file_path)

# Save as CSV file
data.to_csv('C:/Users/Matias/Desktop/customer_segmentation/2_data/online_retail.csv', index=False)
print("Excel file converted to CSV successfully!")

# Display the first few rows
print("First rows of the dataset:")
print(data.head())

# Display data structure
print("\nDataset structure:")
print(data.info())