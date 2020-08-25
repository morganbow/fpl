#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:45:10 2020

@author: morgan
"""

import pandas as pd
import numpy as np

df = pd.read_csv('fpl_g.csv')

df["Value"] = (df.Points / df.Price)
df['Value/90'] = (df.Value / df.Time) * 90
df['Value/App'] = (df.Value / df.App)

df['Saves/90'] = (df.Saves / df.Time) * 90
df['BP/90'] = (df.BP / df.Time) * 90



#removing relageted teams
df = df[df.Team != 'WAT ']
df = df[df.Team != 'BOU ']      
df = df[df.Team != 'NOR ']

#removing people who barely played or had v low xg

df = df[df['Time'] > 800 ]


df.to_csv("cleanfpl_g.csv", index = False)