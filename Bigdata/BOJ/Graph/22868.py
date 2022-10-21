'''
4 5
1 2
1 3
2 3
2 4
3 4
1 4
'''

import sys
sys.stdin = open("Graph/input.txt","r")

N, M = map(int, input().split())

li =[]

for i in range(M):
    A, B = map(int, input().split())
    li.append([A,B])

S, E =map(int ,input().split())

visited = [0] *(N+1)

arr = [[] for _ in range(N+1)]
for val in li:
    arr[val[0]].append(val[1])
    arr[val[1]].append(val[0])

print(arr)

def bfs(S):

    q = []
    q.append(S)
    visited[S] = 0
    
    while q:
        temp = q.pop(0)

        print(temp, end=" ")
        for val in arr[temp]:
            if not visited[val]:
                q.append(val)
                visited[val] = 1
        
bfs(S)
