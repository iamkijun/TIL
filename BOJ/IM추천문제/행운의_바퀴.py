import sys
sys.stdin = open('input.txt','r')

N, K = map(int, input().split())

li = ['?'] * N
iserror = 0

for i in range(K):
    S, st = map(str, input().split())
    S = int(S) % N
    
    #바퀴 돌리기, 뒤에 s칸이 앞으로 당겨오는 느낌!!
    li = li[-S:] + li[:-S] 
    
    #화살표가 가르키는 지점 확인

    # 아직 안정해졌다면, 
    if li[0] =='?':
        # st가 이미 li안에 있으면 중복이므로 오류
        if st in li:
            iserror = 1
            break
        # st로 변경
        else:
            li[0] = st
    #들어가려는 자리가 st와 같다면 그대로 내비둠
    elif li[0] == st:
        pass
    #들어가려는 자리가 st와 다르다면 오류
    else:
        iserror = 1
        break

if iserror == 1:
    print("!")
else:
    print(''.join(li))
