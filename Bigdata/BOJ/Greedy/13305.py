import sys
sys.stdin = open("Greedy/input.txt","r")

N = int(input())        #   도시의 개수

distance = list(map(int, input().split()))      #  도시 사이의 길이 ( N-1개 )

price = list(map(int, input().split()))         #  주유소의 기름 가격 (N)
price.pop(-1)

min_price = price[0]

total = 0       # 지불해야 하는 금액

for i in range(N-1):

    if price[i] < min_price:
        min_price = price[i]

    total += (min_price * distance[i])

print(total)
