import csv
import sys

def main():
    # Get season from command line argument, default to 2025
    season = 2025
    if len(sys.argv) > 1:
        try:
            season = int(sys.argv[1])
        except ValueError:
            print(f"Invalid season '{sys.argv[1]}', using default 2025")

    input_file = 'data/nfl_games_pfr_raw.csv'
    output_file = 'data/games_dates_season_extracted.csv'

    # Column names from the raw file
    date_col = 'Date'
    week_col = 'Week'

    # Use a set to track unique dates and store the data
    unique_dates = {}

    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            date = row[date_col]
            week = row[week_col]
            # Store date with its corresponding week (first occurrence wins)
            if date not in unique_dates:
                unique_dates[date] = week

    # Write the aggregated data
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        # Write header to match expected format
        writer.writerow(['', 'Date', 'season', 'week'])
        for date, week in sorted(unique_dates.items()):
            # Write index 0, date, season (from parameter), and week
            writer.writerow([0, date, season, week])

    print(f"Extracted games info to {output_file} with season {season}")

if __name__ == "__main__":
    main()