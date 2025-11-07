import streamlit as st

st.title("Columns With Padding")
st.write("Kelompok: 10")
st.markdown("""
- Haura Tsabitah (0110222242)
- Ahmad Al-Faqih Asasi (0110222190)
- Muhammad Reza Pahlevi Harahap (0110122110)
""")

from PIL import Image
img = Image.open("../images/kucing2.jpeg")
st.title("Padding")

# Defining Padding with columns
col1, padding, col2 = st.columns((10, 2, 10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)