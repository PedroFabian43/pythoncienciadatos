import matplotlib.pyplot as plt

semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
temperaturas = []

for dia in semana:
    print(f"Temperatura del {dia}")
    temp = int(input())
    temperaturas.append(temp)
#La ventaja d elos graficos está en que si le metemos mas series podemos representarlas en distintas labels
#PAsamos las cosas estilo x e y
plt.plot(semana, temperaturas, 'rD-', label="Semana")
temperaturas2 = [4, 18, 5, 23, 12, 15, 16]
plt.plot(semana, temperaturas2, 'g^--', label="Semana 2",)
plt.legend()
plt.title("Temperaturas febrero")
plt.xlabel("Dia semana")
plt.ylabel("Temperatura")
plt.savefig('images/temperaturas.png')
plt.show()