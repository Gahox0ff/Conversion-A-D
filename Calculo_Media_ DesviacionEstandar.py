import numpy as np

# Ruta del archivo
file_path = "MUESTRAS_1.1V.txt"  # Asegrate de colocar la ruta correcta si ejecutas en tu PC

# Leer el archivo y extraer la columna de voltaje
voltages = []

with open(file_path, "r") as file:
    for line in file:
        values = line.strip().split()  # Suponiendo que
        if len(values) == 2:  # Asegurar que hay dos columnas (tiempo y voltaje)
            try:
                voltage = float(values[1])  # Segunda columna es voltaje
                voltages.append(voltage)
            except ValueError:
                continue  # Ignorar tos

# Calcular la media y la de
if voltages:
    media = np.mean(voltages)
    desviacion = np.std(voltages)
    print(f"Media del voltaje: {media:.5f} V")
    print(f"Desviacion estandar: {desviacion:.5f} V")
else:
    print("No se encontraron datos de voltaje en el archivo.")
