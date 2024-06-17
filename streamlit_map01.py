import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'asylum-decisions.csv'
df = pd.read_csv(file_path)

# Filter the data for Canada and exclude "Unknown" entries
df_canada = df[(df['Country of asylum'] == 'Canada') & (df['Country of origin'] != 'Unknown')]

# Streamlit app
st.subheader('Choropleth Map of Asylum Seekers to Canada')
st.sidebar.title('Filter')

# Dropdown for selecting year
year = st.sidebar.selectbox('Select Year', df_canada['Year'].unique())

# Filter data for the selected year
df_year = df_canada[df_canada['Year'] == year]

# Group by country of origin
df_grouped = df_year.groupby('Country of origin')['Recognized decisions'].sum().reset_index()

# Add Canada to the dataframe with a separate value to highlight it
df_canada_highlight = pd.DataFrame({'Country of origin': ['Canada'], 'Recognized decisions': [0]})
df_grouped = pd.concat([df_grouped, df_canada_highlight], ignore_index=True)

# Create choropleth map
fig = px.choropleth(df_grouped,
                    locations="Country of origin",
                    locationmode='country names',
                    color="Recognized decisions",
                    hover_name="Country of origin",
                    color_continuous_scale=px.colors.sequential.YlOrRd,
                    title=f'Choropleth Map of Asylum Seekers to Canada in {year}')

# Highlight Canada in green
fig.add_scattergeo(
    locations=['Canada'],
    locationmode='country names',
    marker=dict(color='green', size=10),
    name='Canada'
)

# Display the choropleth map
st.plotly_chart(fig)

