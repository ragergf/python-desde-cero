print("\nPROCESAR LISTAS")
productos = ["Laptop", "Mouse", "Teclado"]
for producto in productos:
    print("Procesando:", producto)

print("\nPROCESAR DATOS")
ventas = [120, 300, 90, 450]
total = 0
for venta in ventas:
    total += venta
print("Total vendido:", total)

print("\nPROCESAR ARCHIVOS")
archivo = open("modulo-1-fundamentos/datos.txt")
for linea in archivo:
    print(linea.strip())
print()