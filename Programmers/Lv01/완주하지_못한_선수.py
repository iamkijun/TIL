participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    dic_par = {}
    dic_com = {}

    for val in participant:
        if val in dic_par:
            dic_par[val] += 1
        else:
            dic_par[val] = 1

    for val in completion:
        if val in dic_com:
            dic_com[val] += 1
        else:
            dic_com[val] = 1

    print(dic_par)
    print(dic_com)

    for key in dic_com:
        dic_par[key] -= dic_com[key]

    for key in dic_par:
        if dic_par[key] >0:
            return key
