# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from pyxirr import xirr
def create_xirr(df_cad, n = 2):
    j = 0
    xirr_ = []
    dates_ = pd.to_datetime(df_cad['Date'])
    dates2 = []
    while j < len(df_cad['Actual Cashflow'])-(n-1):
        temp = [-df_cad['Value'][j], df_cad['Actual Cashflow'][j], df_cad['Actual Cashflow'][j+(n-1)], df_cad['Value'][j+(n-1)]]
        dates = [dates_[j],dates_[j],dates_[j+(n-1)],dates_[j+(n-1)]]
    #     print(dates)
        dates2.append(df_cad["Date"][j+(n-1)])
    #     print(temp)
        date_diff = (dates_[j+n-1]-dates_[j]) /  pd.Timedelta(days=(n-1))
#         print(date_diff)
        xirr_.append(xirr(dates,temp)*(date_diff)/365)
        j += (n-1)
    return xirr_, dates2

def create_quarterly_ac(df1, n = 3):
    i = 0
    # new_date = []
    # new_value = []
    # new_actual = []
    df_list_cad = []
    while i < len(df1.Date):
        temp = []
        temp.append(df1.Date[i+(n-1)])
        temp.append(df1.Value[i+(n-1)])
        temp.append(df1['Actual Cashflow'][i:i+n].sum())
        df_list_cad.append(temp)
        i += n # i = i + 3
    df_cad = pd.DataFrame(df_list_cad, columns=['Date', 'Value', 'Actual Cashflow'])
    return df_cad
