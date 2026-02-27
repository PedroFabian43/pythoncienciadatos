import matplotlib.pyplot as plt

productos = []
ventas = []

#Deseamos pedir 5 productos

for i in range(1, 6):
    print("Nombre del producto")
    prod = input()
    productos.append(prod)
    print("Introduzca el número de ventas")
    num = int(input())
    ventas.append(num)

plt.pie(ventas, labels=productos)
plt.title("Venta de Juegos")
plt.savefig('images/ventas_tarta.png')
plt.show()