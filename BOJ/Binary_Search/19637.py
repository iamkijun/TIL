import re
import sys
input = sys.stdin.readline
# sys.stdin = open('Binary_Search/input.txt','r')

N, M = map(int, input().split())

dic = {}

for n in range(N):
    li = list(input().split())
    dic[int(li[1])] = li[0]

sorted(dic.keys())
# sorted()
for m in range(M):
    num = int(input())

    for val in dic:
        if num <= val:
            print(dic[val])
            break
