# Django
---
## 0907
---
### Django authentication system

- Authentication(인증)
  - 신원 확인
  - 사용자가 자신이 누군인지 확인하는 것
- Authorization(권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

``` python
# settings.py

AUTH_USER_MODEL = 'auth.User'

# accounts/models. py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass

# settings.py

AUTH_USER_MODEL = 'accounts.User'

# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.adin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



데이터베이스 초기화

1. migrations 파일 삭제
   - migrations 폴더 및 __init__.py 는 삭제하지 않음
   - 번호가 붙은 파일만 삭제
2. db.sqlite3 삭제
3. migrations 진행
   - makemigrations
   - migrate\

### HTTP 특징

1. 비연결 지향(connectionless)
   - 서버는 요청에 대한 응답을 보낸 후 응답을 끊음
2. 무상태(stateless)
   - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며, 상태 정보가 유지되지 않음
   - 클라이언트와 서버가 주고 받는 메시지들은 서로 완전히 독립적

상태가 있는 세션을 유지하기 위해서 쿠키가 나왔다.

### 쿠키

HTTP 쿠키는 상태가 있는 세션을 만들도록 해줌

사용목적

- 세션관리
- 개인화
- 트래킹