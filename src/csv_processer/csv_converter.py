import pandas as pd
from .data_loader import read_csv

def csvPathToJson(path):
    df = read_csv(path)

    print(df)
    