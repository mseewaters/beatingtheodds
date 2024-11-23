
#Load the game data to pandas data frame
df  = pd.read_csv('../data/nfl_games.csv')

# 1. Create Wins DataFrame
wins = df[['season', 'winner']].rename(columns={'winner': 'team'})
wins['wins'] = 1
wins_agg = wins.groupby(['season', 'team'], as_index=False)['wins'].sum()

# 2. Create Losses DataFrame
losses = df[['season', 'loser']].rename(columns={'loser': 'team'})
losses['losses'] = 1
losses_agg = losses.groupby(['season', 'team'], as_index=False)['losses'].sum()

# 3. Merge Wins and Losses
record = pd.merge(wins_agg, losses_agg, on=['season', 'team'], how='outer').fillna(0)

# 4. Convert to Integer
record['wins'] = record['wins'].astype(int)
record['losses'] = record['losses'].astype(int)

# 5. (Optional) Sort the DataFrame for better readability
record = record.sort_values(['season', 'losses']).reset_index(drop=True)

print(record.to_string(index=False))


#Create a directed graph
G = nx.DiGraph()

# Use dictionaries to store total margin and count of games
margin_totals = defaultdict(float)
game_counts = defaultdict(int)

df_filtered = df[(df['Season'] == 2024) & (df['Week'] <= 18)]

#Add edges to the graph
for index, row in df_filtered.iterrows():
    winner = row['Winner']
    loser = row['Loser']
    week = row['Week']
    margin = row['Margin_Perc']*100*week/18

    key = (loser, winner)
    margin_totals[key] += margin
    game_counts[key] += 1

# Calculate average margin and add edges
for (loser, winner), total_margin in margin_totals.items():
    avg_margin = total_margin / game_counts[(loser, winner)]
    G.add_edge(loser, winner, weight=avg_margin)

print("Graph Info:", G.number_of_nodes(), G.number_of_edges())  
# print("Nodes:", G.nodes())
# print("Edges:", G.edges())

team_rankings = nx.pagerank(G, alpha=0.9, weight='weight')
ranking_df = pd.DataFrame(list(team_rankings.items()), columns=['Team', 'Rank']).sort_values(by='Rank', ascending=False)
print(ranking_df)


filtered_played = merged_played[merged_played['Delta_ScoreRank'].abs() >= 0.00]

# Print the results DataFrame
print(results.to_csv(index=False))