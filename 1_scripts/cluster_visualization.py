import pandas as pd
import matplotlib.pyplot as plt

# Absolute paths
input_file = 'C:/Users/Matias/Desktop/customer_segmentation/4_results/rfm_clusters.csv'
output_folder = 'C:/Users/Matias/Desktop/customer_segmentation/4_results/'

print("Loading clustered RFM data...")
# Load clustered data
rfm_clusters = pd.read_csv(input_file)
print("Clustered RFM data loaded successfully!")

# Define cluster names based on characteristics
cluster_names = {
    0: "Frequent High Spenders",      # High Frequency, High Monetary, Low Recency
    1: "Moderate Spenders",           # Moderate Frequency, Moderate Monetary, Higher Recency
    2: "Rare and Low Spenders",       # Low Frequency, Low Monetary, High Recency
    3: "Occasional Spenders",         # Moderate Frequency, Low-Moderate Monetary, Moderate Recency
}

# Add cluster names to the dataframe
rfm_clusters['Cluster_Name'] = rfm_clusters['Cluster'].map(cluster_names)

# Scatter plots for different combinations
print("Creating scatter plots...")

# Scatter: Recency vs Frequency
plt.figure(figsize=(8, 6))
for cluster, group in rfm_clusters.groupby('Cluster'):
    plt.scatter(group['Recency'], group['Frequency'], label=cluster_names[cluster], alpha=0.7)
plt.title('Recency vs Frequency by Cluster', fontsize=14)
plt.xlabel('Recency', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(True)
output_path_rf = f"{output_folder}scatter_recency_frequency.png"
plt.savefig(output_path_rf)
plt.show()
print(f"Scatter plot saved: {output_path_rf}")

# Scatter: Frequency vs Monetary
plt.figure(figsize=(8, 6))
for cluster, group in rfm_clusters.groupby('Cluster'):
    plt.scatter(group['Frequency'], group['Monetary'], label=cluster_names[cluster], alpha=0.7)
plt.title('Frequency vs Monetary by Cluster', fontsize=14)
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Monetary', fontsize=12)
plt.legend()
plt.grid(True)
output_path_fm = f"{output_folder}scatter_frequency_monetary.png"
plt.savefig(output_path_fm)
plt.show()
print(f"Scatter plot saved: {output_path_fm}")

# Scatter: Recency vs Monetary
plt.figure(figsize=(8, 6))
for cluster, group in rfm_clusters.groupby('Cluster'):
    plt.scatter(group['Recency'], group['Monetary'], label=cluster_names[cluster], alpha=0.7)
plt.title('Recency vs Monetary by Cluster', fontsize=14)
plt.xlabel('Recency', fontsize=12)
plt.ylabel('Monetary', fontsize=12)
plt.legend()
plt.grid(True)
output_path_rm = f"{output_folder}scatter_recency_monetary.png"
plt.savefig(output_path_rm)
plt.show()
print(f"Scatter plot saved: {output_path_rm}")

print("Cluster visualization with saved images completed!")