# Bitácora de Prompts (Prompts Log)
**Sistema de Gestión de Biblioteca Digital**
**Alumno:** Diaz Ibarra
**Matrícula:** 221941093

---

## Tarea 1.1 — Configuración del entorno y repositorio
### Prompt #1
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Soy estudiante de programación usando Python 3.10 y VS Code. Necesito crear la estructura de carpetas para un proyecto llamado 'sgbd' que contendrá: módulos de modelos, servicios y utilidades. Dame los comandos bash/terminal para crear esa estructura y el contenido de un .gitignore apropiado para Python. Explica brevemente para qué sirve cada carpeta.
**Respuesta recibida (resumen):** La IA generó los comandos de PowerShell para inicializar el repositorio y crear las carpetas principales (modelos, servicios, utils, datos, tests) y archivos base. También entregó el contenido para el `.gitignore`.
**Código adoptado / modificado:** Usé el `.gitignore` propuesto y dejé que la IA ejecutara los comandos de creación en el workspace.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí a estructurar un proyecto en Python en paquetes lógicos (con `__init__.py`) y la importancia de no versionar archivos autogenerados ni datos en crudo usando el `.gitignore`.
**Temas de la materia que aplica este prompt:** Entorno de desarrollo, Repositorios de código.

---

## Tarea 1.2 — Variables y validadores (Parte 1: ISBN)
### Prompt #2
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** necesito implementar una funcion llamada validar_isbn13 como requisitos debe verificar que el isbn tenga exactamente 13 caracteres, todos deben ser digitos y debe validar correctamente el digito verificador segun el algoritmo isbn13 pero como restricciones no debe tener librerias externas y usar solo python basico, quiero que incluyas docstring claro con una explicacion, ejemplos de uso (doctest), casos de prueba y explicaciones paso a paso del algoritmo
**Respuesta recibida (resumen):** La IA generó la función `validar_isbn13` en `utils/validadores.py` usando solo Python estándar. Incluyó la lógica del algoritmo alternando multiplicadores 1 y 3, así como validaciones previas de longitud y tipo. También agregó un bloque de pruebas unitarias locales (manuales y doctest).
**Código adoptado / modificado:** El código fue adoptado íntegramente ya que cumple con los requerimientos exactos de la práctica y documenta bien la lógica interna.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí cómo aplicar el algoritmo ISBN-13 matemáticamente y cómo los docstrings pueden ser usados directamente como pruebas automáticas usando el módulo `doctest`.
**Temas de la materia que aplica este prompt:** Operadores, Sentencias de control.

---

## Tarea 1.2 — Variables y validadores (Parte 2: Constantes y Email)
### Prompt #3
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Necesito completar la Tarea 1.2 creando dos archivos: constantes.py y validadores.py. 1) En constantes.py: Definir constantes usando mayúsculas... 2) En validadores.py: Crear dos funciones... No uses librerías externas.
**Respuesta recibida (resumen):** La IA creó `constantes.py` con las variables en mayúsculas requeridas y añadió `validar_email` al archivo `validadores.py` existente. Utilizó métodos básicos de string como `.split('@')` y `.count()` para validar la estructura del correo electrónico sin expresiones regulares.
**Código adoptado / modificado:** El código fue integrado directamente al proyecto porque cumple las restricciones estipuladas de no usar módulos externos.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí el concepto de `SCREAMING_SNAKE_CASE` en Python y cómo validar cadenas de texto complejas sin depender de `re` (expresiones regulares).
**Temas de la materia que aplica este prompt:** Identificadores, Variables, Manejo de Strings básico.

---

## Tarea 1.3 — Operadores y sentencias de control
### Prompt #4
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Necesito una función Python llamada 'calcular_multa' que reciba dos parámetros: dias_retraso (int) y tipo_usuario (str: 'alumno', 'profesor', 'admin'). La lógica es: alumnos pagan $5 MXN por día, profesores $2 MXN/día, admins no pagan. Si el retraso supera 30 días, la multa total aumenta 20%. Muéstrame dos versiones: una con if/elif/else y otra con match/case. Incluye docstring con ejemplos (doctest).
**Respuesta recibida (resumen):** La IA generó dos versiones de la función (`calcular_multa_if` y `calcular_multa_match`) en `servicios/calculo_multas.py`. Ambas manejan los distintos casos y aplican el recargo del 20% si excede los 30 días.
**Código adoptado / modificado:** Adoptado tal cual, configurando la versión `match/case` como la principal para aprovechar las características de Python 3.10.
**Lo que aprendí / Lo que la IA no entendió:** El uso de `match/case` simplifica la sintaxis condicional anidada, y aprendí que debo asegurar que las comparaciones de texto no sean sensibles a mayúsculas usando `.lower()`.
**Temas de la materia que aplica este prompt:** Operadores, Sentencias de control.

---

## Tarea 1.4 — Manejo de Strings
### Prompt #5
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Necesito implementar en Python una función 'normalizar_titulo' que reciba un string con el título de un libro y lo limpie: eliminar espacios múltiples, capitalizar cada palabra (title case), y remover caracteres que no sean letras, números, espacios o comas. También quiero una función 'generar_slug' que convierta el mismo título a formato URL (minúsculas, guiones, sin acentos). Usa el módulo 'unicodedata' para los acentos. Explica cada paso.
**Respuesta recibida (resumen):** Se implementaron las funciones `normalizar_titulo` y `generar_slug` junto con `formatear_reporte_libro` y `buscar_en_texto` en `utils/formato_texto.py`. Se utilizó `unicodedata` para remover diacríticos y f-strings para formateo.
**Código adoptado / modificado:** Adoptado sin modificaciones. Los doctests confirman que limpian caracteres extraños adecuadamente.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí a usar el módulo `unicodedata` (`normalize('NFD')`) para separar los caracteres base de sus tildes y luego filtrarlos, una técnica muy robusta para limpieza de strings.
**Temas de la materia que aplica este prompt:** Manejo de Strings.

---

## Tarea 2.1 — Clases, objetos y encapsulamiento
### Prompt #6
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Necesito crear una clase Python 'Libro' con encapsulamiento completo. Los atributos deben ser privados (_titulo, _autor, _isbn, _anio, _disponible) y accesibles mediante @property con getters y setters. El setter de isbn debe llamar a una función externa validar_isbn13(isbn). El setter de anio debe rechazar años fuera del rango 1440-2025. Necesito también __str__, __repr__, __eq__ (igualdad por isbn) y los métodos to_dict() / from_dict(). Muéstrame el código completo con type hints y docstrings.
**Respuesta recibida (resumen):** La IA generó la clase `Libro` en `modelos/libro.py`. Además, se aseguró de que heredara de `Entidad` (de la Tarea 2.2 para mantener la jerarquía) e importó correctamente `validar_isbn13`. 
**Código adoptado / modificado:** El código se adoptó tal cual. Los métodos dunder y el encapsulamiento funcionan perfectamente.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí a usar decoradores `@property` para emular getters y setters de manera pythónica, asegurando que las validaciones se corran siempre que un atributo se intente cambiar.
**Temas de la materia que aplica este prompt:** Clases y Objetos, Encapsulamiento, Métodos, Abstracción.

---

## Tarea 2.2 — Abstracción y clases abstractas
### Prompt #7
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Explícame cómo usar el módulo 'abc' de Python para crear clases abstractas. Necesito una clase base 'Entidad' con un UUID generado con uuid.uuid4() y un timestamp de creación. Debe declarar como métodos abstractos __str__ y to_dict. Luego quiero una subclase abstracta 'Usuario(Entidad)' que añada el método abstracto puede_pedir_prestado(). ¿Cómo verifico en código que intentar instanciar estas clases arroja TypeError?
**Respuesta recibida (resumen):** La IA implementó `Entidad` en `modelos/entidad.py` y `Usuario` en `modelos/usuario.py`. Añadió código bajo `if __name__ == "__main__":` en el módulo de usuario para demostrar que tratar de instanciarlas lanza `TypeError`.
**Código adoptado / modificado:** Adoptado. Cumple perfectamente con el módulo `abc`.
**Lo que aprendí / Lo que la IA no entendió:** Entendí que el módulo `abc` (Abstract Base Classes) sirve como contrato. Obliga a que cualquier clase que herede de `Entidad` implemente `to_dict()` y `__str__()`.
**Temas de la materia que aplica este prompt:** Abstracción, Clases abstractas (ABC).

---

## Tarea 2.3 — Herencia
### Prompt #8
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Tengo una clase base 'Libro' en Python. Necesito dos subclases: 1) 'LibroDigital' que añada: formato (validado en ['PDF','EPUB','MOBI']), tamano_mb (float > 0) y url_descarga (str con validación básica de URL). 2) 'LibroFisico' que añada: ubicacion (str no vacío) y num_ejemplares (int >= 1). Ambas deben llamar super().__init__() correctamente y sobreescribir __str__. Muéstrame también cómo validar instancias con isinstance() e issubclass() y añade las clases Alumno, Profesor y Administrador heredando de Usuario.
**Respuesta recibida (resumen):** La IA añadió `LibroDigital` y `LibroFisico` en `modelos/libro.py` y completó la jerarquía de `Usuario` (`Alumno`, `Profesor`, `Administrador`) en `modelos/usuario.py`. Usó `super().__init__()` correctamente y sobreescribió `__str__` en cada caso para diferenciar la representación.
**Código adoptado / modificado:** Adoptado. Cumple con la sobreescritura (override) y extiende el diccionario `to_dict()`.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí a usar `super().__str__()` para no repetir el formato base y solo agregar los detalles específicos de las subclases.
**Temas de la materia que aplica este prompt:** Herencia, Polimorfismo, Clases y Objetos.

---

## Tarea 2.4 — Polimorfismo y sobreescritura de métodos
### Prompt #9
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Explícame polimorfismo en Python con un ejemplo concreto usando mis clases Libro, LibroDigital y LibroFisico. Quiero: 1) Una función 'mostrar_info(item)' que funcione con cualquier subclase de Libro sin usar isinstance, aprovechando que todas sobreescriben __str__. 2) Una función 'generar_reporte(items: list)' que use duck typing: asume que todos los objetos tienen to_dict() y genera un texto tabulado. 3) Ordenar libros por titulo con sorted() y una lambda. Muéstrame el código y explica qué es duck typing en tus propias palabras. Añade calcular_multa() en Alumno y Profesor.
**Respuesta recibida (resumen):** Se generó el archivo `utils/display.py` conteniendo `mostrar_info` y `generar_reporte` demostrando Duck Typing. Además, se insertó `calcular_multa` en las clases de usuarios.
**Código adoptado / modificado:** Adoptado sin modificaciones.
**Lo que aprendí / Lo que la IA no entendió:** Entendí que "Duck Typing" significa que Python no comprueba el tipo del objeto, sino si el objeto "sabe hacer" lo que se le pide (ej. si tiene el método `to_dict()`).
**Temas de la materia que aplica este prompt:** Polimorfismo, Duck Typing, Métodos.

---

## Tarea 2.5 — Protocolo / Interfaz y Catálogo
### Prompt #10
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** En Python necesito: 1) Un 'Protocol' llamado 'Buscable' con el método buscar(query: str) -> list. 2) Una clase 'Catalogo' que implemente ese protocolo y gestione tres colecciones: - libros: list[Libro] - usuarios: dict[str, Usuario] (clave = email) - prestamos: list[Prestamo] Necesito métodos para CRUD de libros y usuarios, y métodos para registrar y cerrar préstamos. El método buscar() debe usar comprensiones de lista para buscar en titulo, autor e isbn de forma case-insensitive. También necesito guardar_json() y cargar_json() con el módulo json. (Añadir también la clase Prestamo requerida para esto).
**Respuesta recibida (resumen):** La IA implementó `Prestamo` en `modelos/prestamo.py` para llevar el control de multas y fechas. Luego implementó `Catalogo` en `modelos/catalogo.py` aplicando el protocolo `Buscable` con `typing.Protocol`. 
**Código adoptado / modificado:** Adoptado sin modificaciones.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí que los `Protocol` en Python permiten definir interfaces formales (como en Java o C#) usando tipado estático, y a usar comprensiones de lista para filtrar objetos eficientemente.
**Temas de la materia que aplica este prompt:** Interfaces/Protocolos, Colecciones (list, dict), Abstracción.

---

## Tarea 2.6 — Colecciones avanzadas
### Prompt #11
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Necesito implementar en Python tres gestores de datos para mi sistema de biblioteca: 1) Cola de espera (FIFO) usando collections.deque para solicitudes de libros. Métodos: encolar(usuario_email, isbn), atender() -> tuple|None, ver() -> list. 2) Historial de acciones (LIFO/pila) usando una lista Python con append/pop. 3) Estadísticas usando collections.Counter para contar préstamos por libro y collections.defaultdict(list) para agrupar por género. Muéstrame los tres con ejemplos de uso y explica la diferencia entre list, deque, Counter y defaultdict.
**Respuesta recibida (resumen):** La IA separó el código en tres archivos dentro de `servicios/`: `gestor_cola.py` para la cola FIFO, `historial.py` para la pila LIFO y `estadisticas.py` con métodos estáticos para los análisis.
**Código adoptado / modificado:** Adoptado de forma directa.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí que `collections.deque` es mucho más rápido para sacar elementos del principio de una lista (`popleft()`) que una lista nativa. También `Counter` me ahorra tener que escribir bucles anidados para contar ocurrencias.
**Temas de la materia que aplica este prompt:** Colecciones avanzadas, list, deque, dict, Counter, defaultdict.

---

## Tarea 2.7 — Integración: menú de consola y main.py
### Prompt #12
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Tengo un sistema de biblioteca en Python con las clases Catalogo, Libro y Usuario. Necesito un archivo main.py que: 1) Al iniciar, intente cargar datos de 'datos/biblioteca.json'. 2) Muestre un menú de consola en while True con match/case. 3) Cada opción llame al método correspondiente. 4) Capture excepciones con try/except. 5) Al salir, guarde los datos. Dame también una función 'seed_data(catalogo)' que inserte datos de prueba. Hazlo también en un menú gráfico.
**Respuesta recibida (resumen):** La IA implementó exactamente la rúbrica solicitada en `main.py` (usando un bucle while True y match/case de consola) y adicionalmente, como un extra, proporcionó `main_gui.py` usando `tkinter` para proveer una interfaz visual. 
**Código adoptado / modificado:** Adoptado. Se mantuvieron ambos archivos para cumplir tanto con la exigencia académica del menú de consola estricto, como con el extra visual.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí a usar `match/case` para manejar flujos interactivos de consola y a manejar persistencia de datos (serialización y deserialización) en el ciclo de vida completo de un programa.
**Temas de la materia que aplica este prompt:** Integración: OOP, Colecciones, Control de flujo, Strings, Archivos.

---

## Extras de Interfaz y Lógica (Mejoras Personalizadas)

### Prompt #13
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Haz que el main.py se convierta completamente en un menú gráfico interactivo usando tkinter, descartando el menú de consola.
**Respuesta recibida (resumen):** La IA reescribió `main.py` con `tkinter`, implementando cuadros de diálogo, botones y un flujo visual básico respetando las clases del modelo.
**Código adoptado / modificado:** Adoptado. Ahora todo el sistema corre de forma nativa en ventanas gráficas.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí que `tkinter` permite usar la lógica de clases que ya habíamos creado (como `Catalogo`) como el "backend" de una aplicación de escritorio conectándola con eventos de botones.
**Temas de la materia que aplica este prompt:** Interfaces Gráficas, Integración.

---

### Prompt #14
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** La interfaz gráfica puedes hacer que todas las opciones principales se vean en una ventana (arriba que aparezcan libros, usuarios, préstamos y reportes), un poco más abajo agregar titulo, isbn, autor y año, y hasta abajo la información del estado del libro incluyendo si está disponible o no.
**Respuesta recibida (resumen):** La IA estructuró la ventana usando `tk.Frame` y `tk.LabelFrame` dividiendo la aplicación en 3 paneles: navegación, formulario de captura y un área `Text` con barra de desplazamiento para mostrar resultados.
**Código adoptado / modificado:** Adoptado tal cual.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí sobre el manejo de Layouts en `tkinter` (`pack` y `grid`) para organizar widgets de forma intuitiva.
**Temas de la materia que aplica este prompt:** Interfaces Gráficas.

---

### Prompt #15
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Agrega la opción para agregar y quitar libros en la interfaz.
**Respuesta recibida (resumen):** Añadió los botones `Agregar` y `Eliminar` junto al de búsqueda, enlazándolos a métodos de la clase `Catalogo`. Validó los datos obtenidos de los `tk.Entry`.
**Código adoptado / modificado:** Se adoptó para registrar libros físicos desde la GUI y permitir borrar usando el ISBN.
**Lo que aprendí / Lo que la IA no entendió:** Comprendí la importancia de extraer el texto (`get().strip()`) y validarlo (ej. parsear enteros) antes de mandar los datos al modelo de objetos.
**Temas de la materia que aplica este prompt:** Validaciones, Integración Modelo-Vista.

---

### Prompt #16
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** A la ventana principal agrégale 4 libros para que cuando abra la ventana se vean en el menú principal. Siguen sin aparecer, arréglalo.
**Respuesta recibida (resumen):** La IA añadió 4 libros a la función `seed_data`. Luego corrigió un bug en la carga JSON: el método de carga estaba vacío y no activaba los datos semilla. Añadió una validación para llamar a `seed_data` si el catálogo está vacío y forzó el listado de libros al abrir la app.
**Código adoptado / modificado:** Adoptado. Ahora la aplicación siempre inicia con datos de prueba visibles.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí que no basta con manejar el `FileNotFoundError`, también hay que verificar la integridad lógica de la carga de datos (es decir, que la lista de memoria realmente contenga elementos).
**Temas de la materia que aplica este prompt:** Archivos, JSON, Manejo de Excepciones.

---

### Prompt #17
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Para la opción de prestar libros agrega que se le ponga a nombre de quién se quedará a cargo el libro.
**Respuesta recibida (resumen):** Cambió el mensaje de confirmación para leer y desplegar `prestamo.usuario.nombre`, haciendo uso de la asociación de objetos dentro del préstamo.
**Código adoptado / modificado:** Adoptado. El mensaje de éxito es más descriptivo.
**Lo que aprendí / Lo que la IA no entendió:** Reforcé que cuando un objeto (`Prestamo`) tiene a otro objeto como atributo (`Usuario`), puedo acceder a sus propiedades anidadas usando notación de puntos.
**Temas de la materia que aplica este prompt:** Clases y Objetos, Atributos de instancia.

---

### Prompt #18
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** En la opción para devolver libros, haz que solamente se necesite poner el ISBN del libro, sin la necesidad de poner el correo electrónico de la persona que lo pidió.
**Respuesta recibida (resumen):** La IA reescribió `procesar_devolucion` en el catálogo para buscar en la lista de préstamos usando únicamente `p.libro.isbn == isbn` en lugar de requerir doble coincidencia. También actualizó la GUI para remover ese campo.
**Código adoptado / modificado:** Adoptado completamente.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí que puedo simplificar las búsquedas en colecciones de objetos adaptándolas al uso real (un ISBN físico es un identificador único en préstamos activos).
**Temas de la materia que aplica este prompt:** Comprensión de colecciones, Algoritmos de búsqueda.

---

### Prompt #19
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Cuando vayas a registrar un libro devuelto, te aparezcan todos los libros prestados con su información para facilitar el proceso. Y al agregar un préstamo, la ventana de libros disponibles.
**Respuesta recibida (resumen):** La IA rediseñó completamente la sección de préstamos creando un `tk.Toplevel` (ventana modal) con un `Listbox`. En ella se listan todos los libros disponibles para prestar, o los activos para devolver, permitiendo seleccionarlos con el ratón sin teclear códigos.
**Código adoptado / modificado:** Adoptado. La interfaz gráfica subió significativamente de nivel.
**Lo que aprendí / Lo que la IA no entendió:** Entendí cómo extraer datos ocultos de cadenas de texto dentro de widgets de interfaz (haciendo `.split("]")[0]`) para relacionar las vistas con el modelo lógico (usando el ISBN como puente).
**Temas de la materia que aplica este prompt:** Manejo de Strings, Listas.

---

### Prompt #20
**LLM usada:** Gemini 3.1 Pro (Antigravity)
**Fecha/Hora:** 2026-05-02
**Prompt enviado:** Agrega que cuando se preste un libro, si el correo no existe, se agregue automáticamente a los usuarios.
**Respuesta recibida (resumen):** La IA modificó `registrar_prestamo` para instanciar automáticamente un objeto `Alumno` por defecto y registrarlo en el diccionario de usuarios si detecta que la clave (email) no se encuentra.
**Código adoptado / modificado:** Adoptado. Simplificó enormemente el flujo de prueba.
**Lo que aprendí / Lo que la IA no entendió:** Aprendí que las funciones del modelo deben ser flexibles y en lugar de simplemente lanzar un `raise ValueError`, es posible aplicar flujos automatizados de resolución de errores.
**Temas de la materia que aplica este prompt:** Diccionarios, Instanciación de Objetos.

---
