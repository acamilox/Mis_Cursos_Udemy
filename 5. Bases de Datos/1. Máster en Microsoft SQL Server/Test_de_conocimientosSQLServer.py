import tkinter as tk
from tkinter import messagebox
import time

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuestionario Avanzado de Microsoft SQL Server")
        self.root.geometry("600x500")

        self.preguntas = [
            {
                "pregunta": "¿Cuántos registros o filas puede tener una tabla?",
                "opciones": ["Solo 1", "Ninguno o muchos", "No existen registros", "Las tablas vienen por defecto con datos almacenados"],
                "respuesta": "Ninguno o muchos"
            },
            {
                "pregunta": "¿Una Tabla puede tener más de un campo como Primary Key?",
                "opciones": ["No, solo puede tener uno", "Sí, puede tener varios campos como Primary Key", "Una tabla no debe tener Primary Key", "Ninguna de las anteriores"],
                "respuesta": "Sí, puede tener varios campos como Primary Key"
            },
            {
                "pregunta": "La Primera Forma Normal, ¿Permite repeticiones de datos en las tablas?",
                "opciones": ["Sí, puedo repetir datos sin problemas", "No, la primera forma normal no permite repeticiones de datos en múltiples registros", "No existe", "No es necesario"],
                "respuesta": "No, la primera forma normal no permite repeticiones de datos en múltiples registros"
            },
            {
                "pregunta": "¿El tipo de dato VARCHAR a que grupo pertenece?",
                "opciones": ["Numéricos", "Fecha y Hora", "Alfanumérico", "Booleano"],
                "respuesta": "Alfanumérico"
            },
            {
                "pregunta": "¿Qué comando se utiliza para seleccionar datos de una tabla en SQL?",
                "opciones": ["SELECT", "INSERT", "UPDATE", "DELETE"],
                "respuesta": "SELECT"
            },
            {
                "pregunta": "¿Cuál es la función de la cláusula WHERE en SQL?",
                "opciones": ["Ordenar los resultados", "Filtrar registros", "Agrupar datos", "Unir tablas"],
                "respuesta": "Filtrar registros"
            },
            {
                "pregunta": "¿Qué comando se utiliza para agregar una nueva fila a una tabla en SQL?",
                "opciones": ["ADD", "INSERT INTO", "UPDATE", "CREATE"],
                "respuesta": "INSERT INTO"
            },
            {
                "pregunta": "¿Qué tipo de dato se utiliza para almacenar valores de fecha y hora en SQL Server?",
                "opciones": ["DATETIME", "VARCHAR", "INT", "FLOAT"],
                "respuesta": "DATETIME"
            },
            {
                "pregunta": "¿Cuál es la función de la cláusula GROUP BY en SQL?",
                "opciones": ["Ordenar los resultados", "Filtrar registros", "Agrupar datos", "Unir tablas"],
                "respuesta": "Agrupar datos"
            },
            {
                "pregunta": "¿Qué comando se utiliza para eliminar una tabla en SQL?",
                "opciones": ["DROP TABLE", "DELETE TABLE", "REMOVE TABLE", "ERASE TABLE"],
                "respuesta": "DROP TABLE"
            },
            {
                "pregunta": "¿Qué tipo de JOIN devuelve todos los registros cuando hay una coincidencia en cualquiera de las tablas?",
                "opciones": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"],
                "respuesta": "FULL JOIN"
            },
            {
                "pregunta": "¿Qué comando se utiliza para modificar datos existentes en una tabla?",
                "opciones": ["ALTER", "UPDATE", "MODIFY", "CHANGE"],
                "respuesta": "UPDATE"
            },
            {
                "pregunta": "¿Qué comando se utiliza para crear una nueva base de datos en SQL Server?",
                "opciones": ["CREATE DATABASE", "NEW DATABASE", "ADD DATABASE", "MAKE DATABASE"],
                "respuesta": "CREATE DATABASE"
            },
            {
                "pregunta": "¿Qué comando se utiliza para eliminar una base de datos en SQL Server?",
                "opciones": ["DELETE DATABASE", "DROP DATABASE", "REMOVE DATABASE", "ERASE DATABASE"],
                "respuesta": "DROP DATABASE"
            },
            {
                "pregunta": "¿Qué es una Vista?",
                "opciones": ["Es una sentencia SELECT específica almacenada en la Base de Datos", "Es una variable", "Es una función", "Ninguna de las anteriores"],
                "respuesta": "Es una sentencia SELECT específica almacenada en la Base de Datos"
            },
            {
                "pregunta": "¿Qué hace la cláusula INNER JOIN?",
                "opciones": ["Conecta dos o más tablas por determinados campos", "Conecta una tabla con un Stored Procedure", "Conecta una tabla con una función", "Ninguna de las anteriores"],
                "respuesta": "Conecta dos o más tablas por determinados campos"
            },
            {
                "pregunta": "La tabla temporal en memoria:",
                "opciones": ["Se elimina cuando finaliza el Script", "Se elimina cuando se reinicia el motor de SQL Server", "Nunca se elimina", "No existe"],
                "respuesta": "Se elimina cuando finaliza el Script"
            },
            {
                "pregunta": "La tabla temporal física:",
                "opciones": ["Sigue existiendo hasta que se reinicia el motor de SQL Server", "Cuando termina el Script desaparece", "Nunca desaparece", "Ninguna de las anteriores"],
                "respuesta": "Sigue existiendo hasta que se reinicia el motor de SQL Server"
            },
            {
                "pregunta": "¿Qué puede retornar una función?",
                "opciones": ["Resultados de tipo tabla o valores escalares, es decir cualquier tipo de dato", "No devuelven nada", "Solo devuelven valores VARCHAR", "Ninguna de las anteriores"],
                "respuesta": "Resultados de tipo tabla o valores escalares, es decir cualquier tipo de dato"
            }
        ]

        self.puntuacion = 0
        self.aciertos = 0
        self.errores = 0
        self.indice_pregunta_actual = 0
        self.tiempo_inicio = time.time()

        self.label_pregunta = tk.Label(root, text="", wraplength=550, font=("Arial", 14))
        self.label_pregunta.pack(pady=20)

        self.botones_opciones = []
        for i in range(4):
            boton = tk.Button(root, text="", width=50, command=lambda i=i: self.verificar_respuesta(i), font=("Arial", 10))
            boton.pack(pady=5)
            self.botones_opciones.append(boton)

        self.boton_siguiente = tk.Button(root, text="Siguiente", width=20, command=self.siguiente_pregunta, font=("Arial", 12))
        self.boton_siguiente.pack(pady=20)

        self.label_tiempo = tk.Label(root, text="Tiempo: 0 segundos", font=("Arial", 12))
        self.label_tiempo.pack(pady=10)

        self.label_puntuacion = tk.Label(root, text="Puntuación: 0", font=("Arial", 12))
        self.label_puntuacion.pack(pady=10)

        self.boton_reiniciar = tk.Button(root, text="Reiniciar", width=20, command=self.reiniciar_cuestionario, font=("Arial", 12))
        self.boton_reiniciar.pack(pady=10)

        self.actualizar_tiempo()
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        pregunta_actual = self.preguntas[self.indice_pregunta_actual]
        self.label_pregunta.config(text=pregunta_actual["pregunta"])

        for i, opcion in enumerate(pregunta_actual["opciones"]):
            self.botones_opciones[i].config(text=opcion, state=tk.NORMAL)

    def verificar_respuesta(self, indice_opcion):
        pregunta_actual = self.preguntas[self.indice_pregunta_actual]
        respuesta_usuario = pregunta_actual["opciones"][indice_opcion]

        if respuesta_usuario == pregunta_actual["respuesta"]:
            self.puntuacion += 1
            self.aciertos += 1
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        else:
            self.errores += 1
            messagebox.showerror("Incorrecto", f"Respuesta incorrecta. La correcta es: {pregunta_actual['respuesta']}")

        self.label_puntuacion.config(text=f"Puntuación: {self.puntuacion}")

        for boton in self.botones_opciones:
            boton.config(state=tk.DISABLED)

    def siguiente_pregunta(self):
        self.indice_pregunta_actual += 1

        if self.indice_pregunta_actual < len(self.preguntas):
            self.mostrar_pregunta()
        else:
            tiempo_total = int(time.time() - self.tiempo_inicio)
            messagebox.showinfo("Fin del cuestionario", 
                              f"Has terminado el cuestionario.\nPuntuación: {self.puntuacion}/{len(self.preguntas)}\nAciertos: {self.aciertos}\nErrores: {self.errores}\nTiempo: {tiempo_total} segundos")
            self.root.quit()

    def actualizar_tiempo(self):
        tiempo_transcurrido = int(time.time() - self.tiempo_inicio)
        self.label_tiempo.config(text=f"Tiempo: {tiempo_transcurrido} segundos")
        self.root.after(1000, self.actualizar_tiempo)

    def reiniciar_cuestionario(self):
        self.puntuacion = 0
        self.aciertos = 0
        self.errores = 0
        self.indice_pregunta_actual = 0
        self.tiempo_inicio = time.time()
        self.label_puntuacion.config(text="Puntuación: 0")
        self.mostrar_pregunta()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()