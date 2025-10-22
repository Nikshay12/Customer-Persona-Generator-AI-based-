import streamlit as st
import pandas as pd
from app.analytics import load_and_preprocess
from app.persona_generator import generate_personas
from app.visualize import plot_persona_distribution

st.title("👤 Customer Persona Generator (AI-based)")
st.write("Generate user personas from demographic and behavior data.")

uploaded_file = st.file_uploader("Upload User CSV", type=["csv"])

if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
    df = load_and_preprocess(uploaded_file)

    personas_df, model = generate_personas(df, n_clusters=3)
    st.subheader("User Personas")
    st.dataframe(personas_df)

    st.subheader("Persona Distribution")
    plt_chart = plot_persona_distribution(personas_df)
    st.pyplot(plt_chart)

else:
    st.info("Upload a CSV file to generate personas.")
