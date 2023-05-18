d = {}

keys = ["nome", "idade", "endereco", "telefone"]

for key in keys:
    value = input(f"Digite o(a) '{key}': ")
    d[key] = value

print(d)