# ASIR Copilot 🤖

**ASIR Copilot** es un asistente de Inteligencia Artificial local diseñado específicamente para alumnos y profesionales del ciclo **ASIR (Administración de Sistemas Informáticos en Red)**. El sistema utiliza modelos de lenguaje de última generación para ofrecer diagnósticos técnicos, explicar comandos complejos y proponer soluciones seguras.

El proyecto destaca por su enfoque **didáctico y seguro**: la IA no solo resuelve el problema, sino que explica la causa raíz y advierte sobre el uso de comandos potencialmente peligrosos en entornos de producción.

---

## 🚀 Tecnologías Usadas

### Backend (Lógica y Procesamiento)
* **Python 3.11+**: Lenguaje principal de desarrollo.
* **FastAPI**: Framework de alto rendimiento para la creación de la API.
* **Uvicorn**: Servidor ASGI para la ejecución del backend.
* **Pydantic**: Validación estricta de esquemas de datos.
* **Ollama**: Motor de inferencia local para garantizar la privacidad y el uso sin conexión.
* **Qwen 2.5 (7b-instruct)**: Modelo de lenguaje especializado en tareas técnicas.

### Frontend (Interfaz de Usuario)
* **HTML5 & CSS3**: Diseño moderno con arquitectura "Dark Mode" y enfoque responsivo.
* **JavaScript (Vanilla)**: Gestión de peticiones asíncronas mediante Fetch API.

### Despliegue y Control
* **Docker & Docker Compose**: Contenedorización completa para asegurar la portabilidad del entorno.
* **Git**: Gestión del ciclo de vida del software y control de versiones.

---

🛠️ Estructura del Proyecto
asir-copilot-python/
├── backend/
│   ├── main.py
│   ├── services.py
│   ├── schemas.py
│   ├── prompts.py
│   ├── .env
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── main.js
├── docker-compose.yml
├── .gitignore
└── validacion.http

---

## ⚙️ Instalación y Configuración

### Requisitos previos
1. Tener instalado **Ollama** y el modelo descargado: `ollama pull qwen2.5:7b-instruct`.
2. Tener instalado **Docker Desktop** (opción recomendada para despliegue).

### Ejecución mediante Docker
Desde la raíz del proyecto, lanza el entorno completo con:
`docker compose up --build -d`

Una vez levantado, accede a la aplicación en: `http://localhost:8000`.

### Ejecución en Modo Desarrollo (Local)
1. Crea un entorno virtual: `python -m venv venv`.
2. Activa el entorno: `.\venv\Scripts\activate` (Windows).
3. Instala las dependencias: `pip install -r backend/requirements.txt`.
4. Inicia el servidor: `uvicorn backend.main:app --reload`.

---

## 👤 Autor
**Miguel Ángel García Cortés**
*Estudiante de Administración de Sistemas Informáticos en Red.*

## 👤 Profesor
**Ana Fuentes**
*Profesora de Administración de Sistemas Informáticos en Red.*

---

## 📄 Licencia
Este proyecto ha sido desarrollado con fines exclusivamente didácticos y académicos para el módulo de Administración de Sistemas.
