import sys
sys.stdin = open('input.txt','r')

T= int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0        #가장 많이 죽였을 때의 값
    
    # [1] 배열 돌기
    for i in range(N-M+1):
        for j in range(N-M+1):
            # [2] 해당 좌표에서 파리잡기 시작
            count_kill = 0      #파리 죽인 횟수 저장하는 변수
            for k in range(M):
                for l in range(M):
                    count_kill += arr[i+k][j+l]
            # [3] 최대값과 비교
            if count_kill > max_kill:
                max_kill = count_kill

    print(f'#{t} {max_kill}')
    


        

    