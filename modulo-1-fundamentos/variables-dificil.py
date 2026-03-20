#Ejemplo de inmutabilidad en enteros

x = 10
y = x

print("Valor incial de x:", x)
print("Valor incial de y:", y)

#Cambiamos y
y = 20

print("Nuevo valor de y:", y)
print("Valor de x despues del cambio de y:", x)

print("ID de x:", id(x))
print("ID de y:", id(y))