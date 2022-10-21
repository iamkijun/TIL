import sys
sys.stdin = open('input.txt','r')

n = int(input())
stk = []
ans = []
i =1
bp = 0
for _ in range(n):
    # [1] 숫자 입력
    num = int(input())

    # [2] 스택 쌓기
    while i <= num:
        stk.append(i)
        ans.append("+")
        i +=1
    
    # [3] 스택 꺼내기
    if stk[-1] == num:
        stk.pop()
        ans.append("-")
    else:
        bp =1

if bp:
    print("NO")
else:
    for val in ans:
        print(val)