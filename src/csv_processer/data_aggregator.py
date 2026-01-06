import pandas as pd

def getCountFromDF(df: pd.DataFrame):
    count = len(df)
    #print(count)

    return count

def getAverageFromDF(df: pd.DataFrame):
    average = df['score'].mean()
    #average = df['score'].mean().round(3) 소수점 정리가 필요한 경우
    return average 

def getMaxFromDF(df: pd.DataFrame):
    max = df['score'].max()

    return max