from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    modo: str = Field(
        min_length=3,
        description="Modo de asistencia: linux, docker, redes, logs o seguridad"
    )
    consulta: str = Field(
        min_length=5,
        description="Consulta o error que se enviará a la IA"
    )

class AskResponse(BaseModel):
    success: bool
    modo: str
    modelo: str
    respuesta: str