print("Ejemplo 1: loop normal")
for numero in range(1,6):
    print(numero)

print("Ejemplo 2: uso break")
for numero in range(1, 10):
    if numero == 5:
        print("se para e 5")
        break
    print(numero)

print("Ejemplo 3: uso continue")
for numero in range(1,6):
    if numero == 3:
        print("me salte 3")
        continue
    print(numero)