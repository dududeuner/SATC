#tuple tupla
p1 = (10, 10, 10, 9, 2)

p2 = (7, 7, 7, 7, 7)

media = sum(p1) / len(p1)

media2 = sum(p2) / len(p2)

print(media, media2)

if media > media2:
    print(f"A turma 1 tem a melhor media: {media}")
else:
    print(f"A turma 2 tem a melhor media: {media2}")

