import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os

from modelos.catalogo import Catalogo
from modelos.libro import LibroFisico, LibroDigital
from modelos.usuario import Alumno, Profesor, Administrador
from servicios.gestor_cola import GestorCola

def seed_data(catalogo: Catalogo) -> None:
    admin = Administrador("Admin Root", "admin@biblioteca.com", "hash_admin", 1)
    alumno1 = Alumno("Juan Perez", "juan@u.edu", "hash_j", "Sistemas", 5)
    profe1 = Profesor("Dr. Alan", "alan@u.edu", "hash_a", "Ciencias")
    
    catalogo.registrar_usuario(admin)
    catalogo.registrar_usuario(alumno1)
    catalogo.registrar_usuario(profe1)
    
    lf1 = LibroFisico("Python Crash Course", "Eric Matthes", "9781593279288", 2019, "Programacion", "Estante A1", 3)
    ld1 = LibroDigital("Design Patterns", "Gang of Four", "9780201633610", 1994, "Ingenieria", "PDF", 2.5, "http://dl/dp.pdf")
    lf2 = LibroFisico("Clean Code", "Robert C. Martin", "9780132350884", 2008, "Ingenieria", "Estante B2", 1)
    lf3 = LibroFisico("Cien Años de Soledad", "Gabriel Garcia M.", "9780306406157", 1967, "Ficcion", "Estante C3", 2)
    
    catalogo.agregar_libro(lf1)
    catalogo.agregar_libro(ld1)
    catalogo.agregar_libro(lf2)
    catalogo.agregar_libro(lf3)
    
    try:
        catalogo.registrar_prestamo("juan@u.edu", "9781593279288")
    except: pass

class BibliotecaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca Digital")
        self.root.geometry("700x600")
        
        self.catalogo = Catalogo()
        self.cola = GestorCola()
        self.ruta_datos = os.path.join(os.path.dirname(__file__), 'datos', 'biblioteca.json')
        
        self.cargar_datos()
        self.crear_interfaz()
        self.mostrar_mensaje("¡Bienvenido al Sistema de Biblioteca Digital!\nSelecciona una opción o realiza una búsqueda.")
        self.listar_libros() # Muestra los libros automáticamente al abrir

    def cargar_datos(self):
        try:
            self.catalogo.cargar_json(self.ruta_datos)
            # Si el JSON existe pero está vacío o no se implementó la carga completa:
            if len(self.catalogo.libros) == 0:
                seed_data(self.catalogo)
        except FileNotFoundError:
            seed_data(self.catalogo)

    def crear_interfaz(self):
        # 1. PARTE SUPERIOR: Opciones Principales
        frame_superior = tk.Frame(self.root, pady=10)
        frame_superior.pack(fill=tk.X)
        
        tk.Button(frame_superior, text="📚 Libros", command=self.listar_libros, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_superior, text="👥 Usuarios", command=self.listar_usuarios, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_superior, text="🔄 Préstamos", command=self.menu_prestamos, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_superior, text="📊 Reportes", command=self.ver_reportes, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_superior, text="💾 Guardar y Salir", command=self.salir, width=15, bg="#ffcccc").pack(side=tk.RIGHT, padx=5)

        # 2. PARTE MEDIA: Formulario (Título, ISBN, Autor, Año)
        frame_medio = tk.LabelFrame(self.root, text="Búsqueda y Registro Rápido", pady=10, padx=10)
        frame_medio.pack(fill=tk.X, padx=10, pady=10)
        
        # Grid layout para los campos
        tk.Label(frame_medio, text="Título:").grid(row=0, column=0, sticky=tk.E, pady=5)
        self.entry_titulo = tk.Entry(frame_medio, width=25)
        self.entry_titulo.grid(row=0, column=1, padx=5)
        
        tk.Label(frame_medio, text="ISBN-13:").grid(row=0, column=2, sticky=tk.E, pady=5)
        self.entry_isbn = tk.Entry(frame_medio, width=20)
        self.entry_isbn.grid(row=0, column=3, padx=5)
        
        tk.Label(frame_medio, text="Autor:").grid(row=1, column=0, sticky=tk.E, pady=5)
        self.entry_autor = tk.Entry(frame_medio, width=25)
        self.entry_autor.grid(row=1, column=1, padx=5)
        
        tk.Label(frame_medio, text="Año:").grid(row=1, column=2, sticky=tk.E, pady=5)
        self.entry_anio = tk.Entry(frame_medio, width=10)
        self.entry_anio.grid(row=1, column=3, sticky=tk.W, padx=5)
        
        # Botones de acción del formulario
        frame_botones = tk.Frame(frame_medio)
        frame_botones.grid(row=0, column=4, rowspan=2, padx=15)
        
        tk.Button(frame_botones, text="➕ Agregar", command=self.agregar_libro, width=10, bg="#d4edda").pack(pady=2)
        tk.Button(frame_botones, text="🔍 Buscar", command=self.buscar_libro, width=10, bg="#e0f7fa").pack(pady=2)
        tk.Button(frame_botones, text="🗑️ Eliminar", command=self.eliminar_libro, width=10, bg="#f8d7da").pack(pady=2)

        # 3. PARTE INFERIOR: Información del estado del libro
        frame_inferior = tk.LabelFrame(self.root, text="Información y Estado", pady=5, padx=5)
        frame_inferior.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Text widget con scroll
        scrollbar = tk.Scrollbar(frame_inferior)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_info = tk.Text(frame_inferior, height=15, yscrollcommand=scrollbar.set, font=("Consolas", 10))
        self.text_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_info.yview)

    def mostrar_mensaje(self, mensaje: str, limpiar: bool = True):
        if limpiar:
            self.text_info.delete(1.0, tk.END)
        self.text_info.insert(tk.END, mensaje + "\n\n")
        self.text_info.see(tk.END)
        
    def agregar_libro(self):
        titulo = self.entry_titulo.get().strip()
        isbn = self.entry_isbn.get().strip()
        autor = self.entry_autor.get().strip()
        anio_str = self.entry_anio.get().strip()
        
        if not (titulo and isbn and autor and anio_str):
            messagebox.showwarning("Faltan datos", "Por favor, llena los 4 campos (Título, ISBN, Autor, Año) para agregar un libro.")
            return
            
        try:
            anio = int(anio_str)
            # Por simplicidad en GUI, lo registramos como Libro Físico genérico
            nuevo_libro = LibroFisico(titulo, autor, isbn, anio, "General", "Estante Nuevo", 1)
            self.catalogo.agregar_libro(nuevo_libro)
            self.mostrar_mensaje(f"✅ Libro agregado exitosamente:\n{nuevo_libro}")
            
            # Limpiar campos
            self.entry_titulo.delete(0, tk.END)
            self.entry_isbn.delete(0, tk.END)
            self.entry_autor.delete(0, tk.END)
            self.entry_anio.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))
            
    def eliminar_libro(self):
        isbn = self.entry_isbn.get().strip()
        if not isbn:
            messagebox.showwarning("Faltan datos", "Por favor, introduce el ISBN del libro que deseas eliminar.")
            return
            
        if self.catalogo.eliminar_libro(isbn):
            self.mostrar_mensaje(f"🗑️ El libro con ISBN {isbn} ha sido eliminado del catálogo.")
            self.entry_isbn.delete(0, tk.END)
        else:
            self.mostrar_mensaje(f"❌ No se encontró ningún libro con el ISBN {isbn}.")

    def listar_libros(self):
        self.mostrar_mensaje("=== LISTADO DE LIBROS ===")
        for libro in self.catalogo.libros:
            estado = "DISPONIBLE" if libro.disponible else "PRESTADO"
            info = f"[{estado}] {libro.titulo} | Autor: {libro.autor} | ISBN: {libro.isbn} | Año: {libro.anio}"
            self.mostrar_mensaje(info, limpiar=False)

    def listar_usuarios(self):
        self.mostrar_mensaje("=== LISTADO DE USUARIOS ===")
        for usuario in self.catalogo.usuarios.values():
            info = f"- {usuario.nombre} ({usuario.__class__.__name__}) | Email: {usuario.email}"
            self.mostrar_mensaje(info, limpiar=False)

    def menu_prestamos(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de Préstamos")
        ventana.geometry("600x400")
        ventana.transient(self.root)
        ventana.grab_set() # Hace que la ventana sea modal
        
        tk.Label(ventana, text="Préstamos Activos en el Sistema:", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        # Frame para la lista
        frame_lista = tk.Frame(ventana)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=20)
        
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, width=80, height=12, font=("Consolas", 10))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        
        # Llenar la lista
        prestamos_activos = [p for p in self.catalogo.prestamos if p.activo]
        if not prestamos_activos:
            listbox.insert(tk.END, "--- No hay préstamos activos actualmente ---")
        else:
            for p in prestamos_activos:
                # Guardamos el ISBN al principio para extraerlo fácil
                listbox.insert(tk.END, f"[{p.libro.isbn}] {p.libro.titulo[:25]}... -> Prestado a: {p.usuario.email}")
                
        def prestar():
            vent_prestamo = tk.Toplevel(ventana)
            vent_prestamo.title("Nuevo Préstamo")
            vent_prestamo.geometry("500x400")
            vent_prestamo.transient(ventana)
            vent_prestamo.grab_set()
            
            tk.Label(vent_prestamo, text="Email del Usuario:", font=("Helvetica", 10, "bold")).pack(pady=5)
            entry_email = tk.Entry(vent_prestamo, width=40)
            entry_email.pack(pady=5)
            
            tk.Label(vent_prestamo, text="Libros Disponibles:", font=("Helvetica", 10, "bold")).pack(pady=5)
            
            frame_disp = tk.Frame(vent_prestamo)
            frame_disp.pack(fill=tk.BOTH, expand=True, padx=20)
            
            scroll_disp = tk.Scrollbar(frame_disp)
            scroll_disp.pack(side=tk.RIGHT, fill=tk.Y)
            
            lista_disp = tk.Listbox(frame_disp, yscrollcommand=scroll_disp.set, font=("Consolas", 10))
            lista_disp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scroll_disp.config(command=lista_disp.yview)
            
            libros_disponibles = self.catalogo.listar_disponibles()
            if not libros_disponibles:
                lista_disp.insert(tk.END, "--- No hay libros disponibles ---")
            else:
                for l in libros_disponibles:
                    lista_disp.insert(tk.END, f"[{l.isbn}] {l.titulo} por {l.autor}")
                    
            def confirmar():
                email = entry_email.get().strip()
                if not email:
                    messagebox.showwarning("Dato requerido", "Por favor ingresa el email del usuario.", parent=vent_prestamo)
                    return
                    
                seleccion = lista_disp.curselection()
                if not seleccion or not libros_disponibles:
                    messagebox.showwarning("Dato requerido", "Por favor selecciona un libro disponible de la lista.", parent=vent_prestamo)
                    return
                
                texto = lista_disp.get(seleccion[0])
                isbn = texto.split("]")[0].replace("[", "").strip()
                
                try:
                    prestamo = self.catalogo.registrar_prestamo(email, isbn)
                    self.mostrar_mensaje(f"✅ Préstamo Exitoso:\nEl libro quedó a cargo de: {prestamo.usuario.nombre} ({email})\nDetalles: {prestamo}")
                    vent_prestamo.destroy()
                    ventana.destroy() # Cierra el gestor para que al volver a abrirlo se actualice
                except Exception as e:
                    # Capturamos error para cola de espera
                    if "disponible" in str(e).lower() or "ejemplares" in str(e).lower():
                        if messagebox.askyesno("No disponible", f"{e}\n¿Deseas entrar a la cola de espera?", parent=vent_prestamo):
                            self.cola.encolar_solicitud(email, isbn)
                            messagebox.showinfo("Cola", "Añadido a la cola exitosamente.", parent=vent_prestamo)
                            vent_prestamo.destroy()
                            ventana.destroy()
                    else:
                        messagebox.showerror("Error", str(e), parent=vent_prestamo)
                        
            tk.Button(vent_prestamo, text="✅ Confirmar Préstamo", command=confirmar, bg="#d4edda", width=25, height=2).pack(pady=10)
                
        def devolver():
            seleccion = listbox.curselection()
            isbn = None
            if seleccion and prestamos_activos:
                # Extraemos el ISBN que está entre corchetes al inicio de la cadena: [ISBN]
                texto = listbox.get(seleccion[0])
                isbn = texto.split("]")[0].replace("[", "").strip()
            else:
                isbn = simpledialog.askstring("Devolución manual", "No seleccionaste nada. Ingresa el ISBN manualmente:", parent=ventana)
                
            if isbn:
                try:
                    multa = self.catalogo.procesar_devolucion(isbn)
                    self.mostrar_mensaje(f"✅ Devolución Exitosa.\nMulta calculada: ${multa} MXN.")
                    ventana.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e), parent=ventana)

        frame_botones = tk.Frame(ventana, pady=15)
        frame_botones.pack()
        
        tk.Button(frame_botones, text="➕ Nuevo Préstamo", command=prestar, width=20, bg="#d4edda").pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botones, text="🔄 Devolver Seleccionado", command=devolver, width=25, bg="#f8d7da").pack(side=tk.LEFT, padx=10)

    def buscar_libro(self):
        # Toma los datos de las cajas de texto (el que tenga texto)
        query = self.entry_titulo.get() or self.entry_isbn.get() or self.entry_autor.get()
        
        if not query:
            self.mostrar_mensaje("Por favor, escribe un título, autor o ISBN en los cuadros de arriba para buscar.")
            return
            
        resultados = self.catalogo.buscar(query)
        self.mostrar_mensaje(f"=== RESULTADOS DE BÚSQUEDA PARA '{query}' ===")
        
        if not resultados:
            self.mostrar_mensaje("No se encontraron coincidencias.", limpiar=False)
        else:
            for libro in resultados:
                estado = "🟢 DISPONIBLE" if libro.disponible else "🔴 NO DISPONIBLE"
                self.mostrar_mensaje(f"{estado}\n Título: {libro.titulo}\n Autor: {libro.autor}\n ISBN: {libro.isbn}\n Año: {libro.anio}\n", limpiar=False)

    def ver_reportes(self):
        rep = self.catalogo.generar_reporte()
        self.mostrar_mensaje("=== REPORTE GENERAL DE LA BIBLIOTECA ===")
        for k, v in rep.items():
            self.mostrar_mensaje(f"- {k.replace('_', ' ').capitalize()}: {v}", limpiar=False)
            
        # Añadir información de la cola
        solicitudes = self.cola.ver_cola()
        self.mostrar_mensaje(f"\n- Personas en cola de espera: {len(solicitudes)}", limpiar=False)

    def salir(self):
        self.catalogo.guardar_json(self.ruta_datos)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()
