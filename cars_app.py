import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import plotly as pl
import plotly.graph_objs as go

@st.cache(allow_output_mutation=True)
def load(data_path, model_path):
    data = pickle.load(open(data_path, 'rb'))
    model = pickle.load(open(model_path, 'rb'))
    # explainer = pickle.load(open(explainer_path, 'rb'))
    return data, model #, explainer

def inference(new_case, model, feat_cols):
    case_to_predict = pd.DataFrame([new_case]) #, columns = feat_cols)
    categoricals = ['manufacturer_name', 'model_name', 'transmission', 'color',
       'engine_fuel', 'engine_has_gas', 'engine_type', 'body_type',
       'has_warranty', 'state', 'drivetrain']
    for feature in categoricals:
        case_to_predict[feature] = pd.Series(case_to_predict[feature], dtype="category")
    price = round(model.predict(case_to_predict)[0], 2)
    answer = 'The predicted price is ' + str(price) + ' $.'
    return answer

st.title('Car Price Prediction App')
image = Image.open("photo.jpeg")
st.image(image, use_column_width=True)

st.write('Please fill in the details of the car in the left sidebar and click on the button below!')

manufacturers = ['Ford', 'Dodge', 'Mazda', 'Audi', 'Volkswagen', 'Opel', 'Volvo',
       'Peugeot', 'Renault', 'Honda', 'Toyota', 'Mercedes-Benz',
       'Citroen', 'Hyundai', 'ВАЗ', 'Skoda', 'BMW', 'Kia', 'Fiat',
       'Chrysler', 'Mitsubishi', 'Rover', 'Chevrolet', 'Nissan', 'Lifan',
       'LADA', 'Jaguar', 'УАЗ', 'Seat', 'Buick', 'Land Rover', 'Porsche',
       'Suzuki', 'Alfa Romeo', 'Daewoo', 'Mini', 'Subaru', 'Lexus',
       'Saab', 'ГАЗ', 'Lancia', 'Pontiac', 'Geely', 'Acura', 'Jeep',
       'Chery', 'Infiniti', 'SsangYong', 'Dacia', 'ЗАЗ', 'Great Wall',
       'Lincoln', 'Cadillac', 'Iveco', 'Москвич']
models = ['Fusion', 'Caravan', 'Galaxy', '6', '80', 'T5 Multivan', 'Astra', 'Sierra', 'S40', 'Partner', 'Golf', 'Megane Scenic', 'CR-V', 'Escort', 'Mondeo', 'Caddy', 'Yaris', 'Vectra', 'CLA200', '626', 'S300', 'C200', 'Megane', 'V60', 'C5', 'Pony', '406', 'Laguna', 'Logan', '21214', 'Octavia', '750', 'S70', 'Rio', 'A4', '525', 'T4 Caravelle', 'Vivaro', 'A6', 'Ulysse', 'Grande Punto', '530', 'Fabia', 'Passat', 'Pacifica', 'Scenic', 'Lantra', 'Polo', 'Camry', 'T4', 'Sorento', 'Civic', '320', 'B-Max', 'Accord', 'E200', 'Space Star', 'Sephia', 'Q7', "Cee'd", 'E300', 'Rapid', 'Highlander', 'Z4', 'Lancer', 'Galant', 'Agila', '440', 'Marea', 'Focus', 'Element', 'Zafira', 'Clio', 'Joice', '400-Series', 'Jetta', 'Tempra', 'X5', 'Land Cruiser', 'Voyager', 'Aveo', 'Carens', 'Superb', '207', 'Maxima', 'Insignia', 'C63AMG', 'Palio', 'S-Max', 'X50', '528', '318', 'Trafic', 'A8', 'E2200', 'X6', 'A150', 'Calibra', 'Granta', 'XKR', 'X5 M', 'Grand Scenic', '39099', 'Toledo', '2109', 'Encore', 'Nemo', 'Range Rover Sport', 'T1', 'Transit', 'Grand Voyager', '2107', 'Expert', 'Brava', 'Corsa', 'Xantia', 'Pathfinder', 'Sportage', 'XM', 'Insight', 'Carina E', 'CLK320', 'Panamera', 'Master', 'Bravo', '600-Series', 'A3', 'Fiesta', 'Cerato', 'C180', 'Felicia', 'Pajero', 'Kuga', 'Baleno', 'Xsara', 'MPV', 'i30', '206', 'Primera', 'Ka', 'S80', 'Mustang', 'Teana', 'Sienna', '156', 'Bora', 'Kodiaq', 'Safrane', 'T5', 'S560', 'Omega', '307', 'Armada', '323', '520', '405', 'Q5', 'Matiz', 'C230', 'Santa Fe', 'Cruze', 'One', 'Alhambra', 'Punto', '635', 'Touareg', 'C-Max', 'Avensis', 'Note', 'Impreza', 'Micra', 'E280', 'CLK200', 'Elantra', 'Escape', 'Roomster', 'Patrol', '100', 'Grand Vitara', 'CX-7', 'Scorpio', 'Polo Sedan', 'Terrano', 'C4 Grand Picasso', 'Legacy', '524', 'Solaris', 'RX', 'Sonata', 'LT', 'Golf Plus', '3', 'Colt', 'XC60', '9000', 'S6', 'Vito', 'S320', 'Sprinter', '850', 'Stratus', '31029', 'Delta', 'XC90', 'GL450', 'G6', 'Stilo', 'Espace', 'A5', 'Xedos 6', 'C3', '605', 'Signum', '208', 'Prelude', 'Carnival', 'Orion', '5008', 'Viano', '308', 'C-ELYSÉE', 'B180', 'Touran', 'RS6', 'Corolla', 'Qashqai', 'Tacuma', 'Emgrand', 'Sharan', 'Tiguan', '735', '118', '316', 'Tiburon', '460', 'Jumper', 'Kangoo', 'GL550', '328', '730', 'RL', 'ML320', 'Nubira', '200-Series', 'Grand Espace', '106', 'RAV4', 'Vario', 'Outlander', 'E220', 'Clarus', 'Carisma', 'Niva', '31514', 'Juke', 'Cayenne', '745', 'X60', 'E350', 'i40', 'A160', 'Sebring', 'Lancer Evolution', '740', 'Matrix', 'Compass', 'G300', 'Leganza', 'Sintra', '1007', 'LHS', 'Boxer', 'S60', '216', 'Wagon R', 'Grand Caravan', 'Ducato', 'E250', 'Dokker', 'Almera', 'A13', '2108', 'Aerodeck', 'Qashqai+2', 'A180', 'QX', '306', 'C70', 'Explorer', '4x4', 'Tribeca', 'Tiida', 'Partner Tepee', 'Vento', 'Grandis', 'Xsara Picasso', 'Freelander', 'Cherokee', '146', 'MX-6', '205', 'Murano', 'Patriot', 'Rexton', 'Bluebird', 'PT Cruiser', 'Accent', 'Sunny', 'Echo', 'S500', '607', '3303', 'Tundra', '2106', 'Evasion', 'Lybra', '3008', 'C4', '407', 'Grand Cherokee', 'Hunter', '968м', 'Duster', 'E230', 'Premacy', 'Terracan', 'Verso', '2105', 'ASX', 'EC7', 'Largus', 'H3', '147', 'Aygo', 'ML350', '620', 'Getz', 'Crafter', 'Navigator', 'S430', 'Cordoba', 'S400', '309', '2410', 'Berlingo', 'Prius', 'Discovery', 'Sandero', '244', 'Meriva', 'E240', 'Escalade', 'Town Car', 'Optima', 'Montero', 'STS', 'QQ', 'A140', 'Coupe', 'FX', 'GS', 'Bipper', '19', 'Captiva', 'Scudo', 'ES', 'Passat CC', 'ZX', 'Daily', 'Twingo', 'Rodius', 'Forester', 'GL320', 'Koleos', 'V50', 'Probe', 'C-Crosser', 'Taunus', '523', 'Intrepid', 'Auris', 'HiAce', 'Таврия', 'Swift', 'Lanos', 'X-Trail', 'Grandland X', 'Fit', '21', 'Almera Tino', 'T3', '2140', 'Mark VIII', 'Vanette', 'Pilot', 'Fox', 'B160', 'Kadjar', 'Navara', '166', '121', 'Expedition', 'X1', 'MDX', '1500', 'E260', '900', 'R350', 'Doblo', 'Yeti', 'Frontera', 'Ibiza', 'i20', 'Neon', 'Phaeton', 'X3', 'Malibu', 'Modus', 'Durango', 'Xedos 9', 'IS', '300', 'Crown Victoria', 'Spectra', 'A7', 'Pajero Sport', 'GL350', 'Jazz', 'E290', 'RX-8', 'V40', '2114', 'Magentis', 'A1', 'Symbol', 'Town&Country', 'X-Type', '3221', 'Countryman', 'T5 Caravelle', 'GLE350', '645', '940', 'Venza', 'C4 Picasso', 'CX-5', '640', '5', 'ix35', 'Starlet', 'GL400', 'C2', 'Outback', '340', 'Shuma', 'S420', 'Spark', 'CT', '806', 'Defender', '116', 'Caliber', 'HR-V', 'Eclipse Cross', 'А22', 'Range Rover', 'Kyron', 'Cirrus', 'CL500', 'T2', 'E320', 'V70', 'H-1', 'Lacetti', 'C220', 'Space Gear', 'SRX', 'Tribute', '200SX', '4008', 'Trax', 'Linea', '21011', 'Kimo', 'C250', 'Vesta', 'Range Rover Evoque', 'E270', '325', 'H6', '1111', '508', '75', '324', 'Zeta', 'Cooper S', '69', 'ML500', 'A6 Allroad', 'Sigma', 'Saxo', 'XC70', 'Altima', '2705', 'Combo', 'Tiggo', 'EX7', 'T6 Caravelle', 'SL500', 'Edge', 'Tucson', 'Forenza', 'Ignis', '3110', 'Millenia', '960', 'Nexia', 'GL500', 'Supra', '45', '155', 'A170', 'Camaro', 'TL', '408', 'XJ', '190', 'AMG GT4', '2101', '3302', '2115', '518', 'CLS400', 'Cooper', 'M', 'Gran Turismo', 'Antara', 'Pixo', 'Arosa', 'SC7', 'Space Wagon', 'C8', 'Croma', 'CLS350', 'Multipla', 'Actyon', 'Serena', 'RVR', 'C3 Picasso', 'Manager', 'Van', 'Fluence', 'Jumpy', 'T4 Multivan', 'CLA45 AMG', 'Contour', 'Ascona', '2104', 'Kalos', 'Catera', '469', '24', '21099', '25', 'Kalina', 'Taurus', 'E63 AMG', 'Corolla Verso', 'Demio', '107', 'Q', '5-Sep', 'Fora', 'NV S', '3-Sep', '2121', 'Kappa', 'Chaser', 'X70', 'B200', '2008', 'XF', 'Legend', 'Creta', 'Espero', 'Dedra', '807', 'Trans Sport', '200', 'L200', 'Previa', 'Splash', 'A200', '120', 'Mirage', 'i10', 'I', 'Journey', 'GLC250', 'MX-3', '4Runner', 'Mohave', 'Hover', 'Peri', '315', 'GL63', 'Volt', '31105', 'CK', 'Q3', '535', 'Skyline', 'Scirocco', 'Crosstour', 'Picnic', 'М5', 'Vel Satis', '3151', '2141', 'F-Pace', 'Quoris', 'GLE300', 'Cebrium', 'S4', '322', 'Musa', 'Kaptur', 'CX-9', 'Vibe', 'S90', 'Ram', 'Seicento', 'Citigo', '330', 'TSX', 'Galloper', 'Rogue', '2', '335', 'Celica', '159', 'Vitara', 'Retona', 'MK', 'Panda', 'Liana', 'Movano', 'XV', 'Chance', 'Leon', '145', 'G', 'LS', 'C1', 'Uno', 'LX', 'Orlando', 'Grand Starex', 'MB100', 'Tacoma', 'Tipo', 'XRAY', 'MKZ', 'ML400', 'S350', 'Paceman', 'А21', 'XE', 'Maverick', 'C320', 'Granada', 'Gol', 'MyWay', 'SX4', 'Altea', 'Firebird', '965', 'GLK220', 'Tigra', 'GX', 'Soul', 'Talisman', 'Mokka', 'Avensis Verso', 'Tourneo Custom', 'Kadett', '550', 'Discovery Sport', 'Libero', 'Space Runner', '500', 'Fiorino', 'ML300', 'Sedona', 'T6', 'Florid', 'Tourneo', 'Phedra', 'G500', 'V250', 'Captur', 'Up', 'F150', '540', '402', '2102', 'E450', 'Trajet', 'Eos', 'R280', 'ML280', 'Le Baron', 'V220', 'ILX', 'A210', 'Priora', 'Mascott', 'Atos', '452', 'Atlas', 'Tracker', 'CLA250', 'LC', '435', 'G270', 'Urban Cruiser', 'SC', 'E420', 'Eldorado', 'GLK300', 'Maxity', '164', 'Venga', '360', 'Cinquecento', 'Protege', 'Vaneo', 'Renegade', 'Liberty', '760', '420', 'Charger', 'S450', 'Latitude', 'CTS', 'De Ville', 'Quest', '100NX', '2110', 'Equinox', '301', 'М20', 'TT', 'Regal', 'F250', 'C6', 'Cavalier', '2112', 'ML63 AMG', 'Endeavor', 'Dart', '110', 'Santamo', '728', '412', 'A4 Allroad', 'Pulsar', 'EcoSport', 'T3 Caravelle', 'Urvan', 'Eclipse', '2103', 'CLS500', '630', 'Giulietta', 'C30', 'Econoline', 'Sentra', 'C280', 'QQ6', 'CR-Z', 'Beetle', 'Safe', '3500', 'S550', 'Pegasus', 'S5', 'Continental', 'Ranger', 'Lumina', 'Versa', 'NX', 'C240', '2113', 'Citan', 'WRX', 'Integra', 'JX', 'HHR', 'S8', 'S-Type', 'MKX', 'Expert Tepee', 'CLK230', '1119', 'Pointer', 'Favorit', '4007', 'E400', 'Epica', 'Elysion', 'Amarok', 'Picanto', '9 - 7X', 'CL550', 'X4', '90', 'Sens', 'Breez', 'ML55 AMG', '725', 'Courier', 'EX', 'Santana', 'Forza', 'Rekord', '410', '3000GT', '31512', 'Solano', 'Albea', 'GLA200', 'Lupo', 'Lodgy', 'Blazer', 'Interstar', 'Trail Blazer', 'Wrangler', 'Odyssey', 'E500', '21213', 'Titan', 'E430', 'Monterey', 'B170', 'Rezzo', 'Kapitan', 'Monza', 'Musso', '2206', 'ML270', 'Macan', '322133', 'ix55', 'Grand C-Max', 'Hilux', 'Concorde', 'Commander', 'GT', 'C25', 'Solara', 'ML430', 'ML250', '3962', 'GTV', 'Avenger', '2131', '929', '2402', 'Justy', 'MKC', 'Pride', '180', 'Cougar', 'IQ', '2752', 'CLS55 AMG', 'Tahoe', 'Alto', 'Emgrand 7', 'Z3', 'CL420', 'Nitro', 'Cabstar', 'Thunderbird', 'Astro Van', 'A2', 'Hd', 'Stealth', 'BX', 'ZDX', 'Corrado', '2120', 'Paseo', 'Starex', 'Verona', 'Venture', '650', 'GLC300', 'X6 M', 'Crown', 'V8', '401', 'Ypsilon', 'Windstar', 'ML230', 'H 100', 'Thesis', 'GLK350', 'Carina II', '3102', '218', 'Streetwise', 'S63 AMG', 'AX', 'CL', 'S600', 'Avella', '21013', '310210', 'CLS320', 'Puma', 'Freemont', 'RDX', 'DS4', 'S-Coupe', 'Prairie', 'S220', 'Seville', 'R500', 'Deer', 'L400', 'ELR', 'Amulet', '545', '112', '350Z', 'SX4 S-Cross', 'Enclave', 'M3', 'Aztek', '500X', '2125', 'Alphard', 'CX', 'Shuttle', 'SLX', 'XG 30', 'FR-V', 'Vision', 'Boxster', '12', 'T5 Shuttle', 'V90', 'Stream', 'Express', 'Idea', '2111', 'Aerio', 'XL7', 'Siena', 'G320', 'CLA180', 'Thema', '240', 'A190', 'Соболь', '125', 'T3 Multivan', '1300', 'Concerto', 'Bipper Tepee', '2401', 'Stavic', '403', 'RSX', 'Pajero Pinin', 'DS5', 'LeMans', '220', 'Gentra', 'C270', 'Thalia', 'G55 AMG', 'Suburban', 'J5', '428', '2123', 'Primastar', 'Challenger', 'CLK270', 'Pregio', 'Lancia', '500L', 'Mii', 'C300', 'R320', '310221', 'H5', 'CLS250', '539', 'L50', '451', 'C4 AirCross', 'Jimny', 'M4', 'T6 Multivan', 'SL320', '966', 'SL350', 'Clubman', 'Genesis', 'Grandeur', 'Spider', '3234', 'Excursion', 'X2', '264', '111', 'City', 'Alero', 'Commodore', 'Grand Am', '800-Series', 'Passport', 'S1000', 'Silverado', 'NV200', '235', 'Logo', '732', 'Magnum', 'John Cooper Works', 'Grand Modus', 'ВИС', 'CLA220', 'Dakota', 'S65 AMG', 'Freestyle', 'Samurai', 'Sequoia', 'Ridgeline', '11', 'F-Type', 'GL420', 'Tempo', 'Smily', 'Campo', '322132', 'ML550', 'M6', 'Besta', '3741', 'Brera', 'Луидор', '9-2X', 'CLS550', 'Aerostar', 'Korando', 'L300', 'Model F', '400', 'Malaga', 'C1500', 'Colorado', 'Impala', 'FJ Cruiser', 'G400']
transmission_type = ['mechanical', 'automatic']
colors = ['blue', 'silver', 'other', 'black', 'grey', 'red', 'white',
       'violet', 'green', 'brown', 'orange', 'yellow']
fuels = ['gasoline', 'diesel', 'gas', 'hybrid-petrol', 'hybrid-diesel']
engine_types = ['gasoline', 'diesel']
body_types = ['hatchback', 'minivan', 'universal', 'sedan', 'van', 'suv',
       'pickup', 'liftback', 'minibus', 'coupe', 'cabriolet', 'limousine']
states = ['owned', 'emergency', 'new']
drivetrains = ['front', 'rear', 'all']

manufacturer_name = st.sidebar.selectbox("Manufacturer", manufacturers)
model_name = st.sidebar.selectbox("Model", models)
transmission = st.sidebar.selectbox("Type of transmission", transmission_type)
color =  st.sidebar.selectbox("Color", colors)
engine_fuel =  st.sidebar.selectbox("Engine fuel", fuels)
engine_has_gas = st.sidebar.selectbox("Engine has gas", [True, False])
engine_type = st.sidebar.selectbox("Engine Type", engine_types)
body_type = st.sidebar.selectbox("Body Type", body_types)
warranty = st.sidebar.selectbox("Warranty", [True, False])
state = st.sidebar.selectbox("State", states)
drivetrains = st.sidebar.selectbox("Drivetrain", drivetrains)
year_produced = st.sidebar.slider('Year Produced', 1950, 2019, 2015, 1)
odometer_value = st.sidebar.slider("Odometer value", 0, 1000000, 1000, 100)

# construct the new case for prediction
new_case = [manufacturer_name, model_name, transmission, color, engine_fuel, engine_has_gas, engine_type, body_type, warranty, state, drivetrains, year_produced, odometer_value]


if (st.button('Find Car Price')):
    
    data, model = load("dataset.pickle", "model.pickle")
    result = inference(new_case, model, data.columns)
    st.write(result)
    temp2 = data['manufacturer_name'].value_counts().to_frame()
    st.write(pl.bar(temp2, temp2.index, temp2['manufacturer_name'], labels={'index':'Manufacturer', 'manufacturer_name':'Count'}))
    
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