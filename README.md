# Poject1-PhonePe Transaction Insights

About The Project

This project involves the extraction, transformation, and visualization of the PhonePe Pulse dataset. The primary goal is to analyze the dynamics of transactions, user engagement, and insurance-related data from the PhonePe digital payments platform. By loading the data into a SQL database and building an interactive Streamlit dashboard, this project aims to uncover key insights into payment trends across India.

Key Features & Analyses Performed
The interactive dashboard allows for real-time data exploration with filters for Year and Quarter. It includes the following detailed analyses:

Geographical analysis of payment trends.

Evaluation of popular payment categories.

Trend analysis of transactions over time.

User engagement and device dominance insights.

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

Create a database named phonepe_insights and execute the necessary scripts to create all tables and load the data.

Run the Streamlit App:
streamlit run app.py

Summary of Business Case Analyses
1. Device Dominance and User Engagement (Case Study #2)
Business Question: Which device brands are most popular among PhonePe users?

Analysis Performed: The total number of registered users was calculated for each mobile device brand and the top 10 were visualized.

Key Finding: The analysis shows that a few major brands, such as Xiaomi, Samsung, and Vivo, hold a significant majority of the user base. This indicates that app performance and user experience optimization should be prioritized for these specific device ecosystems.

2. User Engagement and Growth Strategy (Case Study #5)
Business Question: Which states show the highest user engagement in terms of app opens?

Analysis Performed: The total number of app opens was aggregated for each state to identify the top 10 most active regions.

Key Finding: States with high transaction volumes also tend to have the highest number of app opens. This strong correlation suggests that high engagement is a direct driver of transaction activity, making app-based promotions and features a key strategy for growth.

3. Transaction Analysis Across States and Districts (Case Study #7)
Business Question: Which districts are the top performers in terms of transaction value?

Analysis Performed: The total transaction amount was calculated for each district in India, and the top 10 were identified and plotted.

Key Finding: Top-performing districts are almost exclusively located in major metropolitan areas like Bangalore, Mumbai, and Delhi. This highlights that digital payment adoption is heavily concentrated in urban centers, presenting an opportunity for targeted expansion into Tier-2 and Tier-3 cities.

4. User Registration Analysis (Case Study #8)
Business Question: Which specific pincodes have the highest concentration of registered users?

Analysis Performed: User registration data was aggregated by pincode to identify the top 10 pincodes with the most registered users.

Key Finding: The analysis reveals that user registration is most concentrated in densely populated urban and semi-urban pincodes. This hyper-local data can be used to guide targeted marketing campaigns and agent network expansion for customer onboarding.

5. Insurance Transactions Analysis (Case Study #9)
Business Question: Which states are leading in the adoption of PhonePe's insurance services?

Analysis Performed: The total number of insurance policies sold was calculated for each state, and the top 10 states were visualized.

Key Finding: The leading states in insurance sales are often the same states that lead in overall transaction volume. This indicates that a mature and active user base is more likely to adopt new financial products, suggesting a strategy of cross-selling insurance services to highly engaged users in top-performing states.

Technical Skills
Languages & Tools: Python, SQL

Libraries: Streamlit, Pandas, Plotly, SQLAlchemy, MySQL Connector

Skills: ETL (Extract, Transform, Load), Data Visualization, Data Analysis






