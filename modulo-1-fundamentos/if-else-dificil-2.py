def mensaje_status(status: int) -> str:
    match status:
        case 200:
            return "ok"
        case 404:
            return "No encontrado"
        case 500:
            return "Error del servidor"
        case _:
            return "Estado desconocido"
        
status = 404
resultado = mensaje_status(status)

print(f"Status: {status}")
print(f"Mensaje: {resultado}")
