from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelos.entidad import Entidad
from modelos.libro import Libro
from modelos.usuario import Usuario

class Prestamo(Entidad):
    """Representa un préstamo de un libro a un usuario."""
    
    def __init__(self, usuario: Usuario, libro: Libro, dias_prestamo: int = 14) -> None:
        super().__init__()
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion_esperada = self.fecha_prestamo + timedelta(days=dias_prestamo)
        self.fecha_devolucion_real: Optional[datetime] = None
        self.activo = True
        
    def cerrar(self) -> float:
        """Cierra el préstamo, marca el libro como disponible y calcula la multa si aplica."""
        if not self.activo:
            return 0.0
            
        self.fecha_devolucion_real = datetime.now()
        self.activo = False
        self.libro.disponible = True
        
        if hasattr(self.usuario, 'libros_actuales'):
            self.usuario.libros_actuales -= 1
            
        return self.calcular_multa()
        
    def calcular_multa(self) -> float:
        """Calcula la multa basándose en la fecha esperada y la fecha real/actual."""
        fecha_fin = self.fecha_devolucion_real or datetime.now()
        diferencia = fecha_fin - self.fecha_devolucion_esperada
        
        dias_retraso = diferencia.days
        if dias_retraso <= 0:
            return 0.0
            
        # Si el usuario tiene su propio método, lo usamos
        if hasattr(self.usuario, 'calcular_multa'):
            return self.usuario.calcular_multa(dias_retraso)
            
        return 0.0
        
    def __str__(self) -> str:
        estado = "Activo" if self.activo else "Devuelto"
        return f"Préstamo: '{self.libro.titulo}' a {self.usuario.nombre} [{estado}]"
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "usuario_email": self.usuario.email,
            "libro_isbn": self.libro.isbn,
            "fecha_prestamo": self.fecha_prestamo.isoformat(),
            "fecha_devolucion_esperada": self.fecha_devolucion_esperada.isoformat(),
            "fecha_devolucion_real": self.fecha_devolucion_real.isoformat() if self.fecha_devolucion_real else None,
            "activo": self.activo
        }
