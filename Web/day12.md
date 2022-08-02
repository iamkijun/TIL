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