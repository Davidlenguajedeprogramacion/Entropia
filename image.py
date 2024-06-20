import math
from collections import Counter

def calcular_entropia(frecuencia, total_caracteres):
    if frecuencia == 0:
        return 0
    probabilidad = frecuencia / total_caracteres
    return -probabilidad * math.log2(probabilidad)

def calcular_entropias(texto):
    total_caracteres = len(texto)
    frecuencias = Counter(texto)
    
    entropias = {char: calcular_entropia(frec, total_caracteres) for char, frec in frecuencias.items()}
    return entropias

def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def escribir_entropias(entropias, ruta):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        for char, entropia in sorted(entropias.items()):
            archivo.write(f'{char}: {entropia:.6f}\n')

def main():
    ruta_entrada = 'cancion.txt'
    ruta_salida = 'entropias.txt'
    
    texto = leer_archivo(ruta_entrada)
    texto = ''.join(filter(str.isalpha, texto.lower()))  # Filtrar solo letras y convertir a minúsculas
    entropias = calcular_entropias(texto)
    escribir_entropias(entropias, ruta_salida)

if __name__ == '__main__':
    main()
