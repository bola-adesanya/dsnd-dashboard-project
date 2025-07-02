# python-package/employee_events/sql_execution.py

import sqlite3
import pandas as pd
from functools import wraps
from pathlib import Path

# This creates a platform-independent path to the database file.
# Path(__file__) gets the path of the current file (sql_execution.py).
# .parent gets the directory this file is in (employee_events/).
# We then append the database file name to this path.
DB_PATH = Path(__file__).parent / 'employee_events.db'

def database_connection(func):
    """
    Decorator to handle the database connection lifecycle:
    1. Opens a connection to the SQLite database.
    2. Executes the SQL query returned by the decorated function.
    3. Closes the database connection.
    4. Returns the fetched data as a pandas DataFrame.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # First, call the original function (the one being decorated).
        # It will return the SQL query string we need to execute.
        query = func(*args, **kwargs)
        
        connection = None
        try:
            # Step 1: Open a connection to the database.
            connection = sqlite3.connect(DB_PATH)
            
            # Step 2 & 4: Execute the query using pandas and return the data.
            # pandas' read_sql_query function is a convenient way to run a query
            # and load the results directly into a DataFrame.
            df = pd.read_sql_query(query, connection)
            return df

        except sqlite3.Error as e:
            # Handle potential database errors, like a missing table.
            print(f"Database error: {e}")
            # Return an empty DataFrame if an error occurs.
            return pd.DataFrame()
            
        finally:
            # Step 3: Close the connection.
            # The 'finally' block ensures that this code runs whether
            # the 'try' block succeeded or an error occurred.
            if connection:
                connection.close()
                
    return wrapper

