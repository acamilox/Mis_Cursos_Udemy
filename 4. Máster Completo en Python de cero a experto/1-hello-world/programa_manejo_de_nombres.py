# programa_manejo_de_nombres.py

def formatea(nombre):
  """
  Esta función toma un nombre y lo transforma.
  Es importante que ninguna otra variable se llame 'formatea'.
  """
  # La variable para el resultado se llama 'resultado_transformado', un nombre único.
  resultado_transformado = f"{nombre[1].upper()}.{nombre[-2:]}"
  return resultado_transformado

# --- Programa Principal ---

# 1. Definir los nombres originales.
nombre1 = "Andrea"
nombre2 = "Maria"
nombre3 = "Pepe"

# 2. Usar la función 'formatea()' para procesar cada nombre.
# Las variables para guardar los resultados tienen nombres distintos a la función.
nuevo_nombre1 = formatea(nombre1)
nuevo_nombre2 = formatea(nombre2)
nuevo_nombre3 = formatea(nombre3)

# 3. Unir los resultados en la variable final que espera el evaluador.
resultado_nombres = f"{nuevo_nombre1}_{nuevo_nombre2}_{nuevo_nombre3}"

# 4. Mostrar el resultado.
print(resultado_nombres)