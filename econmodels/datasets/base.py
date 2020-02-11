import pandas as pd
import random

"""
Returns a dataframe with media spend by day for a hotel with KPI's
Enquiries, Books and Revenue. A randomseed can be set to modify the
base dataset
"""
def load_hotel(randomseed=1234):
    random.seed(randomseed)
    df = pd.read_csv('hotel.csv',index_cols='Date')
    return df
