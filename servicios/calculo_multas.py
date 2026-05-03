def calcular_multa_if(dias_retraso: int, tipo_usuario: str) -> float:
    """
    Calcula la multa por retraso en la devolución de un libro utilizando sentencias if/elif/else.
    
    Reglas:
    - Sin retraso (dias_retraso <= 0): multa = 0
    - Alumno: $5 MXN por día
    - Profesor: $2 MXN por día
    - Admin: sin multa ($0)
    - Si el retraso supera los 30 días, se aplica un 20% adicional de penalización sobre el total.
    
    Ejemplos (Doctest):
    >>> calcular_multa_if(0, "alumno")
    0.0
    >>> calcular_multa_if(10, "alumno")
    50.0
    >>> calcular_multa_if(10, "profesor")
    20.0
    >>> calcular_multa_if(10, "admin")
    0.0
    >>> calcular_multa_if(40, "alumno") # 40 * 5 = 200 + 20% = 240
    240.0
    """
    if dias_retraso <= 0:
        return 0.0
        
    tipo_usuario = tipo_usuario.lower()
    multa_base = 0.0
    
    if tipo_usuario == "alumno":
        multa_base = dias_retraso * 5.0
    elif tipo_usuario == "profesor":
        multa_base = dias_retraso * 2.0
    elif tipo_usuario == "admin":
        multa_base = 0.0
    else:
        raise ValueError(f"Tipo de usuario desconocido: {tipo_usuario}")
        
    # Aplicar recargo del 20% si excede 30 días
    if dias_retraso > 30:
        multa_base = multa_base * 1.20
        
    return float(multa_base)


def calcular_multa_match(dias_retraso: int, tipo_usuario: str) -> float:
    """
    Calcula la multa por retraso en la devolución de un libro utilizando sentencias match/case (Python 3.10+).
    
    Reglas idénticas a la función anterior.
    
    Ejemplos (Doctest):
    >>> calcular_multa_match(15, "alumno")
    75.0
    >>> calcular_multa_match(50, "profesor") # 50 * 2 = 100 + 20% = 120
    120.0
    """
    if dias_retraso <= 0:
        return 0.0
        
    tipo_usuario = tipo_usuario.lower()
    multa_base = 0.0
    
    match tipo_usuario:
        case "alumno":
            multa_base = dias_retraso * 5.0
        case "profesor":
            multa_base = dias_retraso * 2.0
        case "admin":
            multa_base = 0.0
        case _:
            raise ValueError(f"Tipo de usuario desconocido: {tipo_usuario}")
            
    if dias_retraso > 30:
        multa_base = multa_base * 1.20
        
    return float(multa_base)

# Exportamos una como la función principal
calcular_multa = calcular_multa_match

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Pruebas Doctest finalizadas para cálculo de multas.")
