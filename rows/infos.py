import logging
from dash import html
import dash_bootstrap_components as dbc

# local imports
from data import DATAFRAME as df

# Using logging instead of print()
logging.basicConfig(level=logging.ERROR)


def dataset_infos_row():
    described_df = df.describe()
    described_df.reset_index(inplace=True)
    
    row = dbc.Row([
        # Column of head
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    html.H4("Dataset's description", className="card-title"),
                ),
                dbc.CardBody([
                    dbc.Table([
                            html.Thead(
                                html.Tr([html.Th(col, className="fw-bold") for col in described_df.columns])
                            ),
                            html.Tbody([
                                html.Tr([
                                    html.Td(described_df.iloc[i][col]) for col in described_df.columns
                                ]) for i in range(min(len(described_df), 100)) # change it if you want
                            ]),
                        ],
                        bordered=True,
                        hover=True,
                        responsive=True,
                        striped=True,
                    ),
                ]),
            ], className="shadow-none border")
        ], className="col-md-7 my-2"), # End Col
        
        
        # Column of infos
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(
                    html.H4("Infos about the dataset", className="card-title"),
                ),
                dbc.CardBody([
                    # Shape
                    html.Div([
                        html.Strong("Dataset's shape:", className="me-2"),
                        html.Span(df.shape, className="text-muted"),
                    ]),
                    
                    # rows in df
                    html.Div([
                        html.Strong("Dataset's rows:", className="me-2"),
                        html.Span(len(df), className="text-muted"),
                    ]),
                    
                    # Columns
                    html.Div([
                        html.Strong("Dataset's columns:", className="me-2"),
                        # html.Span(str(col), className="text-muted") for col in df.columns.to_list(),
                        html.Span([html.Span(f"{str(col)} - ", className="text-muted") for col in df.columns])
                    ]),
                ]),
            ], className="shadow-none border"), # end of Card()
        ], className="col-md-5 my-2"), # End Col
    ], className="mt-4")
    
    return row
