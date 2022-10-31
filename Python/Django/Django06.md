# Django
---
## 0908
---
### 복습

장고 폼의 장점
- 유효성 검증이나 폼 자체를 자동으로 랜더링
- 반복되는 코드를 줄일 수 있다.

forms.form

### 위젯

Textarea 큼지막한 입력공간

### 모델 폼

폼 필드 선언을 하나씩 안해도 됨
필드를 작성하지 않아도 되니 중복된 코드를 줄일 수 있음

수정할땐 instance를 인자로 꼭 받아야댐
인자를 넣지 않으면 수정(edit)이 아니라 생성(create)

### HTTP requests

### HTTP methods
view함수가 특정한 요청 method만 허용하도록 하는 데코레이터

require_safe를 사용하는 것을 권장

### AbstractUser
AbstractBaseUser을 활용한다면 원하는 내용들만 추가해서 사용하면 됨.

### MIGRATION 초기화
1. migrations 폴더에 init 남기고 지운다.
2. db.sqlite3를 지운다
3. make migrations
4. migrate

### 쿠키
데이터를 저장하는 작은 공간
세션 - 클라이언트와 서버간의 상태를 연결해주는 데이터베이스

### HTTP
1. 비연결 지향
2. 무상태

로그인 상태를 유지하기 위해 쿠키와 세션을 통해 서버-클라이언트간 지속적인 상태 유지

로그인 메서드 하나로 검증

1. 탈퇴 후
2. 로그아웃