import pandas as pd
import plotly.graph_objects as go

# Load the dataset
file_path = 'asylum-decisions.csv'
df = pd.read_csv(file_path)

# Filter the data for Canada
df_canada = df[df['Country of asylum'] == 'Canada']

# Group by year and country of origin, summing recognized decisions
df_canada_grouped = df_canada.groupby(['Year', 'Country of origin'])['Recognized decisions'].sum().reset_index()

# Pivot the data for the alluvial chart
pivot_df = df_canada_grouped.pivot(index='Year', columns='Country of origin', values='Recognized decisions').fillna(0)

# Sort columns by total recognized decisions over the years
sorted_columns = pivot_df.sum().sort_values(ascending=False).index
pivot_df = pivot_df[sorted_columns]

# Create the alluvial chart
fig = go.Figure()

for column in pivot_df.columns:
    fig.add_trace(go.Scatter(
        x=pivot_df.index,
        y=pivot_df[column].cumsum(),
        fill='tonexty',
        name=column,
        hoverinfo='x+y+name'
    ))

fig.update_layout(
    title="Alluvial Chart of Recognized Decisions for Asylum Seekers to Canada by Year and Country of Origin",
    xaxis_title="Year",
    yaxis_title="Cumulative Recognized Decisions",
    hovermode="x unified"
)

fig.show()

