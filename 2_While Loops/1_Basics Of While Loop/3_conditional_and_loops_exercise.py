
# program: sum of first N Natural Numbers
# Natural Number =>  are all positive integer from 1 to infinity

n = int(input("Enter sum of n: "))
sum = 0

while n > 0:
    sum += n
    n -= 1
print(sum)


