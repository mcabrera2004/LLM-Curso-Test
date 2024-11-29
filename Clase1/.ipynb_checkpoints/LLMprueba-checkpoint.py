import openai
from openai import OpenAI

openai.api_key = ""

system_response = '''Hacé de cuenta que sos un profesor de historia
                encargado de mantener una conversación formal con el que
                te pregunta. Responde en 25 palabras o menos.'''

def obtener_respuesta(mensajes):
    response = openai.chat.completions.create(
        model="gpt-4o", 
        messages=mensajes,
        max_tokens = 100
    )
    respuesta = response.choices[0].message.content
    return respuesta

mensajes = [{"role": "system", "content": system_response}]

while True:
    mensaje = input("Usuario: ")
    mensajes.append({"role": "user", "content": mensaje})
    if mensaje == "-1":
        break
    respuesta_ia = obtener_respuesta(mensajes)
    print("Bot:", respuesta_ia)
    mensajes.append({"role": "assistant", "content": respuesta_ia})