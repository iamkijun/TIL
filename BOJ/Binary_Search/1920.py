
import sys
sys.stdin = open('input.txt','r')

N = int(input())

n_list = list(map(int, input().split()))
n_list.sort()

M = int(input())

m_list = list(map(int, input().split()))

def Bi(li,key):
    s = 0
    e = len(li)-1

    while s <= e:
        middle = (s+e) // 2
        if li[middle] == key:
            return 1
        elif li[middle] > key:
            e = middle - 1
        elif li[middle] < key:
            s = middle + 1

    return 0

for i in range(M):
    print(Bi(n_list,m_list[i]))
