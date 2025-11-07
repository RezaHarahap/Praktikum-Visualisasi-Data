import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok: 10")
st.markdown("""
- Haura Tsabitah (0110222242)
- Ahmad Al-Faqih Asasi (0110222190)
- Muhammad Reza Pahlevi Harahap (0110122110)
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"] 
)

st.map(df)