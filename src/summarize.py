import argparse
from pathlib import Path
from csv_processer.csv_converter import csvPathToJson

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
        print("해당 파일이 존재하지 않습니다.")
    except Exception as e:
        print("예상치 못한 예외가 발생했습니다.")

if __name__ == "__main__":
    main()