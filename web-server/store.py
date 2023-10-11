import requests #importamos esta libreria para poder hacer las peticiones al api

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #aca hacemos la peticion para que nos devuelva la informacion de las categorias, en la variable r se almacenara el resultado
    print(r.status_code) #nos va imprimir el codigo de estado de la solicitud, si es 200 es porque fue exitosa la consulta
    print(r.text) #nos mostrara los datos de la consulta del api, viene en formato string
    categories = r.json() #con el metodo json que ya lo trae la libreria, nos ayuda a convertirlo en una lista que podremos manipular.

    for categorory in categories:
        print(categorory['name']) #de esta forma vamos a imprimir solo el titulo de las categorias 