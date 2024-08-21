import logging
from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc

# local imports
from data import DATAFRAME as df

# Using logging instead of print()
logging.basicConfig(level=logging.ERROR)


HISTOGRAM_FUNCTIONS = ["count", "sum", "avg", "min", "max"]


def analysis_based_on_genders_and_departments_rows():
    gender_counts = df["Gender"].value_counts()
    gender_distribution_fig = px.pie(
        values=gender_counts,
        names=gender_counts.index,
        color_discrete_sequence=["#66b3ff","#ff9999"]
    )
    
    
    employees_per_dept = df["Department"].value_counts()
    employees_per_dept_graph = px.pie(
        values=employees_per_dept,
        names=employees_per_dept.index,
    )
    
    
    num_bins = min(10, len(df))
    employees_countries_graph = px.histogram(
        data_frame=df,
        x="Country",
        color="Country",
        nbins=num_bins,
    )
    
    
    salaries_based_on_genders_graph = px.histogram(
        data_frame=df,
        x="Monthly Salary",
        color="Gender",
        nbins=num_bins,
        barmode="overlay", # or overlay, stack
    )
    
    
    jobs_rate_based_on_genders_graph = px.histogram(
        data_frame=df,
        x="Job Rate",
        color="Gender",
    )
    
    
    
    correlation_job_rate_overtime_hours_graph = px.scatter(
        data_frame=df,
        x="Job Rate",
        y="Overtime Hours",
        trendline_color_override="red"
    )
    
    
    
    # Page content
    section = html.Section([
        html.Div([
            html.H2("Analysis based on Genders, Departments and Countries", className="h2 text-decoration-underline"),
        ], className="col my-2"),
        
        
        
        dbc.Row([
            # Column of genders pie graph
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Gender Distribution", className="card-title"),
                        dcc.Graph(id="genders-distribution-graph", figure=gender_distribution_fig),
                    ]),
                ], className="shadow-none border"), # end of Card()
            ], className="col-md-3 my-2"), # End Col
            
            # Column of depts pie graph
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Employees per Department - Departments ({len(df["Department"].unique())})", className="card-title"),
                        dcc.Graph(id="employees-per-department-graph", figure=employees_per_dept_graph),
                    ]),
                ], className="shadow-none border"), # end of Card()
            ], className="col-md-5 my-2"), # End Col
            
            # Column of countries graph
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Countries of employees ({len(df["Country"].unique())})", className="card-title"),
                        dcc.Graph(id="countries-of-employees-graph", figure=employees_countries_graph),
                    ]),
                ], className="shadow-none border"), # end of Card()
            ], className="col-md-4 my-2"), # End Col
        ]),
        
        
        
        dbc.Row([
            # Column of salaries by gender graph
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Salaries based on genders", className="card-title"),
                        dcc.Graph(id="salaries-based-on-genders-graph", figure=salaries_based_on_genders_graph),
                    ]),
                ]), # end of Card()
            ], className="col-md-6 my-2"), # End Col
            
            
            # Column of job's rate by gender graph
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5(f"Job's rate based on genders", className="card-title"),
                        dcc.Graph(id="jobs-rate-based-on-genders-graph", figure=jobs_rate_based_on_genders_graph),
                    ]),
                ]), # end of Card()
            ], className="col-md-6 my-2"), # End Col
        ]),
        
        
        
        dbc.Row([
            # Column of salaries per dept graph
            dbc.Col([
                html.H2(f"Salaries per department", className="h2"),
                dbc.Card([
                    dbc.CardBody([
                        dcc.Dropdown(
                            id="functions-of-emplayees-salaries-per-dept",
                            value=None,
                            placeholder="Select a function",
                            options=[{"label": str(func).capitalize(), "value": func} for func in HISTOGRAM_FUNCTIONS],
                        ),
                        dcc.Graph(id="functions-of-emplayees-salaries-per-dept-graph"),
                    ]),
                ]), # end of Card()
            ], className="col-md-8 my-2"), # End Col
            
            dbc.Col([
                html.H2(f"Correlation Job Rate - Overtime", className="h2"),
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id="correlation-job-rate-overtime-hours-graph", figure=correlation_job_rate_overtime_hours_graph, className="p-0"),
                    ], className="p-0"), # reset padding to use full space available
                ], className="p-0"), # end of Card()
            ], className="col-md-4 my-2"), # End Col
        ], className="mt-4")
    
    ], className="mt-4") # End Section
    
    return section
