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
    result = csvPathToJson(path)

    print(result)

if __name__ == "__main__":
    main()