#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 00:45:20 2022

@author: vasiliskalyvas
"""

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import numpy as np
import altair as alt

@st.cache(allow_output_mutation=True)
def load(data_path):
    data = pickle.load(open(data_path, 'rb'))
    return data

data = load("/Users/vasiliskalyvas/Documents/GitHub/streamlit/dataset.pickle")

top_10_brands_in_count = list(data.groupby(by='manufacturer_name').size().reset_index(name="counts").sort_values('counts', ascending=False).head(10)['manufacturer_name'])
df_top_10_brands_in_count = data[data['manufacturer_name'].isin(top_10_brands_in_count)]

grouped = df_top_10_brands_in_count.groupby(by='manufacturer_name').size().reset_index(name="counts").sort_values('counts', ascending=False)
st.bar_chart(grouped, x='manufacturer_name', y='counts')
