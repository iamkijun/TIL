import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    S = input()

    ans = [[] for _ in range(len(S))]

    dic = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111',
           '8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

    ans_str = ''
    for i in range(len(S)):
        ans[i].append(dic[S[i]])
        ans_str += ans[i][0]

    new = []
    for i in range(0,len(ans_str),7):
        try:
            new.append(ans_str[i:i+7])
        except:
            new.append(ans_str[i:])

    print(f'#{t}', end=" ")

    for i in range(len(new)):
        val = 0
        for j in range(len(new[i])-1,-1,-1):
            if new[i][j] =='1':
                val += 2**(len(new[i])-1-j)

        print(val, end=" ")

    print()

