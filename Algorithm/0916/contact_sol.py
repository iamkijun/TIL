import sys
sys.stdin = open('input.txt','r')

def bfs(s):
    q = [s]          # q, visited 기타 초기화
    visited = [0] * 101
    ans = s
    visited[s] = 1

    while q:
        c = q.pop(0)
        #정답처리: 더 늦게 방문 or 같은 거리인데 더 큰 번호인 경우
        if visited[ans] < visited[c] or visited[ans] == visited[c] and ans<c:
            ans = c
        for e in adjL[c]:
            if not visited[e]:
                q.append(e)
                visited[e] = visited[c] + 1

    return ans

for t in range(1,11):

    N, S = map(int, input().split())        # N: 데이터의 길이, S: 시작점

    li = list(map(int, input().split()))

    # [1] 연결을 인접리스트에 저장
    adjL = [[] for _ in range(101)]
    for i in range(0,N,2):
        p, c = li[i], li[i+1]
        adjL[p].append(c)

    ans = bfs(S)

    print(f'#{t} {ans}')

