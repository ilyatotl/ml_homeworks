import pickle
import streamlit as st
import pandas as pd
import numpy as np

st.title("Домашнее задание 1")

with open('ridge.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


year = int(st.selectbox('year of car', [i for i in range(1900, 2027)]))

km_driven_raw = st.text_input("enter km_driver", "100000")
try:
    km_driven = int(km_driven_raw)
except ValueError:
    st.write(f"invalid km_driven type - it must be a number")


mileage_raw = st.text_input("enter mileage", "20.12")
try:
    mileage = float(mileage_raw)
except ValueError:
    st.write(f"invalid mileage type - it must be a number")


engine_raw = st.text_input("enter engine", "1248")
try:
    engine = int(engine_raw)
except ValueError:
    st.write(f"invalid engine type - it must be a number")


max_power_raw = st.text_input("enter max_power", "103.52")
try:
    max_power = float(max_power_raw)
except ValueError:
    st.write(f"invalid max_power type - it must be a number")


fuel = st.selectbox('fuel_type', ['Diesel', 'Petrol', 'LPG', 'CNG'])
seller_type = st.selectbox('seller_type', ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission = st.selectbox('transmission', ['Manual', 'Automatic'])
owner = st.selectbox('owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
seats = int(st.selectbox('seats', [ 5, 4, 7, 8, 6, 9, 10, 14, 2]))

if st.button('Предсказать стоимость машины'):
    df = pd.DataFrame(
        {
            'year': [year], 
            'km_driven': [km_driven],
            'mileage': [mileage],
            'engine': [engine],
            'max_power': [max_power],
            'seats_4': [int(seats == 4)],
            'seats_5': [int(seats == 5)],
            'seats_6': [int(seats == 6)],
            'seats_7': [int(seats == 7)],
            'seats_8': [int(seats == 8)],
            'seats_9': [int(seats == 9)],
            'seats_10': [int(seats == 10)],
            'seats_14': [int(seats == 14)],
            'fuel_Diesel': [int(fuel == "Diesel")],
            'fuel_LPG': [int(fuel == "LPG")],
            'fuel_Petrol': [int(fuel == "Petrol")],
            'seller_type_Individual': [int(seller_type == "Individual")],
            'seller_type_Trustmark Dealer': [int(seller_type == "Trustmark Dealer")],
            'transmission_Manual': [int(transmission == "Manual")],
            'owner_Fourth & Above Owner': [int(owner == "Fourth & Above Owner")],
            'owner_Second Owner': [int(owner == "Second Owner")],
            'owner_Test Drive Car': [int(owner == "Test Drive Car")],
            'owner_Third Owner': [int(owner == 'Third Owner')]
        }
    )

    st.write(f"Предполагаемая стоимость машины: {loaded_model.predict(df)[0]:.2f}")