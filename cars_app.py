import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import plotly.express as pl
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache(allow_output_mutation=True)
def load(data_path, model_path):
    data = pickle.load(open(data_path, 'rb'))
    model = pickle.load(open(model_path, 'rb'))
    return data, model

def inference(new_case, model):
    feat_cols = ['manufacturer_name', 'model_name', 'transmission', 'color',
       'engine_fuel', 'engine_has_gas', 'engine_type', 'body_type',
       'has_warranty', 'state', 'drivetrain', 'year_produced','odometer_value']
    case_to_predict = pd.DataFrame([new_case], columns = feat_cols)
    categoricals = ['manufacturer_name', 'model_name', 'transmission', 'color',
       'engine_fuel', 'engine_has_gas', 'engine_type', 'body_type',
       'has_warranty', 'state', 'drivetrain']
    for feature in categoricals:
        case_to_predict[feature] = pd.Series(case_to_predict[feature], dtype="category")
    price = round(model.predict(case_to_predict)[0], 2)
    answer = 'The predicted price is ' + str(price) + ' $.'
    return answer

st.title('Car Price Prediction App')


# image = Image.open("photo.jpeg")
image = Image.open("/Users/vasiliskalyvas/Documents/GitHub/streamlit/photo.jpeg")
st.image(image, use_column_width=True)

st.write('Please fill in the details of the car in the left sidebar and click on the button below!')

# data, model = load("dataset.pickle", "model.pickle")
data, model = load("/Users/vasiliskalyvas/Documents/GitHub/streamlit/dataset.pickle", "/Users/vasiliskalyvas/Documents/GitHub/streamlit/model.pickle")


manufacturers = data['manufacturer_name'].unique().tolist()
models = data.groupby('manufacturer_name')['model_name'].unique().apply(list).to_dict()
transmission_type = data['transmission'].unique().tolist()
colors = data['color'].unique().tolist()
fuels = data['engine_fuel'].unique().tolist()
engine_types = data['engine_type'].unique().tolist()
body_types = data['body_type'].unique().tolist()
states = data['state'].unique().tolist()
drivetrains = data['drivetrain'].unique().tolist()

manufacturer_name = st.sidebar.selectbox("Manufacturer", manufacturers)
model_name = st.sidebar.selectbox("Model", models[manufacturer_name])
transmission = st.sidebar.selectbox("Type of transmission", transmission_type)
color =  st.sidebar.selectbox("Color", colors)
engine_fuel =  st.sidebar.selectbox("Engine fuel", fuels)
engine_type = st.sidebar.selectbox("Engine Type", engine_types)
body_type = st.sidebar.selectbox("Body Type", body_types)
state = st.sidebar.selectbox("State", states)
drivetrains = st.sidebar.selectbox("Drivetrain", drivetrains)
engine_has_gas = st.sidebar.radio("Engine has gas", [True, False])
warranty = st.sidebar.radio("Warranty", [True, False])
year_produced = st.sidebar.slider('Year Produced', 1950, 2019, 2015, 1)
odometer_value = st.sidebar.slider("Odometer value", 0, 1000000, 1000, 100)

# construct the new case for prediction
new_case = [manufacturer_name, model_name, transmission, color, engine_fuel, engine_has_gas, engine_type, body_type, warranty, state, drivetrains, year_produced, odometer_value]


#### Prediction and Boxplots
if (st.button('Find Car Price')):
    
    ## A: Read the data, load the model, make the prediction and print it
    result = inference(new_case, model)
    st.write(result)
    st.write('----------------------------------------------------------------------------------------------------------------')
    
    ## B: Boxplots
    st.write('See the price ranges per Manufacturer and Engine fuel:')
    fig = go.Figure()
    dropdown = []
    true_false = [False]*55
    cars = sorted(data['manufacturer_name'].unique())
    default = manufacturer_name
    
    for i, company in enumerate(cars):
        temp = data[data['manufacturer_name']==company][['engine_fuel','price_usd']]
        fig.add_trace(go.Box(x=temp['engine_fuel'], y=temp['price_usd'], name=company, visible=(company==default)))
        true_false2 = true_false.copy()
        true_false2[i] = True
        dropdown.append({'method':'update',
                          'label':company,
                          'args': [{"visible": true_false2}, 
                                  {"title": company}]
                        })
    
    updatemenus = [{'buttons':dropdown,
                    'direction':'down',
                    'showactive':False,
                    'active': cars.index(default)}]
    fig.update_layout(updatemenus=updatemenus, showlegend=True)
    st.plotly_chart(fig)
