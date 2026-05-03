from abc import abstractmethod
from typing import Dict, Any
import sys
import os

# Asegurar que se puedan importar módulos locales
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos.entidad import Entidad

class Usuario(Entidad):
    """
    Clase abstracta que representa a un usuario genérico del sistema.
    Hereda de Entidad y obliga a implementar la lógica de préstamos.
    """
    
    def __init__(self, nombre: str, email: str, contrasena_hash: str) -> None:
        """Inicializa los datos básicos de un usuario."""
        super().__init__()
        self._nombre = nombre
        self._email = email
        self._contrasena_hash = contrasena_hash
        
    @property
    def nombre(self) -> str:
        return self._nombre
        
    @property
    def email(self) -> str:
        return self._email
        
    @abstractmethod
    def puede_pedir_prestado(self) -> bool:
        """
        Método abstracto que determina si el usuario tiene permitido 
        pedir más libros prestados según sus reglas específicas.
        """
        pass
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._nombre} ({self._email})"
        
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el usuario a un diccionario."""
        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "tipo_usuario": self.__class__.__name__,
            "nombre": self.nombre,
            "email": self.email,
            "contrasena_hash": self._contrasena_hash
        }

from utils.constantes import MAX_LIBROS_ALUMNO, MAX_LIBROS_PROFESOR

class Alumno(Usuario):
    """Usuario tipo Alumno."""
    def __init__(self, nombre: str, email: str, contrasena_hash: str, carrera: str, semestre: int) -> None:
        super().__init__(nombre, email, contrasena_hash)
        self.carrera = carrera
        self.semestre = semestre
        self.max_libros = MAX_LIBROS_ALUMNO
        self.libros_actuales = 0
        
    def puede_pedir_prestado(self) -> bool:
        return self.libros_actuales < self.max_libros
        
    def calcular_multa(self, dias_retraso: int) -> float:
        return float(dias_retraso * 5)
        
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({"carrera": self.carrera, "semestre": self.semestre, "max_libros": self.max_libros})
        return data

class Profesor(Usuario):
    """Usuario tipo Profesor."""
    def __init__(self, nombre: str, email: str, contrasena_hash: str, departamento: str) -> None:
        super().__init__(nombre, email, contrasena_hash)
        self.departamento = departamento
        self.max_libros = MAX_LIBROS_PROFESOR
        self.libros_actuales = 0
        
    def puede_pedir_prestado(self) -> bool:
        return self.libros_actuales < self.max_libros
        
    def calcular_multa(self, dias_retraso: int) -> float:
        return float(dias_retraso * 2)
        
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({"departamento": self.departamento, "max_libros": self.max_libros})
        return data

class Administrador(Usuario):
    """Usuario tipo Administrador con permisos elevados."""
    def __init__(self, nombre: str, email: str, contrasena_hash: str, nivel_acceso: int) -> None:
        super().__init__(nombre, email, contrasena_hash)
        self.nivel_acceso = nivel_acceso
        
    def puede_pedir_prestado(self) -> bool:
        return True # Admin no tiene límite estricto en este caso base
        
    def calcular_multa(self, dias_retraso: int) -> float:
        return 0.0 # Admin no paga multa
        
    def agregar_libro(self, libro: Any) -> str:
        return f"Libro '{getattr(libro, 'titulo', 'Desconocido')}' agregado por Admin."
        
    def eliminar_usuario(self, email: str) -> str:
        return f"Usuario {email} eliminado por Admin."
        
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({"nivel_acceso": self.nivel_acceso})
        return data

if __name__ == "__main__":
    # Demostración de que no se puede instanciar
    try:
        usuario_invalido = Usuario("Test", "test@test.com", "hash123")
    except TypeError as e:
        print(f"Demostración exitosa: No se pudo instanciar Usuario. Error: {e}")
        
    try:
        entidad_invalida = Entidad()
    except TypeError as e:
        print(f"Demostración exitosa: No se pudo instanciar Entidad. Error: {e}")
