import sys
sys.stdin = open('DP/input.txt','r')

'''
5
1 2 3 4 2
'''
# 5582 -> 9251 -> 1695

#제한된 선택지에서 선택하는 문제는, DP로 접근하자.

N = int(input())

li = list(map(int, input().split()))

