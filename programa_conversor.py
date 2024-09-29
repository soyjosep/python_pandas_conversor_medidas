import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


df = pd.read_csv("muebles_medidas.csv")

df["Pulgadas"] = df["Centímetros"].apply(cm_a_pulgadas)

df.to_csv("mueble_medidas_convertidas.csv", index=False)

print(
    "Conversión completada y guardada en un nuevo archivo llamado 'mueble_medidas_convertidas.csv"
)