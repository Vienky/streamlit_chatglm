import streamlit as st 
st.title('st.experiment')

with st.expander('About this app'):
    st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
  
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')

st.header('2. Contents of st.experimental_get_query_params')
st.write(st.query_params())

# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.query_params()['firstname'][0]
surname = st.query_params()['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')

import numpy as np
import pandas as pd
from time import time

st.title('st.cache')
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.randn(2000000,5),
        columns = ['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
    df = pd.DataFrame(
        np.random.randn(2000000,5),
        columns = ['a', 'b', 'c', 'd', 'e']
    )
    return df
st.write(load_data_a())
b1 = time()
st.info(b1-b0)
