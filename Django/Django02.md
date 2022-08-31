# Django

---

## 0831

---

### url태그

{% url 'articles:greeting' %}

app_name을 지정한 이후에는 url태그에서 반드시 app_name:url_name 형태로만 사용해야 함. 그렇지 않으면 NoReverceMatch 에러가 발생



폴더 구조를 app_name/templates/app_name/ 형태로 변경



### 데이터베이스

- 체계화된 데이터의 모임. 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해서 조직화된 데이터를 수집하는 저장 시스템

### Model

새 프로젝트 작성 초기 세팅

$ django-admin startproject crud .   (프로젝트 생성)

$ python manage.py startapp articles.    (앱 생성)

settings.py 들어가서 INSTALLED_APPS에 'articles' 추가



모델 클래스를 작성하는 것은 데이터베이스의 테이블 스키마를 정의하는 것. 모델 클래스 == 테이블 스키마

각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨

데이터 유형에 따라 다양한 모델 필드를 제공

- DataField(), CharField(), IntegerField() 등
- CharField(max_length = None, **options)
  - 길이의 제한이 있는 문자열을 넣을 때 사용(필수 인자)
  - 유효성 검사에서 활용됨
- TextField(**options)
  - 글자의 수가 많을 때 사용
  - max_length 옵션 x



python manage.py makemigrations

마이그레이션 - 설계도, 청사진. "모델과 DB의 동기화"

1. showmigrations
   - $ python manage.py showmigrations
   - migrations파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
   -  X 표시가 있으면 migrate가 완료되었음을 의미
2. sqlmigrate
   - $ python manage.py sqlmigrate articles 0001
   - 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인할 수 있음

Models.py에서 변경사항이 발생하면

makemigrations (migration 생성)

Migrate (db반영, 모델과 db의 동기화)



### ORM

Object-Relational-Mapping

객체지향 프로그래밍언어를 사용하여 호환되지 않은 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

한마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개

ORM만으로는 세밀한 데이터베이스 조작 구현이 어려운 경우가 있다.