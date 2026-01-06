import pandas as pd
from .data_loader import read_csv
from .data_aggregator import getCountFromDF
from .data_aggregator import getAverageFromDF
from .data_aggregator import getMaxFromDF
from .data_aggregator import getMinFromDF
import json


def csvPathToJson(path):
    df = read_csv(path)

    #print(df)

    count = getCountFromDF(df)
    #print(f"count: {count}")

    average = getAverageFromDF(df)
    #print(f"average: {average}")

    max = getMaxFromDF(df)
    #print(f"max: {max}")

    min = getMinFromDF(df)
    #print(f"min: {min}")

    # dictionary로 만들어서 반환
    data = {
        "count":count,
        "average":average,
        "max":max,
        "min":min
    }

    #print(data)
    return data
    