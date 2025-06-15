import pandas as pd
import plotly.express as px
from plotly.offline import plot

# 1. Prepare your data
df = pd.DataFrame({
    'Country': ['Country A','Country B','Country C','Country A','Country B','Country C'],
    'Year':    [2000,        2000,        2000,        2021,        2021,        2021],
    'CO2_per_Capita':          [5.1,         10.2,         2.3,          6.7,         12.5,         2.8],
    'Healthy_Life_Expectancy': [60.2,        65.4,        55.8,         62.5,        67.8,        57.1]
})

# 2. Build the Plotly scatter figure
fig = px.scatter(
    df,
    x='CO2_per_Capita',
    y='Healthy_Life_Expectancy',
    color='Year',
    symbol='Country',
    size='CO2_per_Capita',                
    hover_name='Country',
    hover_data={
        'Year': True,
        'CO2_per_Capita': ':.1f',
        'Healthy_Life_Expectancy': ':.1f'
    },
    labels={
        'CO2_per_Capita': 'CO₂ Emissions per Capita (metric tons)',
        'Healthy_Life_Expectancy': 'Healthy Life Expectancy at Birth (years)',
        'Year': 'Year'
    },
    title='CO₂ Emissions vs. Healthy Life Expectancy (2000 vs. 2021)',
    template='plotly_white'
)

# 3. Add linear trend lines for each year
for year in df['Year'].unique():
    sub = df[df['Year'] == year]
    trend = px.scatter(sub, x='CO2_per_Capita', y='Healthy_Life_Expectancy', trendline='ols')
    # trend.data[1] is the OLS line
    fig.add_traces(trend.data[1])

# 4. Tidy up marker style and layout
fig.update_traces(marker=dict(opacity=0.8, line=dict(width=1, color='DarkSlateGrey')))
fig.update_layout(
    legend_title_text='Year',
    title_x=0.5,
    xaxis=dict(ticks="outside", gridcolor='lightgrey'),
    yaxis=dict(ticks="outside", gridcolor='lightgrey')
)

# 5. Generate the standalone DIV (no full HTML wrapper)
plot_div = plot(
    fig,
    include_plotlyjs='cdn',  # automatically load Plotly.js
    output_type='div'
)

# 6. Read your existing HTML file
input_path = r"C:\M2-data-story-website\co2_health_life_expectancy.html"
with open(input_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 7. Replace the placeholder with the generated plot DIV
new_html = html.replace('<!-- PLOTLY_PLACEHOLDER -->', plot_div)

# 8. Write the updated HTML back to disk
with open(input_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("✅ Graph successfully embedded into existing HTML!")
