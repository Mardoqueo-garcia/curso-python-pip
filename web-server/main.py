import store
from fastapi import FastAPI #importamos la libreria para poder usarla
from fastapi.responses import HTMLResponse #Para que la respuesta del servidor sea codigo html

app = FastAPI() #Creamos una instancia de la aplicacion

#EJEMPLO
@app.get('/') #Un decorador, lleva la ruta donde podran ingresar desde la web. De esta forma creamos nuestro primer recurso que se vera desde al web.
def generate_list(): #metodo que nos volvera una lista de numeros
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse) #ejemplo de ruta de contacto, la nueva clase para retornar codigo html y no datos directos
def generate_list():
    return """
        <h1>Mardoqueo Garcia</h1>
        <p>Esta sera una tienda en linea para compra de granos basicos</p>
    """


def run():
    store.get_categories()

#ejecutar como scripts
if __name__ == '__main__':
    run() 