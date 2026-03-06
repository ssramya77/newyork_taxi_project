# NYC Yellow Taxi Analytics Project

## Overview

This project demonstrates an end-to-end **analytics engineering workflow** using the **New York City Yellow Taxi dataset**. The objective is to transform raw taxi trip data into an analytics-ready dimensional model using **dbt**, and build an interactive analytics dashboard using **Python and Streamlit**.

The project highlights modern data stack practices including **data modeling, transformation, analytics, and visualization**.

---

# Tech Stack

* **Python** – Data analysis and Streamlit dashboard development
* **Streamlit** – Interactive analytics application
* **SQL** – Data transformations and analytical queries
* **dbt (Data Build Tool)** – Data transformation and dimensional modeling
* **Snowflake** – Cloud data warehouse
* **GitHub** – Version control and project documentation

---

# Architecture

Raw NYC Taxi Data
⬇
Snowflake Data Warehouse
⬇
dbt Transformations (Staging → Dimensional Models)
⬇
Python + Streamlit Dashboard

---

# Data Source

The dataset used in this project comes from the **NYC Taxi & Limousine Commission (TLC)**.

The dataset contains information about taxi trips including:

* pickup and dropoff timestamps
* passenger counts
* trip distance
* fare amounts
* payment types
* pickup and dropoff locations

---

# dbt Data Modeling

The transformation layer was implemented using **dbt Studio** to build a dimensional data model.

## Staging Layer

Staging models clean and standardize raw taxi trip data.

Examples:

* `stg_yellow_trips`
* `stg_taxi_zone_lookup`

These models perform tasks such as:

* column renaming
* data type standardization
* filtering invalid records

---

## Mart Layer (Dimensional Model)

The mart layer builds analytics-ready tables.

### Dimension Tables

* `dim_datetime`
* `dim_vendor`
* `dim_payment_type`
* `dim_zones`

These tables store descriptive attributes used for analytics.

### Fact Table

`fct_trips`

The fact table contains core trip metrics such as:

* trip distance
* passenger count
* total fare
* trip duration
* pickup and dropoff relationships

This dimensional structure enables efficient analytical queries.

---

# Python + Streamlit Dashboard

A **Python-based Streamlit dashboard** was built to visualize taxi trip insights.

Features include:

* Taxi pickup heatmaps across NYC
* Borough-level trip analysis
* Trip distance and fare exploration
* Interactive time-based filtering

The dashboard allows users to explore taxi usage patterns across New York City.

---

# Project Structure

```
NEWYORK_TAXI_PROJECT
│
├── app.py
├── ui.py
├── queries.py
├── constants.py
│
├── dbt studios new york taxi repo.zip
│
├── snowflakecode.txt
│
├── streamlit-app-NewYork Yellow Taxi Visualizations.webm
│
└── README.md



```

## File Description

**app.py**
Main entry point for the Streamlit analytics dashboard.

**ui.py**
Contains UI components and layout logic for the Streamlit application.

**queries.py**
Stores SQL queries used to retrieve data from Snowflake.

**constants.py**
Defines reusable constants such as database names, table names, and configuration variables.

**dbt studios new york taxi repo.zip**
Full dbt project exported from dbt Studio containing staging models, dimension tables, fact tables, and transformation logic.

**snowflakecode.txt**
Contains Snowflake SQL scripts used for data loading and preparation.

---

# How to Run the Project

## Run the Streamlit Dashboard

```python
streamlit run app.py
```

This will start the Streamlit analytics dashboard in your browser.

---

# Skills Demonstrated

* Analytics engineering
* Dimensional data modeling
* SQL transformations with dbt
* Python data analysis
* Streamlit dashboard development
* Data visualization
* End-to-end analytics pipeline development

---

# Future Improvements

* Add dbt tests and documentation
* Implement incremental models
* Deploy the Streamlit dashboard to the cloud
* Add automated data pipeline orchestration

---
