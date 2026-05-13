# utils/preprocessing.py

import pandas as pd
import numpy as np


def load_data(path):
    df = pd.read_excel(path)

    # Fix headers if required
    df.columns = [str(col).strip().upper() for col in df.columns]

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert month
    if 'MONTH' in df.columns:
        df['MONTH'] = pd.to_datetime(df['MONTH'])

    # Fill missing values
    numeric_cols = df.select_dtypes(include=np.number).columns
    categorical_cols = df.select_dtypes(include='object').columns

    df[numeric_cols] = df[numeric_cols].fillna(0)
    df[categorical_cols] = df[categorical_cols].fillna('Unknown')

    return df


def feature_engineering(df):

    # GM %
    if 'GROSS MARGIN' in df.columns and 'NET_REVENUE' in df.columns:
        df['GM_PERCENT'] = np.where(
            df['NET_REVENUE'] != 0,
            (df['GROSS MARGIN'] / df['NET_REVENUE']) * 100,
            0
        )

    # EBITDA %
    if 'KITCHEN EBITDA' in df.columns:
        df['EBITDA_PERCENT'] = np.where(
            df['NET_REVENUE'] != 0,
            (df['KITCHEN EBITDA'] / df['NET_REVENUE']) * 100,
            0
        )

    # AOV
    if 'ORDER COUNT' in df.columns:
        df['AOV'] = np.where(
            df['ORDER COUNT'] != 0,
            df['NET_REVENUE'] / df['ORDER COUNT'],
            0
        )

    # Discount %
    if 'DISCOUNT' in df.columns and 'CART SALES' in df.columns:
        df['DISCOUNT_PERCENT'] = np.where(
            df['CART SALES'] != 0,
            (df['DISCOUNT'] / df['CART SALES']) * 100,
            0
        )

    # Variance %
    if 'VARIANCE' in df.columns and 'IDEAL FOOD COST' in df.columns:
        df['VARIANCE_PERCENT'] = np.where(
            df['IDEAL FOOD COST'] != 0,
            (df['VARIANCE'] / df['IDEAL FOOD COST']) * 100,
            0
        )

    # Variance Buckets
    conditions = [
        df['VARIANCE_PERCENT'] < 2,
        (df['VARIANCE_PERCENT'] >= 2) & (df['VARIANCE_PERCENT'] < 3),
        (df['VARIANCE_PERCENT'] >= 3) & (df['VARIANCE_PERCENT'] < 5),
        df['VARIANCE_PERCENT'] >= 5
    return df