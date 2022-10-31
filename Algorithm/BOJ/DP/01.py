today = "2022.05.19"
terms = ["A 6","B 12","C 3"]
privacies = ["2021.05.02 A","2021.07.01 B","2022.02.19 C","2022.02.20 C"]

def solution(today, terms, privacies):
    today = "2022.05.19"
terms = ["A 6","B 12","C 3"]
privacies = ["2021.05.02 A","2021.07.01 B","2022.02.19 C","2022.02.20 C"]

def solution(today, terms, privacies):
    answer = []

    # if terms[i][0] == 
    for i in range(len(privacies)):
        for val in terms:
            if privacies[i][-1] == val[0]:
                temp = int(val[2:])
                break

        y = int(privacies[i][:4])
        m = int(privacies[i][5:7]) + temp
        d = int(privacies[i][8:10]) - 1
        cnt= 0
        while m >12:
            if m > 12:
                m -= 12
                y += 1
        
        if d < 1 and m == 1:
            y -=1
            m = 12
            d = 28

        if d == 0:
            d = 28
            m -= 1


        y = str(y)
        if m<10:
            m = '0' + str(m)
        if d<10:
            d = '0' + str(d)
        
        
        privacies[i] = str(y)+ '.' + str(m)+'.' + str(d)


        if privacies[i] < today:
            answer.append(i+1)
        
    return answer

print(solution(today,terms,privacies))