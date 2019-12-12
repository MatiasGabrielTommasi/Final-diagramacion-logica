import Recursos.Utilidades
import Recursos.Preguntas

ListadoPreguntas = Recursos.Preguntas.preguntas
preguntaActual = ListadoPreguntas[0]
preguntaSeleccionada = 0
opciones = Recursos.Utilidades.BuscarHijos(ListadoPreguntas, preguntaActual["index"])
Recursos.Utilidades.MostrarOpciones(preguntaActual)
respuesta = input("ingresa su respuesta: ")

while True:
	while Recursos.Utilidades.ValidarEntrada(respuesta) != True:
		respuesta = input("ingresa una respuesta válida: ")

	if Recursos.Utilidades.ValidarEntrada(respuesta):
		preguntaSeleccionada = ListadoPreguntas[int(respuesta)]

		while preguntaSeleccionada not in opciones:
			respuesta = input("ingresa una respuesta válida: ")
			if Recursos.Utilidades.ValidarEntrada(respuesta):
				preguntaSeleccionada = ListadoPreguntas[int(respuesta)]
				
	preguntaActual = Recursos.Utilidades.BuscarHijos(ListadoPreguntas, int(preguntaSeleccionada["index"]))[0]
	opciones = Recursos.Utilidades.BuscarHijos(ListadoPreguntas, int(preguntaActual["index"]))
	Recursos.Utilidades.MostrarOpciones(preguntaActual)	
	if len(opciones) == 0:
		break
	respuesta = input("ingresa su respuesta: ")
print("fin del juego")