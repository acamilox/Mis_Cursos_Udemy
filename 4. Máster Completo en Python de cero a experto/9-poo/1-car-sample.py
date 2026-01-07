# =================================================================
#               SCRIPT DE DEMOSTRACIÓN DE OBJETOS 'CAR'
# =================================================================

# --- 1. Importaciones: Preparando las "plantillas" o clases ---
# Para poder construir un "Carro", primero necesitamos importar su plano (la clase Car).
# Hacemos lo mismo para sus componentes: el Motor (Engine) y el Tanque de Combustible (FuelTank).
# También importamos EngineType, que seguramente define los tipos de motor (GASOLINE, DIESEL, etc.).

from andres.poo.car.car import Car
from andres.poo.car.engine import Engine, EngineType
from andres.poo.car.fuel_tank import FuelTank


# --- 2. Creación del primer carro: El Subaru (paso a paso) ---

# Creamos una 'instancia' u 'objeto' de la clase Car.
# Es como construir un carro real a partir del plano. Le damos la marca 'Subaru' al crearlo.
car = Car('Subaru')

# Ahora, usamos métodos 'setter' para configurar las propiedades del carro una por una.
car.set_color('Gris')       # Le asignamos el color 'Gris'.
car.set_model('Impreza')    # Le asignamos el modelo 'Impreza'.

# --- Composición: Un objeto que contiene otros objetos ---
# Creamos un objeto Engine (motor de 1.5L a gasolina) y se lo "instalamos" a nuestro carro.
# El carro 'tiene un' motor. Este concepto clave se llama Composición.
car.engine = Engine(1.5, EngineType.GASOLINE)

# También podemos modificar un 'atributo' (una variable del objeto) directamente.
car.model = 'Impreza Modificado'

# Hacemos lo mismo con el tanque de combustible: creamos uno de 30L y se lo asignamos al carro.
car.fuel_tank = FuelTank(30)


# --- 3. Interactuando con el Subaru ---

# Usamos un método 'getter' para obtener el valor de un atributo y mostrarlo en pantalla.
print("Color del primer carro:", car.get_color())

# Llamamos a un método que nos da un resumen completo de los detalles del carro.
print("Detalles del Subaru:", car.details())

# Podemos acceder a los atributos de los objetos que están DENTRO de nuestro carro.
# Aquí accedemos al atributo 'cylinder' del objeto 'engine' que está en 'car'.
print("Cilindraje del Subaru:", car.engine.cylinder)

# Llamamos a un método que simula una acción compleja.
print("Acción del Subaru:", car.accelerate_and_brake(4000, 120))


# ==================================================================
#                 CREACIÓN DE UN SEGUNDO CARRO
# ==================================================================

# --- 4. Creación del segundo carro: El Mazda (forma directa) ---

# Aquí creamos otro carro, pero pasamos casi todos los datos directamente
# al momento de la creación (en el 'constructor'). Es una forma más rápida y común.
# Le pasamos marca, modelo, color y hasta un objeto Engine nuevo.
mazda = Car('Mazda', '3', 'Blanco', Engine(2.0, EngineType.GASOLINE))

# Aún después de crearlo, podemos modificar los atributos de sus componentes.
mazda.engine.cylinder = 3.0


# --- 5. Interactuando con el Mazda y métodos especiales ---

print("\nDetalles del Mazda:", mazda.details())
print("Cilindraje del Mazda:", mazda.engine.cylinder)

# --- Métodos especiales __str__ y __repr__ ---

# Al hacer 'print()' sobre un objeto, Python busca el método especial __str__.
# Este método debe devolver una representación "amigable" del objeto para el usuario.
print("\nImprimiendo el objeto 'car' con print() [usa __str__]:", car)

# La función repr() es diferente, busca el método especial __repr__.
# Este devuelve una representación "técnica" del objeto, útil para desarrolladores,
# que idealmente podría usarse para recrear el objeto.
print("Representación técnica de 'car' con repr() [usa __repr__]:", repr(car))


# --- 6. Más acciones y cálculos con el Mazda ---

# Llamamos a métodos que simulan acciones sencillas del carro.
print("\nAcción del Mazda:", mazda.accelerate(3000, 100))
print("Acción del Mazda:", mazda.brake())

# Usamos un método para realizar un cálculo basado en parámetros de entrada.
# Aquí calculamos el consumo de combustible (kilómetros recorridos / litros consumidos).
print(f'Cálculo de consumo 1: {mazda.calculate_consumption(300, 60)} km/l')
print(f'Cálculo de consumo 2: {mazda.calculate_consumption(300, 0.60)} km/l')