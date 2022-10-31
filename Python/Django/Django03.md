# Django
---
## 0901
---
### Django

MODEL - ORM을 통한 데이터베이스 조작

Render / Redirect

### HTTP response status code
1. Informational responses  (1xx)
2. Successful response      (2xx)     성공
  - 200 **OK**
  - 201 Created
3. Redirection messages     (3xx)
4. Client error responses   (4xx)     실패(클라이언트)
  - 401 Unauthorized
  - 403 Forbidden
  - 404 Not Found
5. Server error responses   (5xx)     실패(서버)
  - 500 Internal Server Error

GET은 데이터를 얻을 때에만, 그 외에 데이터베이스를 수정해야 하는 모든 연산은 POST

method="POST"를 넣는 순간 form 하위에 {% csrf_token %}를 넣어줘야 한다.