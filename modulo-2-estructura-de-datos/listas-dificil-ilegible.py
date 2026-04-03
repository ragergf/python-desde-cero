usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Luis", "edad": 17, "activo": True},
    {"nombre": "Pedro", "edad": 30, "activo": False},
    {"nombre": "Sofia", "edad": 22, "activo": True}
]
resultado = [
    (u["nombre"].upper(), "ADULTO" if u["edad"] >= 18 else "MENOR")
    for u in usuarios
    if u["activo"] and (u["edad"] > 20 or u["nombre"].startswith("A"))
]
print(f"\n{resultado}\n")