import sys
sys.stdin = open('D3/input.txt','r')

for t in range(1,11):
    N = int(input())

    li = list(map(int, input().split()))

    #조망권이 확보된 세대의 수
    total = 0

    #2부터 N-2까지 (맨 왼쪽 2칸과 맨 오른쪽 2칸은 빈칸이니까)
    for i in range(2,N-2):

        #자기를 기준으로 왼쪽 두칸과 오른쪽 두칸의 리스트
        l2r2_list = [li[i-2],li[i-1],li[i+1],li[i+2]]
        #그 가운데 최대값을 담아두는 변수를 왼쪽 두번째칸으로 초기 선언
        max_l2r2 = l2r2_list[0]

        # 최대값 찾기
        for j in range(1,4):
            if l2r2_list[j] > max_l2r2:
                max_l2r2 = l2r2_list[j]
        
        # 조망권 확보된 세대 수 저장
        if li[i] > max_l2r2:
            total += (li[i] - max_l2r2)
        
    print(f'#{t} {total}')