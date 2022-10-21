import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())

li = list(map(int, input().split()))

max_honey = 0
a = sum(li[1:])
b = sum(li[1:])
#[1] 벌벌 꿀 (꿀통이 맨 오른쪽)
for i in range(1,N-1):
    honey = a +b-li[i]*2
    b = b - li[i]
    
    if honey > max_honey:
        max_honey = honey

#[2] 꿀 벌벌 (꿀통이 맨 왼쪽)
a = sum(li[:-1])
b = sum(li[:-1])
for i in range(N-2,0,-1):
    honey = a + b - li[i]*2
    b -= li[i]

    if honey > max_honey:
        max_honey = honey

#[3] 벌 꿀 벌 (꿀통이 가운데)
honey = sum(li[1:-1]) + max(li[1:-1])

if honey > max_honey:
    max_honey = honey

print(max_honey)