import random

#Se crea una clase pregunta con el fin de que se pueda utilizar más adelante en una clase examen y se puedan mostrar las preguntas
"""
Falta doctstring y seguir las buenas prácticas que es escribir los tipos de datos
El resto está bien
"""
class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
    
    def verificar_respuesta(self, respuesta):
        return respuesta == self.respuesta_correcta

# Se crea una clase examen la cual tiene como finalidad tanto pedir el nombre del usuario como el de mostrar las preguntas, a su vez se verificará
#si on correctas o no
class Examen:
    def __init__(self, preguntas):
        """
        Bien, pero para su proyecto editen eso de modo que no se repitan las preguntas en los diferentes intentos
        """
        self.preguntas = preguntas
        self.preguntas_aleatorias = random.sample(preguntas, 10)
    
    def realizar_examen(self):
        """
        Esto no es tan relevante, no lo dejen aquí, esto en la parte del script de prueba está bien.
        """
        nombre = input("Ingresa tu nombre: ")
        print(f"\n¡Hola {nombre}! Bienvenido al examen de Programación\n")

        respuestas = []
        correctas = []
        incorrectas = []

        """
        Por el momento está bien aquí, pero consideren que en el proyecto la interfaz
        va a ser también una clase por lo que no van a llamar a los widgets desde aquí,
         de modo que deberán modificar esto para que obtegan los datos que necesitan y los muestren en la interfaz.
        """
        for i, pregunta in enumerate(self.preguntas_aleatorias):
            print(f"Pregunta {i+1}: {pregunta.enunciado}")
            for j, opcion in enumerate(pregunta.opciones):
                print(f"{j+1}. {opcion}")
            
            respuesta = input("Ingresa tu respuesta (1, 2 o 3): ")

            """
            No queremos que le muestre el resultado hasta que se haya concluido el examen.
            Aquí está muy simple que no se tiene que hacer una búsqueda de la pregunta para verificar
            la respuesta ya que la verfican desde ahora pero no, se debe verificar hasta el final
            """
            if pregunta.verificar_respuesta(respuesta):
                print("¡Correcto!")
                correctas.append(i+1)
            else:
                print("Incorrecto.")
                incorrectas.append(i+1)

        """
        Esto metando en otro método
        """
        #Se le da la calificación obtenida al usuario y las preguntas que tuvo correctas y las incorrectas
        print(f"\n{nombre}, has contestado correctamente {len(correctas)} preguntas y {len(incorrectas)} preguntas incorrectamente.")
        print(f"Tu calificación es: {(len(correctas)/10)*10}/10")

        print("\nLas preguntas respondidas correctamente fueron:")
        for pregunta_num in correctas:
            print(f"- Pregunta {pregunta_num}")
        
        print("\nLas preguntas respondidas incorrectamente fueron:")
        for pregunta_num in incorrectas:
            print(f"- Pregunta {pregunta_num}")
        
        print("\n¡Gracias por participar en el examen!")
#Se agregan las preguntas del examen        
pregunta1 = Pregunta("Es un paradigma de programación que utiliza objetos, que son instancias de clases, para representar datos y comportamiento\n" ,["programación orientada a objetos\n", "programar\n","objetos y clases\n"],"1")
pregunta2 = Pregunta("Descripción del conjunto de cadenas de símbolos que serán considerados programas válidos\n" , ["redacción\n", "codigo\n","sintaxis\n"],"3")
pregunta3 = Pregunta("método especial que se utiliza para inicializar un objeto cuando se crea def _init_(self):\n",["método constructor\n","método de acceso\n","método modificador\n"],"1") 
pregunta4 = Pregunta("Método que accesa al valor de un atributo def get_nombre_atributo(self):\n",["método constructor\n","método de acceso\n","método modificador\n"],"2") 
pregunta5 = Pregunta("Método que cambia el valor de un atributo def set_nombre(self, nuevo):\n",["método constructor\n","método de acceso\n","método modificador\n"],"3")
pregunta6 = Pregunta("Son las características de un intérprete excepto\n",["El programa fuente se traduce instrucción por instrucción.\n","No se guarda el resultado de esa traducción\n","se guarda el resultado de las traducciones\n"],"2")
pregunta7 = Pregunta("Son las características de un compilador excepto\n",["El programa fuente se traduce una vez\n","Se genera un archivo que se puede distribuir en otra computadora\n","El programa se traduce instrucción por instrucción\n"],"3")
pregunta8 = Pregunta("Es un modelo o plantilla para crear objetos\n",["sintaxis\n","clase\n","moldeador\n"],"2")
pregunta9 = Pregunta("Es una instancia de una clase\n",["objeto\n","resultado\n","modelo\n"],"1")
pregunta10 = Pregunta("¿Que caracteres no se permiten en los nombres de las variables?\n",["_ y -\n","MAYÚSCULAS\n ","@,$ y % ✨\n"],"3")
pregunta11 = Pregunta("Son los tipos de datos, excepto \n",["Enteros (int): -13, 19, 21...\n","Flotantes o decimales (float): 14.3, 4536.654, 4325.0,. \n","palabras (gtr): Hola, adios, Pyton \n"],"3")
pregunta12 = Pregunta("Sirven para ejecutar una secuencia especifica de instrucciones cuando se cumplen ciertas condiciones\n",["sintaxis\n"," B) estructuras condicionales\n ","funciones\n"],"2") 
pregunta13 = Pregunta("Se usa cuando sólo se quiere evaluar una condición\n",["if\n","else\n","elif\n"],"1")
pregunta14 = Pregunta("Se usa cuando se quiere poner una segunda condición\n",["if\n","else\n","elif\n"],"2") 
pregunta15 = Pregunta("Se ejecuta cuando las condicionales se evalúan cómo falsas\n",["if\n","else\n","elif\n"],"3")
pregunta16 = Pregunta("Estructura de ejecución repetida bajo una condición permite ejecutar una secuencia especifica de instrucciones tantas veces como se cumpla cierta condición\n",["while\n","continue\n","if\n"],"1")
pregunta17 = Pregunta("Proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa.\n",["continue\n","break\n","end\n"],"2")
pregunta18 = Pregunta("Omite la parte de un bucle en la que se activa una condición externa, pero continua para completar el resto del bucle.\n",["continue\n","break \n","end\n"],"1")
pregunta19 = Pregunta("Operador que toma tres operandos. ejemplo: mayor = a if a>b else b\n",["operador ternario \n","operador lógico\n","operador Booleano\n"],"1")
pregunta20 = Pregunta("Es para ejecutar un conjunto de declaraciones/operaciones, una vez para cada elemento de una lista, tupla, conjunto, etc.\n",["ciclo for \n","while\n","if \n"],"1")
pregunta21 = Pregunta("Son las ventajas de la programación orientada a objetos excepto\n",["Mantenimiento de un sistema más fácil\n","reparación de errores automática \n","reutilización de código (Herencia)\n"],"2")
pregunta22 = Pregunta("Es lo que define el comportamiento del objeto\n",["método \n","sintaxis\n","clase\n"],"1")
pregunta23 = Pregunta("Método para imprimir el estado del objeto\n",["método str \n","método de acceso\n","método modificador\n"],"3") 
pregunta24 = Pregunta("Son las características de un atributo privado, excepto\n",["deberá de empezar con dos guiones bajos\n","Solo será accedido dentro de la clase\n","Asegura que un elemento externo no pueda acceder a ese atributo\n"],"1")
pregunta25 = Pregunta("Representa la instancia de una clase\n",["self\n","objeto\n","métodos\n"],"2") 
pregunta26 = Pregunta("Proveen una funcionalidad definida y auto contenida, se constituyen usando patrones de diseño. Su característica principal es su alta cohesión y bajo acoplamiento\n",["funciones \n","bibliotecas \n","scripts\n "],"2")
pregunta27 = Pregunta("son las ventajas de una biblioteca excepto\n",["Evitar errores de codificación\n","Acelerar el proceso de desa\n","importar libros literarios\n"],"3")
pregunta28 = Pregunta("Son cosas que hace la biblioteca numpy excepto\n",["proporciona objetos de arreglos multidimensionales\n","manipulación matemática, de formas, clasificación, selección, etc.\n","números griegos\n"],"3")
pregunta29 = Pregunta("¿Cómo se importa la biblioteca numpy?\n",["import numpy as np\n","no sé necesita importar\n","class_numpy__\n"],"1")
pregunta30 = Pregunta("¿Que imprime este código?\ndef números (num:int) -> None: for i in range (1, num + 1): \n for j in range (1, i + 1):\n print (j, end="  ")\nprint ()\nnúmeros (9)\n",["1 2 3 4 5 6 7 8 9 10\n","1 2 3 4 5 6 7 8 9\n","1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n1 2 3 4 5 6\n1 2 3 4 5 6 7\n1 2 3 4 5 6 7 8\n1 2 3 4 5 6 7 8 9\n"],"1")

# Crear el examen y simularlo
examen = Examen([pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10,pregunta11,pregunta12,pregunta13,pregunta14,pregunta15,pregunta16,pregunta17,pregunta18,pregunta19,pregunta20,pregunta21,pregunta22,pregunta23,pregunta24,pregunta25,pregunta26,pregunta27,pregunta28,pregunta29,pregunta30])
examen.realizar_examen()






