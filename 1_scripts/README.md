## Scripts Overview
This folder contains the Python scripts used in the customer segmentation project. Each script performs a specific task in the workflow. Below is a description of each script and how to run it.

**load_and_convert.py**
This script loads the original dataset (online_retail.xlsx), preprocesses it, and saves it as a CSV file for further use.

**customer_segmentation.py**
This script calculates RFM (Recency, Frequency, Monetary) values for each customer and saves the results to a CSV file.

**rfm_clustering.py**
This script performs clustering on the RFM data using the K-Means algorithm and saves the clustered data.

**cluster_visualization.py**
This script visualizes the clustered data and generates scatter plot images.

**run_pipeline.py**
This script automates the entire workflow by executing all the scripts in the correct order.
Run the script using the command:
`python 1_scripts/run_pipeline.py`

Before running any scripts, ensure you have installed the required libraries in your virtual environment. Activate the environment and install dependencies using the **requirements.txt** file.

### Outputs
Preprocessed data is saved in the 2_data folder.
RFM values are saved in the 3_cleaned_data folder.
Clustering results and visualizations are saved in the 4_results folder.