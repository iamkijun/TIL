import sys
sys.stdin = open("input.txt","r")
T= 3

for _ in range(1,T+1):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 가이드에 따른 데이터 저장
    way1 = [-1] * 100
    way2 = [-1] * 100
    for n in range(N):
        if way1[arr[2 * n]] == -1:
            way1[arr[2 * n]] = arr[2 * n + 1]
        else:
            way2[arr[2 * n]] = arr[2 * n + 1]

    print(way1)
    print(way2)
    stk = []
    now = ans = 0