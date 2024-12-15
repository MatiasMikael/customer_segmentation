import pandas as pd
import numpy as np

# Absolute paths
input_file = 'C:/Users/Matias/Desktop/customer_segmentation/2_data/online_retail.csv'
output_file = 'C:/Users/Matias/Desktop/customer_segmentation/3_cleaned_data/rfm_data.csv'

print("Loading dataset...")
# Load the dataset
data = pd.read_csv(input_file)
print("Dataset loaded successfully!")

# Remove rows with negative values in Quantity or UnitPrice
print("Filtering out rows with negative Quantity or UnitPrice...")
data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]
print(f"Remaining rows after filtering: {len(data)}")

# Calculate TotalPrice
print("Calculating TotalPrice...")
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

# Convert InvoiceDate to datetime format
print("Converting InvoiceDate to datetime format...")
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Define a reference date (e.g., one day after the last transaction in the dataset)
reference_date = data['InvoiceDate'].max() + pd.Timedelta(days=1)
print(f"Reference date for Recency calculation: {reference_date}")

# Calculate RFM values
print("Calculating RFM values...")
rfm = data.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,  # Recency
    'InvoiceNo': 'count',  # Frequency
    'TotalPrice': 'sum'    # Monetary
}).reset_index()

# Rename columns for clarity
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalPrice': 'Monetary'
}, inplace=True)

# Save the RFM data to the cleaned data folder
print(f"Saving RFM data to {output_file}...")
rfm.to_csv(output_file, index=False)
print("RFM data has been calculated and saved successfully!")

# Display first rows of RFM data
print("\nFirst rows of the calculated RFM data:")
print(rfm.head())