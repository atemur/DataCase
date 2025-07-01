import streamlit as st
import pandas as pd
import altair as alt

from utils.organisation_data import get_all_powerplants, get_all_uevcbs
from api.generation import GenerationClient
from config.settings import organizationIDs, start_date, end_date
from core.auth import tgt

def fdpp_dashboard():
    st.title("Finalized Daily Production Plan")
    selected_orgs = st.multiselect("Select Organizations", options=organizationIDs)

    if not selected_orgs:
        st.warning("Please select at least one organization.")
        return

    powerplants = get_all_powerplants(selected_orgs)
    uevcbs = get_all_uevcbs(powerplants)

    uevcb_options = [f"{item['id']} - {item.get('name', 'UEVCB')}" for item in uevcbs]
    selected_uevcb_display = st.selectbox("Select a UEVCB", options=uevcb_options)

    selected_uevcb = next(u for u in uevcbs if f"{u['id']} - {u.get('name', 'UEVCB')}" == selected_uevcb_display)
    selected_uevcb_id = selected_uevcb["id"]

    client = GenerationClient(tgt_token=tgt, start_date=start_date, end_date=end_date)
    kgup_data = client.fetch_dpp(region="TR1", uevcb_id=selected_uevcb_id)

    df = pd.DataFrame(kgup_data)
    df.fillna(0, inplace=True)
    st.dataframe(df)

    if "date" in df.columns and "hour" in df.columns:
        df["date"] = pd.to_datetime(df["date"].astype(str).str[:10] + " " + df["hour"])

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    numeric_cols = [col for col in numeric_cols if col not in ["hour"]]

    if "date" in df.columns and numeric_cols:
        st.subheader("FDPP Production Plan")

        chart_type = st.radio("Chart Type", ["Line", "Bar"], horizontal=True)
        y_col = st.selectbox("Type of production to display", numeric_cols, index=numeric_cols.index("total") if "total" in numeric_cols else 0)

        chart = alt.Chart(df)

        if chart_type == "Line":
            chart = chart.mark_line().encode(
                x=alt.X("date:T", title="date"),
                y=alt.Y(f"{y_col}", title=f"{y_col}"),
                tooltip=["date:T", f"{y_col}"]
            )
        else:
            chart = chart.mark_bar().encode(
                x=alt.X("date:T", title="date"),
                y=alt.Y(f"{y_col}", title=f"{y_col}"),
                tooltip=["date", f"{y_col}"]
            )

        chart = chart.properties(width=750, height=350, title=f"{y_col} Production Time Series")
        st.altair_chart(chart)
