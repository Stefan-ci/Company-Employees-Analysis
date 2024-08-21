import logging
import pandas as pd

logging.basicConfig(level=logging.ERROR)

def load_data():
    """
    Load and preprocess employees data from a Excel file.
    
    Returns:
        DataFrame: A pandas DataFrame containing the preprocessed data.
                    Returns None if an error occurs.
    """
    # All exceptions aren't necessary
    try:
        data = pd.read_excel(r"assets/Employees.xlsx")
    except FileNotFoundError:
        logging.error("Error: The file was not found.")
        return None
    except pd.errors.EmptyDataError:
        logging.error("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        logging.error("Error: The file could not be parsed.")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None
    
    return data

# let's export dataframe to a const and rename "No" to "ID"
DATAFRAME = load_data().rename(columns={"No": "ID"}).copy()
