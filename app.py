import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI-Assisted Smart Disaster Response",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 AI-Assisted Smart Disaster Response")
st.subheader("Emergency Coordination & Resource Management Platform")

st.markdown("""
This platform supports disaster incident monitoring, emergency coordination,
resource allocation, shelter management and AI-assisted response.
""")

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Active Incidents", "12")
col2.metric("People Affected", "4,850")
col3.metric("Rescue Teams", "18")
col4.metric("Shelter Occupancy", "72%")

st.divider()

# Incident dashboard
st.header("📍 Disaster Incident Dashboard")

data = pd.DataFrame({
    "Incident": [
        "Urban Flood",
        "Flash Flood",
        "Building Collapse",
        "Landslide",
        "Cyclone"
    ],
    "Affected Population": [1250, 840, 320, 610, 1830],
    "Response Time (min)": [18, 24, 15, 31, 27],
    "Status": [
        "Active",
        "Active",
        "Contained",
        "Active",
        "Monitoring"
    ]
})

st.dataframe(data, use_container_width=True)

st.divider()

# Charts
st.header("📊 Response Analytics")

chart_data = data.set_index("Incident")

st.bar_chart(chart_data["Affected Population"])

st.header("⏱️ Average Response Time")
st.line_chart(chart_data["Response Time (min)"])

st.divider()

# Resource management
st.header("🚑 Emergency Resources")

r1, r2, r3 = st.columns(3)

r1.metric("Medical Kits", "425")
r2.metric("Food Packets", "2,840")
r3.metric("Drinking Water", "5,600 L")

st.divider()

# AI triage
st.header("🤖 AI-Assisted Emergency Triage")

description = st.text_area(
    "Enter an incident description",
    placeholder="Example: Heavy flooding reported near residential area..."
)

if st.button("Analyze Incident"):
    if description:
        st.success("Incident analyzed successfully.")
        st.info(
            "Priority: HIGH\n\n"
            "Recommended action: Dispatch rescue team and medical support."
        )
    else:
        st.warning("Please enter an incident description.")

st.divider()

st.caption(
    "AI-Assisted Smart Disaster Response and Emergency Coordination Platform"
)