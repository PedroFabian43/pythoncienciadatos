import matplotlib.pyplot as plt

#La mayoria de los graficos dibujan sus elementos a partir de X e Y

x = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]

#Valor del mercado
y = [30, 400, 66, 20]

#Libreria mediante libreria(alias).bar
plt.scatter(x, y)
#PErsonalizamos el gráfico 
plt.title("Gráfico de dispersion")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")
#Podemos gurdar los gráficos en imágenes
plt.savefig('images/dispersion.png')
plt.show()