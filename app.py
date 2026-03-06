import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px
from queries import get_sample_trips, get_kpi_metrics, get_trips_by_day, get_top_routes_by_day, get_trips_by_borough, get_pickup_demand
from ui import setup_page, show_header, show_divider, show_kpis, show_trips_by_hour_chart, show_top_routes, show_graphstitle, show_borough_map, show_pickup_heatmap
from constants import DAY_MAP, PART_OF_DAY, BOROUGH_COORDS


setup_page()
show_header()

# Snowflake connection
conn = snowflake.connector.connect(
    user="USERNAME",
    password="PASSWORD",
    account="ACCOUNTID",
    warehouse="transforming",
    database="analytics",
    schema="dbt_ssimhadri"
)

print("Connected successfully")


query = get_kpi_metrics()

kpi_df = pd.read_sql(query, conn)

# st.dataframe(kpi_df)

total_trips = int(kpi_df["TOTAL_TRIPS"][0])
total_revenue = float(kpi_df["TOTAL_REVENUE"][0])
avg_trip_duration = float(kpi_df["AVG_TRIP_DURATION"][0])
avg_trip_distance = float(kpi_df["AVG_TRIP_DISTANCE"][0])

show_kpis(total_trips, total_revenue, avg_trip_duration, avg_trip_distance)

show_divider()

show_graphstitle()

##day selection filter

day_selected = st.selectbox(
    "Select Day of Week",
     list(DAY_MAP.keys())
)
day_abbr = DAY_MAP[day_selected]

trips_by_day_query = get_trips_by_day(day_abbr)

trips_by_day_df = pd.read_sql(trips_by_day_query, conn)

# send dataframe to UI
show_trips_by_hour_chart(trips_by_day_df, day_selected)


part_selected = st.selectbox(
    "Select Part of Day",
    list(PART_OF_DAY.keys()),
    index = 0 # default to "All Day"
)

time_range  = PART_OF_DAY[part_selected]


## top routes by day
routes_query = get_top_routes_by_day(day_abbr, time_range)

routes_df = pd.read_sql(routes_query, conn)

show_top_routes(routes_df, day_selected)


borough_query = get_trips_by_borough(day_abbr, time_range)

borough_df = pd.read_sql(borough_query, conn)

borough_df["lat"] = borough_df["BOROUGH"].map(
    lambda b: BOROUGH_COORDS.get(b, (None, None))[0]
)

borough_df["lon"] = borough_df["BOROUGH"].map(
    lambda b: BOROUGH_COORDS.get(b, (None, None))[1]
)

borough_df = borough_df.dropna(subset=["lat", "lon"])

show_borough_map(borough_df, day_selected)


pickup_query = get_pickup_demand(day_abbr, time_range)

pickup_df = pd.read_sql(pickup_query, conn)

pickup_df["lat"] = pickup_df["BOROUGH"].map(
    lambda b: BOROUGH_COORDS.get(b, (None, None))[0]
)

pickup_df["lon"] = pickup_df["BOROUGH"].map(
    lambda b: BOROUGH_COORDS.get(b, (None, None))[1]
)

pickup_df = pickup_df.dropna(subset=["lat", "lon"])

show_pickup_heatmap(pickup_df, day_selected)