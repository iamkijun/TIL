import sys
sys.stdin = open('DP/input.txt','r')

'''
ABRACADABRA
ECADADABRBCRDARA
'''
# 5582 -> 9251 -> 1695

#제한된 선택지에서 선택하는 문제는, DP로 접근하자.

s = input()
t = input()

for i in range(len(s)):
    