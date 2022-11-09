## 1107

---

### UX

- User Experience

### UI

- User Interface
- 유저에게 보여지는 화면을 디자인

### History🦔

- 브라우저의 History API를 활용한 방식

### router-link

- a태그와 비슷한 기능 -> URL을 이동시킴
  - 히스토리에서 router-link는 클릭 이벤트를 차단
- 목표 경로는 'to'로 지정

### router-view

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- block tag와 비슷한 기능
- App.vue는 base.html의 역할
- router-view는 block 태그로 감싼 부분

### 선언적 방식 네비게이션

- router-link의 'to'속성으로 주소 전달

### 프로그래밍 방식 네이게이션

- Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음
- 다른 URL로 이동하려면 this.$router.push를 사용

## 전역가드

### Global Before Guard

- 다른 url 주소로 이동할 때 항상 실행
- router/index.js에 router.beforeEach()를 사용하여 항상 설정
- 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음

  - to: 이동할 url 정보가 담긴 Route 객체
  - from: 현재 url 정보가 담긴 Route 객체
  - next: 지정한 URL로 이동하기 위해 호출하는 함수
    - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
    - 기본적으로 to에 해당하는 URL로 이동

- URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
  - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함
  - next()가 호출되기 전까지 화면이 전환되지 않음

## 라우터 가드

전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용

- beforeEnter()
  - route에 진입했을 때 실행됨
  - 라우터를 등록한 위치에 추가
  - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고, 다른 경로에서 탐색할 때만 실행됨

## 컴포넌트 가드

특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용

- beforeRouteUpdate()
  - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

### optional changing

?. 앞의 평가대상이 undefined나 null이면 에러가 발생하지 않고 undefined를 반환
