import dash
import logging
import plotly.express as px
from dash import html, Output, Input
import dash_bootstrap_components as dbc

# local imports
from data import DATAFRAME as df
from rows.infos import dataset_infos_row
from rows.genders_and_dept import analysis_based_on_genders_and_departments_rows, HISTOGRAM_FUNCTIONS


# Using logging instead of print()
logging.basicConfig(level=logging.ERROR)


# Initializing Dash() app
app = dash.Dash(
    __name__,
    title="Company's Employees Analysis - Dashboard",
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# Displaying all page content (layout) in a Container() component
app.layout = dbc.Container([
    # Page header row
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("Company's Employees Analysis - Dashboard", className="fw-bold h1 text-primary text-uppercase text-decoration-underline"),
            ])
        ], className="text-center mt-2")
    ]),
    
    
    # Infos about the dataset row
    dataset_infos_row(),
    
    
    # Analysis' row based on genders
    analysis_based_on_genders_and_departments_rows(),
    
], className="mb-5", fluid=True)





# callback of salaries per dept graph
@app.callback(
    Output("functions-of-emplayees-salaries-per-dept-graph", "figure"), # "figure" from plotly
    Input("functions-of-emplayees-salaries-per-dept", "value")
)
def update_salaries_per_dept_graph_on_func_select(selected_func):
    if selected_func:
        if not isinstance(selected_func, str):
            return dbc.Alert(f"Invalid input type. Must be a string and match one of {str(HISTOGRAM_FUNCTIONS)}", color="error")
        
        elif selected_func not in HISTOGRAM_FUNCTIONS:
            return dbc.Alert("Selected function type isn't available", color="error")
    
    else:
        selected_func = "avg" # by default, display averages
    
    # else
    fig = px.histogram(
        data_frame=df,
        x="Department",
        y="Monthly Salary",
        marginal="rug",
        histfunc=selected_func,
    )
    return fig





# running the app (with Flask)
if __name__ == "__main__":
    app.run_server(debug=True)
