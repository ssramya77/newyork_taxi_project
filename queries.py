def get_sample_trips():
    return """SELECT * FROM fct_trips LIMIT 10"""


def get_kpi_metrics():
    return """SELECT COUNT(*) as total_trips, 
    SUM(total_amount) as total_revenue, 
    AVG(TRIP_DURATION_MINUTES) as avg_trip_duration,
    AVG(TRIP_DISTANCE) as avg_trip_distance 
    FROM fct_trips"""


def get_trips_by_day(day):
    return f"""
    SELECT
        EXTRACT(hour FROM pickup_ts) AS hour,
        COUNT(distinct trip_id) AS trips
    FROM fct_trips
    WHERE DAYNAME(pickup_ts) = '{day}'
    GROUP BY 1
    ORDER BY 1
    """

def get_top_routes_by_day(day, time_range):
    if time_range is None:
        hour_filter = ""

    else:
        start_hour, end_hour = time_range

        if start_hour < end_hour:
            hour_filter = f"""
            AND EXTRACT(hour FROM t.pickup_ts) >= {start_hour}
            AND EXTRACT(hour FROM t.pickup_ts) < {end_hour}
            """
        else:
            hour_filter = f"""
            AND (
                EXTRACT(hour FROM t.pickup_ts) >= {start_hour}
                OR EXTRACT(hour FROM t.pickup_ts) < {end_hour}
            )
            """
    return f"""
    SELECT
        pu.zone AS pickup_zone,
        do.zone AS dropoff_zone,
        COUNT(DISTINCT t.trip_id) AS trips
    FROM fct_trips t
    JOIN dim_zones pu
        ON t.pu_location_id = pu.location_id
    JOIN dim_zones do
        ON t.do_location_id = do.location_id
    WHERE DAYNAME(t.pickup_ts) = '{day}'
    {hour_filter}
    GROUP BY 1,2
    ORDER BY trips DESC
    LIMIT 5
    """

def get_trips_by_borough(day, time_range):
    if time_range is None:
        hour_filter = ""

    else:
        start_hour, end_hour = time_range

        if start_hour < end_hour:
            hour_filter = f"""
            AND EXTRACT(hour FROM t.pickup_ts) >= {start_hour}
            AND EXTRACT(hour FROM t.pickup_ts) < {end_hour}
            """
        else:
            hour_filter = f"""
            AND (
                EXTRACT(hour FROM t.pickup_ts) >= {start_hour}
                OR EXTRACT(hour FROM t.pickup_ts) < {end_hour}
            )
            """
    return f"""
    SELECT
        z.borough,
        COUNT(distinct trip_id) AS trips
    FROM fct_trips t
    JOIN dim_zones z
        ON t.pu_location_id = z.location_id
    WHERE DAYNAME(t.pickup_ts) = '{day}'
    {hour_filter}
    GROUP BY z.borough
    """

def get_pickup_demand(day, time_range):
    if time_range is None:
        hour_filter = ""

    else:
        start_hour, end_hour = time_range

        if start_hour < end_hour:
            hour_filter = f"""
            AND EXTRACT(hour FROM t.pickup_ts) >= {start_hour}
            AND EXTRACT(hour FROM t.pickup_ts) < {end_hour}
            """
        else:
            hour_filter = f"""
            AND (
                EXTRACT(hour FROM t.pickup_ts) >= {start_hour}
                OR EXTRACT(hour FROM t.pickup_ts) < {end_hour}
            )
            """
    return f"""
    SELECT
        z.borough,
        z.zone,
        COUNT(*) AS trips
    FROM fct_trips t
    JOIN dim_zones z
        ON t.pu_location_id = z.location_id
    WHERE DAYNAME(t.pickup_ts) = '{day}'
    {hour_filter}
    GROUP BY z.borough, z.zone
    """