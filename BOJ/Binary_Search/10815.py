import sys
sys.stdin = open('input.txt','r')

N = int(input())

n_list = set(map(int, input().split()))

M = int(input())

m_list = list(map(int, input().split()))

cnts =[0] * M

for i in range(M):
    if m_list[i] in n_list:
        cnts[i] = 1
    

print(*cnts)