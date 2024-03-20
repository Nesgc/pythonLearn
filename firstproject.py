# No es posible ejecutar código interactivo que solicite entrada del usuario directamente aquí.
# Sin embargo, puedo proporcionarte un esquema completo del código que puedes ejecutar en tu entorno local.

# Este es el esquema del código que cumple con las consignas del proyecto:

def analizar_texto():
    # Solicitar texto al usuario
    texto = input("Por favor, ingresa un texto: ")
    # Solicitar tres letras
    letras = input("Ingresa tres letras separadas por espacio (ejemplo: a b c): ").split()

    # Convertir el texto a minúsculas para la búsqueda insensible a mayúsculas/minúsculas
    texto_min = texto.lower()

    # 1. Contar cuántas veces aparece cada letra
    frecuencias = {letra.lower(): texto_min.count(letra.lower()) for letra in letras}

    # 2. Contar cuántas palabras hay en el texto
    num_palabras = len(texto.split())

    # 3. Encontrar la primera y la última letra del texto (ignorando espacios)
    texto_sin_espacios = texto.replace(" ", "")
    primera_letra = texto_sin_espacios[0]
    ultima_letra = texto_sin_espacios[-1]

    # 4. Invertir el orden de las palabras del texto
    palabras_invertidas = " ".join(texto.split()[::-1])

    # 5. Verificar si la palabra "Python" está en el texto (insensible a mayúsculas/minúsculas)
    contiene_python = "python" in texto_min

    # Imprimir resultados
    print("\nResultados del análisis de texto:")
    for letra, frecuencia in frecuencias.items():
        print(f"La letra '{letra}' aparece {frecuencia} veces.")
    print(f"El texto contiene {num_palabras} palabras.")
    print(f"La primera letra del texto es '{primera_letra}' y la última letra es '{ultima_letra}'.")
    print(f"El texto con el orden de las palabras invertido es: {palabras_invertidas}")
    print(f"¿El texto contiene la palabra 'Python'? {'Sí' if contiene_python else 'No'}")

# Debido a la naturaleza interactiva, este código necesita ser ejecutado en un entorno Python local.
# Simplemente copia y pega el código en tu editor de Python y ejecútalo para probar su funcionamiento.

# analizar_texto() # Descomenta esta línea para ejecutar la función cuando corras el código localmente.
analizar_texto()