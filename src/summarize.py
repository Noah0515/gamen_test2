import argparse
from pathlib import Path
from csv_processer.data_loader import read_csv

def main():
    # argument 읽는 부분
    parser = argparse.ArgumentParser()
    parser.add_argument("arg01", type=str)
    args = parser.parse_args()

    #print(f"arg: {args.arg01}")
    
    path = Path(args.arg01).resolve()
    print(path)
    read_csv(path)

if __name__ == "__main__":
    main()