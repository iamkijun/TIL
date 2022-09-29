numbers=[1,2,3,4,6,7,8,0]
def solution(numbers):
    answer = 0
    num_li = [x for x in range(10)]
    print(num_li)
    for val in num_li:
        if val not in numbers:
            answer += val

    return answer

print(solution(numbers))