## 1107
---
### 상태 관리
- 현재에 대한 정보(data)
- 각 component는 독립적이기 때문에 각각의 상태(data)를 가짐
- 하지만 각각의 component들이 모여서 하나의 App을 구성할 예정
- 여러개의 component가 같은 상태를 유지할 필요가 있음 => 상태 관리가 필요 !!

- Pass Props & Emit Event는 component의 중첩이 깊어지면 데이터 전달이 쉽지 않음
- 중앙 저장소(Store)에 데이터를 모아서 상태 관리
  - 계층에 상관이 없어진다.

### Vuex
- 상태관리 패턴 + 라이브러리 for vue.js
- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙 설정
- Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공

```
vue create vuex-app
```
src에 store라는 디렉토리가 생김.
``` javascript

// ./src/store/index.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
```

state - data
getters - computed
mutations, actions - methods

### State
- vue 인스턴스의 data
- 중앙에서 관리하는 모든 상태 정보
- 원래는 각각의 component에서 관리, 이젠 중앙 저장소에서 관리
- $store.state로 state 데이터에 접근

### Mutations
- 실제로 state를 변경하는 유일한 방법
- Mutations에서 호출되는 핸들러(handler) 함수는 반드시 동기적이어야 함
- 첫번째 인자로 state를 받으며, component 혹은 Actions에서 commit() 메서드로 호출됨.

### Actions
- Mutations와 비슷하지만 **비동기** 작업을 포함할 수 있음
- state를 직접 변경하지 않고 commit() 메서드로 mutations를 호출해서 state를 변경함
- context 객체를 인자로 받으며 store.js의 모든 요소와 메서드에 접근할 수 있음 (즉 state를 직접 변경할 수 있지만 하지 않아야 함)
- component에서 dispatch() 메서드에 의해 호출됨
- 첫번째 인자는 context, 두번째 인자는 payload

### Getters
- state를 활용하여 계산된 값을 얻고자 할 때 사용
- computed와 마찬가지로 getters의 결과는 캐시(cache) 되며, 종속된 값이 변경된 경우에만 재계산됨
- 첫번째 인자로 state, 두번째 인자로 getter를 받음


## Lifecycle Hooks
- 각 Vue 인스턴스는 생성과 소멸 과정 중 단계별 초기화 과정을 거침


### Local Storage
- 브라우저에서 제공하는 저장공간 중 하나인  Local Storage에 관련된 속성
- 데이터가 문자열 형태로 저장
- setItem(key, value) - key, value 형태로 저장
- getItem(key) - key에 해당하는 데이터 조회
