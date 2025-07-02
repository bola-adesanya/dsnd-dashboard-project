# python-package/employee_events/employee.py

from .query_base import QueryBase
from .sql_execution import database_connection

class Employee(QueryBase):
    name = "employee"

    def names(self):
        """
        Returns a list of tuples with (full_name, employee_id) for all employees.
        This is the required format for the Dropdown component.
        """
        df = self._get_names_as_df()
        # Convert the DataFrame to a list of tuples.
        return df.to_records(index=False).tolist()

    def username(self, id):
        """
        Returns the full name of a single employee as a string.
        """
        df = self._get_username_as_df(id)
        # The DataFrame will have one row, one column. Get that single value.
        return df.iloc[0, 0] if not df.empty else ""

    # --- Helper methods that use the decorator ---

    @database_connection
    def _get_names_as_df(self):
        """Query 3: Returns a DataFrame with names and IDs."""
        return """
            SELECT
                first_name || ' ' || last_name AS full_name,
                employee_id
            FROM
                employee
            ORDER BY
                full_name;
        """
    
    @database_connection
    def _get_username_as_df(self, id):
        """Query 4: Returns a DataFrame with a single employee's name."""
        return f"""
            SELECT
                first_name || ' ' || last_name AS full_name
            FROM
                employee
            WHERE
                employee_id = {id};
        """

    @database_connection
    def model_data(self, id):
        # This method correctly returns a DataFrame as required by the ML model.
        return f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                         USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
               """