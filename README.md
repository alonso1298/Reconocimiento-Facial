# 🧠 Reconocimiento Facial con Python
Este proyecto implementa un sistema de reconocimiento facial usando Python. Utiliza la librería face_recognition para identificar personas a través de imágenes o capturas de cámara en tiempo real. Es útil para sistemas de asistencia, seguridad o pruebas académicas.

## 📂 Estructura del proyecto
```bash
Copiar
Editar
Reconocimiento-Facial/
├── asistencia.py               # Script principal para reconocimiento en tiempo real
├── empleados/                    # Carpeta con imágenes de rostros conocidos
├── registros.csv               # Archivo donde se guarda el registro de asistencias
├── requirements.txt            # Dependencias del proyecto
```

## ⚙️ Instalación
1. Clona el repositorio:

``` bash
git clone https://github.com/alonso1298/Reconocimiento-Facial.git
cd Reconocimiento-Facial
```
2. Crea y activa un entorno virtual (opcional pero recomendado):

``` bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```
3. Instala las dependencias:

``` bash
pip install -r requirements.txt
```
⚠️ Es posible que necesites instalar dlib o sus dependencias manualmente si tienes errores en la instalación. Consulta la documentación de face_recognition para más ayuda.

## 🖼️ Uso del sistema
### 1. Entrenamiento de rostros conocidos 
Coloca imágenes de personas conocidas dentro de la carpeta empleados/, asegurándote de que el nombre del archivo corresponda con el nombre de la persona (ej. alonso.jpg).

Ejecuta:

```bash
python entrenar.py
```
Esto genera codificaciones faciales para ser comparadas durante la identificación.

### 2. Reconocimiento en tiempo real
Conecta tu cámara y ejecuta:

``` bash
python asistencia.py
```
El sistema reconocerá a las personas y registrará su nombre y hora en el archivo registros.csv.

## 🧪 Tecnologías utilizadas
- Python 3.10+

- face_recognition

- OpenCV

- NumPy

📄 Licencia
Este proyecto está bajo la licencia MIT.