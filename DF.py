import pandas as pd
import numpy as np
import streamlit as st
import time

df = pd.read_csv('Salary_Data.csv')

st.dataframe(df,width=500,height=500)

@st.cache_data
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox('1'):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))