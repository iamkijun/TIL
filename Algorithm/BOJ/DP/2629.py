import sys
sys.stdin = open('DP/input.txt','r')

'''
2
1 4
2
3 2
'''

#제한된 선택지에서 선택하는 문제는, DP로 접근하자.

N,M = map(int, input().split())
