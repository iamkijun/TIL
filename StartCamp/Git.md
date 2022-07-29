# 이기준

날짜: 2022년 7월 14일 오후 2:37

---

# 7/14 필기

**git**: 분산 버전 관리 프로그램

중앙 집중식 버전 관리 / 분산 버전 관리

서버터지면 날라가는걸 분산 버전 관리를 통해 복구 가능

github: Git 기반의 저장소 서비스를 제공하는 서버

**gitlab(samsung)**, github(microsoft), bitbucket

git ≠github

github 개방적인 프로그램 

1일 1커밋 하자.

 CLI: 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식

(↔GUI: 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식)

CLI 장점 - 경제적이다.

GUI 장점 - 가시적이다.

touch 파일 생성

MKdir 새폴더 생성

ls 현재 작업중인 파일과 폴더 목록

cd 디렉토리 변경 (cd.. ← 상위폴더로)

start, open 폴더나 파일을 여는 명령어

rm 파일을 삭제(-r 폴더 삭제)

![Untitled](%E1%84%8B%E1%85%B5%E1%84%80%E1%85%B5%E1%84%8C%E1%85%AE%E1%86%AB%20d094dd7f18a048cbbf679e5dacc088fb/Untitled.png)

~ 현재 작업중인 위치

C:\Users\multicampus ← 홈디렉토리

.은 나 자신, ..은 상위

절대경로 - 모든 경로를 전부 작성

상대경로 - 내가 작업하고 있는 디렉토리를 기준으로 

(./ 현재 작업하고 있는 폴더, ../ 현재 작업하고 있는 폴더의 부모 폴더)

Markdown: 텍스트 기반의 가벼운 마크업(markup) 언어

[README.md](http://README.md) ← 특별한.. 오픈 소스의 공식 문서 작성

~~typora 실시간 마크다운 변환~~

~~환경설정 이미지, 경로로 이미지 복사, 1235~~

~~저장 test.md~~

#헤딩 - 제목이나 소제목으로만.

#1~#6개(노션은 3개까지)

문서 구조의 기본

리스트 - 순서가 있는 리스트/ 순서가 없는 리스

탭 들여쓰기, 시프트 탭 내어쓰기

별표나 하이픈

---

코드블럭 - 일반 텍스트와 다르게 코드를 이쁘게 출력

‘’’code block’’’ ‘inline code block’

` ← 요걸 백틱이라고 부른다 

```python
신기합니다.
```

[stirng](url) 링크

![stirng](url) 이미지의 url, 이미지의 경로

```python
**bold** *italic* ~~strikeout~~
```

**bold** *italic* ~~strikeout~~

---

---

수평선은 -*3 ___

[마크다운 치트시트]([https://www.markdownguide.org/cheat-sheet/](https://www.markdownguide.org/cheat-sheet/))

[README.md](http://README.md) 모든 개발자들에게 특별하다. ← 설명서/소개문서 같은 파일

---

### Git

특정 폴더를 기준으로 , 버전 관리의 기준

git init 명령어로 로컬 저장소를 생성

.git 디렉토리에 버전 관리에 필요한 모든 것이 들어있음

(master) ← 깃 생긴거라는 뜻

특정 버전으로 남긴다 = “커밋한다”

커밋은 3가지 영역을 바탕으로 동작

1. Working Directory(내가 작업중인),
2. **Staging Area**(커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳), **???**
3. Repository(커밋들이 저장되는 저장소)

**git add** - working directory에 있는 작업중인걸 특정 버전으로 남기는 → staged 된다.

**git commit -** 변경사항들을 커밋하여 repository에 저장

git commit -m “메시지 따옴표 안에 남기기”

**git status** - 현재 git으로 관리되고 있는 파일들의 상태

git log - 기록 보기

git diff A B

A를 기준으로 B가 어떻게 변경되어 있는지 알려준다.

git push A B

A -  어디로, B -

git push -u origin master

깃 푸시하면 자동으로 푸시 

커밋한 파일을 수정하고 싶다 - 다시 워킹디렉토리로. 하지만 이때는 untracted 상태가 아닌, modified 상태

vs code

폰트설정부터

d2coding

2번째 d2coding all

설정(컨트롤 컴마(,))

font family - D2Coding

#### 저장을 습관화하자

git bash

방향키 위로 올리면 히스토리 볼 수 있음

git remote add **origin** {[remote_repo](https://github.com/iamkijun/first_repo)}

git push -u **origin** master

get clone {remote_repo} ← remote repo 를 local로 복사

git push origin master

컨트롤 k f 다 끄기

깃 배쉬에서 code . 하면 vs코드 열림

TIL Today I Learned

마크다운