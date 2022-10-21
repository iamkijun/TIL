import sys
input=sys.stdin.readline
# sys.stdin = open('Tree/input.txt','r')

N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (N+1)

q = [1]

li =[]

while q:

    num = q.pop(0)
    
    visited[num] = 1

    if num != 1 and len(arr[num]) == 1:      # 리프 노드일 때
        li.append(num)
        continue

    for nn in arr[num]:
        if visited[nn] == 0:
            q.append(nn)

if len(li) % 2:
    print('Yes')
else:
    print('No')