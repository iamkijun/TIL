import sys
sys.stdin = open('Stack/input.txt','r')

icp = {'(':3,')':3,'+':1,'-':1,'*':2,'/':2}  #incomming priority
isp = {'(':0,')':0,'+':1,'-':1,'*':2,'/':2}  #in stack priority

S = input()
stk = [] #임시 저장소
ans = '' #값들 저장소
for val in S:
    if val.isalpha():
        ans += val
    
    else:
        #무조건 스택에 저장하는 경우
        if val == '(':
            stk.append(val)
        elif val == ')':
            if stk:
                while stk[-1] != '(':
                    ans+= stk.pop()
            stk.pop()
        else:
            while stk and isp[stk[-1]] >= icp[val]:
                ans += stk.pop()
            stk.append(val)
    
    
while stk:
    ans += stk.pop()

print(ans)

    