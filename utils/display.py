import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos.entidad import Entidad
from modelos.libro import LibroDigital, LibroFisico
from modelos.usuario import Alumno, Profesor, Administrador

def mostrar_info(item: Entidad) -> None:
    """
    Función polimórfica que invoca el método __str__ de cualquier Entidad.
    No usa isinstance(), confía en que todas las subclases sobreescriben __str__.
    """
    print(f"[INFO] {item}")

def generar_reporte(items: list) -> str:
    """
    Demostración de Duck Typing.
    Acepta cualquier objeto que posea el método to_dict() y genera un reporte.
    """
    reporte = ["=== REPORTE GENERADO ==="]
    for obj in items:
        try:
            datos = obj.to_dict()
            # Mostramos las primeras 3 claves/valores principales
            resumen = ", ".join(f"{k}={v}" for k, v in list(datos.items())[:3])
            reporte.append(f"- {resumen}")
        except AttributeError:
            reporte.append(f"- [Error] El objeto {type(obj).__name__} no soporta to_dict()")
    
    return "\n".join(reporte)

if __name__ == "__main__":
    # 1. Crear objetos mixtos
    libro1 = LibroDigital("Python 101", "Guido", "9781234567897", 2020, "Programación", "PDF", 1.5, "http://dl.com")
    libro2 = LibroFisico("Clean Code", "Robert C.", "9780132350884", 2008, "Software", "Estante B", 3)
    alumno = Alumno("Juan", "juan@u.edu", "hash1", "Sistemas", 5)
    profe = Profesor("Alan", "alan@u.edu", "hash2", "Ciencias")
    
    # 2. Polimorfismo con mostrar_info
    print("--- Polimorfismo ---")
    lista_mixta = [libro1, libro2, alumno, profe]
    for item in lista_mixta:
        mostrar_info(item)
        
    # 3. Duck Typing
    print("\n--- Duck Typing ---")
    print(generar_reporte(lista_mixta))
    
    # 4. Ordenamiento con lambda
    print("\n--- Ordenamiento con Lambda ---")
    libros = [libro2, libro1]
    libros_ordenados = sorted(libros, key=lambda b: b.titulo)
    for b in libros_ordenados:
        print(b.titulo)
