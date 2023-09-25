from fastapi import FastAPI
import mook
app = FastAPI()


@app.get("/")
def root():
    return {
        "Servicio": "Estructura de Datos"
    }

@app.post("/indices-invertidos")
def indices_invertidos(palabra: dict):
    cache = {}
    for idex, documento in enumerate(mook.my_documents):
        words = documento.lower().split()
        for word in words:
            if word in cache:
                if documento not in cache[word]:
                    cache[word].append(documento)
            else:
                cache[word] = [documento]
    resultado = cache.get(palabra["palabra"], "No se encontró")
    return resultado