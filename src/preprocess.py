import pandas as pd
import numpy as np
import re
import os

# Paths
RAW_DIR = "data/raw/"
PROCESSED_DIR = "data/processed/"
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_data(filename="genz_social_edia_usage_1M.csv"):
    df = pd.read_csv(
        os.path.join(RAW_DIR, filename),
        encoding="latin-1",
        header=None,
        names=["polarity", "id", "date", "query", "user", "text"]
    )
    return df

