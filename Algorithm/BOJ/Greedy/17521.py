import sys
sys.stdin = open("Greedy/input.txt","r")

n, W = map(int, input().split())

price_list = []

for i in range(n):
    price = int(input())
    price_list.append(price)


for i in range(n-1):
    if price_list[i] < price_list[i+1]:
        W = W + (W//price_list[i])*(price_list[i+1]-price_list[i])

print(W)