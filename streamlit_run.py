import streamlit as st
from streamlit_app.market_view import market_dashboard
from streamlit_app.realtime_view import realtime_dashboard
from streamlit_app.fdpp_view import fdpp_dashboard

st.sidebar.title("Page Selection")
selected_page = st.sidebar.radio("Select the section you want to go to", ["Market Data", "Real Time Production", "FDPP / Finalized Daily Production Plan"])

if selected_page == "Market Data":
    market_dashboard()
elif selected_page == "Real Time Production":
    realtime_dashboard()
elif selected_page == "FDPP / Finalized Daily Production Plan":
    fdpp_dashboard()
