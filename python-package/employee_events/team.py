# python-package/employee_events/team.py

from .query_base import QueryBase
from .sql_execution import database_connection

class Team(QueryBase):
    name = "team"

    def names(self):
        """
        Returns a list of tuples with (team_name, team_id) for all teams.
        """
        df = self._get_names_as_df()
        # Convert the DataFrame to a list of tuples.
        return df.to_records(index=False).tolist()
    
    def username(self, id):
        """
        Returns the name of a single team as a string.
        """
        df = self._get_username_as_df(id)
        return df.iloc[0, 0] if not df.empty else ""

    # --- Helper methods that use the decorator ---

    @database_connection
    def _get_names_as_df(self):
        """Query 5: Returns a DataFrame with team names and IDs."""
        return """
            SELECT
                team_name,
                team_id
            FROM
                team
            ORDER BY
                team_name;
        """

    @database_connection
    def _get_username_as_df(self, id):
        """Query 6: Returns a DataFrame with a single team's name."""
        return f"""
            SELECT
                team_name
            FROM
                team
            WHERE
                team_id = {id};
        """
    
    @database_connection
    def model_data(self, id):
        # This method correctly returns a DataFrame.
        return f"""
                    SELECT positive_events, negative_events FROM (
                            SELECT employee_id
                                 , SUM(positive_events) positive_events
                                 , SUM(negative_events) negative_events
                            FROM {self.name}
                            JOIN employee_events
                                 USING({self.name}_id)
                            WHERE {self.name}.{self.name}_id = {id}
                            GROUP BY employee_id
                           )
               """