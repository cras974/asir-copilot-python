const modoSelect = document.querySelector("#modo");
const consultaTextarea = document.querySelector("#consulta");
const btnConsultar = document.querySelector("#btnConsultar");
const btnLimpiar = document.querySelector("#btnLimpiar");
const respuestaDiv = document.querySelector("#respuesta");
const estadoDiv = document.querySelector("#estado");
const exampleButtons = document.querySelectorAll(".example");

async function cargarModos() {
    try {
        const response = await fetch("/api/modos");
        const data = await response.json();
        if (!data.success) {
            throw new Error("No se pudieron cargar los modos.");
        }
        modoSelect.innerHTML = "";
        const opcionInicial = document.createElement("option");
        opcionInicial.value = "";
        opcionInicial.textContent = "Selecciona un modo";
        modoSelect.appendChild(opcionInicial);

        data.modos.forEach((modo) => {
            const option = document.createElement("option");
            option.value = modo.id;
            option.textContent = `${modo.nombre} - ${modo.descripcion}`;
            modoSelect.appendChild(option);
        });
    } catch (error) {
        mostrarEstado("Error cargando modos: " + error.message, "error");
    }
}

async function consultarIA() {
    const modo = modoSelect.value;
    const consulta = consultaTextarea.value.trim();

    if (!modo) {
        mostrarEstado("Debes seleccionar un modo.", "error");
        return;
    }
    if (consulta.length < 5) {
        mostrarEstado("La consulta es demasiado corta.", "error");
        return;
    }

    try {
        btnConsultar.disabled = true;
        btnConsultar.textContent = "Consultando IA...";
        respuestaDiv.textContent = "Generando respuesta, puede tardar unos segundos...";
        mostrarEstado("Consulta enviada a Ollama.", "ok");

        const response = await fetch("/api/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                modo: modo,
                consulta: consulta
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Error desconocido.");
        }

        if (!data.success) {
            throw new Error("La API respondió con error.");
        }

        respuestaDiv.textContent = data.data.respuesta;
        mostrarEstado("Respuesta generada correctamente.", "ok");

    } catch (error) {
        respuestaDiv.textContent = "No se pudo obtener respuesta.";
        mostrarEstado("Error: " + error.message, "error");
    } finally {
        btnConsultar.disabled = false;
        btnConsultar.textContent = "Consultar IA";
    }
}

function limpiar() {
    consultaTextarea.value = "";
    respuestaDiv.textContent = "Todavía no hay respuesta.";
    estadoDiv.classList.add("oculto");
}

function mostrarEstado(mensaje, tipo) {
    estadoDiv.textContent = mensaje;
    estadoDiv.className = `estado ${tipo}`;
    estadoDiv.classList.remove("oculto");
}

btnConsultar.addEventListener("click", consultarIA);
btnLimpiar.addEventListener("click", limpiar);

exampleButtons.forEach((button) => {
    button.addEventListener("click", () => {
        consultaTextarea.value = button.textContent.trim();
    });
});

cargarModos();