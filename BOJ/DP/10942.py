import sys
sys.stdin = open('DP/input.txt','r')

'''
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
'''

#제한된 선택지에서 선택하는 문제는, DP로 접근하자.

N = int(input())

li = list(map(int, input().split()))

M = int(input())

for _ in range(M):
    S, E = map(int,input().split())

    if li[S-1:E] == li[S-1:E][::-1]:
        print(1)
    else:
        print(0)