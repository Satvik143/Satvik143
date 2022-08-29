def swap_items_in_list():
    a = n[0]
    b = n[-1]
    n[0] = b
    n[-1] = a


i = int(input("How Many Items Do You Want To Swap : "))

j = 1

n = []

while j <= i:
    n.append(input(f"{j} : "))
    j += 1

print("Before")
print(n)
swap_items_in_list()
print("After")
print(n)

