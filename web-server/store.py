import requests #importamos esta libreria para poder hacer las peticiones al api

#Variables
url_categories = 'https://api.escuelajs.co/api/v1/categories' #url de todas las categorias

def get_categories():
    try:
        r = requests.get(url_categories) #aca hacemos la peticion para que nos devuelva la informacion de las categorias, en la variable r se almacenara el resultado.

        status = r.status_code
        print(status) #nos va imprimir el codigo de estado de la solicitud, si es 200 es porque fue exitosa la consulta

        if status == '200 ok':
            print('La consulta fue exitosa')

            print(r.text) #nos mostrara los datos de la consulta del api, viene en formato string
            categories = r.json() #con el metodo json que ya lo trae la libreria, nos ayuda a convertirlo en una lista que podremos manipular.
            
        elif status == '404 not found':
            print('Ha ocurrido un error al conectarse con el servidor web.')

        for categorory in categories:
            print(categorory['name']) #de esta forma vamos a imprimir solo el titulo de las categorias 

    except:
        print('======== ALERTA ========')
        print('Error inesperado, intentalo cuando tengas conexion')


    