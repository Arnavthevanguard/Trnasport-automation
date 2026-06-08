import streamlit as st

st.title("Transport Automation")

st.write("Prototype Version 1")

bill = st.file_uploader("Upload Bill Image")

invoice = st.file_uploader("Upload Invoice PDF")

if st.button("Generate Report"):
    st.success("Report Generated!")