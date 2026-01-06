import pandas as pd
from .data_loader import readCsv
from .data_aggregator import getCountFromDF
from .data_aggregator import getAverageFromDF
from .data_aggregator import getMaxFromDF
from .data_aggregator import getMinFromDF


def csvPathToJson(path):
    # 파일경로로 csv파일을 DataFrame으로 변환
    df = readCsv(path)

    # 변환된 DataFramen 객체로 각 데이터들을 계산
    count = getCountFromDF(df)
    average = getAverageFromDF(df)
    max = getMaxFromDF(df)
    min = getMinFromDF(df)

    # dictionary로 만들어서 반환
    data = {
        "count":count,
        "average":average,
        "max":max,
        "min":min
    }

    return data
    