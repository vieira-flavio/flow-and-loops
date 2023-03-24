num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for a in sorted(num_list):
    if a >= 45:
        print(f"Over 45: {a}")
    else:
        a <= 45
        print(f"Under 45: {a}")

print(" ")        

index = num_list.index(36)

for b in enumerate(num_list):
    if 36 in b:
        print(f"Number 36 found at position in the original list {index}")


count = 0

for i in num_list:
    i + 1
    break
    
print(f"\ncount variable value: {i}")