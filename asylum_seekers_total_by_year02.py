import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'asylum-decisions.csv'
df = pd.read_csv(file_path)

# Filter the data for the years since 2015
df_recent = df[df['Year'] >= 2015]

# Group by year and country of asylum, then sum the 'Recognized decisions'
grouped = df_recent.groupby(['Year', 'Country of asylum'])['Recognized decisions'].sum().reset_index()

# Find the top 20 countries (excluding Canada) with the most recognized decisions since 2015
top_countries = (grouped.groupby('Country of asylum')['Recognized decisions']
                 .sum().sort_values(ascending=False).head(21).index.tolist())

# Exclude Canada from the top 20 countries list
top_countries = [country for country in top_countries if country != 'Canada']

# Filter the data for these top countries and Canada
filtered_data = grouped[grouped['Country of asylum'].isin(top_countries + ['Canada'])]

# Pivot the data for plotting
pivot_df = filtered_data.pivot(index='Year', columns='Country of asylum', values='Recognized decisions').fillna(0)

# Plot the data with adjustments
plt.figure(figsize=(14, 8))

# Plot very light grey lines for top 20 countries
for country in top_countries:
    plt.plot(pivot_df.index, pivot_df[country], color='lightgrey', alpha=0.8, linewidth=1)

# Plot the bright orange line for Canada, thicker
plt.plot(pivot_df.index, pivot_df['Canada'], color='orange', linewidth=3, label='Canada')

plt.title('Recognized Decisions for Asylum Seekers by Year (Canada vs Top 20 Countries)')
plt.xlabel('Year')
plt.ylabel('Recognized Decisions')
plt.legend()
plt.tight_layout()
plt.show()
