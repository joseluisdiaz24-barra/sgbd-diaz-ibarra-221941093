def validar_isbn13(isbn: str) -> bool:
    """
    Valida si un string corresponde a un ISBN-13 válido.
    
    Requisitos:
    1. Debe tener exactamente 13 caracteres.
    2. Todos los caracteres deben ser dígitos numéricos.
    3. El dígito verificador (último dígito) debe ser correcto según el algoritmo ISBN-13.

    Algoritmo ISBN-13:
    - Se toman los primeros 12 dígitos.
    - Se multiplican alternadamente por 1 y por 3 (el primer dígito por 1, el segundo por 3, etc.).
    - Se suman todos los resultados.
    - Se calcula el resto de la división de la suma entre 10 (suma % 10).
    - El dígito verificador debe ser igual a (10 - resto) % 10.
    
    Equivalentemente, la suma de los 13 dígitos multiplicados alternadamente por 1 y 3 
    debe ser un múltiplo de 10.

    Ejemplos de uso (Doctest):
    >>> validar_isbn13("9780306406157")
    True
    >>> validar_isbn13("9780306406158") # Dígito verificador incorrecto
    False
    >>> validar_isbn13("978030640615") # Menos de 13 caracteres
    False
    >>> validar_isbn13("978030640615A") # Contiene letras
    False
    """
    # 1. Verificar que tenga exactamente 13 caracteres
    if len(isbn) != 13:
        return False
        
    # 2. Verificar que todos los caracteres sean dígitos
    if not isbn.isdigit():
        return False
        
    # 3. Validar el dígito verificador
    suma_total = 0
    for i in range(12):
        digito = int(isbn[i])
        # Multiplicamos por 1 si el índice es par, por 3 si es impar
        if i % 2 == 0:
            suma_total += digito * 1
        else:
            suma_total += digito * 3
            
    # Calculamos el dígito verificador esperado
    resto = suma_total % 10
    digito_verificador_esperado = (10 - resto) % 10
    
    # Comparamos el último dígito con el esperado
    digito_verificador_actual = int(isbn[12])
    
    return digito_verificador_esperado == digito_verificador_actual

def validar_email(email: str) -> bool:
    """
    Valida que un string tenga un formato básico de correo electrónico.
    
    Requisitos:
    - Debe contener exactamente un '@'.
    - Debe tener un dominio con al menos un punto después del '@'.
    - No puede empezar ni terminar con '@' o '.'.
    
    Ejemplos de uso:
    >>> validar_email("alumno@universidad.edu")
    True
    >>> validar_email("profesor.com") # Falla por no tener @
    False
    >>> validar_email("admin@sistema") # Falla por no tener punto después de @
    False
    """
    if email.count('@') != 1:
        return False
        
    usuario, dominio = email.split('@')
    
    # El usuario y el dominio no pueden estar vacíos
    if len(usuario) == 0 or len(dominio) == 0:
        return False
        
    # El dominio debe contener al menos un punto
    if '.' not in dominio:
        return False
        
    # El dominio no puede empezar ni terminar con un punto
    if dominio.startswith('.') or dominio.endswith('.'):
        return False
        
    return True

# === Casos de prueba adicionales ===
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Pruebas Doctest finalizadas.")
    
    # Pruebas manuales
    print("\n--- Pruebas manuales ---")
    casos = {
        "9780306406157": True,   # Caso válido
        "9783161484100": True,   # Otro caso válido
        "1234567890123": False,  # Verificador inválido
        "97803064061": False,    # Longitud corta
        "97803064061578": False, # Longitud larga
        "9780306406I57": False,  # Contiene letra 'I'
    }
    
    todos_pasaron = True
    for caso, esperado in casos.items():
        resultado = validar_isbn13(caso)
        if resultado != esperado:
            print(f"FALLO: validar_isbn13('{caso}') -> {resultado} (Se esperaba {esperado})")
            todos_pasaron = False
            
    if todos_pasaron:
        print("¡Todos los casos de prueba manuales pasaron exitosamente!")
