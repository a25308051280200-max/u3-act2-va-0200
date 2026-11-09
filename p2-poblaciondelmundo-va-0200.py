import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Definición de los datos
esp = ["España", "Madrid", True, 47.4]
mex = ["México", "CDMX", False, 126.7]
fra = ["Francia", "París", True, 67.7]
arg = ["Argentina", "Buenos Aires", False, 45.8]
jap = ["Japón", "Tokio", False, 125.7]

listas_paises = [esp, mex, fra, arg, jap]

# 2. Creación del DataFrame
df_paises = pd.DataFrame(
    listas_paises, columns=["País", "Capital", "Pertenece_UE", "Población"]
)
print(df_paises)

# ---------------------------------------------------------
# GUARDAR EN ARCHIVO CSV (Línea activada)
# ---------------------------------------------------------
df_paises.to_csv("paises.csv", index=False)
print("\n¡El archivo 'paises.csv' ha sido creado con éxito!")

# 3. Gráfica de líneas
plt.plot(df_paises["País"], df_paises["Población"])
plt.title("Gráfica de Países 0200")
plt.xlabel("Nombre del País")
plt.ylabel("Población (millones)")
plt.show()

# 4. Gráfica de puntos (dispersión)
plt.scatter(df_paises["País"], df_paises["Población"])
plt.title("Gráfica de Países 0200")
plt.xlabel("Nombre del País")
plt.ylabel("Población (millones)")
plt.show()

# 5. Gráfica de barras (sin ordenar)
plt.bar(df_paises["País"], df_paises["Población"])
plt.title("Países 0200")
plt.xlabel("Los Países")
plt.ylabel("Población (millones)")
plt.show()

# 6. Gráfica de barras ordenadas (sin color personalizado)
df_paises_ordenar = df_paises.sort_values("Población", ascending=False)
plt.bar(df_paises_ordenar["País"], df_paises_ordenar["Población"])
plt.title("Países 0200 (Ordenados)")
plt.xlabel("Los Países")
plt.ylabel("Población (millones)")
plt.show()

# 7. Gráfica de barras ordenadas (con color)
df_paises_ordenar = df_paises.sort_values("Población", ascending=False)
plt.bar(
    df_paises_ordenar["País"],
    df_paises_ordenar["Población"],
    color=["b", "g", "c", "y", "r"],
)
plt.title("Países 0200 (Ordenados)")
plt.xlabel("Los Países")
plt.ylabel("Población (millones)")
plt.show()

# 8. Gráfica de pastel
plt.pie(df_paises["Población"], labels=df_paises["País"])
plt.title("Países 0200 (Distribución de Población)")
plt.show()