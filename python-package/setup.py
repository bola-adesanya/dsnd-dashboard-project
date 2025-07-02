from pathlib import Path
from setuptools import setup, find_packages

cwd = Path(__file__).resolve().parent
requirements = ['pandas']

if __name__ == "__main__":
    setup(
        name='employee_events',
        version='0.0.1', # It's good practice to use a 3-part version
        description='SQL Query API',
        packages=find_packages(),
        package_data={'employee_events': ['employee_events.db', 'requirements.txt']},
        install_requires=requirements,
    )