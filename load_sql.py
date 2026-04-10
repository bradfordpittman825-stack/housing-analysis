import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine('sqlite:///housing.db')

# Load cleaned data
df = pd.read_csv('housing_cleaned.csv')
national = pd.read_csv('output_national_trend.csv')
covid = pd.read_csv('output_covid_comparison.csv')
rates = pd.read_csv('output_rates_vs_values.csv')

# Write each to its own table in the database
df.to_sql('housing_data', engine, if_exists='replace', index=False)
national.to_sql('national_trend', engine, if_exists='replace', index=False)
covid.to_sql('covid_comparison', engine, if_exists='replace', index=False)
rates.to_sql('rates_vs_values', engine, if_exists='replace', index=False)

print("All tables loaded successfully!")