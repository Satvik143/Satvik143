def P_S_U (j):
    while j > 0:
        print("*",end=" ")
        j -= 1

n = int(input("Enter Height Value Of Diamond Pyramid : "))
i = 1

while i <= n:
    print((n-i)*" ",end="")
    P_S_U(i)
    print()
    i += 1

i = n - 1

while i >= 1:
    print((n-i)*" ",end="")
    P_S_U(i)
    print()
    i -= 1
