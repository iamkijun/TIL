import sys
sys.stdin = open('string/input.txt','r')

s = input()
t = input()

if s *len(t) == t * len(s):
    print(1)
else:
    print(0)