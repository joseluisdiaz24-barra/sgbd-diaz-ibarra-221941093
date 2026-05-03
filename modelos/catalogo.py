import json
import os
from typing import Protocol, List, Dict, Any

from modelos.libro import Libro, LibroDigital, LibroFisico
from modelos.usuario import Usuario, Alumno, Profesor, Administrador
from modelos.prestamo import Prestamo
from utils.formato_texto import buscar_en_texto

class Buscable(Protocol):
    """Protocolo que define un contrato para objetos que pueden ser buscados."""
    def buscar(self, query: str) -> list:
        ...

class Catalogo:
    """
    Gestor principal de la biblioteca. Implementa el protocolo Buscable.
    """
    def __init__(self) -> None:
        self.libros: List[Libro] = []
        self.usuarios: Dict[str, Usuario] = {} # email -> Usuario
        self.prestamos: List[Prestamo] = []
        
    def agregar_libro(self, libro: Libro) -> None:
        self.libros.append(libro)
        
    def eliminar_libro(self, isbn: str) -> bool:
        for i, libro in enumerate(self.libros):
            if libro.isbn == isbn:
                self.libros.pop(i)
                return True
        return False
        
    def registrar_usuario(self, usuario: Usuario) -> None:
        self.usuarios[usuario.email] = usuario
        
    def registrar_prestamo(self, email: str, isbn: str) -> Any:
        usuario = self.usuarios.get(email)
        if not usuario:
            # Creación automática del usuario si no existe
            usuario = Alumno(email.split('@')[0], email, "hash_auto", "General", 1)
            self.registrar_usuario(usuario)
            
        if not usuario.puede_pedir_prestado():
            raise ValueError("El usuario ha alcanzado su límite de préstamos.")
            
        libro = next((l for l in self.libros if l.isbn == isbn), None)
        if not libro:
            raise ValueError("Libro no encontrado en el catálogo.")
            
        if not libro.disponible:
            raise ValueError("El libro no está disponible actualmente.")
            
        if isinstance(libro, LibroFisico):
            res = libro.reservar()
            if "exitosa" not in res.lower():
                raise ValueError("No hay ejemplares físicos disponibles.")
        
        prestamo = Prestamo(usuario, libro)
        libro.disponible = False
        if hasattr(usuario, 'libros_actuales'):
            usuario.libros_actuales += 1
            
        self.prestamos.append(prestamo)
        return prestamo
        
    def procesar_devolucion(self, isbn: str) -> float:
        prestamo = next((p for p in self.prestamos if p.activo and p.libro.isbn == isbn), None)
        if not prestamo:
            raise ValueError("No se encontró un préstamo activo para ese ISBN.")
            
        if isinstance(prestamo.libro, LibroFisico):
            prestamo.libro.num_ejemplares += 1
            
        multa = prestamo.cerrar()
        return multa
        
    def buscar(self, query: str) -> list:
        """Busca libros por título, autor o ISBN ignorando mayúsculas."""
        return [
            libro for libro in self.libros 
            if buscar_en_texto(libro.titulo, query) 
            or buscar_en_texto(libro.autor, query) 
            or buscar_en_texto(libro.isbn, query)
        ]
        
    def listar_disponibles(self) -> list:
        return [libro for libro in self.libros if libro.disponible]
        
    def generar_reporte(self) -> dict:
        return {
            "total_libros": len(self.libros),
            "total_usuarios": len(self.usuarios),
            "prestamos_activos": sum(1 for p in self.prestamos if p.activo)
        }
        
    def guardar_json(self, ruta: str) -> None:
        """Guarda el estado del catálogo en un archivo JSON."""
        datos = {
            "libros": [l.to_dict() for l in self.libros],
            "usuarios": [u.to_dict() for u in self.usuarios.values()],
            "prestamos": [p.to_dict() for p in self.prestamos]
        }
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
            
    def cargar_json(self, ruta: str) -> None:
        """Carga el estado del catálogo desde un archivo JSON."""
        # Se omitió la instanciación completa por simplicidad de este examen,
        # pero aquí se reconstruirían los objetos usando from_dict y factorías.
        pass
