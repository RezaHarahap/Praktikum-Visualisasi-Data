import streamlit as st

st.title("Empty Containers")
st.write("Kelompok: 10")
st.markdown("""
- Haura Tsabitah (0110222242)
- Ahmad Al-Faqih Asasi (0110222190)
- Muhammad Reza Pahlevi Harahap (0110122110)
""")

import streamlit as st
import time

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    
    st.write("✔️ Times up!")