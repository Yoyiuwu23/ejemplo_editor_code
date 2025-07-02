# Ejemplo Editor de Código


Este proyecto es un **editor de texto/código minimalista** desarrollado en Python y Tkinter, pensado exclusivamente con **fines pedagógicos** para ayudar a entender el funcionamiento interno de los editores de texto y código.  
No busca reemplazar a editores profesionales, sino servir como base de aprendizaje y experimentación.


## Características principales


- Interfaz gráfica con Tkinter
- Explorador de archivos y carpetas
- Contador de líneas sincronizado (al estilo VSCode)
- Resaltado de sintaxis modular para varios lenguajes (Python, HTML, CSS, JS, C, C++, C#, SQL)
- Modo claro/oscuro configurable
- Guardar, abrir y crear archivos
- Estructura modular y fácil de extender


---


## Instalación y uso


### Opción 1: Usar el ejecutable (recomendado para usuarios de Linux)


Puedes usar el ejecutable ya compilado que se encuentra en la carpeta `dist/`.  
No necesitas instalar Python ni dependencias.


```

cd dist
chmod +x main
./main

```


> **Nota:**  
> Este binario fue compilado en Linux x86_64.  
> Si tienes otra arquitectura o sistema, usa la opción 2.


---


### Opción 2: Ejecutar desde el código fuente


#### 1. Clona el repositorio


```

git clone git@github.com:Yoyiuwu23/ejemplo_editor_code.git
cd ejemplo_editor_code

```


#### 2. (Opcional) Crea un entorno virtual


```

python3 -m venv venv
source venv/bin/activate

```


#### 3. Instala dependencias


Este editor solo requiere Python 3 y Tkinter (que suele venir por defecto en la mayoría de distribuciones).  
Si usas Ubuntu/Debian y no tienes Tkinter:


```

sudo apt-get install python3-tk

```


#### 4. Ejecuta el editor


```

python3 main.py
```
## Estructura del proyecto

```


editor/
├── line_numbers/           \# Contador de líneas sincronizado
├── syntax_highlighter/     \# Resaltado de sintaxis modular por lenguaje
├── project_explorer.py     \# Explorador de archivos
├── menu_bar.py             \# Barra de menú
├── text_editor.py          \# Lógica principal del editor
file_ops.py                 \# Operaciones de archivos
main.py                     \# Punto de entrada
dist/                       \# Ejecutable compilado (main)


```


## Licencia

Este proyecto se distribuye bajo la licencia [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.txt).

---

**IMPORTANTE:**
Este software es solo para fines educativos y de aprendizaje.
No se recomienda su uso en entornos de producción ni para edición de archivos críticos.

---

## Créditos

Desarrollado por [Yoyiuwu23](https://github.com/Yoyiuwu23).
Inspirado en un gran maestro cuyo lema era "Si puedes imaginarlo, puedes programarlo".