# Web

---

## day12, 8월 2일 화요일

---

## 웹 복습

live server 설치
auto rename tag 설치
highlight matching tag 설치

! + tab 자동완성(html    기본구조)

---

html에 style 적용하기
1. 인라인
2. 외부파일
3. 내부 style 태그 

요소 = 태그 + 내용

href = "https://google.com"
속성명 = 속성값

class: 여러개의 요소에 적용할 때 클래스를 부여
id: 문서 전체에서 유일한 고유 식별자 지정


검색 엔진 최적화를 위해 시맨틱 태그 사용

### DOM트리
Document Object Model
HTML은 텍스트다. 브라우저에 렌더링 하기 위해 DOM구조

인라인 / 블록 요소
a태그 URL
br 줄바꿈
img 이미지
span 의미는 인라인 컨테이너

form
사용에게 데이터를 받기 위한 
action: form을 처리할 서버의 URL
method: 데이터를 갖고오는 과정 get 
(민감한 정보는 get이 아니라 post로)
input 태그: type(크게 거르는 작업)/name(데이터를 구분)/value  
label 태그: name과 쌍으로
for랑 id값을 일치시켜서 해당 데이터라고

required, autofocus

checkbox: 다중 선택
radio: 단일 선택 (라디오는 버튼 하나만 누를 수 있음)

HTML/CSS -> 마스터 할 생각을 버려라...

hidden: 사용자에게 보이지 않는 input

img src = 소스
img alt = 이미지가 안나올 때 화면에 보여줄  
70p 실습해보기

---

## CSS

1. 선택하고
2. 스타일을 지정한다.

선택자{속성:값}  

### CSS 정의 방법
- 인라인
해당 태그에 직접 style 속성을 활용. 각각의 스타일은 ;으로 구분
- 내부참조(embedding)
해드 태그 내에 스타일 지정
- 외부참조
외부 css파일을 헤드 내 링크를 통해 불러오기

### CSS Selectors
**- 기본 선택자**
- 전체 선택자 * {}
- 요소 선택자 div {}
- 클래스 선택자 .my_class {}
- 아이디 선택자 #my_id {}
- 속성 선택자 bu
**- 결합자**
- 자손 띄어쓰기
- 자식 >
- 인접 +


### CSS 적용 우선순위

!important - 인라인 - id - class - 속성 - pseudo-class - 요소 - pseudo-element
!important를 남발해선 안된다.

p103 시험문제 무조건 나옴. 풀어보고 왜 그렇게 되는지 이해 마치기.

취소선: 이러한 애들이 적용되고 있었는데, 최종적으로는 다른 색이 적용되고 있다.

### CSS 상속
CSS 상속은 자동으로 일어나는데, 상속 되는 게 있고 안되는 게 있다.

### 크기단위
em 바로 위
rem 제일 위

###  색상 단위
- 색상 키워드
- RGB 색상(rgb(0,255,0)) +a는 투명도

외우는게 아니라 많이 써서 익숙해질 수 있도록
컬러, 배경 정도만 

### BOX MODEL

(Content - Padding) - Border - Margin
백그라운드 컬러 적용

**시험에 나옴**
margin shorthand
margin: 한개만 쓰면 상하좌우
margin: 두개 쓰면 상하/좌우
margin: 세개 쓰면 나누기 1/2/1
margin: 네게 쓰면 상부터 시계방향

box-sizing
padding을 제외한 순수 contents 영역만을 box로 지정
다만, 우리가 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
이 경우, box-sizing을 border-box로 설정

### CSS Display
블럭요소/인라인요소
display: block
display: inline

- 대표적인 블록 레벨 요소
  -   div p hr form
- 대표적인 인라인 레벨 요소
  - span a img input label

block의 기본 너비는 갖리 수 있는 너비의 100%
블럭요소는 width를 주면 나머지는 margin으로 먹는다.


### 정렬
margin-right:auto; text-align:left;
margin-left:auto; text-align:right;
margin-right:auto;margin-left:auto; text-align:center;

### display
**display: inline-block**
- block과 inline 레벨 요소
**display: none**
- 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
- 이와 비슷한 visibility:hidder은 해당 요사가 공간은 차지하나 화면에 표시만 하지 않는다.

155p 코드 직접 쳐보기


### CSS position

'mdn position' search on google

position: static; -> normal flow를 따른다.(기본, 쓰나 마나 똑같다.)
position: relative; -> 원래 자리를 차지하고 있고, 우리 눈에 다른 위치로 보이는 것.
position: absolute; -> 원래 자리를 차지하지 않고, 부모 요소의 왼쪽 상단을 기준으로 이동.
position: sticky; -> 항상 내가 있는 위치를 기준으로 띄우겠다.

165p 형 동생 하는거 직접 쳐보기

### Emmet

[치트시트 바로가기](https://docs.emmet.io/cheat-sheet/)


! tab
p*5 tab
div*3 tab
단축기 잘쓰자.

flukeout.github.io

