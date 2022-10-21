import copy as cp

N =int(input())

count =1
num = 1
if N == 1:
    print(0)
elif N > 900:
    print(-1)
else:
    while True:
        n = cp.deepcopy(num)

        mod_list = [-1]

        bp = 0
        while n != 0:
            mods= n%10
            mod_list.append(mods)
            if mod_list[-2]<mod_list[-1]:
                pass
            else:
                bp = 1
                break
            n = n //10

        if bp:
            num +=1
            continue
        else:
            count+=1
            if count == N:
                print(num)
                break
            else:
                num +=1

        if num > 1000000:
            print(-1)
            break

        

        

        