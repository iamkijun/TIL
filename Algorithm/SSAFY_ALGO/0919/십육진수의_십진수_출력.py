import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    S = str(input())

    print(f'#{t}',end=" ")
    
    li = []
    
    for i in range(len(S)):
        if S[i].isdigit():
            if S[i] == 10:
                li.append(10 * 16**(len(S)-1-i))
            else:
                li.append(int(S[i]) * 16**(len(S)-1-i))
        else:
            li.append((ord(S[i])-55) * 16**(len(S)-1-i))


    x = sum(li)
    y =''
    while x>0:
        y=str(x%2)+y
        x//=2

    print(y)
    
    # for i in range(len(y)//7):