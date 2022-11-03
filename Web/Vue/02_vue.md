## 1102 VUE
---
### Vue CLI
Command Line Interface

자바스크립트를 구동하기 위한 런타임 환경인 Node.js로 인해 브라우저가 아닌 환경에서도 구동할 수 있게 됨.

### NPM (Node Package Manage)
- 자바스크립트 패키지 관리자
  - python에 pip가 있다면 node.js에는 npm
  - pip와 마찬가지로 다양한 의존성 패키지 관리

### Vue CLI Quick Start
- 설치
  - npm install -g @vue/cli
- 프로젝트 생성
  - vue create vue-cli
  - vue2 버전 선택
- 프로젝트 생성 성공
  - cd vue-cli
  - npm run serve

### node_modules- Babel
- "JavaScript compiler"
- ES6+ 코드를 구버전으로 번역/변환 해주는 도구
- 파편화, 표준화의 영향으로 작성된 스펙트럼이 매우 다양

### node_modules- Webpack
- "static module bundler"
- 모듈 간의 의존성 문제를 해결하기 위한 도구
프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

### Module
- 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
- 따라서 자연스럽게 파일 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈(module) 즉, js 파일 하나가 하나의 모듈
- 모듈은 대개 기능 단위로 분리, 클래스 하나 혹은 

fabicon
- 서버 켰을 때 나오는 아이콘

src
- assets
  - 정적파일을 저장하는 디렉토리
- components
  - 하위 컴포넌트들이 위치
  - App.vue
  - 최상위 컴포넌트
  - public/index.html과 연결됨

### Component
- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
  - ex)HTML 요소들의 중첩, Body Tag를 root node로 하는 Tree 구조


### SFC
- 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다.
  - 즉, Single File Component
- Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리
- 컴포넌트 기발 개발의 핵심 기능

### Vue component 실습 
1. 컴포넌츠 폴더에 파일 만들기
2. 이름 등록
3. 템플릿에 최상위 요소 추가

### component 등록 3단계
1. 불러오기
``` vue
import MyComponentVue from './components/MyComponent.vue'
import MyComponentVue from '@/components/MyComponent'
```
@:절대경로

2. 등록하기
``` vue
components: {
  HelloWorld,
  // 2. 등록하기
  MyComponentVue,
}
```
중요한 폴더는 전부 src에 담겨있음.
경로 설정 단계에서 @로, 확장자가 .vue일 경우 생략해도 된다.

3. 보여주기
``` vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 -->
    <MyComponent/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>
```

### Data in components
- 부모 => 자식으로의 데이터의 흐름
  - pass props의 방식
- 자식 => 부모로의 데이터 흐름
  - emit event의 방식

### Pass **Props**
- 요소의 속성(property)을 활용하여 데이터 전달
- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- props 속성값에 뭘 받았는지 명시적으로 작성 해주어야 함

부모에서 넘겨주는 props
- kebab-case

자식에서 받는 props
- camelCase

단방향 데이터 흐름
- 모든 props는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성
- 부모 속성이 업데이트 되면 자식으로 흐르지만, 반대 방향은 아님
  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨.
- 하위 컴포넌트에서 prop을 변경하려고 시도해서는 안되며 그렇게 하면 VUE는 콘솔에서 경고를 출력함.

### Emit **Event**
- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때 이벤트 발생
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러함수(ChildToParent) 호출
2. 호출된 함수에서 $emit을 통해 부모 컴포넌트에 이벤트(child-to-parent)를 발생
  - 이벤트 데이터(child data)를 함께 전달
3. 부모 컴포넌트는 자식 컴포넌트의 이벤트(child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent) 호출, 함수의 인자로 전달된 데이터(child data)가 포함되어 있음
4. 호출된 함수에서 console.log(`~child data~`) 실행

### pass props / emit event 컨벤션
- HTML 요소에서 사용할 때는 kebab-case
- JavaScript 요소에서 사용할 때는 camelCase

props
- 상위 => 하위 흐름에서 HTML 요소로 내려줌: kebab-case
- 하위에서 받을 때 JavaScript에서 받음: camelCase

emit
- emit 이벤트를 발생시키면 HTML 요소가 이벤트를 쟁취함:kebab-case
- 메서드, 변수명 등은 JavaScript에서 사용함: camelCase