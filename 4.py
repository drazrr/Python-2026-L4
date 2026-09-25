n = int(input("Enter a number ? "))
tong_uoc = 0
for i in range (1,n):
    if n % i == 0: 
        tong_uoc += i

if tong_uoc == n and n > 0: 
    print(f"{n} is a perfect number")
else : 
    print(f"{n} is a NOT perfect number")
    