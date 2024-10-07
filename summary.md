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

