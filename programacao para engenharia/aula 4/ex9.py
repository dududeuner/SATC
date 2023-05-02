a2 = 2
b2 = 4
x2 = 12
y2 = 10
z2 = 3
t2 = 0.0


if x2 < y2 + z2:
    if y2 != z2 * 4 - 2:
        t2 = y2 / z2
    else:
        a2 = y2 % z2
else:
    b2 = z2 + y2 / x2


print(a2, b2, x2, y2, z2, t2)

