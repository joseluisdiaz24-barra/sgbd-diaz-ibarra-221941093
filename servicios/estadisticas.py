from collections import Counter, defaultdict
from typing import List, Dict, Any
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelos.prestamo import Prestamo
from modelos.libro import Libro

class Estadisticas:
    """
    Clase utilitaria para generar estadísticas de la biblioteca
    utilizando colecciones avanzadas de Python.
    """
    
    @staticmethod
    def libro_mas_prestado(prestamos: List[Prestamo]) -> Optional[str]:
        """Utiliza collections.Counter para encontrar el ISBN más prestado."""
        if not prestamos:
            return None
            
        conteo = Counter(p.libro.isbn for p in prestamos)
        # most_common(1) retorna una lista de tuplas [(elemento, cuenta)]
        return conteo.most_common(1)[0][0]
        
    @staticmethod
    def usuario_con_mas_prestamos(prestamos: List[Prestamo]) -> Optional[str]:
        """Encuentra el email del usuario con más préstamos registrados."""
        if not prestamos:
            return None
            
        conteo = Counter(p.usuario.email for p in prestamos)
        return conteo.most_common(1)[0][0]
        
    @staticmethod
    def distribucion_por_genero(libros: List[Libro]) -> Dict[str, List[str]]:
        """
        Agrupa los títulos de libros por su género utilizando collections.defaultdict.
        Retorna un dict donde la clave es el género y el valor es una lista de títulos.
        """
        distribucion = defaultdict(list)
        for libro in libros:
            distribucion[libro.genero].append(libro.titulo)
            
        # Retornamos como dict normal para facilitar su lectura/serialización
        return dict(distribucion)
