# Algorithm-Study


### 파이썬 함수
* `[i for i,v in enumerate(list) if v == '']`: 조건문 만족하는 index값 출력 
* `eval()`: 문자열 수식 계산
* `x = y[:]`: 리스트 얕은 복사
* `f'{}'`: f-string 
* `''.join(list)`: 문자열 붙이기 
* `continue`: 실행코드 건너뛰기
* `break`: 반복문 끝내기
* `zip`: iterable한 자료형 묶기
* `list(itertools.product(*cases))`: 곱집합

### 아이디어
* 2차원 좌표로 생각하기 
* 레퍼런스 활용하기
* BFS: 너비우선탐색, `deque()`, `popleft()` or `pop(0)` 
* DFS: 깊이우선탐색, `list()`, `pop()` 

### SQL 함수
* `LIMIT`: 출력 개수 선정
* `DESC`: 내림차순 정렬
* `ASC`: 오름차순 정렬
* `DISTINCT`: 중복 제거
* `HAVING`: 조건
* `HOUR`: 시간
* `BETWEEN A AND B`: A와 B 사이
* `LIKE "%A%"`: "A"를 포함하는 문자
* `CASE WHEN 조건 THEN 값1 ELSE 값2 END AS 변수`: 조건문
* `DATE_FORMAT(DATETIME 변수, '%Y-%m-%d')`: 날짜 변환
