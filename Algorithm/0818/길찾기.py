import sys
sys.stdin = open("input.txt","r")

T= 3

for t in range(1,T+1):
    N,leng = map(int,input().split()) # N: test_case number, leng = 길의 총 개수
    arr = list(map(int, input().split()))

    arr1 = [0] * 100        #정적 배열 두개 생성
    arr2 = [0] * 100        #arr1이 우선적, arr2이 후순위로

    for i in range(leng):
        if arr1[arr[2*i]] == 0:
            arr1[arr[2*i]] = arr[2*i+1]
        else:
            arr2[arr[2*i]] = arr[2*i+1]

    stk = []
    s = 0 #시작
    ans = 0
    print(arr1)
    print(arr2)
    while True:
        if s == 99:     #끝까지 갔을 경우
            ans = 1     #경로가 있다고 봄
            break

        if arr1[s] != 0:    #arr1에 경로가 있을 경우
            stk.append(s)
            s = arr1[s]     #그 다음으로
            arr1[stk[-1]] = 0

        elif arr2[s] != 0:
            stk.append(s)
            s = arr2[s]
            arr2[stk[-1]] = 0

        else:                   #갈 곳이 없어서
            s = stk.pop(-1)         #빠꾸

        if stk == []:           #올라 갈 곳이 없어서
            break               #실패 ans = 0

    print(f'#{t} {ans}')


