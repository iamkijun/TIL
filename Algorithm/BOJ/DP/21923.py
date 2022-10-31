import sys
sys.stdin = open('DP/input.txt','r')

'''
3 4
1 5 -6 1
3 -3 9 5
1 -1 1 -3
'''

#제한된 선택지에서 선택하는 문제는, DP로 접근하자.

N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]