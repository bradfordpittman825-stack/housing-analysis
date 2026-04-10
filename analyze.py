import pandas as pd

df = pd.read_csv('housing_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

# --- 1. National average home value over time ---
national = df.groupby('date')['median_home_value'].mean().reset_index()
national.to_csv('output_national_trend.csv', index=False)
print("National trend saved.")

# --- 2. Pre vs Post COVID comparison (2019 vs 2023) ---
pre_covid = df[df['date'].dt.year == 2019].groupby('state')['median_home_value'].mean()
post_covid = df[df['date'].dt.year == 2023].groupby('state')['median_home_value'].mean()
covid_comparison = pd.DataFrame({
    'pre_covid_avg': pre_covid,
    'post_covid_avg': post_covid
}).reset_index()
covid_comparison['pct_change'] = (
    (covid_comparison['post_covid_avg'] - covid_comparison['pre_covid_avg'])
    / covid_comparison['pre_covid_avg'] * 100
).round(2)
covid_comparison = covid_comparison.sort_values('pct_change', ascending=False)
covid_comparison.to_csv('output_covid_comparison.csv', index=False)
print("COVID comparison saved.")
print(covid_comparison.head(10))

# --- 3. Mortgage rate vs national home value correlation ---
national_with_rates = df.groupby('date').agg(
    avg_home_value=('median_home_value', 'mean'),
    mortgage_rate=('mortgage_rate', 'mean')
).reset_index()
national_with_rates.to_csv('output_rates_vs_values.csv', index=False)
correlation = national_with_rates['avg_home_value'].corr(
    national_with_rates['mortgage_rate']
)
print(f"\nCorrelation between mortgage rates and home values: {correlation:.3f}")