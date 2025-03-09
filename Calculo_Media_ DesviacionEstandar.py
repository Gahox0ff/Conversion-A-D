# Ruta del archivo
ruta_archivo = "MUESTRAS_0V.txt"

# Leer el archivo y extraer los valores de voltaje
voltajes = []

with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split()  # Separar los valores (tiempo y voltaje)
        if len(datos) == 2:  # Verificar que haya dos columnas
            try:
                voltaje = float(datos[1])  # Extraer el voltaje
                voltajes.append(voltaje)
            except ValueError:
                pass  # Ignorar líneas con datos inválidos

# Calcular y mostrar la media y la desviación estándar
if voltajes:
    media = np.mean(voltajes)
    desviacion = np.std(voltajes)
    print(f"Media del voltaje: {media:.5f} V")
    print(f"Desviación estándar: {desviacion:.5f} V")
else:
    print("No se encontraron datos de voltaje en el archivo.")
