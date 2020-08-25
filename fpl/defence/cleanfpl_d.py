#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:23:22 2020

@author: morgan
"""

import pandas as pd
import numpy as np

df = pd.read_csv('fpl_d.csv')

df["Value"] = (df.Points / df.Price)
df['Value/90'] = (df.Value / df.Time) * 90
df['Value/App'] = (df.Value / df.Appearances)

df['BP/90'] = (df.BP / df.Time) * 90


#xg and xa per 90
df['xG/90'] = (df.xG / df.Time) * 90
df['xA/90'] = (df.xA / df.Time) * 90


#removing relageted teams
df = df[df.Team != 'WAT ']
df = df[df.Team != 'BOU ']      
df = df[df.Team != 'NOR ']

#removing people who barely played or had v low xg

df = df[df['Time'] > 700 ]

#creating xValue/90
df['xPoints'] = (df.xG * 6) + (df.xA * 3)
df["xValue"] = (df.xPoints / df.Price)
df['xValue/90'] = (df.xValue / df.Time) * 90
df['xValue/App'] = (df.xValue / df.Appearances)



df.to_csv("cleanfpl_d.csv", index = False)