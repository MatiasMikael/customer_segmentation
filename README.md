## customer_segmentation
### Overview
This project segments customers based on purchasing behavior using RFM analysis and K-Means clustering. Insights are visualized with scatter plots, helping to identify tailored strategies for each segment.

### Tools Used
Python (Pandas, Matplotlib, Scikit-learn)
### Workflow
* Preprocessing: Cleaned online_retail.xlsx and saved as online_retail.csv.
* RFM Analysis: Calculated Recency, Frequency, and Monetary metrics, saved to rfm_data.csv.
* Clustering: Applied K-Means to segment customers, saved to rfm_clusters.csv.
* Visualization: Created scatter plots, saved as PNG files.
* Automation: Run all steps with run_pipeline.py.
### How to Run
* Clone the repository.
* Install dependencies.
* Execute the pipeline:
`python 1_scripts/run_pipeline.py`
* Results are saved in the 4_results folder.

### License
This project is licensed under the MIT License.

Data License:
This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

Data Source:
Chen, D. (2015). Online Retail, UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33.
