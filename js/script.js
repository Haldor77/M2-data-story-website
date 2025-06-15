window.addEventListener('DOMContentLoaded', () => {
  const data = {
    x: [/* CO₂-waarden per land, bijv. [4.5, 16.2, …] */],
    y: [/* HALE-waarden per land, bijv. [72.3, 79.1, …] */],
    mode: 'markers',
    type: 'scatter',
    text: [/* Landnamen voor tooltips, bijv. ['Nederland', 'VS', …] */],
    hovertemplate: '%{text}<br>CO₂: %{x} ton<br>HALE: %{y} jaar<extra></extra>'
  };
  const layout = {
    title: 'CO₂-uitstoot vs Gezonde Levensverwachting per land (2021)',
    xaxis: { title: 'CO₂-uitstoot (ton per capita)' },
    yaxis: { title: 'Gezonde Levensverwachting (jaren)' }
  };
  Plotly.newPlot('scatterChart', [data], layout);
});
