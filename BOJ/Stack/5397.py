import sys
sys.stdin = open('Stack/input.txt','r')

T = int(input())

for t in range(T):
    
    S=list(input())

    left = []
    right = []

    cursor = 0
    
    for val in S:
        if val.isalnum():
            left.append(val)

        elif val == '<':
            if left:
                right.append(left.pop())
                
        elif val == '>':
            if right:
                left.append(right.pop())

        elif val == '-':
            if left:
                left.pop()

    print(''.join(left)+''.join(right[::-1]))