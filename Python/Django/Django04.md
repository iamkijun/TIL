# Django
---
## 0906
---
### Django Form Class

Form Class 선언

- 앱 폴더에 forms.py를 생성 후 ArticleFormClass선언
- Form에는 TextField가 존재하지 않음.

1. 'new' view함수 업데이트

``` python
# articles/views.py
from .forms import ArticleForm

def new(request):
  form = ArticleForm()
  context = {
    'form':form,
  }
  return render(request,'articles/new.html', context)
```

2. 'new' 템플릿 업데이트

   ``` html
   form 안에
   {{form.as_p}}
   ```

   

   ### From rendering options

   1. as_p()

      - 각 필드가 단락(<p> 태그)으로 감싸져서 렌더링

   2. as_ul()

      - 각 필드가 목록 항목(<li>태그)으로 감싸져서 렌더링
      - 'ul'태그는 직접 작성해야 한다.

   3. as_table()

      - 각 필드가 테이블(<tr>태그) 행으로 감싸져서 렌더링

      

      ### 특별한 상황이 아니면 as_p()만 사용할 것



Django의 2가지 HTML input 요소 표현

1. forms.CharField()

2. forms.CharField(widget=forms.Textarea)



다양한 위젯이 존재한다.



### Django ModelForm

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음

- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언

  ``` python
  #articles/forms.py
  
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
    class Meta:
      model = Article
      fields = '__all__'
      #exclude = ('title',)
  ```



### ModelForm with view functions

### Create

- 유효성 검사를 통과하면 데이터 저장 후 상세 페이지로 리다이렉트

- 유효성 검사를 통과하지 못하면 작성 페이지로 리다이렉트

  ``` python
  # articles/views.py
  
  def create(request):
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
    return redirect('articles:new')
  ```



intance인자가 제공되면 해당 인스턴스를 수정

instance인자가 제공되지 않으면 새 인스턴스를 만듬

Error 속성 포함

``` python
# articles/views.py

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



### Widgets

``` python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
```



### Allowed HTTP methods

- django.views.decorators.http 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있음

1. require_http_methods()
2. require_POST()
3. require_safe()



### 마무리

- Django Form Class
  - Django 프로젝트의 주요 유효성 검사 도구
  - 공격 및 데이터 손상에 대한 중요한 방어 수단
  - 유효성 검사에 대해 개발자에게 강력한 편의를 제공
- View 함수 구조 변화
  - HTTP requests 처리에 따른 구조 변화