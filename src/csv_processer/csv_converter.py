import pandas as pd
from .data_loader import read_csv
from .data_aggregator import getCountFromDF
from .data_aggregator import getAverageFromDF
from .data_aggregator import getMaxFromDF


def csvPathToJson(path):
    df = read_csv(path)

    #print(df)

    count = getCountFromDF(df)
    print(f"count: {count}")

    average = getAverageFromDF(df)
    print(f"average: {average}")

    max = getMaxFromDF(df)
    print(f"max: {max}")
    