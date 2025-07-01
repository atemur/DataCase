import streamlit as st
import pandas as pd
import altair as alt

from datetime import datetime, time
from api.market import MarketClient
from config.settings import organizationIDs, start_date, end_date
from core.auth import tgt

def chart_of_market(df, title):
    st.subheader(title)

    colons = ["matchedOffers", "matchedBids", "bids", "offers"]
    usable_colons = [col for col in colons if col in df.columns]

    if "date" in df.columns and "hour" in df.columns:
        df["date"] = pd.to_datetime(df["date"].astype(str).str[:10] + " " + df["hour"])
    else:
        df["date"] = pd.to_datetime(df["date"])

    if "date" in df.columns and usable_colons:
        y_col = st.selectbox("Value to be Shown on the Chart", usable_colons, key=title+"_y")
        chart_type = st.radio("Chart Type", ["Line", "Bar"], horizontal=True, key=title+"_chart")

        chart = alt.Chart(df)
        chart = chart.mark_line() if chart_type == "Line" else chart.mark_bar()
        chart = chart.encode(
            x=alt.X("date", title="date"),
            y=alt.Y(f"{y_col}:Q", title=y_col),
            tooltip=["date", f"{y_col}"]
        ).properties(width=750, height=350, title=f"{y_col} Time Series")

        st.altair_chart(chart, use_container_width=True)

    else:
        st.caption("No graphs are shown for this data type.")

    st.dataframe(df)


def market_dashboard():
    st.header("Market Data")

    selected_orgs = st.multiselect("Select Organization", organizationIDs)

    if not selected_orgs:
        st.warning("Please select at least one organization.")
        return

    data_type = st.selectbox("Data Type", ["DAM Matching", "IDM Matching",
                                           "Bilateral Agreements"])
    client = MarketClient(tgt_token=tgt, start_date=start_date, end_date=end_date)
    now = datetime.now()

    for org_id in selected_orgs:
        if data_type == "DAM Matching":
            if now.time() < time(14, 0):
                st.warning("Day Ahead Market (DAM) data is published every day at 14:00."
                              "There may not be any up-to-date data yet for the data type you have selected.")
                df = pd.DataFrame([])
                st.dataframe(df)

            else:
                df = pd.DataFrame(client.fetch_dam_quantities(org_id))
                chart_of_market(df, f"Organization: {org_id}")

        elif data_type == "IDM Matching":
            df = pd.DataFrame(client.fetch_idm_quantities(org_id))
            st.subheader(f"Organization: {org_id}")
            st.dataframe(df)

        elif data_type == "Bilateral Agreements":
            df_buy = pd.DataFrame(client.fetch_bilateral_bids(org_id)).rename(columns={"quantity": "bids"})
            df_sell = pd.DataFrame(client.fetch_bilateral_offers(org_id)).rename(columns={"quantity": "offers"})
            df_merged = pd.merge(df_buy, df_sell, on=["date", "hour"])
            chart_of_market(df_merged, f"Organization: {org_id}")
