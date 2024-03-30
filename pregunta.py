"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    # Datos faltantes
    df.dropna(inplace=True)

    # Convertir a string
    df=df.apply(lambda x: x.astype(str))

    # Sin caracteres especiales
    df=df.apply(lambda x: x.str.replace("$", ""))
    df=df.apply(lambda x: x.str.replace(",", ""))
    df=df.apply(lambda x: x.str.replace("¿", ""))
    #Guiones por espacios
    df=df.apply(lambda x: x.str.replace("_", " "))
    df=df.apply(lambda x: x.str.replace("-", " "))
    # Todo a mínusculas
    df=df.apply(lambda x: x.str.lower())
    # Remueva espacios en blanco al principio y al final
    # df=df.apply(lambda x: x.str.strip())
    # Remueva errores tipográficos de barrios
    # df.barrio=df.barrio.str.replace("beln", "belen")
    # df.barrio=df.barrio.str.replace("antonio nario", "antonio nariño")
    # monto_del_credito a float
    df.monto_del_credito=df.monto_del_credito.astype(float)
    #Formato fecha_de_beneficio día-mes-año
    df.fecha_de_beneficio=pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format='mixed')



    # Duplicados
    df.drop_duplicates(inplace=True)


    return df
# columna barrio con valores únicos
# print(sorted(clean_data().barrio.unique()))
# print(sorted(clean_data().barrio.to_list()))
# print(clean_data().barrio.value_counts().to_list())
# print(clean_data().sexo.value_counts().to_list())
# print(clean_data())
