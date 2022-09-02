prices = [7,1,5,3,6,4]

def maxProfit(li):
    max_price = 0

    for i, price in enumerate(li):
        for j in range(i,len(li)):
            max_price = max(max_price, li[j]-price)
    
    return max_price

print(maxProfit(prices))

