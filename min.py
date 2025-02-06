# Read two space-separated integers
a, b = map(int, input("Enter two numbers separated by space: ").split())
# Determine and print the maximum number
if a > b:
    print("The maximum is:", a)
else:
    print("The maximum is:", b)
