import pandas as pd
import numpy as np
import re
import os

# Paths
RAW_DIR = "data/raw/"
PROCESSED_DIR = "data/processed/"
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_data(filename="genz_social_media_usage_1M.csv"):
    df = pd.read_csv(
        os.path.join(RAW_DIR, filename),
        encoding="latin-1"
    )
    return df

def clean_data(df):
    # Rename for clarity (this isn't Twitter data, but social media usage data)
    df.columns = df.columns.str.lower().str.strip()

    # Drop rows missing key fields
    df = df.dropna(subset=["mental_health_score", "addiction_level", "primary_platform"])

    # Normalize text columns
    df["gender"] = df["gender"].str.strip().str.title()
    df["country"] = df["country"].str.strip().str.title()
    df["primary_platform"] = df["primary_platform"].str.strip().str.title()
    df["purpose"] = df["purpose"].str.strip().str.title()

    # Convert addiction_level to numeric for analysis
    addiction_map = {"Low": 1, "Medium": 2, "High": 3}
    df["addiction_level_numeric"] = df["addiction_level"].map(addiction_map)

    # Ensure numeric columns are correct types
    numeric_cols = [
        "age", "daily_usage_hours", "num_platforms_used",
        "avg_session_minutes", "mental_health_score",
        "night_usage", "screen_time_before_sleep"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop any rows where numeric conversion failed on key columns
    df = df.dropna(subset=["mental_health_score", "daily_usage_hours"])

    return df

social_media_df = load_data()
social_media_df = clean_data(social_media_df)
social_media_df.to_csv(os.path.join(PROCESSED_DIR, "social_cleaned.csv"), index=False)