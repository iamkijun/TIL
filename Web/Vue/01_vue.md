## 1031 VUE
---
### Front-end
- 사용자에게 보여주는 화면 만들기

### SPA(Single Page Application)
- 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
  - CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문.
  - 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
  1. 필요한 페이지를 서버에 AJAX로 요청
  2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
  3. JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)

CSR 방식의 장점
- 트래픽 감소 -> 응답 속도가 빨라진다.
- 매번 새 문서를 받아 새로고침 하는 것이 아니라, 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
- BE와 FE의 작업 영역을 명확히 분리 할 수 있음. 협업에 용이

### Vue의 구조
HTML ( <template> )
JS ( <script> )
CSS ( <style> )

부착해야지만 쓸 수 있다.

### el
- Vue instance와 DOM을 mount(연결)하는 옵션

### data
- 데이터 객체는 반드시 기본 객체 {} (Object)여야 함.
- interpolation {{}}을 통해 view에 렌더링 가능함.

### Directives
- v-접두사가 있는 특수 속성에는 값을 할당할 수 있음
  - 값에는 JS 표현식을 작성할 수 있음
- directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것

-v-on
  - @ shortcut
-v-bind

method VS computed
- method
  - 호출 될 때마다 함수를 실행
  - 같은 결과여도 매번 새롭게 계산
- computed
  - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
  - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환

