id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dic = {}
    
    for val in id_list:
        dic[val] = [0]*len(id_list)
    
    for i in range(len(report)):
        a = report[i].split()
        dic[a[0]][id_list.index(a[1])] += 1
        if dic[a[0]][id_list.index(a[1])] == 1:
            answer[id_list.index(a[1])] += 1
    
    geniue = [0]*len(id_list)

    for i in range(len(answer)):
        if answer[i] >= k:
            for val in id_list:
                if dic[val][i] >= 1:
                    geniue[id_list.index(val)] +=1
    return geniue

print(solution(id_list,report,k))

