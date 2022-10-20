N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

smalls = []
for i in range(N):
    smalls.append(min(arr[i]))

print(max(smalls))