def solution(sizes):
    if len(sizes)==1:
        answer = sizes[0][0]*sizes[0][1]
    else:
        for val in sizes:
            val.sort(reverse=True)
        sizes.sort(key = lambda x:x[0],reverse=True)

        val1 = sizes[0][0]
        temp = sizes[0][1]

        sizes = sizes[1:]

        sizes.sort(key = lambda x:x[1],reverse= True)

        val2 = max(temp,sizes[0][1])

        answer = val1 * val2
    return answer