import numpy as np
import openpyxl
from openpyxl.styles import Border, Side, Font, PatternFill
import pandas as pd

# Warnings
import warnings
warnings.filterwarnings('ignore')

unemployment_month = pd.read_excel("~/Desktop/unemployment rate 19-21(1).xlsx")
#Drop the data of D.C. and Puerto Rico since they are not included in other datasets.
unemployment_month = unemployment_month.drop([8,51],axis = 0).reset_index(drop=True)
#Since we need the unemployment rate be presented by quarter, we need to divide the 12 months into 4 parts, take the respective means of them, and save the data in columns.
unemployment_month['2019_Q1'] = (unemployment_month['2019-Jan']+unemployment_month['2019-Feb']+unemployment_month['2019-Mar'])/3
unemployment_month['2019_Q2'] = (unemployment_month['2019-Apr']+unemployment_month['2019-May']+unemployment_month['2019-Jun'])/3
unemployment_month['2019_Q3'] = (unemployment_month['2019-Jul']+unemployment_month['2019-Aug']+unemployment_month['2019-Sep'])/3
unemployment_month['2019_Q4'] = (unemployment_month['2019-Oct']+unemployment_month['2019-Nov']+unemployment_month['2019-Dec'])/3
unemployment_month['2020_Q1'] = (unemployment_month['2020-Jan']+unemployment_month['2020-Feb']+unemployment_month['2020-Mar'])/3
unemployment_month['2020_Q2'] = (unemployment_month['2020-Apr']+unemployment_month['2020-May']+unemployment_month['2020-Jun'])/3
unemployment_month['2020_Q3'] = (unemployment_month['2020-Jul']+unemployment_month['2020-Aug']+unemployment_month['2020-Sep'])/3
unemployment_month['2020_Q4'] = (unemployment_month['2020-Oct']+unemployment_month['2020-Nov']+unemployment_month['2020-Dec'])/3
unemployment_month['2021_Q1'] = (unemployment_month['2021-Jan']+unemployment_month['2021-Feb']+unemployment_month['2021-Mar'])/3
unemployment_month['2021_Q2'] = (unemployment_month['2021-Apr']+unemployment_month['2021-May']+unemployment_month['2021-Jun'])/3
unemployment_month['2021_Q3'] = (unemployment_month['2021-Jul']+unemployment_month['2021-Aug']+unemployment_month['2021-Sep'])/3
unemployment_month['2021_Q4'] = (unemployment_month['2021-Oct']+unemployment_month['2021-Nov']+unemployment_month['2021-Dec'])/3
#Create a new dataframe to store these columns that we need.
data = [unemployment_month['2019_Q1'],unemployment_month['2019_Q2'],unemployment_month['2019_Q3'],unemployment_month['2019_Q4'],unemployment_month['2020_Q1'],unemployment_month['2020_Q2'],unemployment_month['2020_Q3'],unemployment_month['2020_Q4'],unemployment_month['2021_Q1'],unemployment_month['2021_Q2'],unemployment_month['2021_Q3'],unemployment_month['2021_Q4']]
headers = ['2019_Q1','2019_Q2','2019_Q3','2019_Q4','2020_Q1','2020_Q2','2020_Q3','2020_Q4','2021_Q1','2021_Q2','2021_Q3','2021_Q4']
unemployment_quarter = pd.concat(data,axis=1,keys = headers)
#data presentation
unemployment_quarter.shape
unemployment_quarter.head()
