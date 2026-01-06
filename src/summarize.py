import argparse

def main():
    # argument 읽는 부분
    parser = argparse.ArgumentParser()

    parser.add_argument("arg01", type=str)

    args = parser.parse_args()

    print(f"arg: {args.arg01}")


if __name__ == "__main__":
    main()