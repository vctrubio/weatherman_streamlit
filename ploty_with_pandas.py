import pandas as pd
import psycopg2
import plotly.express as px
import streamlit as st
import numpy as np


'''
Streamlit is used to display data fast
pandas is used to extract that data
plotly is used to plot that data
'''

color_dict = {
    'Tarifa': 'salmon',
    'Lisboa': 'dodgerblue',
    'Madrid': 'ivory',
    'Jarandilla de la vera': 'green',
    'Barcelona': 'purple'
    # Add more locations and colors as needed
}


def plot(location_ptr):
    data_by_days = []
    length = len(location_ptr)
    for i in range(length):
        print('debug_: ', i)
        for location in location_ptr[i]:
            for _ in location:
                for day in location['days']:
                    scatter_data = {
                        'date': pd.to_datetime(day['datetime']),
                        # (°F − 32) × 5/9
                        'temp': int((day['feelslike'] - 32) * 5/9),
                        'rain': day['precip'],
                        'location': location['address'].split(',')[0]
                    }
                    data_by_days.append(scatter_data)
                    # print('debug_: ', scatter_data['location'], ' : ' ,scatter_data['date'])

    df = pd.DataFrame(data_by_days)
    
    print(df.to_string())

    max_date = df['date'].max()
    min_date = df['date'].min()

    # Create a date range selector for date selection
    selected_date_range = st.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # Convert date range values to Timestamp objects
    start_date = pd.Timestamp(selected_date_range[0])
    end_date = pd.Timestamp(selected_date_range[1])

    # Filter the DataFrame based on the selected date range
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    # st.write(
    #     f'Selected Date Range: {start_date.strftime("%d-%m-%Y")} to {end_date.strftime("%d-%m-%Y")}')

    fig = px.scatter(filtered_df, x='date', y='temp', color='location',
                     color_discrete_map=color_dict)  # size='rain
    st.plotly_chart(fig)

    return
#TODO ADD range, of min and max. (like an error bar)
# https://plotly.com/python/line-and-scatter/


def get_data():
    conn = psycopg2.connect(
        "dbname=weatherman user=client password=password host=localhost port=5432")
    query = 'select * from days'
    df_days = pd.read_sql(query, conn)
    query = 'select * from locations'
    df_location = pd.read_sql(query, conn)
    conn.close()
    return df_days, df_location


def plot_streamlit():
    conn = psycopg2.connect(
        "dbname=weatherman user=client password=password host=localhost port=5432")
    query = 'select * from days'
    df_days = pd.read_sql(query, conn)
    query = 'select * from locations'
    df_location = pd.read_sql(query, conn)

    # Streamlit
    st.title("Streamlit with PostgreSQL Example")
    st.data_editor(df_days)
    st.data_editor(df_location)

    conn.close()


'''
X = location
Y = categories we pick - total rainfall, or temp, min, max mean
For selected date I guess, filter by slide

# To SHOW
# LOCATION with 
    #TOTAL precip
    #average feelslike

#filter/slide by datetime. 
'''
