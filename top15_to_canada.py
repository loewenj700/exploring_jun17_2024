import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'asylum-decisions.csv'
df = pd.read_csv(file_path)

# Filter the data for Canada and the desired years
df_canada = df[(df['Country of asylum'] == 'Canada') & (df['Year'] >= 2015) & (df['Year'] <= 2023)]

# Exclude "Unknown" entries
df_canada = df_canada[df_canada['Country of origin'].str.strip().str.lower() != 'unknown']

# Group by country of origin, summing recognized decisions
df_total_decisions = df_canada.groupby('Country of origin')['Recognized decisions'].sum().reset_index()

# Sort by total recognized decisions and select top 15
df_top_15 = df_total_decisions.nlargest(15, 'Recognized decisions')

# Create the horizontal bar chart using Plotly Express
fig = px.bar(df_top_15,
             x='Recognized decisions',
             y='Country of origin',
             orientation='h',
             title='Top 15 Countries by Total Recognized Decisions for Asylum Seekers to Canada (2015-2023)',
             labels={'Recognized decisions': 'Total Recognized Decisions', 'Country of origin': 'Country of Origin'})

# Update the layout to ensure the largest is at the top
fig.update_layout(xaxis_title='Total Recognized Decisions', yaxis_title='Country of Origin', yaxis=dict(categoryorder='total ascending'), hovermode='y')

fig.show()


