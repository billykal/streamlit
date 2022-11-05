#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:08:15 2022

@author: vasiliskalyvas
"""
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


@st.cache(allow_output_mutation=True)
def load(data_path):
    data = pickle.load(open(data_path, 'rb'))
    return data

data = load("/Users/vasiliskalyvas/Documents/GitHub/streamlit/dataset.pickle")


st.write('--------------------------------------------------------- **Some key insights:** ---------------------------------------------------------')


# top 10 brands by count and by median price
top_10_brands_in_count = list(data.groupby(by='manufacturer_name').size().reset_index(name="counts").sort_values('counts', ascending=False).head(10)['manufacturer_name'])
df_top_10_brands_in_count = data[data['manufacturer_name'].isin(top_10_brands_in_count)]

top_10_brands_in_median_price = list(data.groupby(by='manufacturer_name')['price_usd'].median().reset_index(name="median_price").sort_values('median_price', ascending=False).head(10)['manufacturer_name'])
df_top_10_brands_in_median_price = data[data['manufacturer_name'].isin(top_10_brands_in_median_price)]


# top 10 models by count and by median price
top_10_models_in_count = list(data.groupby(by='model_name').size().reset_index(name="counts").sort_values('counts', ascending=False).head(10)['model_name'])
df_top_10_models_in_count = data[data['model_name'].isin(top_10_models_in_count)]

top_10_models_in_median_price = list(data.groupby(by='model_name')['price_usd'].median().reset_index(name="median_price").sort_values('median_price', ascending=False).head(10)['model_name'])
df_top_10_models_in_median_price = data[data['model_name'].isin(top_10_models_in_median_price)]


# plots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(25,15))

sns.boxplot(data=df_top_10_brands_in_count, x='manufacturer_name', y='price_usd', ax=axs[0][0], order=top_10_brands_in_count)
axs[0][0].set(title='Price variance for top 10 manufacturers by count')
sns.boxplot(data=df_top_10_brands_in_median_price, x='manufacturer_name', y='price_usd', ax=axs[0][1], order=top_10_brands_in_median_price)
axs[0][1].set(title='Price variance for top 10 manufacturers by median price')

sns.boxplot(data=df_top_10_models_in_count, x='model_name', y='price_usd', ax=axs[1][0], order=top_10_models_in_count)
axs[1][0].set(title='Price variance for top 10 models by count')
sns.boxplot(data=df_top_10_models_in_median_price, x='model_name', y='price_usd', ax=axs[1][1], order=top_10_models_in_median_price)
axs[1][1].set(title='Price variance for top 10 models by median price')

st.write(fig)

st.markdown("""
            #### The above plots show that:
            most **popular** cars (either in terms of manufacturer or model) tend to be more **stable in their price ranges**.
            """)


st.write('----------------------------------------------------------------------------------------------------------------')


# Plot the categorical variables, both on their own (on the left) and against price (on the right):
fig, axs = plt.subplots(nrows=9, ncols=2, figsize=(15,50))

sns.countplot(data=data, x='transmission', ax=axs[0][0])
sns.boxplot(data=data, x='transmission', y='price_usd', ax=axs[0][1])

sns.countplot(data=data, x='engine_fuel', ax=axs[1][0])
sns.boxplot(data=data, x='engine_fuel', y='price_usd', ax=axs[1][1])

sns.countplot(data=data, x='engine_has_gas', ax=axs[2][0])
sns.boxplot(data=data, x='engine_has_gas', y='price_usd', ax=axs[2][1])

sns.countplot(data=data, x='engine_type', ax=axs[3][0])
sns.boxplot(data=data, x='engine_type', y='price_usd', ax=axs[3][1])

sns.countplot(data=data, x='body_type', ax=axs[4][0])
sns.boxplot(data=data, x='body_type', y='price_usd', ax=axs[4][1])

sns.countplot(data=data, x='has_warranty', ax=axs[5][0])
sns.boxplot(data=data, x='has_warranty', y='price_usd', ax=axs[5][1])

sns.countplot(data=data, x='state', ax=axs[6][0])
sns.boxplot(data=data, x='state', y='price_usd', ax=axs[6][1])

sns.countplot(data=data, x='drivetrain', ax=axs[7][0])
sns.boxplot(data=data, x='drivetrain', y='price_usd', ax=axs[7][1])

sns.countplot(data=data, x='color', ax=axs[8][0])
sns.boxplot(data=data, x='color', y='price_usd', ax=axs[8][1])

st.write(fig)

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


fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10,10))

sns.boxplot(data=data, y='year_produced', ax=axs[0][0])
sns.boxplot(data=data, y='odometer_value', ax=axs[0][1])
sns.boxplot(data=data, y='engine_capacity', ax=axs[1][0])
sns.boxplot(data=data, y='duration_listed', ax=axs[1][1])

st.write(fig)

st.markdown("""
            #### The dataset mainly consists of:
            - cars mostly produced around 2002, with avg odometer value of 250K km
            - mainly with 2 engines, being listed mostly under 100 days
            """)