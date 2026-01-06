import argparse
from pathlib import Path
from csv_processor.csv_converter import csvPathToJson

def main():
    # argument 읽는 부분
    parser = argparse.ArgumentParser()
    parser.add_argument("arg01", type=str)
    args = parser.parse_args()

    #print(f"arg: {args.arg01}")
    
    path = Path(args.arg01).resolve()

    try:
        result = csvPathToJson(path)
        print(result)
    except FileNotFoundError as e:
        # 파일 경로나 이름이 잘못된 경우
        print("해당 파일이 존재하지 않습니다.")
    except KeyError as e:
        # csv파일에 score 열이 없는 경우 
        print("score 열이 없습니다.")
    except Exception as e:
        # 그 외 파악하지 못한 예외 
        print("예상치 못한 예외가 발생했습니다.")
        print(f"에러타입: {type(e)}")

if __name__ == "__main__":
    main()