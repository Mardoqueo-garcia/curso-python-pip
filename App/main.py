import utils #para obtener la lista segun el pais seleccionado
import read_csv #para leer el archivo csv
import charts 
import pandas as pd #importamos la libreria pandas

def run():

  #CODIGO MANUALMENTE PARA PODER LEER Y FILTRAR DATOS DEL CSV
  '''
  #aca filtraremos solo los paises de sur america para que sea facil de graficar
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  #obtenemos los paises
  countries = list(map(lambda x : x['Country/Territory'], data))
  #obtenemos el porcentage
  #porcentaje = list(map(lambda por : por['World Population Percentage'], data))
  #charts.generate_pie_chart(countries, porcentaje) #creamos la grafica


data = read_csv.read_csv('data.csv') #obtenemos la data
  country = input('Dijite el pais ==> ') #Ingresan el pais

  result = utils.poblacion_by_pais(data, country)

  if len(result) > 0: # si viene mayor a cero es xq encontro los datos
    country = result[0]
    labels, values = utils.get_poblacion(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  else:
    print('Pais no encontrado, por favor intenta con otro.')

'''
#CODIGO USANDO LA LIBRERIA DE PANDAS
  print('Iniciando la ejecucion del programa')
  df = pd.read_csv('data.csv') #de esta forma estamos leyendo el csv, ahorrando muchas lineas de codigo
  df2 = df[df['Continent']=='Asia'] #de esta forma estamos filtrando los datos del csv conforme el continente dado
  countries = df2['Country/Territory'].values #de esta manera estamos trayendo todos los valores de esa columna
  porcentaje = df2['World Population Percentage'].values
  charts.generate_pie_chart(countries, porcentaje) 
  print('Termino la ejecusion')


if __name__ == '__main__':
  run()
