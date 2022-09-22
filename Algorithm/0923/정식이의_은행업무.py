import sys
sys.stdin = open('input.txt','r')

T = int(input())

def two_to_ten(s):
    global a
    a= 0
    for i in range(len(two)):
        a += int(two[i])*(2**(len(two)-1-i))
    return a

def three_to_ten(s):
    global b
    b = 0
    for i in range(len(three)):
        b += int(three[i]) * (3 ** (len(three) - 1 - i))
    return b

def change_one_two(s):
    global two_list
    two_list = []
    for i in range(len(two)):
        if two[i] == '1':
            two[i] = '0'
            two_list.append(two_to_ten(two))
            two[i] = '1'
        elif two[i] == '0':
            two[i] = '1'
            two_list.append(two_to_ten(two))
            two[i] = '0'
    return two_list

def change_one_three(s):
    global three_list
    three_list = []
    for i in range(len(three)):
        if three[i] == '0':
            three[i] = '1'
            three_list.append(three_to_ten(three))
            three[i] = '2'
            three_list.append(three_to_ten(three))
            three[i] = '0'
        elif three[i] == '1':
            three[i] = '2'
            three_list.append(three_to_ten(three))
            three[i] = '0'
            three_list.append(three_to_ten(three))
            three[i] = '1'
        elif three[i] == '2':
            three[i] = '0'
            three_list.append(three_to_ten(three))
            three[i] = '1'
            three_list.append(three_to_ten(three))
            three[i] = '2'
    return three_list

for t in range(1,T+1):

    two = list(input())
    three = list(input())

    two_list = change_one_two(two)
    three_list = change_one_three(three)
    for val in two_list:
        if val in three_list:
            print(f'#{t} {val}')