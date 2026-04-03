productos = [
    {"nombre": "Laptop", "stock": 3},
    {"nombre": "Mouse", "stock": 0},
    {"nombre": "Teclado", "stock": 5},
    {"nombre": "Monitor", "stock": 0}
]
dispobibles = [
    producto["nombre"]
    for producto in productos
    if producto["stock"] > 0
]
print("\n")
print(dispobibles)
print("\n")