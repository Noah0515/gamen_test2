import pandas as pd

# 받은 df의 row 개수 반환
def getCountFromDF(df: pd.DataFrame):
    count = len(df)
    #print(count)

    return count

# 받은 df에서 score column의 평균 반환
def getAverageFromDF(df: pd.DataFrame):
    average = df['score'].mean()
    #average = df['score'].mean().round(3) 소수점 정리가 필요한 경우
    return average 

# 받은 df에서 score column의 최댓값 반환
def getMaxFromDF(df: pd.DataFrame):
    max = df['score'].max()

    return max

# 받은 df에서 score column의 최솟값 반환
def getMinFromDF(df: pd.DataFrame):
    min = df['score'].min()

    return min