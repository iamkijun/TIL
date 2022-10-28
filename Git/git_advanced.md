
## Git undoing

### git의 환경 3가지

1. working directory
   - 이전 커밋 상태로 되돌리기
   - git restore
2. staging area
   - Staging Area에 반영된 파일을 Working Directory 되돌리기
   - git rm --cached
   - git restore --staged
3. repository
   - 커밋을 완료한 파일을 Staging Area로 되돌리기
   - git commit -amend


### working directory
- 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
**- git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것 !**
- git restore {파일 이름}
- 이전 버전에서는 git checkout -- {파일 이름}

### staging area
- root-commit이 없는 경우: git rm --cached {파일 이름}
  - 커밋이 하나도 없는 경우
- root-commit이 있는 경우: git restore --staged {파일 이름}
  - 커밋이 한개라도 있는 경우
  - 이전 버전에서는 git reset HEAD {파일 이름}

### Repository
- git commit --amend
- 수정 사항을 반영하기 위해 새로운 커밋을 생성하지 않아도 됨
- Staging area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
- Staging area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기 

### Reset & Revert
- git reset --[옵션] {커밋 ID}
  - 시계를 마치 과거로 되돌리는 듯한 행위로, 프로젝트를 특정 커밋(버전) 상태로 되돌림
  - 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
  - 옵션은 soft, mixed, hard 중 하나를 작성 (default = mixed)
    - soft
      - 해당 커밋으로 되돌아가고
      - 되돌아간 커밋 이후의 파일들은 Staging Area로 되돌려놓음
    - mixed
      - 해당 커밋으로 되돌아가고
      - 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
      - git reset 옵션의 기본값
    - hard
      - 해당 커밋으로 되돌아가고
      - 되돌아간 커밋 이후의 파일들은 Working Director에서 삭제 **(위험!!!)**
      - 기존은 Untracked 파일은 사라지지 않고 Untracked로 남아있음
  - 커밋ID는 되돌아가고 싶은 시점의 커밋 ID를 작성

- git reflog
  - reset 하기 전의 과거 커밋 내역을 모두 조회 가능
  
- git revert {커밋 ID}
  - 커밋 ID는 취소하고 싶은 커밋 ID를 작성
  - 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성함

### Git Branch
- 나 혼자 x 여러명이서 같이
- 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
- 지금까지의 commit history를 건드리지 않고 보존한 상태에서 이어서 개발하고 싶을 때 언제든지 활용

장점
1. 독립공간을 형성하기 때문에 원본(master)에 대해 안전함
2. 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
3. Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

git branch
- 조회
  - **git branch** #로컬 저장소의 브랜치 목록 확인
  - git branch -r #원격 저장소의 브랜치 목록 확인
- 생성
  - **git branch {브랜치 이름}** #새로운 브랜치 생성
  - git branch {브랜치 이름} {커밋 ID} #특정 커밋 기준으로 브랜치 생성
- 삭제
  - **git branch -d {브랜치 이름}** #병합된 브랜치만 삭제 가능
  - git branch -D {브랜치 이름} #강제 삭제\


git switch
- 현재 브랜치에서 다른 브랜드로 이동하는 명령어
- git switch {브랜치 이름} #다른 브랜치로 이동
- git switch -c {브랜치 이름} #브랜치를 새로 성생 및 이동
- git switch -c {브랜치 이름} {커밋 ID} 3특정 커밋 기준으로 브랜치 생성 및 이동
- switch 하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의할 것~~!
  - 다른 브랜치에서 파일을 만들고 커밋 하지 않는 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨.

git merge
- 분기된 브랜치(Branch)들을 하나로 합치는 명령어
- master 브랜치가 사용이므로, 주로 master 브랜치에 병합
- git merge {합칠 브랜치 이름}
  - 병합하기 전에 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야함
  - 병합에서는 세 종류가 존재
      1. fast-foward
      2. 3-way merge
      3. merge conflict