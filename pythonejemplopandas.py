#Necesitamos la libreria importada
import pandas as pd

#Las series tienen que ser iguales entre ellas SIEMPRE
#Si son 7 datos siempre 7 datos en todos aunque sea nulo
#Representan elementos de datos

datos = {
    'Nombres': ['Ana', 'Adrian', 'Lucia', 'Antonia'],
    'Edad': [23, 25, 12, 40],
    'Ciudades': ['Madrid', 'Sevilla', 'Toledo', 'Gijon']
}

#Estas series de datos se alamacenan dentro de objetos llamados DataFrames de la libreria Pandas
#a los DataFrame s eles suele llamar df
df = pd.DataFrame(datos)
#Mis primeros datos
print(df)

#Podemos filtrar los datos si queremos
#Pra filtrar se pone df[df['DATO'] = > valor]
print("-----DataFrame filtrado-----")
dffiltrado = df[df['Edad'] > 24]
print(dffiltrado)
print("-----DataFrame ordenado-----")
dforden = df.sort_values('Edad')
print(dforden)

