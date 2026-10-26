from tkinter import*
import random

preguntas_disponibles=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def siguiente_pregunta():
	global correcta, preguntas_disponibles

	numero = random.choice(preguntas_disponibles)
	preguntas_disponibles.remove(numero)
	
	if numero == 1:
		pregunta.config(text="¿Qué fase ocurre cuando la Luna está entre la Tierra y el Sol?")
		correcta="Luna Nueva"

	elif numero == 2:
		pregunta.config(text="¿Qué fase viene justo después de la Luna Nueva?")
		correcta="Luna Creciente"

	elif numero == 3:
		pregunta.config(text="Cómo se llama cuando vemos exactamente la mitad derecha iluminada?")
		correcta="Cuarto Creciente"

	elif numero == 4:
		pregunta.config(text="¿Qué fase muestra casi toda la superficie iluminada antes de llenarse?")
		correcta="Gibosa Creciente"

	elif numero == 5:
		pregunta.config(text="¿En qué fase la Tierra está entre el Sol y la Luna?")
		correcta="Luna Llena"

	elif numero == 6:
		pregunta.config(text="¿Qué fase viene decreciendo justo después de la Luna Llena?")
		correcta="Gibosa Menguante"

	elif numero == 7:
		pregunta.config(text="¿Cómo se llama cuando vemos exactamente la mitad izquierda iluminada?")
		correcta="Cuarto Menguante"

	elif numero == 8:
		pregunta.config(text="¿Qué fase es la última antes de volver a empezar el ciclo?")
		correcta="Luna Menguante"

	elif numero == 9:
		pregunta.config(text="¿Cuánto tarda aproximadamente el ciclo lunar completo?")
		correcta="29 Dias"

	elif numero == 10:
		pregunta.config(text="¿La Luna emite su propia luz?")
		correcta="No, refleja la luz del sol"

def iniciar_juego():
    frame_inicio.pack_forget()
    frame1.pack(pady=10, fill="both", expand=True)
    frame2.pack(pady=10, fill="both", expand=True)
    siguiente_pregunta()

def reiniciar_juego():
    global puntaje, numero_pregunta, preguntas_disponibles

    puntaje = 0
    numero_pregunta = 0
    preguntas_disponibles = list(range(1,11))

    frame_final.pack_forget()

    for b in botones:
        b.config(state=NORMAL, bg="white")

    contador.config(text="Pregunta 1 de 10")
    resultado.config(text="")

    frame1.pack(pady=10, fill="both", expand=True)
    frame2.pack(pady=10, fill="both", expand=True)

    siguiente_pregunta()

def comprobar(boton):
	global puntaje, numero_pregunta

	respuesta=boton.cget("text")

	if respuesta == correcta:
		resultado.config(text="CORRECTO", fg="green", font=("arial", 20, "bold"))
		puntaje += 1
		boton.config(bg="gray", state=DISABLED)

	else:
		resultado.config(text="INCORRECTO", fg="red", font=("arial", 20, "bold"))

	numero_pregunta += 1

	if numero_pregunta < 10:
		contador.config(text=f"Pregunta {numero_pregunta + 1} de 10")
		siguiente_pregunta() 

	else:
		frame1.pack_forget()
		frame2.pack_forget()

		puntaje_final.config(text=f"puntaje: {puntaje} de 10")

		frame_final.pack(fill="both", expand=True)

puntaje = 0
numero_pregunta = 0

base=Tk()
base.geometry ("500x880")

frame_inicio = Frame(base)
frame_inicio.config(bg="dark violet", width=500, height=880)
frame_inicio.pack(fill="both", expand=True)

titulo_inicio = Label(frame_inicio)
titulo_inicio.config(text="CUESTIONARIO LUNAR", font=("arial", 30, "bold"), bg="dark violet", fg="white")
titulo_inicio.pack(pady=100)

boton_inicio = Button(frame_inicio, text="COMENZAR", width=20, font=("arial", 15), command=iniciar_juego)
boton_inicio.pack(pady=30)

frame_final = Frame(base)
frame_final.config(bg="dark violet", width=500, height=880)
frame_final.pack_forget()

titulo_final = Label(frame_final)
titulo_final.config(text="¡JUEGO TERMINADO!", font=("arial", 25, "bold"), bg="dark violet", fg="white")
titulo_final.pack(pady=100)

puntaje_final = Label(frame_final)
puntaje_final.config(text="", font=("arial", 20), bg="dark violet", fg="white")
puntaje_final.pack(pady=30)
boton_reintentar = Button(frame_final, text="INTENTAR OTRA VEZ", width=20, font=("arial", 15), command=reiniciar_juego)
boton_reintentar.pack(pady=30)

frame1= Frame (base)
frame1.config (bg="dark violet", width="500", height="150")
frame1.pack(pady = 5, fill="both", expand= "true")
frame1.pack_forget()

titulo1= Label (frame1)
titulo1.config (text="CUESTIONARIO LUNAR", font= ("arial", 15), bg="dark violet")
titulo1.pack (pady = 25)

contador= Label (frame1)
contador.config (text="Preguntas 1 de 10", font= ("arial", 15), bg="dark violet")
contador.pack (pady = 25)

pregunta= Label (frame1)
pregunta.config (text=" ", font= ("arial", 15), bg="dark violet")
pregunta.pack (pady = 25)

resultado = Label(frame1)
resultado.config(text="", font=("arial", 15), bg="dark violet")
resultado.pack(pady=10)

frame2= Frame (base)
frame2.config (bg="purple", width="500", height="220")
frame2.pack(pady = 10, fill="both", expand= "true")
frame2.pack_forget()

respuestas = [
	"Luna Nueva","Luna Creciente", "Cuarto Creciente","Gibosa Creciente","Luna Llena", "Gibosa Menguante","Cuarto Menguante","Luna Menguante", "29 Dias","No, refleja la luz del sol"]

botones= []

for texto in respuestas:
	btn = Button(frame2, text=texto, width="25", font= ("arial", 11), bg="white")
	btn.config(command=lambda b=btn: comprobar(b))
	btn.pack(pady=2)
	botones.append(btn)


base.mainloop ()