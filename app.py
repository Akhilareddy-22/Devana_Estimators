import streamlit as st
import pandas as pd
from database import engine

st.set_page_config(page_title="DEVANA Construction Estimator")

st.title("🏗️ DEVANA Construction Estimator")

project_name = st.text_input("Project Name")
area = st.number_input("Built-up Area (sq.ft)", min_value=0.0)

if st.button("Generate Estimate"):

    total_cost = area * 2200
    cement = area * 0.4
    steel = area * 4
    bricks = area * 8

    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO estimates (project_name, area, total_cost, cement, steel, bricks)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (project_name, area, total_cost, cement, steel, bricks)
    )
    conn.commit()
    cursor.close()
    conn.close()

    st.success("Estimate Generated and Saved Successfully")
    st.write("### Estimation Report")
    st.write(f"Project Name: {project_name}")
    st.write(f"Area: {area} sq.ft")
    st.write(f"Total Cost: ₹{total_cost:,.2f}")
    st.write(f"Cement Bags: {cement}")
    st.write(f"Steel Required: {steel} kg")
    st.write(f"Bricks Required: {bricks}")