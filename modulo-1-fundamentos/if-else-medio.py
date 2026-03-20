def clasificar_persona(edad: int, tiene_licencia: bool) -> None:
    """
    Clasifica a una persona según su edad
    y si puede conducir.
    """
    print("Edad:", edad)
    print("Tiene licencia:", tiene_licencia)
    # Clasificación por edad
    if edad < 65:
        print("Es Adulto")
    elif edad < 18  :
        print("Es Menor")
    else:
        print("Es adulto mayor")
    # Uso de operadores lógicos
    if edad >= 18 and tiene_licencia:
        print("Puede manejar")
    elif edad >= 18 and not tiene_licencia:
        print("Es adulto pero no puede manejar")
    else:
        print("no puede manjer")

def main():
    edad = 10
    tiene_licencia = True
    clasificar_persona(edad, tiene_licencia)

if __name__ == "__main__":
    main()