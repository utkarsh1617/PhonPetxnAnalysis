# Poject1-PhonePe Transaction Insights

PhonePe Transaction Insights
About The Project
This project involves the extraction, transformation, and visualization of the PhonePe Pulse dataset. The primary goal is to analyze the dynamics of transactions, user engagement, and insurance-related data from the PhonePe digital payments platform. By loading the data into a SQL database and building an interactive Streamlit dashboard, this project aims to uncover key insights into payment trends across India.


Key Features & Analyses Performed
This dashboard provides several interactive analyses that address key business use cases, including:


Geographical Insights: Understanding payment trends at state, district, and pincode levels for targeted marketing efforts.


Payment Performance: Evaluating the popularity and distribution of different payment categories to inform strategic investments.


Trend Analysis: Examining transaction trends over time to understand growth and anticipate demand fluctuations.


User Engagement: Monitoring user activity, including registered users and app opens, to develop strategies that enhance retention.


Device Dominance: Analyzing user preferences across different device brands to improve app performance and user experience.

How to Run This Project
To run this application on your local machine, please follow these steps:

Clone the Repository:
git clone <your-repository-link>

Navigate to the Project Directory:
cd <your-project-folder-name>

Install the Required Libraries:
pip install pandas mysql-connector-python SQLAlchemy plotly streamlit

Set Up the Database:

Ensure you have a MySQL server running.

Create a database named phonepe_insights.

Run the necessary scripts to create all tables and load the data.

Run the Streamlit App:
streamlit run app.py

Technical Skills
Languages & Tools: Python, SQL

Libraries: Streamlit, Pandas, Plotly, SQLAlchemy, MySQL Connector

Skills: ETL (Extract, Transform, Load), Data Visualization, Data Analysis





