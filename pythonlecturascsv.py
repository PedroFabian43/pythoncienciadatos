import pandas as pd

#Vamos a leer daos de nuestro csv
#Creamos un DataFrame a partir del fichero

#Los csv suelen ir separados en "," pero aquie es ";" y podemos decirle que es el separador
df = pd.read_csv('data/datos.csv', delimiter=";")
#Pintamos el DataFrame
print(df)

#podemos indicar el numero de filas a mostrar
print("-----Seleccionando X filas-----")
print(df.head(6)) #Si no pones número solo muestra 5 filas

#Podemos convertir los datos en diccionarios para trabajar con python puro

diccionario = df.to_dict(orient='records') #df.to_dict es guardarlo en un diccionario y que lo guarda como un registro cada elemento

for registro in diccionario:
    print(registro)

#Podemos hacer calculos, por ejemplo la media de elementos númericos solo

df_media = df['edad'].mean()
print(df_media)

#Podemos agrupar por columnas si deseamos 
df_grupo = df.groupby('ocupacion')
print(df_grupo.size())
#Si en el print no ponemos el variable.size() nos saca el objeto ocupacion del dataframe, con el size() sale cuanta gente hay de la ocupacon que se repita
