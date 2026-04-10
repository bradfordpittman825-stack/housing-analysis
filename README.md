# Post-Pandemic Housing Market Analysis

## Overview
An end-to-end data analysis project examining how the COVID-19 pandemic 
reshaped the U.S. housing market. Built using Python, SQL, and Power BI.

## Key Findings
- National median home values increased **45% between 2019 and 2024**
- Montana and Idaho saw the largest price surges (63%+), driven by remote work migration
- 2023-2025 mortgage rates are the highest since 2000, yet prices remain elevated
- Sun Belt and Mountain West states dominated post-COVID appreciation

## Tools Used
- **Python** (Pandas, NumPy) — data cleaning and analysis
- **SQLite + SQLAlchemy** — data storage and querying
- **Power BI** — interactive dashboard (see below)

## Data Sources
- [Zillow Research Data](https://www.zillow.com/research/data/) — State-level median home values
- [FRED](https://fred.stlouisfed.org/series/MORTGAGE30US) — 30-year fixed mortgage rates

## Project Structure
- `clean.py` — loads, merges, and cleans raw data
- `analyze.py` — generates analytical output CSVs
- `load_sql.py` — loads data into SQLite database
- `queries.py` — SQL queries answering key business questions