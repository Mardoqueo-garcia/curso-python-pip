#modulo nativo de python para leer archivos csv
import csv

'''
def read_csv(path): #recibira la ruta del archivo como parametro
  with open(path, 'r') as csvFile: #sera solo de modo lectura
    reader = csv.reader(csvFile, delimiter=',') #el delimitador es la separacion q trae el archivo de sus datos, en este archivo va separado por comas
    for row in reader: #leemos el archivo
      print('===========' * 10) 
      print(row) #imprmimos cada una de sus lineas de textos, nos devolvera los daos dentro de una lista, dada linea sera una lista por aparte
'''
def read_csv(path):
  with open(path, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    header = next(reader) #obtenemos la primera columna de forma manual,q seria comom la primera fila, sus llaves de acceso
    data = [] #creamos una lista donde guardaremos los diccionarios
    for row in reader:
      iterable = zip(header,row) #unimos los dos array, presentara los datos en tuplas, su llave y su valor
      country_dict = {key : value for key, value in iterable } #aca estamos creando un diccionario para q sea facil de acceder y leer los datos dentro de el
      data.append(country_dict) #cada iteracion se ira agregando a nuestra lista
      
    return data



#Lo vamos a correr como un scrip, para que pueda ejecutarse desde aca y desde otro modulo
if __name__ == '__main__':
  data = read_csv('./app/data.csv') #le mandamos la ruta del archivo