import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("asylum-decisions.csv")

# Filter data for Canada as the country of asylum
df_canada = df[df['Country of asylum'] == 'Canada']

# Group by year and sum the 'Recognized decisions'
recognized_decisions_by_year = df_canada.groupby('Year')['Recognized decisions'].sum().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(recognized_decisions_by_year['Year'], recognized_decisions_by_year['Recognized decisions'])
plt.title('Total Recognized Decisions for Asylum Seekers to Canada by Year')
plt.xlabel('Year')
plt.ylabel('Recognized Decisions')
#plt.xticks(recognized_decisions_by_year['Year'])
plt.tight_layout()
plt.show()
