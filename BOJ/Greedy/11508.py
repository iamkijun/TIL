import sys
sys.stdin = open('Greedy/input.txt','r')

N = int(input())

milk_list = [0] * N

for i in range(N):
    milk_list[i] = int(input())

milk_list.sort()

ans = 0
while len(milk_list) >= 3:
    
    ans += milk_list.pop(-1)
    ans += milk_list.pop(-1)
    milk_list.pop(-1)

if milk_list:
    ans += sum(milk_list)

print(ans)