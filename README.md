# gamen_test

# 1. 실행방법
/gamen_test2/csv_data 디렉토리에 테스트데이터들이 있습니다.<br><br>
윈도우의 cmd기준
1. 프로젝트의 루트디렉토리에서 python src\summarize.py csv_data\scores01.csv
2. src 디렉토리에서 python summarize.py ..\csv_data\scores06.csv
<br>위 두 명령어중 하나를 선택하시면 됩니다.

# 2. 구현에 대한 설명
1. 폴더 구조 설명<br>
   - 루트 디렉토리를 보변 크게 소스코드가 들어있는 src 디렉토리와 테스트데이터가 들어있는 csv_data 디렉토리로 나눴습니다.<br>
   - src의 경우 main()이 있는 summarize.py와 csv 데이터를 처리할 코드를 모은 csv_processor디렉토리로 나눴습니다.<br>
   - csv_data에는 테스트를 위해 양의정수, 음수, 실수, 공백, 문자열, 문자열로된 숫자, 잘못된 열 이름 등 다양한 경우를 고려하여 테스트데이터를 만들었습니다.<br>
  
2. 소스코드 설명<br>
   - 과제 설명에서처럼 실행하기 위해 main을 summarize.py 파일에 넣고 읽을 csv파일을 하나 받을 수 있도록 args 설정을 했습니다.<br>
   - main의 Path(args.arg01).resolve() 이 부분은 운영체제마다, 실행 환경에 따라 파일경로가 틀어지는 문제를 해결하기 위해 넣었습니다.<br>
   - 파일경로를 json데이터로 바꾸는 부분은 /src/csv_processor/csv_converter.csvPathToJson 함수를 통해 변환합니다.<br>
   - 해당 함수 내부에선 먼저 /src/data_loader.readCsv 함수를 통해 파일경로에 있는 csv파일을 pandas의 DataFrame으로 변환합니다.<br>
**※만약 이 때 파일의 경로나 이름이 잘못된 경우를 대비해 main에서 csvPathToJson를 호출할 때 예외를 잡아 처리합니다.**<br>
   - 정상적으로 csv파일을 DataFrame으로 변환한 경우 /src/csv_processor/data_aggregator의 함수들을 이용해 데이터요약 하며<br>
   - 각 함수들은 DataFrame의 함수를 이용해 필요한 값들을 구합니다.<br>
**※score 열의 숫자들을 다루는 경우 잘못된 값이 들어가면 에러가 생기므로 pd.to_numeric(df['score'], errors='coerce') 이 부분을 넣어 문자열인 경우엔 Nan, 문자열로 된 숫자("30"같은 경우)는 숫자로 바꿔 계산하도록 했습니다.<br>그리고 score라는 열이 없는 경우에도 main에서 예외를 처리하도록 했습니다.**<br>
   - 필요한 데이터들을 잘 구했다면 json형식과 같은 dictionary 타입으로 데이터를 저장하여 반환하도록 했습니다.<br>
   - 이 과정에서 제가 파악하지 못한 예외가 있는 경우 Exception으로 예외를 잡도록 했습니다.

# 3. 과제 선택 이유
- python을 이용해 csv파일을 조회하고 이를 pandas의 DataFrame으로 다루는 것이 더 익숙해서 2번 과제를 선택했습니다.

