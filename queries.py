import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///housing.db')

queries = {
    "Top 10 most expensive states (latest month)": """
        SELECT state, ROUND(median_home_value, 0) as home_value
        FROM housing_data
        WHERE date = (SELECT MAX(date) FROM housing_data)
        ORDER BY median_home_value DESC
        LIMIT 10
    """,
    "Top 10 biggest COVID price jumps": """
        SELECT state, 
               ROUND(pre_covid_avg, 0) as pre_covid,
               ROUND(post_covid_avg, 0) as post_covid,
               pct_change
        FROM covid_comparison
        ORDER BY pct_change DESC
        LIMIT 10
    """,
    "Years with highest average mortgage rates": """
        SELECT STRFTIME('%Y', date) as year,
               ROUND(AVG(mortgage_rate), 2) as avg_rate
        FROM rates_vs_values
        GROUP BY year
        ORDER BY avg_rate DESC
        LIMIT 10
    """,
    "National home value before and after COVID": """
        SELECT STRFTIME('%Y', date) as year,
               ROUND(AVG(avg_home_value), 0) as avg_national_value
        FROM rates_vs_values
        WHERE STRFTIME('%Y', date) BETWEEN '2018' AND '2024'
        GROUP BY year
        ORDER BY year
    """
}

for title, query in queries.items():
    print(f"\n--- {title} ---")
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
        print(df.to_string(index=False))