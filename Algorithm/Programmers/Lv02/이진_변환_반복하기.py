s = "1111111"

def solution(s):

    cut_zero = 0
    cnt = 1
    
    def make_two(s):
        binary = ""
        
        while s:
            binary += str(s%2)
            s = s // 2
        
        binary = binary[::-1]

        return binary

    
    while True:
        tem = ""
        for val in s:
            if val == '0':
                cut_zero +=1
            else:
                tem += "1"
        if tem == '1':
            break
        else:
            s = make_two(len(tem))
            cnt+=1

    

    answer = [cnt, cut_zero]

    return answer

print(solution(s))