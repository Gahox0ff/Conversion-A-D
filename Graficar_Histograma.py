# Intentar leer el archivo directamente y extraer los datos para graficar el histograma
import matplotlib.pyplot as plt
# Ruta del archivo
ruta_archivo = "HISTOGRAMA_0V.txt"

# Listas para almacenar los valores
valores_adc = []
frecuencias = []

# Leer el archivo y extraer datos
with open(ruta_archivo, "r") as archivo:
    next(archivo)  # Saltar la primera línea (encabezado)
    for linea in archivo:
        datos = linea.strip().split()  # Separar valores por espacios o tabulación
        if len(datos) == 2:
            try:
                valores_adc.append(int(datos[0]))  # Primera columna: Valor ADC
                frecuencias.append(int(datos[1]))  # Segunda columna: Frecuencia
            except ValueError:
                pass  # Ignorar líneas con errores

# Graficar el histograma
plt.figure(figsize=(10, 6))
plt.bar(valores_adc, frecuencias, color='b', alpha=0.7, edgecolor='black')
plt.xlabel("Valor ADC (12 bits)")
plt.ylabel("Frecuencia")
plt.title("Histograma de valores ADC (0V)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
