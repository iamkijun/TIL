import sys
sys.stdin = open('input.txt','r')


for t in range(1,11):

    N, S = map(int, input().split())        # N: 데이터의 길이, S: 시작점

    li = list(map(int, input().split()))

    dic = {x:[] for x in range(101)}

    for i in range(0,N,2):
        if li[i+1] not in dic[li[i]]:
            dic[li[i]].append(li[i+1])
    graph = []

    for i in range(101):
        graph.append(dic[i])

    stack = [S]
    visited = [0] * 101

    visited[S] = 1

    while stack:

        a = stack.copy()

        for i in range(len(stack)):
            tem = stack.pop(0)
            for j in graph[tem]:
                if not visited[j]:
                    visited[j] = 1
                    stack.append(j)

    print(f'#{t} {max(a)}')