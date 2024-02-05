import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(np.random.randn(20,  3),
                               columns = ['a', 'b', 'c'])
                          
print(chart_data)
st.line_chart(chart_data)

st.header('st.selectbox')
option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green', 'Yellow')
)
st.write('Your favorite color is', option)

st.header('st.multiselect')

options = st.multiselect(
    'What are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected', options)

st.header('check box')
st.write('What would you like to order?')

ice_cream = st.checkbox('ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if ice_cream:
    st.write("Great! Here's some more 🍦")
if coffee:
    st.write("Okay, here's some coffee ☕")
if cola:
    st.write("Here you go 🥤")
