import sys
sys.stdin = open("sample_input.txt")

def pop(li):
    stack1 = [] # ()
    stack2 = [] # []
    stack3 = [] # {}
    stack4 = [] # <>

    ans = 1

    for val in li:
        if val == '(':
            stack1.append('(')
        elif val == ')':
            if stack1:
                stack1.pop()
            else:
                ans = 0
                break

        elif val == '[':
            stack2.append('[')
        elif val == ']':
            if stack2:
                stack2.pop()
            else:
                ans = 0
                break
        
        elif val == '{':
            stack3.append('{')
        elif val == '}':
            if stack3:
                stack3.pop()
            else:
                ans = 0
                break

        elif val == '<':
            stack4.append('<')
        elif val == '>':
            if stack4:
                stack4.pop()
            else:
                ans = 0
                break
    
    return ans

for t in range(1, 11):
    n = int(input())

    li = list(map(str,input()))

    print(f'#{t} {pop(li)}')

    