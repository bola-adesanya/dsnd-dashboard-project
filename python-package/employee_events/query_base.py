# python-package/employee_events/querybase.py

# Import any dependencies needed to execute sql queries
import pandas as pd
from .sql_execution import database_connection

# Define a class called QueryBase
class QueryBase:
    """
    A generic base class for building and executing SQL queries.
    
    Subclasses should define the `name` class attribute (e.g., "employee" or "team")
    to make the methods in this class work correctly.
    """

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments. This is a placeholder to be overridden by subclasses.
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method that receives an `id` argument.
    # This method returns a pandas dataframe.
    @database_connection
    def event_counts(self, id):
        """
        QUERY 1: Generic query to get event counts for an employee or a team.
        """
        # This query joins the primary table (employee or team) with employee_events
        # to get the sum of events, grouped by date.
        return f"""
            SELECT
                ee.event_date,
                SUM(ee.positive_events) AS total_positive,
                SUM(ee.negative_events) AS total_negative
            FROM
                {self.name} t
            JOIN
                employee_events ee ON t.{self.name}_id = ee.{self.name}_id
            WHERE
                t.{self.name}_id = {id}
            GROUP BY
                ee.event_date
            ORDER BY
                ee.event_date;
        """

    # Define a `notes` method that receives an id argument.
    # This function returns a pandas dataframe.
    @database_connection
    def notes(self, id):
        """
        QUERY 2: Generic query to get notes for an employee or a team.
        """
        # This query joins the primary table (employee or team) with notes
        # to retrieve all notes associated with that entity.
        return f"""
            SELECT
                n.note_date,
                n.note
            FROM
                {self.name} t
            JOIN
                notes n ON t.{self.name}_id = n.{self.name}_id
            WHERE
                t.{self.name}_id = {id}
            ORDER BY
                n.note_date;
        """

