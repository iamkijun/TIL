import sys
sys.stdin = open('Binary_Search/input.txt','r')

N = int(input())

n_list = list(map(int, input().split()))
n_list.sort()

cnt ={}
for card in n_list:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

M = int(input())

m_list = list(map(int, input().split()))

NM = [0] * N

for i in range(M):
    if m_list[i] in cnt:
        print(cnt[m_list[i]], end=" ")
    else:
        print(0, end=" ")
    
print()