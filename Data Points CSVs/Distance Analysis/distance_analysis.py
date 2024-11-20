#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:59:09 2022

@author: paulpiercejr
"""

import pandas as pd
from os import path
import numpy as np
from functools import reduce
import csv

DATA_PATH = '/Data Points CSVs/'

# load driving distance data
df_distance = pd.read_csv(path.join(DATA_PATH, 'driving_distance.csv'))

# load strokes gained total data
df_sg_total = pd.read_csv(path.join(DATA_PATH,'sg_total.csv'))
df_sg_approach = pd.read_csv(path.join(DATA_PATH,'sg_approach_green.csv'))
df_sg_putting = pd.read_csv(path.join(DATA_PATH,'sg_putting.csv'))
df_sg_off_tee = pd.read_csv(path.join(DATA_PATH,'sg_off_tee.csv'))
df_sg_tee_to_green = pd.read_csv(path.join(DATA_PATH,'sg_tee_to_green.csv'))
df_stroke_diff_v_field = pd.read_csv(path.join(DATA_PATH,'stroke_differential_field_avg.csv'))
df_top_tens = pd.read_csv(path.join(DATA_PATH,'top_tens2.csv'))
df_total_distance_drives = pd.read_csv(path.join(DATA_PATH,'total_distance_drives2.csv'))
df_proximity_to_hole = pd.read_csv(path.join(DATA_PATH,'proximity_to_hole.csv'))
df_driving_accuracy = pd.read_csv(path.join(DATA_PATH,'driving_accuracy.csv'))
df_missed_fairway_other = pd.read_csv(path.join(DATA_PATH,'missed_fairway_other.csv'))
df_total_putting = pd.read_csv(path.join(DATA_PATH,'total_putting.csv'))

df_total_distance_drives['player_name'].replace('\n','',regex=True, inplace=True)
df_distance['player_name'].replace('\n','',regex=True, inplace=True)
df_sg_total['player_name'].replace('\n','',regex=True, inplace=True)
df_sg_approach['player_name'].replace('\n','',regex=True, inplace=True)
df_sg_putting['player_name'].replace('\n','',regex=True, inplace=True)
df_sg_off_tee['player_name'].replace('\n','',regex=True, inplace=True)
df_sg_tee_to_green['player_name'].replace('\n','',regex=True, inplace=True)
df_stroke_diff_v_field['player_name'].replace('\n','',regex=True, inplace=True)
df_top_tens['player_name'].replace('\n','',regex=True, inplace=True)
df_proximity_to_hole['player_name'].replace('\n','',regex=True, inplace=True)
df_driving_accuracy['player_name'].replace('\n','',regex=True, inplace=True)
df_missed_fairway_other['player_name'].replace('\n','',regex=True, inplace=True)
df_total_putting['player_name'].replace('\n','',regex=True, inplace=True)

driving_total = pd.merge(df_distance,df_total_distance_drives, how='outer', on=['year','player_name'])
driving_total.to_csv(path.join(DATA_PATH,'aggregates2','driving_total.csv'))
df_total_distance_drives.dtypes
df_sg_total.dtypes
df_total_distance_drives['player_name'] = df_total_distance_drives['player_name'].astype(str)
df_total_distance_drives.to_csv(path.join(DATA_PATH,'total_distance_drives2.csv'),quoting=csv.QUOTE_NONNUMERIC,escapechar="\\",doublequote=False,index=False)
df_top_tens.to_csv(path.join(DATA_PATH,'top_tens2.csv'),quoting=csv.QUOTE_NONNUMERIC,escapechar="\\",doublequote=False,index=False)

# create large data frame of all data
# define list of dataframes
dfs = [df_sg_total,df_sg_approach,df_sg_putting,df_sg_off_tee,df_sg_tee_to_green,df_proximity_to_hole,df_stroke_diff_v_field,df_top_tens2,df_distance,df_total_distance_drives2,df_driving_accuracy,df_missed_fairway_other,df_total_putting]

stats = reduce(lambda left, right: pd.merge(left,right,on=['year','player_name'], how='outer'),dfs)
stats.columns
stats.to_csv(path.join(DATA_PATH,'aggregates2','full_stats.csv'))


# merge distance & sg total distance together - merge on year and player_name
df_distance.columns
df_sg_total.columns

df_distance_sg_tot = pd.merge(df_distance, df_sg_total, how='left', on=['year','player_name'])

df_distance_sg_tot = df_distance_sg_tot.loc[(df_distance_sg_tot['year'] >= 2004)]
df_distance_sg_tot.reset_index(drop=True, inplace = True)

df_distance_sg_tot.to_csv(path.join(DATA_PATH,'aggregates2','distance_sg_total.csv'))

print(df_distance_sg_tot)

df_distance_sg_tot.plot.scatter(x="distance_avg", y="average")

df_distance_sg_tot.loc[(df_distance_sg_tot['year'] == 2021)].plot.scatter(x="distance_avg", y="average")


#df_sg_approach = pd.read_csv(path.join(DATA_PATH,'sg_approach_green.csv'))

df_distance_sg_green = pd.merge(df_distance, df_sg_approach, how='left', on=['year','player_name'])
df_distance_sg_green = df_distance_sg_green.loc[(df_distance_sg_green['year'] >= 2004)]
df_distance_sg_green.to_csv(path.join(DATA_PATH,'aggregates2','distance_sg_green.csv'))

df_distance_sg_green.columns

df_distance_sg_green.plot.scatter(x="distance_avg", y="sg_app_green_avg")

#df_sg_putting = pd.read_csv(path.join(DATA_PATH,'sg_putting.csv'))

df_distance_putting = pd.merge(df_distance, df_sg_putting, how='left', on=['year','player_name'])
df_distance_putting = df_distance_putting.loc[(df_distance_putting['year']>= 2004)]
df_distance_putting.to_csv(path.join(DATA_PATH,'aggregates2','distance_putting.csv'))

df_distance_putting.columns
df_distance_putting.plot.scatter(x="distance_avg", y="sg_putting_avg")

# strokes gain total and sg putting
df_sg_tot_putting = pd.merge(df_sg_total, df_sg_putting, how='left', on=['year','player_name'])
df_sg_tot_putting = df_sg_tot_putting.loc[(df_sg_tot_putting['year']>=2004)]
df_sg_tot_putting.to_csv(path.join(DATA_PATH,'aggregates2','sg_total_putting.csv'))
df_sg_tot_putting.columns
df_sg_tot_putting.plot.scatter(y="average", x="sg_putting_avg")


# mean, median, mode
# golfer in a specific year who averages between 290 and 292 etc
# median strokes gain total for each distance 290 - <291
df_distance_sg_tot.loc[(df_distance_sg_tot['distance_avg']>=310) & (df_distance_sg_tot['distance_avg']<350) & (df_distance_sg_tot['year']==2019)].min()

df_distance_sg_tot_filtered = df_distance_sg_tot[['year','player_name','distance_avg','average']]

df_distance_sg_tot_filtered



smallest = 258
largest = 324
edges = 34
ind = np.digitize(df_distance_sg_tot_filtered['distance_avg'], np.linspace(smallest, largest, edges))
ind

df_distance_sg_tot_filtered['bin'] = ind

df_distance_sg_tot_filtered.to_csv(path.join(DATA_PATH,'aggregates2','distance_total_filtered_2004.csv'))

# create new DF with year and distance join to get mean, median, min, max of sg_total
df_distance_sg_tot_filtered_groups = df_distance_sg_tot_filtered.groupby(['year','bin']).median()
print(df_distance_sg_tot_filtered_groups)

df_distance_sg_tot_filtered_groups.to_csv(path.join(DATA_PATH,'aggregates2','distance_groups.csv'))

df_distance_sg_grouped = pd.read_csv(path.join(DATA_PATH,'aggregates2','distance_groups.csv'))

df_distance_sg_grouped.columns


df_distance_sg_grouped.loc[(df_distance_sg_grouped['year'] == 2021)].plot.scatter(x="distance_avg", y="average")




#
