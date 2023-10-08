import utils #para obtener la lista segun el pais seleccionado
import read_csv #para leer el archivo csv
import charts #para graficar

def run():
  data = read_csv.read_csv('data.csv') #obtenemos la data

  #aca filtraremos solo los paises de sur america para que sea facil de graficar
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  
  #obtenemos los paises
  countries = list(map(lambda x : x['Country/Territory'], data))

  #obtenemos el porcentage
  #porcentaje = list(map(lambda por : por['World Population Percentage'], data))
  #charts.generate_pie_chart(countries, porcentaje) #creamos la grafica

  country = input('Dijite el pais ==> ') #Ingresan el pais

  result = utils.poblacion_by_pais(data, country)

  if len(result) > 0: # si viene mayor a cero es xq encontro los datos
    country = result[0]
    labels, values = utils.get_poblacion(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  else:
    print('Pais no encontrado, por favor intenta con otro.')

if __name__ == '__main__':
  run()