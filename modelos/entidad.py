import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any

class Entidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    
    Provee identificadores únicos y marcas de tiempo, y exige a sus 
    subclases la implementación de representación en cadena y 
    serialización a diccionario.
    """
    
    def __init__(self) -> None:
        """Inicializa una entidad con un UUID y la fecha actual."""
        self._id = str(uuid.uuid4())
        self._fecha_creacion = datetime.now()
        
    @property
    def id(self) -> str:
        """Obtiene el identificador único de la entidad."""
        return self._id
        
    @property
    def fecha_creacion(self) -> datetime:
        """Obtiene la fecha y hora de creación de la entidad."""
        return self._fecha_creacion
        
    @abstractmethod
    def __str__(self) -> str:
        """Representación amigable de la entidad."""
        pass
        
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convierte la entidad a un diccionario para persistencia."""
        pass
