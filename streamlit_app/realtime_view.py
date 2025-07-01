import streamlit as st
import pandas as pd
import altair as alt

from utils.matching import get_matching_gzu_ids
from config.settings import organizationIDs
from api.generation import GenerationClient
from core.auth import tgt
from config.settings import start_date, end_date_for_c1


def realtime_dashboard():
    st.title("Realtime Production Data")

    selected_orgs = st.multiselect("Select Organizations", options=organizationIDs)

    if not selected_orgs:
        st.warning("Please select at least one organization.")
        return

    matched_gzus = get_matching_gzu_ids(selected_orgs)

    gzu_options = [f"{gzu['gzu_id']} (Org: {gzu['organization_id']})" for gzu in matched_gzus]
    selected_gzu_display = st.selectbox("Select a GZU", options=gzu_options)

    selected_gzu = next(g for g in matched_gzus if f"{g['gzu_id']} (Org: {g['organization_id']})"
                        == selected_gzu_display)
    gzu_id = selected_gzu["gzu_id"]

    st.write(f"Selected GZU ID: `{gzu_id}`")
    generation_client = GenerationClient(tgt_token=tgt, start_date=start_date, end_date=end_date_for_c1)
    gzu_data = generation_client.fetch_realtime_generation(gzu_id)

    if not gzu_data:
        st.warning("No production data found for this GZU.")
        return

    df = pd.DataFrame(gzu_data)
    st.dataframe(df)
    st.subheader("Realtime Production Data Table")

    if "date" in df.columns and "hour" in df.columns:
        df["date"] = pd.to_datetime(df["date"].astype(str).str[:10] + " " + df["hour"])

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    numeric_cols = [col for col in numeric_cols if col not in ["hour"]]

    if "date" in df.columns and numeric_cols:
        st.subheader("Realtime Production Data Dashboard")

        chart_type = st.radio("Chart Type", ["Line", "Bar"], horizontal=True)
        y_col = st.selectbox("Type of production to display", numeric_cols,
                             index=numeric_cols.index("total") if "total" in numeric_cols else 0)

        chart = alt.Chart(df)

        if chart_type == "Line":
            chart = chart.mark_line().encode(
                x="date",
                y=alt.Y(f"{y_col}:Q", title=f"{y_col}"),
                tooltip=["date", f"{y_col}"]
            )
        else:
            chart = chart.mark_bar().encode(
                x="date",
                y=alt.Y(f"{y_col}", title=f"{y_col}"),
                tooltip=["date", f"{y_col}"]
            )

        chart = chart.properties(width=750, height=350, title=f"{y_col} Production Time Series")
        st.altair_chart(chart)
