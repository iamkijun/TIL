import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())

arr = []

for i in range(N):
    
    start, end = map(int, input().split())

    arr.append([start,end])
    
arr.sort(key = lambda a:a[0])
arr.sort(key = lambda a:a[1])

time = 0
cnt = 0
for start, end in arr:
    if start >= time:
        cnt +=1
        time = end

print(cnt)