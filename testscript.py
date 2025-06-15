import pandas as pd
import plotly.express as px
from plotly.offline import plot

# 1. Maak je figuur (gebruik je eigen merged_df)
merged_df = pd.DataFrame({
    'country': ['Country A','Country B','Country C','Country A','Country B','Country C'],
    'year':    [2000,        2000,        2000,        2021,        2021,        2021],
    'co2_per_capita':              [5.1,         10.2,         2.3,          6.7,         12.5,         2.8],
    'healthy_life_expectancy_at_birth': [60.2,        65.4,        55.8,         62.5,        67.8,        57.1]
})
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

# 2. Genereer de standalone DIV (zonder de full HTML wrapper)
plot_div = plot(
    fig,
    include_plotlyjs='cdn',  # laad Plotly.js automatisch
    output_type='div'
)

# 3. Lees je bestaande HTML
input_path = r"C:\M2-data-story-website\co2_health_life_expectancy.html"
with open(input_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 4. Vervang de placeholder door je plot_div
new_html = html.replace('<!-- PLOTLY_PLACEHOLDER -->', plot_div)

# 5. Schrijf het resultaat terug
with open(input_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Grafiek succesvol ingebed in bestaande HTML 🎉")
