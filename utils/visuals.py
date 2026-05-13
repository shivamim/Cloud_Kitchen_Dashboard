# utils/visuals.py

import plotly.express as px
import plotly.graph_objects as go


def revenue_vs_ebitda(df):

    fig = px.scatter(
        df,
        x='NET_REVENUE',
        y='KITCHEN EBITDA',
        color='VARIANCE_BUCKET',
        size='ORDER COUNT',
        hover_data=['STORE'],
        title='Revenue vs EBITDA Analysis'
    )

    return fig


def monthly_trend(df):

    trend = df.groupby('MONTH').agg({
        'NET_REVENUE': 'sum',
        'KITCHEN EBITDA': 'sum'
    }).reset_index()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=trend['MONTH'],
        y=trend['NET_REVENUE'],
        mode='lines+markers',
        name='Revenue'
    ))

    fig.add_trace(go.Scatter(
        x=trend['MONTH'],
        y=trend['KITCHEN EBITDA'],
        mode='lines+markers',
        name='EBITDA'
    ))

    fig.update_layout(title='Monthly Revenue & EBITDA Trend')

    return fig


def top_ebitda_stores(df):

    top = (
        df.groupby('STORE')['KITCHEN EBITDA']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x='KITCHEN EBITDA',
        y='STORE',
        orientation='h',
        title='Top 10 Stores by EBITDA'
    )

    return fig


def variance_distribution(df):

    fig = px.histogram(
        df,
        x='VARIANCE_PERCENT',
        color='VARIANCE_BUCKET',
        title='Variance Distribution'
    )

    return fig