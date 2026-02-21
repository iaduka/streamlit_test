# import streamlit as st
# st.title("Hello World!")

import streamlit as st
import pandas as pd
import numpy as np

# Sample Data
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['chocolate', 'ice-cream', 'cookies']
)

st.title("Streamlit's Three Chart Samples")

st.subheader("Line Chart")
st.line_chart(df) # Uses index as x-axis, columns as series

st.subheader("Area Chart")
st.area_chart(df, x='chocolate', y=['ice-cream', 'cookies']) # Specify x and y

st.subheader("Bar Chart")
st.bar_chart(df[['chocolate', 'ice-cream', 'cookies']]) # Plot specific columns
