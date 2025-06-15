import pandas as pd
import plotly.express as px
import plotly.offline as pyo

# 1. Data inladen of samenstellen
data = {
    'country': ['Country A', 'Country B', 'Country C', 'Country A', 'Country B', 'Country C'],
    'year': [2000, 2000, 2000, 2021, 2021, 2021],
    'co2_per_capita': [5.1, 10.2, 2.3, 6.7, 12.5, 2.8],
    'healthy_life_expectancy_at_birth': [60.2, 65.4, 55.8, 62.5, 67.8, 57.1]
}
merged_df = pd.DataFrame(data)

# 2. Maak de interactieve scatterplot
fig = px.scatter(
    merged_df,
    x='co2_per_capita',
    y='healthy_life_expectancy_at_birth',
    color='year',
    symbol='country',
    labels={
        'co2_per_capita': 'CO₂ Emissies per Capita (ton)',
        'healthy_life_expectancy_at_birth': 'Gezonde Levensverwachting (jaren)',
        'year': 'Jaar'
    },
    title='CO₂ Emissies vs Gezonde Levensverwachting'
)

# 3. Exporteer naar HTML-bestand
output_file = 'visualization.html'
pyo.plot(
    fig,
    filename=output_file,
    auto_open=False,
    include_plotlyjs='cdn'
)
print(f"HTML opgeslagen als {output_file}")
