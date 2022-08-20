while True:
    try:
        s, t = map(str, input().split())

        S = list(s)
        T = list(t)

        new_T = []
        for val in T:
            if val in S:
                new_T.append(val)

        ans = 0

        for i in range(len(new_T)-len(S)+1):
            if S[0] == new_T[i]:
                k = i + 1
                j = 1
                count = 1
                for v in range(len(S)-1):
                    if S[j] in new_T[k:]:
                        k = i + new_T[k:].index(S[j]) + 2
                        j +=1
                        count +=1
                    else:
                        break
            if count == len(S):
                ans = 1
                break

        if ans == 0:
            print('No')
        elif ans == 1:
            print('Yes')

    except:
        break