from collections import deque
from typing import Tuple, Optional

class GestorCola:
    """
    Gestiona una cola de espera (FIFO) para libros no disponibles
    usando collections.deque.
    """
    def __init__(self) -> None:
        self._cola: deque[Tuple[str, str]] = deque()
        
    def encolar_solicitud(self, usuario_email: str, libro_isbn: str) -> None:
        """Añade una nueva solicitud al final de la cola."""
        self._cola.append((usuario_email, libro_isbn))
        
    def atender_siguiente(self) -> Optional[Tuple[str, str]]:
        """Atiende y remueve la solicitud más antigua de la cola (FIFO)."""
        if not self._cola:
            return None
        return self._cola.popleft()
        
    def ver_cola(self) -> list[Tuple[str, str]]:
        """Retorna una lista con el estado actual de la cola."""
        return list(self._cola)
