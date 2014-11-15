import random
found_even = []
while True:
    current = random.randint(0,100)
    if not current % 2:
        if current not in found_even:
            found_even.append(current)
    if len(found_even) == 51:
        break
print(found_even)
