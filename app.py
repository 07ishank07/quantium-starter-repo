from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# 1. Load and clean data
df = pd.read_csv("./formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# 2. Create the figure
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time")

# 3. CRITICAL CHANGE: Convert the string to a Timestamp object here
price_increase_date = pd.Timestamp("2021-01-15")

# 4. Use that object in the vertical line
fig.add_vline(
    x=price_increase_date.timestamp() * 1000, # Plotly sometimes likes milliseconds
    line_dash="dash", 
    line_color="red", 
    annotation_text="Price Increase"
)

# If the above line still fails, try this simpler version:
# fig.add_vline(x=price_increase_date, line_dash="dash", line_color="red")

app.layout = html.Div([
    html.H1('Pink Morsel Visualiser', style={'textAlign': 'center'}),
    dcc.Graph(id='sales-line-chart', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)