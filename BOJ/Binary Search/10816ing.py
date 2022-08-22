import sys
sys.stdin = open('input.txt','r')

N = int(input())

n_list = list(map(int, input().split()))

M = int(input())

m_list = list(map(int, input().split()))

m_count = [0] * M

for i in range(M):
    m_count[i] = n_list.count(m_list[i])

print(*m_count)