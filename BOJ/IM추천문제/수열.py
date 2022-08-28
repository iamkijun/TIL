import sys
sys.stdin = open('IM추천문제/input.txt','r')

N, K = map(int, input().split())

N_list = list(map(int,input().split())) +[-100]

first_sum = sum(N_list[:K])
max_sum = sum(N_list[:K])

for i in range(1,N-K+1):
    tem1 = N_list[i-1]
    tem2 = N_list[i+K-1]
    first_sum = first_sum - tem1 + tem2
    if first_sum > max_sum:
        max_sum = first_sum
    
print(max_sum)