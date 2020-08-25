#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:29:32 2020

@author: morgan
"""

import pandas as pd
import numpy as np

dfm = pd.read_csv('postfpl_am.csv')

#xg and xa per 90
dfm['xG/90'] = (dfm.xG / dfm.Time) * 90
dfm['xA/90'] = (dfm.xA / dfm.Time) * 90
dfm['xGI/90'] = (dfm.xGI / dfm.Time) * 90

#removing relageted teams
dfm = dfm[dfm.Team != 'WAT ']
dfm = dfm[dfm.Team != 'BOU ']      
dfm = dfm[dfm.Team != 'NOR ']

#removing people who barely played or had v low xg
dfm = dfm[dfm['xG/90'] > 0.02 ]
dfm = dfm[dfm['Time'] > 100 ]

#creating xValue/90
dfm['xPoints'] = (dfm.xG * 5) + (dfm.xA * 3)
dfm["xValue"] = (dfm.xPoints / dfm.Price)
dfm['xValue/90'] = (dfm.xValue / dfm.Time) * 90
dfm['xValue/App'] = (dfm.xValue / dfm.App)



 



#Doing same for forawards data

df = pd.read_csv('postfpl_af.csv')



#xg and xa per 90
df['xG/90'] = (df.xG / df.Time) * 90
df['xA/90'] = (df.xA / df.Time) * 90
df['xGI/90'] = (df.xGI / df.Time) * 90

#removing relageted teams
df = df[df.Team != 'WAT ']
df = df[df.Team != 'BOU ']      
df = df[df.Team != 'NOR ']

#removing people who barely played or had v low xg
df = df[df['xG/90'] > 0.02 ]
df = df[df['Time'] > 100 ]

#creating xValue/90
df['xPoints'] = (df.xG * 4) + (df.xA * 3)
df["xValue"] = (df.xPoints / df.Price)
df['xValue/90'] = (df.xValue / df.Time) * 90
df['xValue/App'] = (df.xValue / df.App)


df_ = pd.concat([dfm, df])
df_ = pd.concat([dfm, df], ignore_index=True)

df_.to_csv("cleanpostfpl_a.csv", index = False)

