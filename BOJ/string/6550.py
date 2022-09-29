import sys
sys.stdin = open('String/input.txt','r')

while True:
    try:
        s, t = input().split()

        # print(s,t)
        idx = 0
        while True:
            if len(s) >= len(t)-idx:
                print('No')
                break
            elif s[0] == t[idx]:
                if s == t[idx:idx+len(s)]:
                    print('Yes')
                    break
                else:
                    idx +=1
            else:
                idx += 1
            # print(s,t[idx:idx+len(s)])
            # print(idx)
    except:
        break