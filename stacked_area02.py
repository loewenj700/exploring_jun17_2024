import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'asylum-decisions.csv'
df = pd.read_csv(file_path)

# Filter the data for Canada and exclude "Unknown" entries
df_canada = df[(df['Country of asylum'] == 'Canada') & (df['Country of origin'] != 'Unknown')]

# Group by year and country of origin, summing recognized decisions
df_canada_grouped = df_canada.groupby(['Year', 'Country of origin'])['Recognized decisions'].sum().reset_index()

# Sort countries by total recognized decisions over the years and select top 10
top_countries = df_canada_grouped.groupby('Country of origin')['Recognized decisions'].sum().nlargest(10).index
df_top_countries = df_canada_grouped[df_canada_grouped['Country of origin'].isin(top_countries)]

# Create the stacked area chart using Plotly Express
fig = px.area(df_top_countries,
              x='Year',
              y='Recognized decisions',
              color='Country of origin',
              title="Stacked Area Chart of Recognized Decisions for Asylum Seekers to Canada by Year and Country of Origin (Top 10 Countries)")

fig.update_layout(xaxis_title="Year", yaxis_title="Recognized Decisions", hovermode="x unified")

fig.show()



