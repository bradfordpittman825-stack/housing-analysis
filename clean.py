import pandas as pd

# --- Load Zillow Data ---
zillow = pd.read_csv('zillow_state.csv')

# Keep only state name and price columns (drop ID/rank columns)
zillow = zillow.drop(columns=['RegionID', 'SizeRank', 'SizeRank'])

# Melt from wide format to long format (one row per state per month)
zillow_long = zillow.melt(
    id_vars=['RegionName', 'RegionType', 'StateName'],
    var_name='date',
    value_name='median_home_value'
)

# Convert date column to datetime
zillow_long['date'] = pd.to_datetime(zillow_long['date'])

# Rename for clarity
zillow_long = zillow_long.rename(columns={'RegionName': 'state'})

# --- Load Mortgage Data ---
mortgage = pd.read_csv('mortgage_rates.csv')
mortgage = mortgage.rename(columns={
    'observation_date': 'date',
    'MORTGAGE30US': 'mortgage_rate'
})
mortgage['date'] = pd.to_datetime(mortgage['date'])

# Resample mortgage to monthly (average rate per month)
mortgage = mortgage.set_index('date').resample('ME').mean().reset_index()

# --- Merge ---
combined = pd.merge(zillow_long, mortgage, on='date', how='left')

# --- Save ---
combined = combined.drop(columns=['StateName', 'RegionType'])
combined = combined.dropna(subset=['median_home_value'])
combined.to_csv('housing_cleaned.csv', index=False)
print("Done! Shape:", combined.shape)
print(combined.head())