import matplotlib.pyplot as plt

def generate_pie_chart(): #funcion para generar grafica
    labels = ["Grupo 1", "Grupo 2", "Grupo 3", "Grupo 4"] #etiquetas
    values = [50, 65, 35, 75] #valores

    fig, ax = plt.subplots() #para crear la grafica con sus labels y coordenadas
    ax.pie(values, labels=labels) #para generar la grafica mandandole los datos
    plt.savefig('pie.png') #para mostrar la grafica y que la guarde, le indicamos cual es el nombre
    plt.close() #para cerrar una vez se halla generado la grafica