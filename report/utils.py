# import pickle
# from pathlib import Path

# # Using the Path object, create a `project_root` variable
# # set to the absolute path for the root of this project directory
# #### YOUR CODE HERE
 
# # Using the `project_root` variable
# # create a `model_path` variable
# # that points to the file `model.pkl`
# # inside the assets directory
# #### YOUR CODE HERE

# def load_model():

#     with model_path.open('rb') as file:
#         model = pickle.load(file)

#     return model

import pickle
from pathlib import Path

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory.
# Path(__file__) is this utils.py file.
# .parent gives the directory it's in ('report/').
# .parent again gives the parent of 'report/', which is the project root.
# .resolve() makes it an absolute path, e.g., /home/user/dsnd-dashboard-project/
project_root = Path(__file__).resolve().parent.parent

# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`.
# Note: The comment in the shell mentions an 'assets' directory, but the
# project structure diagram shows model.pkl in the root. This code follows
# the directory structure diagram.
model_path = project_root / 'assets' / 'model.pkl'

def load_model():
    """
    Opens the model file from the specified model_path and unpickles it.
    """
    with model_path.open('rb') as file:
        model = pickle.load(file)

    return model