import unicodedata

def normalizar_titulo(titulo: str) -> str:
    """
    Normaliza el título de un libro.
    - Capitaliza cada palabra (title case)
    - Elimina espacios extra
    - Quita caracteres especiales (deja letras, números, espacios y comas)
    
    >>> normalizar_titulo(" el   sEñor  de_los *anillos, 1 ")
    'El Señor De Los Anillos, 1'
    """
    # Eliminar espacios múltiples usando split y join
    palabras = titulo.split()
    titulo_limpio = " ".join(palabras)
    
    # Capitalizar cada palabra
    titulo_limpio = titulo_limpio.title()
    
    # Remover caracteres que no sean letras, números, espacios o comas
    resultado = []
    for char in titulo_limpio:
        if char.isalnum() or char.isspace() or char == ',':
            resultado.append(char)
            
    return "".join(resultado)

def generar_slug(texto: str) -> str:
    """
    Convierte un texto a formato slug para URLs.
    - Minúsculas
    - Reemplaza espacios por guiones
    - Elimina acentos
    
    >>> generar_slug("Crónica de una muerte anunciada")
    'cronica-de-una-muerte-anunciada'
    """
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar acentos usando unicodedata
    texto_sin_acentos = "".join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    
    # Reemplazar espacios por guiones y limpiar
    palabras = texto_sin_acentos.split()
    return "-".join(palabras)

def formatear_reporte_libro(libro_dict: dict) -> str:
    """
    Genera una cadena multilínea formateada con f-strings para un libro.
    
    >>> libro = {'titulo': '1984', 'autor': 'George Orwell', 'isbn': '9780451524935'}
    >>> print(formatear_reporte_libro(libro))
    ========================================
    TÍTULO : 1984
    AUTOR  : George Orwell
    ISBN   : 9780451524935
    ========================================
    """
    return (
        f"{'='*40}\n"
        f"TÍTULO : {libro_dict.get('titulo', 'N/A')}\n"
        f"AUTOR  : {libro_dict.get('autor', 'N/A')}\n"
        f"ISBN   : {libro_dict.get('isbn', 'N/A')}\n"
        f"{'='*40}"
    )

def buscar_en_texto(haystack: str, needle: str) -> bool:
    """
    Busca una subcadena dentro de otra de forma case-insensitive.
    
    >>> buscar_en_texto("Cien años de soledad", "AÑOS")
    True
    """
    return needle.lower() in haystack.lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Pruebas Doctest finalizadas para formato de texto.")
