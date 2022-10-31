def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    for i in range(len(d)):
        if sum(d[i:]) <= budget:
            answer = len(d) -i
            break
    return answer