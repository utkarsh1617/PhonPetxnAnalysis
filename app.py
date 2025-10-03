import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from urllib.parse import quote_plus

st.set_page_config(layout="wide")
st.title("PhonePe Pulse: A Data-Driven Presentation")
st.write("An interactive dashboard presenting key findings and business insights from the PhonePe dataset.")

password = "Utkarsh@17"
encoded_password = quote_plus(password)
engine = create_engine(f"mysql+mysqlconnector://root:{encoded_password}@localhost/phonepe_insights")

st.sidebar.header("Select a Business Case")
year = st.sidebar.selectbox("Select Year", options=[2022, 2021, 2020, 2019, 2018])
quarter = st.sidebar.selectbox("Select Quarter", options=[1, 2, 3, 4])

choice = st.sidebar.selectbox(
    "Choose an Analysis",
    (
        "Device Dominance & User Engagement",
        "User Engagement & Growth Strategy",
        "Top Districts by Transaction Value",
        "Top Pincodes by User Registration",
        "Top States by Insurance Adoption"
    )
)

col1, col2 = st.columns([1, 2])

if choice == "Device Dominance & User Engagement":
    with col1:
        st.subheader("Business Question")
        st.write("Which device brands are most popular among PhonePe users?")
        st.subheader("Key Finding")
        st.write("A few major brands like Xiaomi and Samsung dominate the user base, indicating that app optimization should be prioritized for these device ecosystems.")

        st.subheader("Overall Analysis")
        overall_query = """
        SELECT device_brand, SUM(registered_users) AS Total_Users
        FROM aggregated_user
        GROUP BY device_brand
        ORDER BY Total_Users DESC
        LIMIT 5;
        """
        overall_df = pd.read_sql(overall_query, engine)
        fig_overall = px.bar(overall_df, x='Total_Users', y='device_brand', orientation='h', title='Top 5 Device Brands (All Years)')
        st.plotly_chart(fig_overall, use_container_width=True)

    with col2:
        st.header(f"Device Dominance in {year} Q{quarter}")
        query = f"""
        SELECT device_brand, SUM(registered_users) AS Total_Users
        FROM aggregated_user
        WHERE year = {year} AND quarter = {quarter}
        GROUP BY device_brand
        ORDER BY Total_Users DESC
        LIMIT 10;
        """
        df = pd.read_sql(query, engine)
        fig = px.bar(df, x='device_brand', y='Total_Users', title=f'Top 10 Device Brands for {year} Q{quarter}')
        st.plotly_chart(fig, use_container_width=True)

elif choice == "User Engagement & Growth Strategy":
    with col1:
        st.subheader("Business Question")
        st.write("Which states show the highest user engagement in terms of app opens?")
        st.subheader("Key Finding")
        st.write("High engagement (app opens) strongly correlates with high transaction volume, making in-app promotions a key growth strategy.")

        st.subheader("Overall Analysis")
        overall_query = """
        SELECT State, SUM(App_Opens) AS Total_App_Opens
        FROM map_user
        GROUP BY State
        ORDER BY Total_App_Opens DESC
        LIMIT 5;
        """
        overall_df = pd.read_sql(overall_query, engine)
        fig_overall = px.bar(overall_df, x='Total_App_Opens', y='State', orientation='h', title='Top 5 States by App Opens (All Years)')
        st.plotly_chart(fig_overall, use_container_width=True)

    with col2:
        st.header(f"User Engagement by App Opens in {year} Q{quarter}")
        query = f"""
        SELECT State, SUM(App_Opens) AS Total_App_Opens
        FROM map_user
        WHERE Year = {year} AND Quarter = {quarter}
        GROUP BY State
        ORDER BY Total_App_Opens DESC
        LIMIT 10;
        """
        df = pd.read_sql(query, engine)
        fig = px.bar(df, x='State', y='Total_App_Opens', title=f'Top 10 States by App Opens for {year} Q{quarter}', color='State')
        st.plotly_chart(fig, use_container_width=True)

elif choice == "Top Districts by Transaction Value":
    with col1:
        st.subheader("Business Question")
        st.write("Which districts are the top performers in terms of transaction value?")
        st.subheader("Key Finding")
        st.write("Top-performing districts are almost exclusively in major metropolitan areas, highlighting that digital payment adoption is heavily concentrated in urban centers.")

        st.subheader("Overall Analysis")
        overall_query = """
        SELECT District, SUM(Transaction_Amount) as Total_Amount
        FROM top_transaction_districts
        GROUP BY District
        ORDER BY Total_Amount DESC
        LIMIT 5;
        """
        overall_df = pd.read_sql(overall_query, engine)
        fig_overall = px.bar(overall_df, x='Total_Amount', y='District', orientation='h', title='Top 5 Districts by Transaction Value (All Years)')
        st.plotly_chart(fig_overall, use_container_width=True)

    with col2:
        st.header(f"Top Districts by Transaction Amount in {year} Q{quarter}")
        query = f"""
        SELECT District, SUM(Transaction_Amount) as Total_Amount
        FROM top_transaction_districts
        WHERE Year = {year} AND Quarter = {quarter}
        GROUP BY District
        ORDER BY Total_Amount DESC
        LIMIT 10;
        """
        df = pd.read_sql(query, engine)
        fig = px.bar(df, x='District', y='Total_Amount', title=f'Top 10 Districts for {year} Q{quarter}', color='District')
        st.plotly_chart(fig, use_container_width=True)

elif choice == "Top Pincodes by User Registration":
    with col1:
        st.subheader("Business Question")
        st.write("Which specific pincodes have the highest concentration of registered users?")
        st.subheader("Key Finding")
        st.write("User registration is most concentrated in densely populated urban and semi-urban pincodes, providing hyper-local data to guide targeted marketing campaigns.")

        st.subheader("Overall Analysis")
        overall_query = """
        SELECT Pincode, SUM(Registered_Users) AS Total_Registered_Users
        FROM top_user_pincodes
        GROUP BY Pincode
        ORDER BY Total_Registered_Users DESC
        LIMIT 5;
        """
        overall_df = pd.read_sql(overall_query, engine)
        fig_overall = px.bar(overall_df, x='Total_Registered_Users', y='Pincode', orientation='h', title='Top 5 Pincodes by Registered Users (All Years)')
        st.plotly_chart(fig_overall, use_container_width=True)

    with col2:
        st.header(f"Top Pincodes by Registered Users in {year} Q{quarter}")
        query = f"""
        SELECT Pincode, SUM(Registered_Users) AS Total_Registered_Users
        FROM top_user_pincodes
        WHERE Year = {year} AND Quarter = {quarter}
        GROUP BY Pincode
        ORDER BY Total_Registered_Users DESC
        LIMIT 10;
        """
        df = pd.read_sql(query, engine)
        fig = px.bar(df, x='Pincode', y='Total_Registered_Users', title=f'Top 10 Pincodes by Registered Users for {year} Q{quarter}')
        st.plotly_chart(fig, use_container_width=True)

elif choice == "Top States by Insurance Adoption":
    with col1:
        st.subheader("Business Question")
        st.write("Which states are leading in the adoption of PhonePe's insurance services?")
        st.subheader("Key Finding")
        st.write("Leading states in insurance sales are often the same ones that lead in overall transaction volume, suggesting a strategy of cross-selling new financial products to a mature user base.")

        st.subheader("Overall Analysis")
        trend_query = """
        SELECT year, SUM(Insurance_Count) AS Total_Policies
        FROM map_insurance
        GROUP BY year
        ORDER BY year;
        """
        trend_df = pd.read_sql(trend_query, engine)
        fig_trend = px.line(trend_df, x='year', y='Total_Policies', title='Overall Trend: Insurance Policies Sold Over Years', markers=True)
        st.plotly_chart(fig_trend, use_container_width=True)

    with col2:
        st.header(f"Top States by Insurance Policies Sold in {year} Q{quarter}")
        query = f"""
        SELECT State, SUM(Insurance_Count) AS Total_Policies
        FROM map_insurance
        WHERE Year = {year} AND Quarter = {quarter}
        GROUP BY State
        ORDER BY Total_Policies DESC
        LIMIT 10;
        """
        df = pd.read_sql(query, engine)
        fig = px.bar(df, x='State', y='Total_Policies', title=f'Top 10 States by Insurance Policies for {year} Q{quarter}', color='State')
        st.plotly_chart(fig, use_container_width=True)

