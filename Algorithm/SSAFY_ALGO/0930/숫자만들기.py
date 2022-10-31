import sys
sys.stdin = open('input.txt','r')

from itertools import permutations
from collections import deque
T = int(input())

def find_max_val(num_li, operator):
    global max_val

for t in range(1,T+1):
    N = int(input())

    operator = list(map(int,input().split()))

    combination = ['+']*operator[0] + ['-']*operator[1] + ['*']*operator[2] + ['/']*operator[3]


    max_val = - (9 ** 12)
    min_val = 9 ** 12

    num_li = list(map(int, input().split()))
    distinct = []
    for a in permutations(combination,sum(operator)):
        if a not in distinct:
            distinct.append(a)
            stk = []
            for i in range(sum(operator)):
                stk.append(num_li[i])
                stk.append(a[i])
            stk.append(num_li[-1])
            # print(stk)
            stk = deque(stk)
            val = 0
            while len(stk) >1:
                if stk[1] == '+':
                    val = stk[0] +stk[2]
                    stk.popleft()
                    stk.popleft()
                    stk.popleft()
                    stk.appendleft(val)
                elif stk[1] == '-':
                    val = stk[0] - stk[2]
                    stk.popleft()
                    stk.popleft()
                    stk.popleft()
                    stk.appendleft(val)

                elif stk[1] == '*':
                    val = stk[0] * stk[2]
                    stk.popleft()
                    stk.popleft()
                    stk.popleft()
                    stk.appendleft(val)

                elif stk[1] == '/':
                    val = int(stk[0] / stk[2])
                    stk.popleft()
                    stk.popleft()
                    stk.popleft()
                    stk.appendleft(val)
            val = stk[0]

            if val > max_val:
                max_val= val
            if val < min_val:
                min_val = val


    print(f'#{t} {max_val-min_val}')

