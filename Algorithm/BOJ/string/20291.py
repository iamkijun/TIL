N = int(input())

dic = {}

for _ in range(N):
    S = input()
    exten = S[S.find('.')+1:] #확장자
    
    if exten not in dic:
        dic[exten] = 1
    elif exten in dic:
        dic[exten] += 1

sorted_dic = sorted(dic.items())

for i in range(len(sorted_dic)):
    print(*sorted_dic[i])