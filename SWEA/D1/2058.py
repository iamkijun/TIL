N = int(input())

four = N//1000
three = (N//100)%10
two = (N//10)%10
one = N%10
print(one+two+three+four)