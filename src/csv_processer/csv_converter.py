import pandas as pd
from .data_loader import read_csv
from .data_aggregator import getCountFromDF


def csvPathToJson(path):
    df = read_csv(path)

    #print(df)

    count = getCountFromDF(df)
    print(f"count: {count}")
    