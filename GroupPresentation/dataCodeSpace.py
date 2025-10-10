import pandas as pd
import numpy as np
from datetime import date, timedelta
import matplotlib.pyplot as plt
from scipy.stats import linregress


def read_working_hours_data():
    '''
    reads annual-working-hours-per-worker.csv file and parses the year column as a date and sets it as an index
    '''
    working_hours_df = pd.read_csv('Retirement_Age.csv', parse_dates=['Year'],  index_col='Year')
    return working_hours_df
    
working_hours_df =read_working_hours_data()

#dropping all na values pre analysis #think smarter not harder
working_hours_df = working_hours_df.dropna(subset=[
                              'Average annual working hours per worker'])