import os

import pandas as pd

path = "data/"

def load_data(filename):
    # Load in the data

    if os.path.exists(path + filename):
        return pd.read_csv("data/" + filename)
    else:
        raise FileNotFoundError()
