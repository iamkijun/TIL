import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())

for t in range(1,T+1):

    N, M = map(int, input().split())
    #외부에 0으로 덮어주기(양 끝을 기준으로 +(M-1)만큼)
    arr = [[0] * (N + 2*(M-1)) for _ in range(M-1)] + [[0] * (M-1) + list(map(int, input().split())) + [0] * (M-1) for _ in range(N)] + [[0] * (N + 2*(M-1)) for _ in range(M-1)]
    #찾고자 하는 최대값
    maxV = 0
    #0이 아닌 입력 배열의 처음과 끝을 전수조사
    for i in range(M-1,M+N-1):
        for j in range(M-1,M+N-1):
            #+모양은 V_plus에, X모양은 V_X에 저장
            V_plus = 0
            V_X = 0
            #M>2이상일 경우 퍼지는 4칸씩을 더해줌
            if M > 2:
                for k in range(1,M):
                    V_plus += arr[i+k][j] + arr[i-k][j] + arr[i][j+k] + arr[i][j-k]
                    V_X += arr[i+k][j+k] + arr[i+k][j-k] + arr[i-k][j+k] + arr[i-k][j-k]
            #M=2일 경우에는 한번만 더해줌
            elif M == 2:
                V_plus = arr[i + 1][j] + arr[i - 1][j] + arr[i][j + 1] + arr[i][j - 1]
                V_X = arr[i + 1][j + 1] + arr[i + 1][j - 1] + arr[i - 1][j + 1] + arr[i - 1][j - 1]
            #M=1에 해당하는 자기 자신 값 더해서 마무리
            V_plus += arr[i][j]
            V_X += arr[i][j]
            #최대값 찾기
            if V_plus > maxV:
                maxV = V_plus
            if V_X > maxV:
                maxV = V_X

    print(f'#{t} {maxV}')