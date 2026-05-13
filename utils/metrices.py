import pandas as pd


def calculate_metrics(df):

    metrics = {
        'Total Revenue': round(df['NET_REVENUE'].sum(), 2),
        'Total EBITDA': round(df['KITCHEN EBITDA'].sum(), 2),
        'Average GM %': round(df['GM_PERCENT'].mean(), 2),
        'Average EBITDA %': round(df['EBITDA_PERCENT'].mean(), 2),
        'Average Variance %': round(df['VARIANCE_PERCENT'].mean(), 2),
        'Active Stores': df['STORE'].nunique(),
        'Loss Making Stores': df[df['KITCHEN EBITDA'] < 0]['STORE'].nunique()
    }

    return metrics