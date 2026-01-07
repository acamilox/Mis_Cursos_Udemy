# =================================================================
#    SCRIPT DE DEMOSTRACIÓN DE MÉTODOS Y ATRIBUTOS DE CLASE
# =================================================================

# --- 1. Importaciones ---
# Importamos las clases necesarias como en el script anterior.
from andres.poo.car.car import Car
from andres.poo.car.engine import EngineType, Engine
from andres.poo.car.fuel_tank import FuelTank


# --- 2. Interactuando con la Clase 'Car' directamente ---

# Esto es un MÉTODO DE CLASE. Se llama sobre 'Car', no sobre un objeto como 'car'.
# Establece un 'ATRIBUTO DE CLASE', una propiedad compartida por TODOS los carros.
# Aquí, definimos que el color de la matrícula para todos los carros será morado.
# 'Car.COLOR_PURPLE' es una constante definida dentro de la clase Car.
Car.set_license_plate_color(Car.COLOR_PURPLE)


# --- 3. "Métodos de Fábrica" - Diferentes maneras de construir un Carro ---
# A continuación, usamos varios métodos de clase que actúan como "constructores alternativos".
# Cada uno nos da una forma rápida de crear un carro con una configuración específica.

print("--- Creando carros con Métodos de Fábrica ---")

# .empty(): Crea un carro completamente vacío, sin ninguna propiedad definida.
car = Car.empty()
print("1. Carro vacío:", car)

# .basic(): Crea un carro con solo la información esencial: marca y modelo.
car1 = Car.basic('Mazda', '3')
print("2. Carro básico:", car1)

# .with_color(): Crea un carro con marca, modelo y color.
car2 = Car.with_color('Citroen', 'C3', Car.COLOR_GRAY)
print("3. Carro con color:", car2)

# .with_cylinder(): Crea un carro que además incluye un motor (Engine).
car3 = Car.with_cylinder('Subaru', 'Legacy', Car.COLOR_RED, Engine(1.80, EngineType.DIESEL))
print("4. Carro con motor:", car3)

# .full_spec(): Crea un carro completo con todas las especificaciones posibles.
car4 = Car.full_spec('Mazda', 'BT-50', Car.COLOR_WHITE, Engine(3.00, EngineType.DIESEL), FuelTank(50))
print("5. Carro full especificaciones:", car4)

# También podemos tener métodos de fábrica para combinaciones específicas.
# .only_tank(): Crea un carro con marca, modelo y tanque de combustible.
car5 = Car.only_tank('Subaru', 'Impreza', FuelTank(50))
print("6. Carro solo con tanque:", car5)

# .only_color(): Crea un carro con marca y color.
car6 = Car.only_color('Subaru', Car.COLOR_BLACK)
print("7. Carro solo con color:", car6)


# --- 4. Accediendo a los Atributos de la Clase ---

print("\n--- Accediendo a información de la Clase ---")

# Usamos otro método de clase para LEER el atributo de clase que establecimos al inicio.
# Debería imprimir 'Purple' o el valor correspondiente.
print("El color de matrícula para todos los carros es:", Car.get_license_plate_color())

# Los atributos de clase también pueden ser constantes, como límites de velocidad.
# Se pueden acceder directamente desde la clase, sin necesidad de crear un objeto.
speed_max_highway = Car.MAX_SPEED_HIGHWAY
print("La velocidad máxima en autopista (leída en una variable) es:", speed_max_highway)
print("La velocidad máxima en autopista (leída directamente) es:", Car.MAX_SPEED_HIGHWAY)