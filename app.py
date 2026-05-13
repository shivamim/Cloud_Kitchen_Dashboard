# app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.preprocessing import load_data, feature_engineering
from utils.metrics import calculate_metrics

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title='Cloud Kitchen Financial Intelligence Platform',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    .metric-card {
        background: linear-gradient(135deg, #1f2937, #111827);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #374151;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    .insight-box {
        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #f59e0b;
        margin-bottom: 10px;
    }

    .title-text {
        font-size: 40px;
        font-weight: bold;
        color: white;
    }

    .subtitle-text {
        color: #9CA3AF;
        font-size: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data

def get_data():

    df = load_data('data/Kittchen PNL Data.xlsx')
    df = feature_engineering(df)

    return df


# =====================================================
# DATA
# =====================================================

try:
    df = get_data()
except Exception as e:
    st.error(f'Error loading data: {e}')
    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.image(
    'https://cdn-icons-png.flaticon.com/512/3595/3595455.png',
    width=100
)

st.sidebar.title('Cloud Kitchen Filters')

# Store Filter
store_filter = st.sidebar.multiselect(
    'Select Store',
    options=sorted(df['STORE'].dropna().unique()),
    default=sorted(df['STORE'].dropna().unique())
)

# Month Filter
month_options = sorted(df['MONTH'].dt.strftime('%Y-%m').unique())

month_filter = st.sidebar.multiselect(
    'Select Month',
    options=month_options,
    default=month_options
)

# Revenue Cohort Filter
if 'REVENUE COHORT' in df.columns:

    revenue_cohort_filter = st.sidebar.multiselect(
        'Revenue Cohort',
        options=df['REVENUE COHORT'].dropna().unique(),
        default=df['REVENUE COHORT'].dropna().unique()
    )
else:
    revenue_cohort_filter = []

# Variance Bucket Filter
variance_filter = st.sidebar.multiselect(
    'Variance Bucket',
    options=df['VARIANCE_BUCKET'].unique(),
    default=df['VARIANCE_BUCKET'].unique()
)

# EBITDA Category Filter
if 'EBITDA CATEGORY' in df.columns:

    ebitda_filter = st.sidebar.multiselect(
        'EBITDA Category',
        options=df['EBITDA CATEGORY'].dropna().unique(),
        default=df['EBITDA CATEGORY'].dropna().unique()
    )
else:
    ebitda_filter = []

# Revenue Range
revenue_min = float(df['NET_REVENUE'].min())
revenue_max = float(df['NET_REVENUE'].max())

revenue_range = st.sidebar.slider(
    'Revenue Range',
    revenue_min,
    revenue_max,
    (revenue_min, revenue_max)
)

# EBITDA Range
if 'KITCHEN EBITDA' in df.columns:

    ebitda_min = float(df['KITCHEN EBITDA'].min())
    ebitda_max = float(df['KITCHEN EBITDA'].max())

    ebitda_range = st.sidebar.slider(
        'EBITDA Range',
        ebitda_min,
        ebitda_max,
        (ebitda_min, ebitda_max)
    )

# =====================================================
# APPLY FILTERS
# =====================================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df['STORE'].isin(store_filter)
]

filtered_df = filtered_df[
    filtered_df['MONTH'].dt.strftime('%Y-%m').isin(month_filter)
]

filtered_df = filtered_df[
    filtered_df['VARIANCE_BUCKET'].isin(variance_filter)
]

filtered_df = filtered_df[
    (filtered_df['NET_REVENUE'] >= revenue_range[0]) &
    (filtered_df['NET_REVENUE'] <= revenue_range[1])
]

if 'KITCHEN EBITDA' in filtered_df.columns:

    filtered_df = filtered_df[
        (filtered_df['KITCHEN EBITDA'] >= ebitda_range[0]) &
        (filtered_df['KITCHEN EBITDA'] <= ebitda_range[1])
    ]

if len(revenue_cohort_filter) > 0 and 'REVENUE COHORT' in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df['REVENUE COHORT'].isin(revenue_cohort_filter)
    ]

if len(ebitda_filter) > 0 and 'EBITDA CATEGORY' in filtered_df.columns:

    filtered_df = filtered_df[
        filtered_df['EBITDA CATEGORY'].isin(ebitda_filter)
    ]

# =====================================================
# HEADER
# ==================================