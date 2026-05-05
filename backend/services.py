import os
import requests
from dotenv import load_dotenv
from prompts import MODOS

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b-instruct")

def obtener_modos():
    """
    Devuelve la lista de modos disponibles para el frontend.
    """
    modos_disponibles = []
    for modo_id, datos in MODOS.items():
        modos_disponibles.append({
            "id": modo_id,
            "nombre": datos["nombre"],
            "descripcion": datos["descripcion"]
        })
    return modos_disponibles

def comprobar_ollama():
    """
    Comprueba si Ollama está funcionando.
    """
    try:
        respuesta = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if respuesta.status_code != 200:
            return {
                "conectado": False,
                "mensaje": f"Ollama respondió con código HTTP {respuesta.status_code}"
            }
        
        datos = respuesta.json()
        modelos = []
        for modelo in datos.get("models", []):
            modelos.append(modelo.get("name"))
            
        return {
            "conectado": True,
            "mensaje": "Ollama conectado correctamente",
            "modelos": modelos
        }
    except requests.exceptions.RequestException as error:
        return {
            "conectado": False,
            "mensaje": "No se pudo conectar con Ollama",
            "error": str(error)
        }

def construir_prompt(modo: str, consulta: str):
    """
    Construye el prompt final que se enviará a Ollama.
    """
    if modo not in MODOS:
        raise ValueError("Modo no válido. Usa linux, docker, redes, logs o seguridad.")
    
    prompt_sistema = MODOS[modo]["prompt"]
    prompt_final = f"""
{prompt_sistema}

Consulta del alumno:
{consulta}

Responde usando esta estructura:
1. Posible explicación del problema
2. Comandos recomendados
3. Qué significa cada comando
4. Precauciones
5. Siguiente paso recomendado

La respuesta debe estar en español y adaptada a alumnado de ASIR.
"""
    return prompt_final

def preguntar_a_ollama(modo: str, consulta: str):
    """
    Envía la consulta a Ollama y devuelve la respuesta generada por la IA.
    """
    if not consulta or len(consulta.strip()) < 5:
        raise ValueError("La consulta es demasiado corta.")
        
    prompt_final = construir_prompt(modo, consulta)
    
    cuerpo_peticion = {
        "model": OLLAMA_MODEL,
        "prompt": prompt_final,
        "stream": False
    }
    
    try:
        respuesta = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=cuerpo_peticion,
            timeout=120
        )
        
        if respuesta.status_code != 200:
            raise RuntimeError(f"Ollama devolvió un error HTTP {respuesta.status_code}")
            
        datos = respuesta.json()
        
        return {
            "modo": modo,
            "modelo": OLLAMA_MODEL,
            "respuesta": datos.get("response", "No se recibió respuesta de Ollama.")
        }
    except requests.exceptions.Timeout:
        raise RuntimeError("Ollama ha tardado demasiado en responder.")
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Error conectando con Ollama: {error}")