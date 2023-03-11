import streamlit as st
import pickle
import altair as alt

st.set_page_config(layout="wide")  # centered, wide

@st.cache(allow_output_mutation=True)
def load(data_path):
    data = pickle.load(open(data_path, 'rb'))
    return data

data = load("dataset.pickle")
# data = load("/Users/vasiliskalyvas/Documents/GitHub/streamlit/dataset.pickle")


st.title("Key insights from the data")


st.write('----------------------------------------------------------------------------------------------------------------')


# Plot 1
df1 = data['manufacturer_name'].value_counts().rename_axis('Manufacturer').reset_index(name='Counts').head(28)
df1_plot = alt.Chart(df1).mark_bar().encode(
    x=alt.X('Manufacturer', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Manufacturer','Counts']
).properties(width=500,height=200, title='Count by Manufacturer')#.interactive()

# Plot 2
df2 = data['model_name'].value_counts().rename_axis('Model').reset_index(name='Counts').head(28)
df2_plot = alt.Chart(df2).mark_bar().encode(
    x=alt.X('Model', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Model','Counts']
).properties(width=500,height=200, title='Count by Model')#.interactive()

st.altair_chart(alt.hconcat(df1_plot, df2_plot))

# Plot 3
df3 = data.groupby(by='manufacturer_name')['price_usd'].median().reset_index(name="Median Price").sort_values('Median Price', ascending=False).reset_index(drop=True).rename(columns={"manufacturer_name": "Manufacturer"}).head(28)
df3_plot = alt.Chart(df3).mark_bar().encode(
    x=alt.X('Manufacturer', sort='-y', title=None),
    y=alt.Y('Median Price', title=None),
    tooltip=['Manufacturer','Median Price']
).properties(width=500,height=200, title='Median Price by Manufacturer')#.interactive()

# Plot 4
df4 = data.groupby(by='model_name')['price_usd'].median().reset_index(name="Median Price").sort_values('Median Price', ascending=False).reset_index(drop=True).rename(columns={"model_name": "Model"}).head(28)
df4_plot = alt.Chart(df4).mark_bar().encode(
    x=alt.X('Model', sort='-y', title=None),
    y=alt.Y('Median Price', title=None),
    tooltip=['Model','Median Price']
).properties(width=500,height=200, title='Median Price by Model')#.interactive()

st.altair_chart(alt.hconcat(df3_plot, df4_plot))


st.write('----------------------------------------------------------------------------------------------------------------')


# Plot 5 - top 10 Brands by count
top_10_brands_in_count = list(data.groupby(by='manufacturer_name').size().reset_index(name="counts").sort_values('counts', ascending=False).head(10)['manufacturer_name'])
df5 = data[data['manufacturer_name'].isin(top_10_brands_in_count)][['manufacturer_name','price_usd']]

df5_plot = alt.Chart(df5).mark_boxplot(extent='min-max').encode(
    x=alt.X('manufacturer_name', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance for Top 10 Manufacturers (by count)')

# Plot 6 - top 10 Brands by median price
top_10_brands_in_median_price = list(data.groupby(by='manufacturer_name')['price_usd'].median().reset_index(name="median_price").sort_values('median_price', ascending=False).head(10)['manufacturer_name'])
df6 = data[data['manufacturer_name'].isin(top_10_brands_in_median_price)][['manufacturer_name','price_usd']]

df6_plot = alt.Chart(df6).mark_boxplot(extent='min-max').encode(
    x=alt.X('manufacturer_name', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance for Top 10 Manufacturers (by median price)')

st.altair_chart(alt.hconcat(df5_plot, df6_plot))

# Plot 7 - top 10 Models by count
top_10_models_in_count = list(data.groupby(by='model_name').size().reset_index(name="counts").sort_values('counts', ascending=False).head(10)['model_name'])
df7 = data[data['model_name'].isin(top_10_models_in_count)][['model_name','price_usd']]

df7_plot = alt.Chart(df7).mark_boxplot(extent='min-max').encode(
    x=alt.X('model_name', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance for Top 10 Models (by count)')

# Plot 8 - top 10 Models by median price
top_10_models_in_median_price = list(data.groupby(by='model_name')['price_usd'].median().reset_index(name="median_price").sort_values('median_price', ascending=False).head(10)['model_name'])
df8 = data[data['model_name'].isin(top_10_models_in_median_price)][['model_name','price_usd']]

df8_plot = alt.Chart(df8).mark_boxplot(extent='min-max').encode(
    x=alt.X('model_name', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance for Top 10 Models (by median price)')

st.altair_chart(alt.hconcat(df7_plot, df8_plot))

st.markdown("""
            #### The above plots show that:
            most **popular** cars (either in terms of manufacturer or model) tend to be more **stable in their price ranges**.
            """)


st.write('----------------------------------------------------------------------------------------------------------------')


# Plot the categorical variables, both on their own (on the left) and against price (on the right):

# Plots - Transmission
df9 = data['transmission'].value_counts().rename_axis('Transmission').reset_index(name='Counts')
df9_plot = alt.Chart(df9).mark_bar().encode(
    x=alt.X('Transmission', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Transmission','Counts']
).properties(width=500,height=200, title='Count by Transmission')#.interactive()

df10_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('transmission', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Transmission')

st.altair_chart(alt.hconcat(df9_plot, df10_plot))

# Plots - Engine Fuel
df11 = data['engine_fuel'].value_counts().rename_axis('Engine Fuel').reset_index(name='Counts')
df11_plot = alt.Chart(df11).mark_bar().encode(
    x=alt.X('Engine Fuel', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Engine Fuel','Counts']
).properties(width=500,height=200, title='Count by Engine Fuel')#.interactive()

df12_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('engine_fuel', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Engine Fuel')

st.altair_chart(alt.hconcat(df11_plot, df12_plot))


# Plots - Engine with Gas
df13 = data['engine_has_gas'].value_counts().rename_axis('Engine with Gas').reset_index(name='Counts')
df13_plot = alt.Chart(df13).mark_bar().encode(
    x=alt.X('Engine with Gas', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Engine with Gas','Counts']
).properties(width=500,height=200, title='Count by Engine with Gas')#.interactive()

df14_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('engine_has_gas', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Engine with Gas')

st.altair_chart(alt.hconcat(df13_plot, df14_plot))


# Plots - Engine Type
df15 = data['engine_type'].value_counts().rename_axis('Engine Type').reset_index(name='Counts')
df15_plot = alt.Chart(df15).mark_bar().encode(
    x=alt.X('Engine Type', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Engine Type','Counts']
).properties(width=500,height=200, title='Count by Engine Type')#.interactive()

df16_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('engine_type', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Engine Type')

st.altair_chart(alt.hconcat(df15_plot, df16_plot))


# Plots - Body Type
df17 = data['body_type'].value_counts().rename_axis('Body Type').reset_index(name='Counts')
df17_plot = alt.Chart(df17).mark_bar().encode(
    x=alt.X('Body Type', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Body Type','Counts']
).properties(width=500,height=200, title='Count by Body Type')#.interactive()

df18_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('body_type', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Body Type')

st.altair_chart(alt.hconcat(df17_plot, df18_plot))


# Plots - Warranty
df19 = data['has_warranty'].value_counts().rename_axis('Warranty').reset_index(name='Counts')
df19_plot = alt.Chart(df19).mark_bar().encode(
    x=alt.X('Warranty', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Warranty','Counts']
).properties(width=500,height=200, title='Count by Warranty')#.interactive()

df20_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('has_warranty', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Warranty')

st.altair_chart(alt.hconcat(df19_plot, df20_plot))


# Plots - State
df21 = data['state'].value_counts().rename_axis('State').reset_index(name='Counts')
df21_plot = alt.Chart(df21).mark_bar().encode(
    x=alt.X('State', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['State','Counts']
).properties(width=500,height=200, title='Count by State')#.interactive()

df22_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('state', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by State')

st.altair_chart(alt.hconcat(df21_plot, df22_plot))


# Plots - Drivetrain
df23 = data['drivetrain'].value_counts().rename_axis('Drivetrain').reset_index(name='Counts')
df23_plot = alt.Chart(df23).mark_bar().encode(
    x=alt.X('Drivetrain', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Drivetrain','Counts']
).properties(width=500,height=200, title='Count by Drivetrain')#.interactive()

df24_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('drivetrain', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Drivetrain')

st.altair_chart(alt.hconcat(df23_plot, df24_plot))


# Plots - Colour
df25 = data['color'].value_counts().rename_axis('Colour').reset_index(name='Counts')
df25_plot = alt.Chart(df25).mark_bar().encode(
    x=alt.X('Colour', sort='-y', title=None),
    y=alt.Y('Counts', title=None),
    tooltip=['Colour','Counts']
).properties(width=500,height=200, title='Count by Colour')#.interactive()

df26_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    x=alt.X('color', sort='-y', title=None),
    y=alt.Y('price_usd')
).properties(width=500,height=200, title='Price Variance by Colour')

st.altair_chart(alt.hconcat(df25_plot, df26_plot))


st.markdown("""
            #### The above plots show that:
            - mechanical cars are double the automatics, however automatics are more expensive (double the price)
            - sedans and front-drive cars are the most popular, but not most expensive
            - the engine type and engine fuel is mostly gasoline, but hybrid-petrol the most expensive
            - vast majority owned and without warranty, but new with guarantee can lead to sigificantly high prices
            - black and silver the most popular, but brown cars have the highest median price
            So, it seems that high prices can be related to automatic cars with hybrid-petrol fuel, that are new and have warranty.
            """)


st.write('----------------------------------------------------------------------------------------------------------------')



df27_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    y=alt.Y('year_produced')
).properties(width=500,height=200, title='Price Variance by Year Produced')

df28_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    y=alt.Y('odometer_value')
).properties(width=500,height=200, title='Price Variance by Odometer Value')

df29_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    y=alt.Y('engine_capacity')
).properties(width=500,height=200, title='Price Variance by Engine Capacity')

df30_plot = alt.Chart(data).mark_boxplot(extent='min-max').encode(
    y=alt.Y('duration_listed')
).properties(width=500,height=200, title='Price Variance by Duration Listed')

df27_28_plots = alt.hconcat(df27_plot, df28_plot)
df29_30_plots = alt.hconcat(df29_plot, df30_plot)

st.altair_chart(alt.vconcat(df27_28_plots, df29_30_plots))


st.markdown("""
            #### The dataset mainly consists of:
            - cars mostly produced around 2002, with avg odometer value of 250K km
            - mainly with 2 engines, being listed mostly under 100 days
            """)