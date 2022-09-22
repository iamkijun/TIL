import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):

    all = list(map(int, input().split()))

    player1 = []
    player2 = []

    one_list = [0]*10
    two_list = [0]*10

    one_run = 0
    two_run = 0


    for i in range(0,12,2):
        player1.append(all[i])
        player2.append(all[i+1])

        one_list[all[i]] += 1
        two_list[all[i+1]] += 1

        for j in range(10):
            if j <=7:
                if one_list[j] >= 1 and one_list[j+1] >= 1 and one_list[j+2] >= 1:
                    one_run = 1
                if two_list[j] >= 1 and two_list[j+1] >= 1 and two_list[j+2] >= 1:
                    two_run = 1

            if one_list[j] ==3:
                one_run =1
            if two_list[j] ==3:
                two_run =1

        if one_run:
            print(f'#{t} 1')
            break
        elif two_run:
            print(f'#{t} 2')
            break
    else:
        print(f'#{t} 0')
