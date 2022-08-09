import pandas as pd

paises = ["Mexico", "Colombia", "Perú", "Argentina"]
poblacion = [90000000,30000000,20000000,31000000]


dict_poblacion = {'Paises':paises, 'Poblacion':poblacion}
df_poblacion = pd.DataFrame.from_dict(dict_poblacion)
df_poblacion.to_csv('poblacion.csv', index=False)
print(df_poblacion)

#with open('test.txt', 'w') as archivo:
#    archivo.write("Data correctamente extraida!")

