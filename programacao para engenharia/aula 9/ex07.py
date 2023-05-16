x = int(input('digite um numero '))

y = int(input('digite outro numero '))

nums = []

if x < y:
    for i in range(x, y+1):
        nums.append(i)

elif y < x:
    for i in range(y, x+1):
        nums.append(i)       

print(nums)