#prime number search
minrange = int(input("ENTER A MINIMUM RANGE: "))
maxrange = int(input("ENTER A MAXIMUM RANGE: "))
primelist = []

for num in range(minrange,maxrange):
    print(num)
    for i in range(2,num):
        if num % i == 0:
            break
        else:
            primelist.append(num)
            break

print(" ")
print("THERE ARE", len(primelist), "PRIME NUMBERS WITHIN THE RANGE OF (", minrange, "AND", maxrange, ")")
print(" ")
print("THOSE NUMBERS ARE: ", primelist)

exit = input("...")
