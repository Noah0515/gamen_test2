import pandas as pd

# 파일경로에 있는 csv 파일을 읽어서 dataframe으로 돌려주는 함수
def read_csv(file_path):
    try:
        df_file = pd.read_csv(file_path)
        #print(df_file)

        return df_file
    except Exception as e:
        # 파일 경로가 잘못되었거나 입력받은 파일이 csv파일이 아닌경우
        print("해당 파일이 없거나 csv가 아닙니다.")


