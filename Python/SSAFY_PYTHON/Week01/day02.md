# 파이썬
---
## day02, 7월 19일 화요일
---

### jupyter notebook 설치
```
pip install jupyter notebook
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

jupyter notebook 실행 후,
확장 프로그램 nbextension 들어가서 체크박스 해제,
table 검색 후 나오는 두개 체크박스 설정

### jupyter notebook의 장점

1. python 코드와 마크다운을 같이 적을 수 있음
2. python 코드의 실행결과를 함께 파일로 저장
3. 전체 파일 단위가 아닌, 셀 단위의 실행


- 셀을 클릭 한 후, m을 누르면 markdown으로 입력 가능
- 셀을 클릭 한 후, y를 누르면 codeset으로 입력 가능
- 기타 단축키는 필요시 Help


### day01 복습

**f-strings-**
문자열 시작하기 전에 f를 붙이고, 중괄호{}안에 변수를 넣으면 출력 가능

**Boolean**

첫 글자를 대문자로 True, False


**비교연산자**
=은 항상 뒤에 있다.

**논리연산자**

A and B - A와 B가 모두 True일때만

A or B - A와 B 둘 중 하나가 True면 True


Falsy: False는 아니지만 False로 취급되는 다양한 값

0, 0.0, (), [], {}, None, ""(빈 문자열)

단축평가를 하게 만든 값을 반환하면 된다.


**리스트**

my_list[a : b : c]

a = start, b = end, c = step

ex) my_list[0:3] -> 0부터 3-1인 2까지(my_list[0],[1],[2])

ex) my_list[0:10:2] -> 0부터 10-1인 9까지 2씩 올라가며(my_list[0],[2],[4],[6],[8])

a,b,c 모두 생략이 가능하다.

ex) [:b] 0부터 b-1까지

ex) [a:] a부터 끝까지

ex) [:] 전체


**딕셔너리**

JSON과 이어지므로 매우 중요


**형변환**

암시적 형변환은 우리들의 코드에 있어서 안된다.

명시적 형변환으로 바꿔야함

---

## 저장장치
1. SSD
2. HDD
3. RAM
우리가 프로그래밍 하는 모든 데이터는 RAM에 저장
램에는 순서대로 주소값이 저장
a = 3이라고 입력을 하지만,  a = A002주소에 넣어줘 이런식으로


## Git
협업할 때
 repository private으로 만든 후 settings - collaborator