from re import L
import sys
sys.stdin = open('String/input.txt','r')


longs = input()
shorts = input()

idx = 0
k = len(shorts)
cnt = 0
while idx <= len(longs)-1:
    if shorts == longs[idx:idx+k]:
        cnt +=1
        idx += k
    else:
        idx +=1

print(cnt)