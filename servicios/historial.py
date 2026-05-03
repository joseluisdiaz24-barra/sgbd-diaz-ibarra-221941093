from typing import Optional

class Historial:
    """
    Gestiona un historial de acciones del sistema usando una Pila (LIFO).
    Implementado sobre una lista nativa de Python usando append() y pop().
    """
    def __init__(self) -> None:
        self._acciones: list[str] = []
        
    def registrar_accion(self, accion: str) -> None:
        """Apila una nueva acción en el historial."""
        self._acciones.append(accion)
        
    def deshacer_ultima_accion(self) -> Optional[str]:
        """Desapila y retorna la última acción registrada (LIFO)."""
        if not self._acciones:
            return None
        return self._acciones.pop()
        
    def ver_historial(self) -> list[str]:
        """Retorna todas las acciones registradas."""
        return list(self._acciones)
