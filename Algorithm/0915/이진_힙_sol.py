import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    li = list(map(int, input().split()))

    # [1] 힙에 데이터 추가 and 최소힙 유지

    heap = [0]*(N+1)
    last = 0
    
    for n in li:
        last += 1           #추가는 제일 마지막!
        heap[last] = n
        
        # 부모가 존재하고, 부모가 나보다 큰 경우: 교환
        c = last
        while c//2 and heap[c] < heap[c//2]:
            heap[c], heap[c//2] = heap[c//2], heap[c]
            c //=2

    # [2] last의 조상노드들의 합
    ans = 0
    c = last//2
    while c:        # 존재하는 노드라면
        ans += heap[c]
        c //= 2

    print(f'#{t} {ans}')