#!/usr/bin/env python

import pandas as pd
from collections import defaultdict


data = pd.read_csv('kmeans_result.csv')


names = data[['Country Code', 'Country Name']] 

country_name = defaultdict()
country_details = defaultdict()
for d in data.iterrows():
    code = d[1][0]
    country = d[1][1]
    year1 = d[1][2]
    year5 = d[1][3]
    year1 = f'Class {year1[-1]}'
    year5 = f'Class {year5[-1]}'
    #print(f'"{code}": ["{country}", "{year1}", "{year5}"],')
    #print(f'"{country}": "{code}",')
    country_name[country] = code
    country_details[code] = [country, year1, year5]

print(country_details['ZWE'][1:3])




