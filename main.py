import streamlit as st
import pandas as pd

st.write(""" # Dashboard Ben  """)

msft = pd.read_csv(r'MSFT.csv',index_col='Date')
msft.index = pd.to_datetime(msft.index)
msft.rename(columns={'Adj Close':'MSFT'}, inplace=True)

st.line_chart(msft)
print()
