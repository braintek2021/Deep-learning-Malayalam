import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.write("""
# My first app
Hello *world!*
""")

np.random.seed(42)  # Set seed for reproducibility
data = {'X': np.arange(1, 11),
        'Y': np.random.randint(0, 100, 10)}

df = pd.DataFrame(data)

st.line_chart(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#https://bgremoval.streamlit.app/