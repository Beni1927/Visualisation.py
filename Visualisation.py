# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 14:21:39 2023
@author: beni vimal ravichandran
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./datas.csv')
df = pd.DataFrame({'year':data.year,
                  'UK':data.UK,
                  'Switzerland': data.Switzerland,
                  'Denmark':data.Denmark,
                  'Canada':data.Canada,
                  'country':data.country,
                   'Forest':data.forest,
                   'population':data.population,
                   'CO2 emissions':data.CO2,
                   'Migrant': data.Migrant
                  })
df.dropna(subset=['year','UK','Denmark','Switzerland','Canada','country','Forest','population','CO2 emissions', 'Migrant'], inplace=True)
df['year'] = pd.to_numeric(df['year'])
df['Switzerland'] = pd.to_numeric(df['Switzerland'])
df
ax=df.plot(x='year', y =['UK','Switzerland','Denmark','Canada'])

def line():
    """
    Plot Line graph for the given data

    Parameters
    ----------
    y: float
    x: float
    colors: default: :rc:'lines.color'
    linestyles: 'solid'
    label: str

    Returns
    -------
    'matplotlib.pyplot.plot'
    """
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Trends')
    plt.grid(True)
    plt.show()

def bar():
    """
    Plot bar graph for the given data

    Parameters
    ----------
    y: float
    x: object
    colors: default: :rc:'bars.color'
    label: str

    Returns
    -------
    'matplotlib.pyplot.bar'
    """
    plt.xlabel('Country')
    plt.ylabel('Forest Area')
    plt.title('Forest Area Coverage')
    plt.bar(df.country, df.Forest, color ='green',
        width = 0.4)

def scatter():
    """
    Plots a Scatter plot for the given data

    Parameters
    ----------
    y: float
    x: float
    colors: default: :rc:'lines.color'
    label: str

    Returns
    -------
    'matplotlib.pyplot.scatter'
    """
    df.plot.scatter(x='year',y='Migrant')
    plt.xlabel('Year')
    plt.ylabel('Number of Migrants')
    plt.title('Migration in Australia')
line()
bar()
scatter()

