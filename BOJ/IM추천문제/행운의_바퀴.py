import sys
sys.stdin = open('IM추천문제/input.txt','r')

N, K = map(int, input().split())

S_list = []
st_list = []

for i in range(K):
    S, st = map(str, input().split())
    S = int(S)
    S_list.append(S)
    st_list.append(st)

li = ['?'] * N
a = 0 #시작점


iserror = 0
for i in range(K):
    if S_list[i]-a > 0:
        if li[S_list[i]-a] =='?':
            li[S_list[i]-a] = st_list[i]
            a = S_list[i]-a             #시작점 초기화
        elif li[S_list[i]-a] == st_list[i]:
            pass
        else:
            iserror = 1
            break

    elif S_list[i]-a < 0:
        if li[S_list[i]-a+8] =='?':
            li[S_list[i]-a+8] = st_list[i]
            a = S_list[i]-a+8             #시작점 초기화
        elif li[S_list[i]-a+8] == st_list[i]:
            pass
        else:
            iserror = 1
            break
    print(li)

if iserror == 1:
    print("!")
else:
    print(li)

    # li = li[::-1]*2
    # print(li[li.index(st):-2])




