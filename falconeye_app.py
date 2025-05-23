import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="FalconEye v0.1 - Aircraft Fault Detection", layout="wide")
st.title("🛩️ FalconEye v0.1")
st.subheader("Aircraft Sensor Fault Detection System")

# Simulate data
num_rows = st.slider("🔧 Number of sensor data rows", 10, 100, 20)
np.random.seed(42)

data = {
    "Engine Temp (°C)": np.random.randint(750, 900, size=num_rows),
    "Fuel Pressure (psi)": np.random.randint(30, 45, size=num_rows),
    "Hydraulic Pressure": np.random.randint(2800, 3200, size=num_rows),
    "Vibration Level": np.round(np.random.uniform(0.5, 2.0, size=num_rows), 2),
}

df = pd.DataFrame(data)

def detect_faults(row):
    faults = []
    if row["Engine Temp (°C)"] > 850:
        faults.append("Engine Overheating")
    if row["Fuel Pressure (psi)"] < 35:
        faults.append("Low Fuel Pressure")
    if row["Hydraulic Pressure"] < 2900 or row["Hydraulic Pressure"] > 3100:
        faults.append("Hydraulic Pressure Fault")
    if row["Vibration Level"] > 1.5:
        faults.append("High Vibration Detected")
    return ", ".join(faults) if faults else "No Fault"

df["Fault Status"] = df.apply(detect_faults, axis=1)

st.success("✅ Data generated and faults detected!")
st.subheader("📊 Sensor Data with Fault Status")
st.dataframe(df, use_container_width=True)

fault_summary = df["Fault Status"].value_counts()
st.subheader("📌 Fault Summary")
st.bar_chart(fault_summary)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Fault Report (CSV)", csv, "fault_report.csv", "text/csv")
