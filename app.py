import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from urllib.parse import quote_plus

st.set_page_config(layout="wide")
st.title("PhonePe Pulse Data Visualization")
st.write("Welcome to the PhonePe Pulse Data Visualization dashboard.")

password = "Utkarsh@17"
encoded_password = quote_plus(password)
engine = create_engine(f"mysql+mysqlconnector://root:{encoded_password}@localhost/phonepe_insights")

st.sidebar.header("Select Your Analysis")

year = st.sidebar.selectbox("Year", options=[2018, 2019, 2020, 2021, 2022, 2023, 2024])
quarter = st.sidebar.selectbox("Quarter", options=[1, 2, 3, 4])

choice = st.sidebar.selectbox(
    "Choose an Analysis",
    (
        "Top States by Transaction Amount",
        "Distribution of Transaction Types",
        "Transaction Trends Over Time",
        "Top States by Registered Users",
        "Device Dominance Analysis",
        "Top 10 Districts by Transaction Amount",
        "Top 10 States by App Opens",
        "Top 10 Pincodes by Registered Users",
        "Top 10 States by Insurance Policies"
    )
)

if choice == "Top States by Transaction Amount":
    st.header(f"Top 10 States by Transaction Amount for {year} - Q{quarter}")
    query = f"""
    SELECT location AS State, SUM(amount) AS Total_Transaction_Amount
    FROM aggregated_transaction
    WHERE year = {year} AND quarter = {quarter}
    GROUP BY location
    ORDER BY Total_Transaction_Amount DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    fig = px.bar(df, x='State', y='Total_Transaction_Amount', title=f'Top 10 States by Transaction Amount for {year} Q{quarter}', color='State')
    st.plotly_chart(fig, use_container_width=True)

elif choice == "Distribution of Transaction Types":
    st.header(f"Distribution of Transaction Types for {year} - Q{quarter}")
    query = f"""
    SELECT transaction_type, SUM(count) AS Total_Transactions
    FROM aggregated_transaction
    WHERE year = {year} AND quarter = {quarter}
    GROUP BY transaction_type
    ORDER BY Total_Transactions DESC;
    """
    df = pd.read_sql(query, engine)
    fig = px.pie(df, values='Total_Transactions', names='transaction_type', title=f'Distribution of Transaction Types for {year} Q{quarter}', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

elif choice == "Transaction Trends Over Time":
    st.header("Total Transaction Amount Over the Years")
    query = """
    SELECT year, SUM(amount) AS Total_Amount
    FROM aggregated_transaction
    GROUP BY year
    ORDER BY year;
    """
    df = pd.read_sql(query, engine)
    fig = px.line(df, x='year', y='Total_Amount', title='Total Transaction Amount Over the Years', markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif choice == "Top States by Registered Users":
    st.header(f"Top 10 States by Registered Users for {year} - Q{quarter}")
    query = f"""
    SELECT State, SUM(Registered_Users) as Total_Users
    FROM top_user_districts
    WHERE Year = {year} AND Quarter = {quarter}
    GROUP BY State
    ORDER BY Total_Users DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    fig = px.bar(df, x='State', y='Total_Users', title=f'Top 10 States by Registered Users for {year} Q{quarter}', color='State')
    st.plotly_chart(fig, use_container_width=True)

elif choice == "Device Dominance Analysis":
    st.header(f"Top 10 Device Brands by Registered Users for {year} - Q{quarter}")
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

elif choice == "Top 10 Districts by Transaction Amount":
    st.header(f"Top 10 Districts by Transaction Amount for {year} - Q{quarter}")
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

elif choice == "Top 10 States by App Opens":
    st.header(f"Top 10 States by App Opens for {year} - Q{quarter}")
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

elif choice == "Top 10 Pincodes by Registered Users":
    st.header(f"Top 10 Pincodes by Registered Users for {year} - Q{quarter}")
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

elif choice == "Top 10 States by Insurance Policies":
    st.header(f"Top 10 States by Insurance Policies Sold for {year} - Q{quarter}")
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