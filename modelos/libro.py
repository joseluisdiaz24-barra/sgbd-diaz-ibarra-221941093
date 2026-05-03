from datetime import datetime
from typing import Dict, Any, Type, TypeVar
import sys
import os

# Asegurar que se puedan importar módulos locales
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos.entidad import Entidad
from utils.validadores import validar_isbn13

T = TypeVar('T', bound='Libro')

class Libro(Entidad):
    """
    Representa un Libro dentro de la biblioteca.
    
    Aplica encapsulamiento estricto protegiendo sus atributos y 
    validando las entradas a través de setters.
    """
    
    def __init__(self, titulo: str, autor: str, isbn: str, anio: int, genero: str, disponible: bool = True) -> None:
        """Inicializa un nuevo Libro y valida los datos provistos."""
        super().__init__()
        self._titulo = titulo
        self._autor = autor
        self.isbn = isbn  # Usa el setter para validar
        self.anio = anio  # Usa el setter para validar
        self._genero = genero
        self._disponible = disponible
        
    @property
    def titulo(self) -> str:
        return self._titulo
        
    @titulo.setter
    def titulo(self, valor: str) -> None:
        self._titulo = valor
        
    @property
    def autor(self) -> str:
        return self._autor
        
    @autor.setter
    def autor(self, valor: str) -> None:
        self._autor = valor
        
    @property
    def isbn(self) -> str:
        return self._isbn
        
    @isbn.setter
    def isbn(self, valor: str) -> None:
        if not validar_isbn13(valor):
            raise ValueError(f"El ISBN provisto no es válido: {valor}")
        self._isbn = valor
        
    @property
    def anio(self) -> int:
        return self._anio
        
    @anio.setter
    def anio(self, valor: int) -> None:
        anio_actual = datetime.now().year
        if not (1440 <= valor <= anio_actual):
            raise ValueError(f"El año de publicación debe estar entre 1440 y {anio_actual}")
        self._anio = valor
        
    @property
    def genero(self) -> str:
        return self._genero
        
    @genero.setter
    def genero(self, valor: str) -> None:
        self._genero = valor
        
    @property
    def disponible(self) -> bool:
        return self._disponible
        
    @disponible.setter
    def disponible(self, valor: bool) -> None:
        self._disponible = valor
        
    def __str__(self) -> str:
        estado = "Disponible" if self._disponible else "Prestado"
        return f"'{self._titulo}' por {self._autor} ({self._anio}) - [{estado}]"
        
    def __repr__(self) -> str:
        return f"Libro(titulo='{self._titulo}', autor='{self._autor}', isbn='{self._isbn}', anio={self._anio})"
        
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Libro):
            return NotImplemented
        return self.isbn == otro.isbn
        
    def to_dict(self) -> Dict[str, Any]:
        """Convierte las propiedades de la instancia a un diccionario."""
        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "anio": self.anio,
            "genero": self.genero,
            "disponible": self.disponible
        }
        
    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        """Crea una instancia de Libro a partir de un diccionario."""
        libro = cls(
            titulo=data["titulo"],
            autor=data["autor"],
            isbn=data["isbn"],
            anio=data["anio"],
            genero=data["genero"],
            disponible=data.get("disponible", True)
        )
        # Restaurar atributos de la clase base si están presentes
        if "id" in data:
            libro._id = data["id"]
        if "fecha_creacion" in data:
            libro._fecha_creacion = datetime.fromisoformat(data["fecha_creacion"])
        return libro

from utils.constantes import FORMATOS_VALIDOS

class LibroDigital(Libro):
    """Representa un libro en formato digital."""
    def __init__(self, titulo: str, autor: str, isbn: str, anio: int, genero: str, formato: str, tamano_mb: float, url_descarga: str, disponible: bool = True) -> None:
        super().__init__(titulo, autor, isbn, anio, genero, disponible)
        if formato not in FORMATOS_VALIDOS:
            raise ValueError(f"Formato inválido. Debe ser uno de {FORMATOS_VALIDOS}")
        if tamano_mb <= 0:
            raise ValueError("El tamaño debe ser mayor a 0 MB")
            
        self.formato = formato
        self.tamano_mb = float(tamano_mb)
        self.url_descarga = url_descarga
        
    def descargar(self) -> str:
        return f"Descargando de {self.url_descarga}..."
        
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} [Digital: {self.formato}, {self.tamano_mb}MB]"
        
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "tipo": "LibroDigital",
            "formato": self.formato,
            "tamano_mb": self.tamano_mb,
            "url_descarga": self.url_descarga
        })
        return data

class LibroFisico(Libro):
    """Representa un libro físico en la biblioteca."""
    def __init__(self, titulo: str, autor: str, isbn: str, anio: int, genero: str, ubicacion: str, num_ejemplares: int, disponible: bool = True) -> None:
        super().__init__(titulo, autor, isbn, anio, genero, disponible)
        if not ubicacion:
            raise ValueError("La ubicación no puede estar vacía")
        if num_ejemplares < 1:
            raise ValueError("Debe haber al menos 1 ejemplar")
            
        self.ubicacion = ubicacion
        self.num_ejemplares = num_ejemplares
        
    def reservar(self) -> str:
        if self.num_ejemplares > 0:
            self.num_ejemplares -= 1
            return "Reserva exitosa"
        return "No hay ejemplares disponibles"
        
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} [Físico: {self.ubicacion}, {self.num_ejemplares} ej.]"
        
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "tipo": "LibroFisico",
            "ubicacion": self.ubicacion,
            "num_ejemplares": self.num_ejemplares
        })
        return data

if __name__ == "__main__":
    # Prueba rápida de instanciación
    try:
        libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "9780306406157", 1967, "Realismo Mágico")
        print(f"Libro creado: {libro1}")
        print(f"Representación: {repr(libro1)}")
        print(f"Diccionario: {libro1.to_dict()}")
        
        # Debe fallar
        libro2 = Libro("Falla ISBN", "Autor", "123", 2000, "Ficción")
    except ValueError as e:
        print(f"Error esperado capturado: {e}")
