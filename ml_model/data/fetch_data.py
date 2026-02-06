import pandas as pd
def get_data():
    df = pd.read_csv("/workspaces/Human-vs-ML-Project/data/Titanic.csv")
    return df