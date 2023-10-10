#para no estar colocando todo el nombre le pondremos un alias, importamos la libreria para poder generar la grafica
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values): #funcion para generar grafica de barra
  #variables que dara la libreria, fig sera la figura y ax las coordenadas
  fig, ax = plt.subplots() #funcion de la libreria
  ax.bar(labels, values) #con estos valores crearemos las grafica , se creara una grafica de barras
  plt.savefig(f'./imgs/{name}.png') #para mostrar la grafica y que la guarde, le indicamos cual es el nombre segun el pais que nos digiten, se guardara en la carpeta imgs
  plt.close() #para cerrar una vez se halla generado la grafica

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('my_pie.png')
  plt.close()

#lo correremos como un scrip
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 60, 120]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)