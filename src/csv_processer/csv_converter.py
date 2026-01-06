import pandas as pd
from .data_loader import read_csv
from .data_aggregator import getCountFromDF
from .data_aggregator import getAverageFromDF


def csvPathToJson(path):
    df = read_csv(path)

    #print(df)

    count = getCountFromDF(df)
    print(f"count: {count}")

    average = getAverageFromDF(df)
    print(f"average: {average}")
    