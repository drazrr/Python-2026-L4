def get_divisor(n):
    divisor = []
    for i in range(1,n +1):
        if n % i == 0:
            divisor += [i]
    return divisor
num = int(input("Enter your number :"))
result = get_divisor(num)
print(result)