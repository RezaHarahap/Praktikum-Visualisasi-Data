import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")
st.write("Kelompok: 10")
st.markdown("""
- Haura Tsabitah (0110222242)
- Ahmad Al-Faqih Asasi (0110222190)
- Muhammad Reza Pahlevi Harahap (0110122110)
""")

df = pd.DataFrame(
    np.random.rand(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.area_chart(df)
