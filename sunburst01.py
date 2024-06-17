import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
asylum_file_path = 'asylum-decisions.csv'
df_asylum = pd.read_csv(asylum_file_path)

# Filter the data for Canada and exclude "Unknown" entries
df_canada = df_asylum[(df_asylum['Country of asylum'] == 'Canada') & (df_asylum['Country of origin'] != 'Unknown')]

# Create the sunburst chart
fig = px.sunburst(df_canada,
                  path=['Year', 'Country of origin'],
                  values='Recognized decisions',
                  title='Sunburst Chart of Recognized Asylum Seekers to Canada by Year and Country of Origin')

# Update the layout to use the plotly_dark theme
fig.update_layout(
    template='plotly_dark',
    margin=dict(t=40, l=0, r=0, b=0)
)

fig.show()
