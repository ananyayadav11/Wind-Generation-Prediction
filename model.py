import numpy as np
import pandas as pd
import xgboost as xgb
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained model from pickle
model = pickle.load(open(os.path.join(BASE_DIR, 'model2.pkl'), "rb"))

# Function to create features from datetime index
def create_f(df):
    df = df.copy()
    df['hour'] = df.index.hour
    df['minute'] = df.index.minute
    df['day'] = df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofweek'] = df.index.dayofweek
    df['dayofyear'] = df.index.dayofyear
    df['weekofyear'] = df.index.isocalendar().week
    return df

# Function to create prediction DataFrame from user input
def create_pd(fr, to):
    new_index = pd.date_range(fr + ' 12:00:00+00:00', to + ' 12:00:00+00:00', freq='10min')
    new_df = pd.DataFrame(index=new_index)
    new_df = create_f(new_df)
    return new_df
