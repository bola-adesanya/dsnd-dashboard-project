# report/dashboard.py

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


from fasthtml.common import * 
from fasthtml.fastapp import fast_app  

# Import from our local packages
from utils import load_model
from employee_events.employee import Employee
from employee_events.team import Team
from base_components import Dropdown, BaseComponent, Radio, MatplotlibViz, DataTable
from combined_components import FormGroup, CombinedComponent


class ReportDropdown(Dropdown):

    def build_component(self, asset_id, model):
        self.label = model.name.title()
        return super().build_component(asset_id, model)

    def component_data(self, asset_id, model):
        return model.names()


class Header(BaseComponent):

    def build_component(self, asset_id, model):
        return H1(f'{model.name.title()} Performance')


class LineChart(MatplotlibViz):

    def visualization(self, asset_id, model):
        data = model.event_counts(asset_id)
        data = data.fillna(0)
        data = data.set_index('event_date')
        data.sort_index(inplace=True)
        data = data.cumsum()
        data.columns = ['Positive', 'Negative']
        fig, ax = plt.subplots()
        data.plot(ax=ax)
        self.set_axis_styling(ax)
        ax.set_title('Cumulative Performance Events')
        ax.set_xlabel('Date')
        ax.set_ylabel('Cumulative Event Count')


class BarChart(MatplotlibViz):
    predictor = load_model()

    def visualization(self, asset_id, model):
        data = model.model_data(asset_id)
        predictions = self.predictor.predict_proba(data)
        risk_scores = predictions[:, 1]

        if model.name == "team":
            pred = risk_scores.mean()
        else:
            pred = risk_scores[0]

        fig, ax = plt.subplots()
        ax.barh([''], [pred])
        ax.set_xlim(0, 1)
        ax.set_title('Predicted Recruitment Risk', fontsize=20)
        self.set_axis_styling(ax)


class Visualizations(CombinedComponent):
    children = [LineChart(), BarChart()]
    outer_div_type = Div(cls='grid')


class NotesTable(DataTable):

    def component_data(self, asset_id, model):
        return model.notes(asset_id)


class DashboardFilters(FormGroup):
    id = "top-filters"
    action = "/update_data"
    method = "POST"
    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
        ),
        ReportDropdown(
            id="selector",
            name="user-selection")
    ]


class Report(CombinedComponent):
    children = [Header(), DashboardFilters(), Visualizations(), NotesTable()]


# --- Corrected App Initialization ---
# ISSUE 3: Use fast_app() to correctly create the app and router
app, rt = fast_app()

# Initialize the Report class
report = Report()


# --- Routes ---
@rt('/')
def home():
    return report(1, Employee())


@rt('/employee/{employee_id:str}')
def employee_report(employee_id: str):
    return report(employee_id, Employee())


@rt('/team/{team_id:str}')
def team_report(team_id: str):
    return report(team_id, Team())


# --- Pre-written HTMX callback routes ---
@app.get('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())


@app.post('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)


# Add a call to serve() if it's not implicitly called by fast_app in your version
# serve()

# Replace serve() with uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
