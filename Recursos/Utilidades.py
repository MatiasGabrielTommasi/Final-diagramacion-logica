import Recursos.Preguntas

def ValidarEntrada(input):
	if len(input) == 0 or input.isdigit() == False:
		return False
	else:
		if int(input) == 0:
			return False
		else:
			return True

def BuscarHijos(lista, index):
	hijos = []
	for item in lista:
		if item["indexPadre"] == index:
			hijos.append(item)
	return hijos

def MostrarOpciones(pregunta):
	print('')
	print('')
	print('')
	print(pregunta["pregunta"])
	print('')
	opciones = BuscarHijos(Recursos.Preguntas.preguntas, pregunta["index"])
	for item in opciones:
		print(str(item["index"]) + ' ' + item["pregunta"])
		print('')