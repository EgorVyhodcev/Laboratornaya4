a, b = input("Enter the 2 numbers ").split()
a = int(a)
b = int (b)
print((a % b) * (b % a) + 1)