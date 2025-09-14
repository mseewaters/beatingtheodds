## Predictive models for NFL games to enable spread betting.

General approach:  Create rankings based on historical games using pagerank algorithm.  Use rankings as of the prior week to predict game spreads using only readily available information.

## Basic data preparation is done in standalone notebooks and written to csv files

dataprep.ipynb
- data source: https://www.aussportsbetting.com/data/historical-nfl-results-and-odds-data/
- data input: data\nfl_games_raw.csv
- data output:  data\nfl_games.csv

dataprep_pfr.ipynb
- data source: https://www.pro-football-reference.com/years/2024/games.htm
- data input: data\nfl_games_pfr_raw.csv
- data output: data\nfl_games_pfr.csv


## Ranks are calculated using page rank and features created using a combination of these

Options:  single win/loss ranking, iterative strength of schedule

## Predictive models are built using ranking features (regression:  target = spread; classification: target = winner)

packages
pandas (import pandas as pd)
networkx (import networkx as nx)
seaborn (import seaborn as sns)
matplotlib (import matplotlib.pyplot as plt)
numpy (import numpy as np)
scikit-learn (from sklearn.model_selection import train_test_split, KFold, from sklearn.feature_selection import RFE, from sklearn.metrics import mean_squared_error, accuracy_score, r2_score, from sklearn.preprocessing import StandardScaler)
scipy (from scipy.stats.mstats import winsorize)

