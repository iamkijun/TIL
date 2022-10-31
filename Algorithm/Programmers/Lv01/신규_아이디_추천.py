new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    answer = ''

    for i in range(len(new_id)):
        #1단계 대문자를 소문자로 바꾸기
        if new_id[i].isupper():
            # print(new_id[i],ord(new_id[i]))
            answer+= chr(ord(new_id[i])+32)
            continue
        
        #2단계 제외한 모든 문자 제거
        elif new_id[i].isdigit() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            answer+=new_id[i]
        else:
            pass
    new_id = answer
    answer = ''
    print(new_id)
    print(1,2)

    #3단계 마침표 2번 이상 반복시 하나로 치환
    idx = 0
    while new_id and idx-1>=len(new_id):
        
        if new_id[idx] =='.' and new_id[idx+1] =='.':
            new_id = new_id[:idx] + new_id[idx+1:]
        else:
            idx +=1
    
    new_id = answer
    answer = ''
    
    print(3)
    #4단계 마침표가 처음이나 끝에 위치할 경우 제거
    if answer[0] == '.':
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    print(4)
    
        # 5단계 빈 문자열일 때 "a" 대입
    if new_id == '':
        new_id = 'a'

    print(5)
    # 6단계 길이가 16자 이상일 때 15자만 남기기
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    elif len(new_id) <= 2:
        while len(new_id) <3:
            new_id += new_id[-1]
    print(6)



    return answer

print(solution(new_id))