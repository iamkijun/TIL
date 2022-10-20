# Django
---
## 0830
---

### Django
Full Stack Framework 지만,
Back end Framework로 사용되고 있고,
Front end Framework로 Vue를 사용.

이미 수없이 개발되었고, 좋은 구조의 코드로 만들어졌음.

Python 기반의 Framework는 Django, Flask

하나의 Framework로 개발할 수 있는 역량을 키우고, 흐름에 따라 다른 Framework를 공부

### MTV Design Pattern

MVC 디자인 패턴을 기반으로 한 MTV패턴(Model Template View)

- Model: **데이터**와 관련된 로직을 관리
- Template: 레이아웃과 **화면**을 처리
- View: Model & Template과 관련한 로직을 처리해서 응답을 반환**(중간처리)**

### 가상환경 만들기

$ python -m venv venv

$ source ./venv/Scripts/activate

(venv) 가상환경 상태

새로운 가상환경을 만들면 pip, setuptolls 밖에 없음
(pip list로 확인)

$ pip install django==3.2.13

패키지 목록 생성
$ pip freeze > requirements.txt

패키지 목록 불러와서 설치
$ pip install -r requirements.txt

LTS - Long Term Support (장기 지원 버전)

$ django-admin startproject firstpjt .

$ python manage.py runserver

서버 종료 - ctrl + C

asgi - 애스기 - 배포시 사용
wsgi - 위스기 - 배포시 사용

settings.py - Django 프로젝트 설정을 관리
urls.py - 사이트의 url과 적절한 views의 연결을 지정

하나의 앱에 여러가지 기능

$ python manage.py startapp articles

settings.py에 들어가서 INSTALLED_APPS 리스트에 'articles' 추가

리스트는 순서가 있는 자료형이므로 내가 작성한 코드를 먼저 입력(위에다가)

1. Url 2. View 3. Template 적는 순서로 많이 가는구나~

render(request, template_name, context)
어딨는줄 알고 template_name을 불러오는걸까?
- 'APP_DIRS': True 
- 'DIRS'에 템플릿이 들어있는 경로를 추가해주자!
- context는 데이터를 불러온다는 뜻

다양한 context - 딕셔너리로 묶어서 부를때 key.value

트레일링 슬래쉬가 기본옵션

앞에 슬래쉬를 붙이면 홈
앞에 슬래쉬를 떼면 내가 있는 위치에서

### Django Template

1. {{variable|filter}} - 변수|필터
2. {% tag %} - 반복, 논리
3. comments


  {% block content %}
  {% endblock content %}
  {% extend '' %}

BASE_DIR - 프로젝트의 홈 경로

settings - 'DIRS': [BASE_DIR/'templates',]

form
1. action
2. method - GET/POST