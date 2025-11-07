import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok: 10")
st.markdown("""
- Haura Tsabitah (0110222242)
- Ahmad Al-Faqih Asasi (0110222190)
- Muhammad Reza Pahlevi Harahap (0110122110)
""")

st.graphviz_chart("""
    digraph {
            "Training Data" => "ML Algorithm"
            "ML Algorithm" => "Model"
            "Model" => Results Forecasting"
            "New Data" => "Model"
        }
""")
