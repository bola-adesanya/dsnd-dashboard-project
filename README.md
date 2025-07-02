
# Employee Performance & Recruitment Risk Dashboard

## Overview

This project addresses a business need to monitor employee performance and proactively identify top talent at risk of being recruited by competitors. This dashboard provides management with a tool to visualize key performance indicators for individual employees and teams, alongside a machine-learning-powered prediction of their likelihood of recruitment.

The application is built with a Python backend, featuring a locally developed data access package and a web interface rendered with FastHTML.

## Features

* **Dual View:** Toggle between viewing data for a single **Employee** or an entire **Team**.
* **Dynamic Selection:** Dropdown menu updates dynamically based on the selected view (Employee or Team).
* **Performance Visualization:** A cumulative line chart displays positive and negative performance events over time.
* **Recruitment Risk Prediction:** A bar chart visualizes the output of a machine learning model that predicts recruitment risk. For teams, it shows the average risk for all team members.
* **Data Table:** Displays detailed text notes related to the selected employee or team.

## Technical Stack

* **Backend:** Python 3.10
* **Data Access Package:** A custom-built, installable Python package for querying the SQLite database.
* **Web Framework:** `python-fasthtml`
* **Data Manipulation:** `pandas`
* **Visualizations:** `matplotlib`
* **Testing:** `pytest`
* **Continuous Integration:** GitHub Actions

## Project Structure

```text
├── .github/workflows/      # CI/CD workflows for testing and linting
├── python-package/         # Source for the installable employee_events data package
│   └── employee_events/
├── report/                 # Source for the FastHTML dashboard application
│   └── src/                # Pre-built UI components
├── tests/                  # Pytest test suite for the data package
├── model.pkl               # Pre-trained machine learning model
├── README.md               # This file
└── requirements.txt        # Project dependencies
```

## Setup and Installation

To set up and run this project locally, please follow these steps:

1.  **Clone the Repository**
```bash
    git clone https://github.com/bola-adesanya/dsnd-dashboard-project
```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    Install all required third-party libraries from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install the Local Package**
    Install the `employee_events` data package in editable mode.
    ```bash
    pip install -e ./python-package
    ```

## How to Run

With your virtual environment active, start the dashboard application by running the following command from the **root directory** of the project:

```bash
python report/dashboard.py
```

After running the command, you will see output in your terminal indicating that the server is running. Open your web browser and navigate to the following URL to view the dashboard:

[**http://127.0.0.1:8000**](http://127.0.0.1:8000)