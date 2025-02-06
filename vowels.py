s=input("enter the string")
vowels="aeiouAEIOU"
count = 0

for char in s:
    if char in vowels:
        count += 1

print("no of voewels in the string is:",count)
