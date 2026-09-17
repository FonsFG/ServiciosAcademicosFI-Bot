import re

def iniciar_chatbot():
    print("Chatbot: ¡Hola! Soy tu asistente de control escolar.")
    print("Puedes preguntarme sobre: inscripciones, horarios, pagos o biblioteca.")
    print("(Escribe 'salir' para terminar)\n")

    while True:
        entrada = input("Tú: ").lower()
        
        if "salir" in entrada:
            print("Chatbot: ¡Hasta luego! Que tengas un excelente día.")
            break
            
        elif re.search(r"\b(inscripción|inscripcion|inscribir|inscripciones)\b", entrada):
            print("Chatbot: Las inscripciones son del 10 al 15 de septiembre en ventanilla de control escolar.")
            
        elif re.search(r"\b(horario|horarios|clases)\b", entrada):
            print("Chatbot: Los horarios de clase están disponibles en tu portal de alumno en la sección académica.")
            
        elif re.search(r"\b(costo|pago|pagos|colegiatura)\b", entrada):
            print("Chatbot: Los pagos correspondientes deben realizarse en la caja de la facultad o mediante ficha bancaria.")
            
        elif re.search(r"\b(biblioteca|libros|prestamo)\b", entrada):
            print("Chatbot: La biblioteca abre de lunes a viernes de 8:00 AM a 7:00 PM con tu credencial vigente.")
            
        else:
            print("Chatbot: No tengo información sobre eso.")
            
        print("Chatbot: ¿Te puedo ayudar en otra cosa? (Recuerda que puedes preguntar por: inscripciones, horarios, pagos o biblioteca)\n")

if __name__ == "__main__":
    iniciar_chatbot()