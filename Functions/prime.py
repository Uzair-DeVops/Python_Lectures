
n = 58080


if n <= 1:
    print("its not a prime ")
for x in range (2, n):
    if n % x == 0:
        print("its not a prime number")
    else:
        print("its a prime number")
