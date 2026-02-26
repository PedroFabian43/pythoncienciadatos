import matplotlib.pyplot as plt

#La mayoria de los graficos dibujan sus elementos a partir de X e Y

#x = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
equipos = ["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]

#Valor del mercado
#y = [30, 400, 66, 20]
valores = [30, 400, 66, 20]


#Libreria mediante libreria(alias).bar
plt.pie(valores, labels=equipos)
#PErsonalizamos el gráfico 
plt.title("Gráfico de Tarta")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")
#Podemos gurdar los gráficos en imágenes

plt.savefig('images/tarta.png')
plt.show()