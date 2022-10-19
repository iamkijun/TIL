import sys
sys.stdin = open('DP/input.txt','r')

'''
1
4 10
'''

#제한된 선택지에서 선택하는 문제는, DP로 접근하자.


T = int(input())
N, M = map(int, input().split())

num_li = [x for x in range(1,M+1)]

dp = [0] * N

