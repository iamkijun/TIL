import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1, T + 1):
    memory = input()
    bit = '0'
    cnts = 0

    for i in memory:
        if bit != i:                   # ch가 0이 아니면
            bit = i                    # bit를 ch로 변경
            cnts += 1                  # 카운트 1 증가
    print(f'#{test_case} {cnts}')