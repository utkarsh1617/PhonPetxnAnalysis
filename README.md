# PhonePe Pulse Data Visualization and Analysis

## Project Overview

This project uses the PhonePe Pulse dataset to extract, transform, and visualize transaction and user data. The goal is to uncover meaningful patterns in digital payments across India. By loading the data into a MySQL database and building an interactive Streamlit dashboard, the project provides insights into geographical trends, payment types, user engagement, and more, addressing several key business case studies.

## Project Workflow

1.  **Data Extraction:** Cloned the PhonePe Pulse GitHub repository and wrote Python scripts to parse and extract data from nested JSON files across various categories (Aggregated, Map, and Top data).
2.  **Data Transformation:** Processed and cleaned the raw data, structuring it into multiple Pandas DataFrames aligned with the dataset's schema.
3.  **Database Engineering (ETL):** Set up a MySQL database named `phonepe_insights`, created a schema with tables for all data categories, and loaded the cleaned DataFrames into the SQL database using SQLAlchemy.
4.  **Data Analysis & Visualization:** Wrote SQL queries to aggregate and filter data to answer specific business questions. Used Plotly to create a variety of interactive visualizations, including bar charts, pie charts, and line charts.
5.  **Dashboard Development:** Built an interactive web application using Streamlit. The dashboard features a presentation-style layout with a sidebar containing dropdown menus for dynamic filtering by year, quarter, and analysis type. Each analysis page includes contextual information and a secondary "overall" chart for a broader perspective.

## Summary of Business Case Analyses

### 1. Device Dominance and User Engagement (Case Study #2)

* **Business Question:** Which device brands are most popular among PhonePe users?
* **Key Finding:** A few major brands, such as Xiaomi and Samsung, hold a significant majority of the user base. This indicates that app performance and user experience optimization should be prioritized for these specific device ecosystems.

### 2. User Engagement and Growth Strategy (Case Study #5)

* **Business Question:** Which states show the highest user engagement in terms of app opens?
* **Key Finding:** States with high transaction volumes also tend to have the highest number of app opens. This strong correlation suggests that engagement is a direct driver of business activity, making in-app promotions a valuable growth strategy.

### 3. Transaction Analysis Across States and Districts (Case Study #7)

* **Business Question:** Which districts are the top performers in terms of transaction value?
* **Key Finding:** Top-performing districts are almost exclusively located in major metropolitan areas like Bangalore and Mumbai. This highlights that digital payment adoption is heavily concentrated in urban centers, presenting an opportunity for targeted expansion into Tier-2 and Tier-3 cities.

### 4. User Registration Analysis (Case Study #8)

* **Business Question:** Which specific pincodes have the highest concentration of registered users?
* **Key Finding:** User registration is most concentrated in densely populated urban and semi-urban pincodes. This hyper-local data can be used to guide targeted marketing campaigns and agent network expansion for customer onboarding.

### 5. Insurance Transactions Analysis (Case Study #9)

* **Business Question:** Which states are leading in the adoption of PhonePe's insurance services?
* **Key Finding:** The leading states in insurance sales are often the same states that lead in overall transaction volume. This indicates that a mature and active user base is more likely to adopt new financial products, suggesting a strategy of cross-selling insurance services to highly engaged users in top-performing states.

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

To explore this project, clone the repository, set up the MySQL database with the required data, install the necessary libraries, and run the Streamlit application using the command `streamlit run app.py`.
