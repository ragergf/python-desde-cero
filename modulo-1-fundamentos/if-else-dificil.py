def clasificar_edad(edad: int) -> str:
    if edad < 18:
        return "menor"
    elif edad < 65:
        return "adulto"
    else:
        return "adulto mayor"

edad = 70
resultado = clasificar_edad(edad)

print(f"edad: {edad}")
print(f"categoria: {resultado}")