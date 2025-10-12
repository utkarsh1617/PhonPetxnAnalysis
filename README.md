# PhonePe Pulse Data Visualization and Analysis

## Project Overview

This project uses the PhonePe Pulse dataset to extract, transform, and visualize transaction and user data. The goal is to uncover meaningful patterns in digital payments across India. By loading the data into a MySQL database and building an interactive Streamlit dashboard, the project provides insights into geographical trends, payment types, user engagement, and more, addressing several key business case studies.

## Project Workflow

1.  **Data Extraction:** Cloned the PhonePe Pulse GitHub repository and wrote Python scripts to parse and extract data from nested JSON files across various categories (Aggregated, Map, and Top data).
2.  **Data Transformation:** Processed and cleaned the raw data, structuring it into multiple Pandas DataFrames aligned with the dataset's schema.
3.  **Database Engineering (ETL):** Set up a MySQL database named `phonepe_insights`, created a schema with tables for all data categories, and loaded the cleaned DataFrames into the SQL database using SQLAlchemy.
4.  **Data Analysis & Visualization:** Wrote SQL queries to aggregate and filter data to answer specific business questions. Used Plotly to create a variety of interactive visualizations, including bar charts, pie charts, and line charts.
5.  **Dashboard Development:** Built an interactive web application using Streamlit. The dashboard features a presentation-style layout with a sidebar containing dropdown menus for dynamic filtering by year, quarter, and analysis type. Each analysis page includes contextual information and a secondary "overall" chart for a broader perspective.

## Key Findings

The analysis successfully answers several key business questions, revealing the following insights:

* **Geographical Concentration:** Digital payment activity is heavily concentrated in a few economically larger states (e.g., Maharashtra, Karnataka) and major metropolitan districts (e.g., Bangalore, Mumbai), highlighting urban centers as the primary drivers of transaction volume.
* **Dominance of P2P Payments:** Peer-to-peer (P2P) payments are the most frequent transaction type, indicating that personal fund transfers are the primary use case for the majority of users.
* **User Engagement as a Growth Driver:** States with high user engagement, measured by app opens, show a strong correlation with high transaction volumes, suggesting that in-app features and promotions are key to driving business growth.
* **Hyper-Local User Density:** User registration is most concentrated in densely populated urban and semi-urban pincodes, providing a granular view for guiding targeted marketing and customer onboarding campaigns.

## Technologies Used

* Python
* SQL (MySQL)
* Pandas
* Streamlit
* Plotly
* SQLAlchemy
* Git & GitHub

## Repository Contents

* `app.py`: The complete Python script for the final, presentation-style Streamlit dashboard.
* `README.md`: This documentation file explaining the project.
* `.gitignore`: Specifies which files and folders for Git to ignore.

## How to Use

To explore this project, clone the repository, set up the MySQL database with the required data, install the necessary libraries, and run the Streamlit application using the command `streamlit run app.py`. The interactive dashboard serves as a live presentation of the project's findings.
