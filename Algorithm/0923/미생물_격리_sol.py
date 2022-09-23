import sys
sys.stdin = open('input.txt','r')

tbl = [0,2,1,4,3]        #현재 방향을 넣으면 반대방향 리털
di = [0,-1,1,0,0]
dj = [0,0,0,-1,1]


T = int(input())

for t in range(1,T+1):

    N, M, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        # [1]칸 이동처리 후 경계인 경우 처리
        for i in range(len(arr)):
            # 0: i좌표, 1: j좌표, 2: 매생물 세포 크기, 3: direction
            arr[i][0] = arr[i][0]+di[arr[i][3]]
            arr[i][1] = arr[i][1]+dj[arr[i][3]]
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] //= 2
                arr[i][3] = tbl[arr[i][3]]

        # [2] 같은좌표 순, 미생물 순 내림차순 정렬
        arr.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)

        # [3] 같은좌표인 경우 합치고(위쪽 큰 미생물과). 나를
        i = 1
        while i < len(arr):
            if arr[i-1][0:2] ==arr[i][0:2]:
                arr[i-1][2] += arr[i][2]        #미생물 수 합침
                arr.pop(i)                      #합쳤으니 나는 제거
            else:
                i += 1

    total = 0
    for i in range(len(arr)):
            total += arr[i][2]

    print(f'#{t} {total}')