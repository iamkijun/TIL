import sys
sys.stdin = open('input.txt','r')

T = int(input())

def find_min_sum():

    global sum_val
    global min_sum_dif

    if sum_val >= B:
        if sum_val - B < min_sum_dif:
            min_sum_dif = sum_val - B
        return

    for i in range(N):

        if not visited[i]:
            visited[i] = True
            sum_val += li[i]
            find_min_sum()
            sum_val -= li[i]
            visited[i] = False

for t in range(1,T+1):

    N, B = map(int, input().split())

    li = list(map(int, input().split()))

    sum_val = 0
    min_sum_dif = sum(li) - B
    visited = [False]*N

    find_min_sum()

    print(f'#{t} {min_sum_dif}')