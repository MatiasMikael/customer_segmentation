import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Absolute paths
input_file = 'C:/Users/Matias/Desktop/customer_segmentation/3_cleaned_data/rfm_data.csv'
output_file = 'C:/Users/Matias/Desktop/customer_segmentation/4_results/rfm_clusters.csv'

print("Loading RFM data...")
# Load the RFM data
rfm = pd.read_csv(input_file)
print("RFM data loaded successfully!")

# Normalize the RFM data (Recency, Frequency, Monetary)
print("Normalizing RFM data...")
scaler = MinMaxScaler()
rfm_normalized = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])
rfm_normalized = pd.DataFrame(rfm_normalized, columns=['Recency', 'Frequency', 'Monetary'])

# Determine the optimal number of clusters using the elbow method
print("Determining the optimal number of clusters...")
inertia = []
for k in range(1, 11):  # Test cluster sizes from 1 to 10
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_normalized)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

# Perform K-Means clustering with chosen number of clusters (e.g., 4)
n_clusters = 4  # Adjust this based on the elbow plot
print(f"Clustering data into {n_clusters} clusters...")
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_normalized)

# Save the results
print(f"Saving clustered data to {output_file}...")
rfm.to_csv(output_file, index=False)
print("Clustered data has been saved successfully!")

# Display first rows of clustered data
print("\nFirst rows of the clustered RFM data:")
print(rfm.head())