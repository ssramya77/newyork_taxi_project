import streamlit as st
import plotly.express as px

def setup_page():
    st.set_page_config(
        page_title="NYC Taxi Analytics",
        page_icon="🚕",
        layout="wide"
    )

def show_header():
    st.title("🚕 NYC Yellow Taxi Analytics")
    st.write("Dashboard exploring taxi trip patterns in New York City during 2023.")

def show_divider():
    st.divider()

def show_graphstitle():
    st.subheader("Trip Details by Day and Time")

def show_kpis(total_trips, total_revenue, avg_trip_duration, avg_trip_distance):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Trips", f"{total_trips:,}")
    col2.metric("Total Revenue ($)", f"{total_revenue:,.0f}")
    col3.metric("Avg Trip Duration (min)", f"{avg_trip_duration:.2f}")
    col4.metric("Avg Trip Distance (miles)", f"{avg_trip_distance:.2f}")


def show_trips_by_hour_chart(df, day):

    fig = px.bar(
        df,
        x="HOUR",
        y="TRIPS",
        title=f"Trips by Hour on {day}"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_top_routes(df, day):

    df["route"] = df["PICKUP_ZONE"] + " → " + df["DROPOFF_ZONE"]

    fig = px.bar(
        df,
        x="TRIPS",
        y="route",
        orientation="h",
        title=f"Top 5 Taxi Routes on {day}",
        labels={"TRIPS": "Number of Trips", "route": "Route"}
    )

    fig.update_layout(yaxis={'categoryorder':'total ascending'})

    st.plotly_chart(fig, use_container_width=True)


def show_borough_map(df, day):

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        size="TRIPS",
        color="BOROUGH",
        hover_name="BOROUGH",
        zoom=9,
        mapbox_style="carto-positron",
        title=f"Taxi Activity by Borough on {day}"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_pickup_heatmap(df, day):

    fig = px.density_mapbox(
        df,
        lat="lat",
        lon="lon",
        z="TRIPS",
        radius=40,
        zoom=9,
        mapbox_style="carto-positron",
        title=f"Taxi Pickup Density on {day}"
    )

    st.plotly_chart(fig, use_container_width=True)