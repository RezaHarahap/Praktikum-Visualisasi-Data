import streamlit as st

st.title("Columns")
st.write("Kelompok: 10")
st.markdown("""
- Haura Tsabitah (0110222242)
- Ahmad Al-Faqih Asasi (0110222190)
- Muhammad Reza Pahlevi Harahap (0110122110)
""")

# Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in column 1
col1.write("First Column")
col1.image("../images/kucing1.jpeg")

# Inserting Elements in column 2
col2.write("Second Column")
col2.image("../images/kucing2.jpeg")