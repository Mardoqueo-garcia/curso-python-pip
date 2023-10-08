#Vamos a crear una funcion sencilla
def get_poblacion(country_dict):
  population_dict = {
    '2022' : int(country_dict['2022 Population']),
    '2020' : int(country_dict['2020 Population']),
    '2015' : int(country_dict['2015 Population']),
    '2010' : int(country_dict['2010 Population']),
    '2000' : int(country_dict['2000 Population']),
    '1990' : int(country_dict['1990 Population']),
    '1980' : int(country_dict['1980 Population']),
    '1970' : int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  
  return labels, values

#metodo para obtener poblacion de un pais
def poblacion_by_pais(data, country):
  #devolvera una lista filtrada del dato del pais que nos pasen, data sera el diccionario a iterar, country el pais (los pasaran como argumeto)
  result = list(filter(lambda item : item['Country/Territory'] == country, data))
  return result