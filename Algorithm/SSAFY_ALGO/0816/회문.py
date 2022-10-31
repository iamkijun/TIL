import sys
sys.stdin = open("input.txt","r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = []  #단어를 담을 리스트
    arr_s =[] #알파벳 하나하나를 담을 리스트

    for i in range(N):
        s = input() #단어를 담은 변수 s
        l = list(s) #알파벳 하나하나를 담은 리스트 l
        arr.append(s)
        arr_s.append(l)

    remember = ""

    # [1] 행을 비교
    for j in range(N):
        for k in range(N-M+1):
            if arr[j][k:k+M] == arr[j][k:k+M][::-1]:
                remember = arr[j][k:k+M]

    # [2] 전치행렬
    for j in range(N):
        for k in range(N):
            if j < k:
                arr_s[j][k], arr_s[k][j] = arr_s[k][j], arr_s[j][k]

    # [3] 열을 비교(전치행렬로 변환 후 행을 비교)
    for j in range(N):
        for k in range(N-M+1):
            if arr_s[j][k:k+M] == arr_s[j][k:k+M][::-1]:
                remember = arr_s[j][k:k+M]
                remember = ','.join(remember)
                remember = remember.replace(',','') #리스트에 담긴 알파벳을 결합


    print(f'#{t} {remember}')