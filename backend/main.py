from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from schemas import AskRequest
from services import comprobar_ollama, obtener_modos, preguntar_a_ollama

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = FastAPI(
    title="ASIR Copilot",
    description="Asistente IA local para Linux, Docker, redes, logs y seguridad usando Ollama.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    """
    Comprueba el estado del backend y la conexión con Ollama.
    """
    estado_ollama = comprobar_ollama()
    return {
        "status": "ok",
        "backend": "funcionando",
        "ollama": estado_ollama
    }

@app.get("/api/modos")
def modos():
    """
    Devuelve los modos disponibles.
    """
    return {
        "success": True,
        "modos": obtener_modos()
    }

@app.post("/api/ask")
def ask(datos: AskRequest):
    """
    Recibe una consulta del frontend y la envía a Ollama.
    """
    try:
        resultado = preguntar_a_ollama(datos.modo, datos.consulta)
        return {
            "success": True,
            "data": resultado
        }
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)

@app.get("/")
def index():
    """
    Sirve la página principal.
    """
    return FileResponse(FRONTEND_DIR / "index.html")