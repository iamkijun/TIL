# from curses.panel import top_panel
import sys
sys.stdin = open("0819/input.txt","r")

T = int(input())

def pop(li):
    stack = []

    for val in li:
        if val == '(':
            stack.append('(')
        elif val == ')':
            if not stack:
                return 0
            else:
                stack.pop()

    if len(stack) == 0:
        return 1
    elif len(stack) != 0:
        return 0


for t in range(1,T+1):
    
    li = list(map(str, input()))

    print(f'#{t} {pop(li)}')