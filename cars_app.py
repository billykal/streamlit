import streamlit as st
import joblib
import pandas as pd
from PIL import Image
import numpy as np
import plotly_express as pl

@st.cache(allow_output_mutation=True)
def load(model_path, loe_path, ohe_path):
    model = joblib.load(model_path)
    loe = joblib.load(loe_path)
    ohe = joblib.load(ohe_path)
    return model, loe, ohe

def inference(row, loe, ohe, model, feat_cols):
    df = pd.DataFrame([row], columns = feat_cols)
    df_loe = df[['manufacturer_name','color','body_type']]
    df_loe = loe.transform(df_loe)
    df_loe = pd.DataFrame(df_loe)
    df_ohe = df[['transmission','engine_fuel','engine_has_gas','engine_type','has_warranty','state','drivetrain']]
    df_ohe = ohe.transform(df_ohe)
    df_ohe = pd.DataFrame(df_ohe, columns=ohe.get_feature_names())
    df_test = df_loe.join(df_ohe).join(df[['odometer_value','year_produced']])
    price = model.predict(df_test)
    answer = 'The predicted price is ' + str(price)
    return answer

st.title('Car Price Prediction App')
#st.write('The data for the following example is originally from the National Institute of Diabetes and Digestive and Kidney Diseases and contains information on females at least 21 years old of Pima Indian heritage. This is a sample application and cannot be used as a substitute for real medical advice.')
image = Image.open("photo.jpeg")
st.image(image, use_column_width=True)
st.write('Please fill in the details of the car in the left sidebar and click on the button below!')

cars = ['Ford', 'Dodge', 'Mazda', 'Audi', 'Volkswagen', 'Opel', 'Volvo',
       'Peugeot', 'Renault', 'Honda', 'Toyota', 'Mercedes-Benz',
       'Citroen', 'Hyundai', 'ВАЗ', 'Skoda', 'BMW', 'Kia', 'Fiat',
       'Chrysler', 'Mitsubishi', 'Rover', 'Chevrolet', 'Nissan', 'Lifan',
       'LADA', 'Jaguar', 'УАЗ', 'Seat', 'Buick', 'Land Rover', 'Porsche',
       'Suzuki', 'Alfa Romeo', 'Daewoo', 'Mini', 'Subaru', 'Lexus',
       'Saab', 'ГАЗ', 'Lancia', 'Pontiac', 'Geely', 'Acura', 'Jeep',
       'Chery', 'Infiniti', 'SsangYong', 'Dacia', 'ЗАЗ', 'Great Wall',
       'Lincoln', 'Cadillac', 'Iveco', 'Москвич']
transmission_type = ['mechanical', 'automatic']
colors = ['blue', 'silver', 'other', 'black', 'grey', 'red', 'white',
       'violet', 'green', 'brown', 'orange', 'yellow']
fuels = ['gasoline', 'diesel', 'gas', 'hybrid-petrol', 'hybrid-diesel']
engine_types = ['gasoline', 'diesel']
body_types = ['hatchback', 'minivan', 'universal', 'sedan', 'van', 'suv',
       'pickup', 'liftback', 'minibus', 'coupe', 'cabriolet', 'limousine']
states = ['owned', 'emergency', 'new']
drivetrains = ['front', 'rear', 'all']

manufacturer_name = st.sidebar.selectbox("Manufacturer", cars)
color =  st.sidebar.selectbox("Color", colors)
body_type = st.sidebar.selectbox("Body Type", body_types)
transmission = st.sidebar.selectbox("Type of transmission", transmission_type)
engine_fuel =  st.sidebar.selectbox("Engine fuel", fuels)
engine_has_gas = st.sidebar.selectbox("Engine has gas", [True, False])
engine_type = st.sidebar.selectbox("Engine Type", engine_types)
warranty = st.sidebar.selectbox("Warranty", [True, False])
state = st.sidebar.selectbox("State", states)
drivetrains = st.sidebar.selectbox("Drivetrain", drivetrains)
odometer_value = st.sidebar.slider("Odometer value", 0, 1000000, 1000, 100)
year_produced = st.sidebar.slider('Year Produced', 1950, 2019, 2015, 1)

row = [manufacturer_name, color, body_type, transmission, engine_fuel, engine_has_gas, engine_type, warranty, state, drivetrains, odometer_value, year_produced]

if (st.button('Find Car Price')):
    feat_cols = ['manufacturer_name','color','body_type','transmission','engine_fuel','engine_has_gas','engine_type','has_warranty','state','drivetrain','odometer_value','year_produced']
    
    model, loe, ohe = load("ranfor.joblib", "loe.joblib", "ohe.joblib")
    result = inference(row, loe, ohe, model, feat_cols)
    st.write(result)