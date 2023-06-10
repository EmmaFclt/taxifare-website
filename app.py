import streamlit as st
import datetime
import requests

'''
# NY Taxi
'''

url = 'https://taxifare.lewagon.ai/predict'


d = st.date_input(
    "Pick-up Date",
    datetime.date(2023, 10, 6))
t = st.time_input('Pick-up time', datetime.time(8, 45))

pick_up_lat = st.number_input('Pick-up latitude')

pick_up_long = st.number_input('Pick-up longitude')

drop_off_lat = st.number_input('Drop-off latitude')

drop_off_long = st.number_input('Drop-off longitude')

passengers = st.slider('Number of passengers', 1, 8, 1)

p_datetime = datetime.datetime.combine(d, t)

params = {
    'pickup_datetime': p_datetime,
    'pickup_longitude':pick_up_long,
    'pickup_latitude':pick_up_lat,
    'dropoff_longitude':drop_off_long,
    'dropoff_latitude':drop_off_lat,
    'passenger_count':passengers
}

response = requests.get(
    url,
    params=params,
).json()
"Price :"
st.text(round(response['fare'],2))
