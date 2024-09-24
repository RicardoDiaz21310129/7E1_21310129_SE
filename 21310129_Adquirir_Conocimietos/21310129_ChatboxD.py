"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
"""

import json
import os


class Chatbot:
    def __init__(self):
        self.database = self.load_database()

    def load_database(self):
        if os.path.exists('database.json'):
            with open('database.json', 'r') as file:
                return json.load(file)
        else:
            return {
                "Hola": "Que rollito primavera",
                "¿Cual linea de lol es mejor y por que TOP?": "Puro fokin top",
                "¿Cuales son tus mains": "Puro fokin Darius, Renekton y Yasuo. ¿main Yasuo?, q gay",
                "Juegas mid?": "Si, soy main Ahri y Orianna",
            }

    def save_database(self):
        with open('database.json', 'w') as file:
            json.dump(self.database, file)

    def get_response(self, user_input):
        response = self.database.get(user_input.lower())

        if response:
            return response
        else:
            return self.ask_for_new_knowledge(user_input)

    def ask_for_new_knowledge(self, user_input):
        new_response = input(f"No tengo una respuesta para: '{user_input}'. ¿Cuál debería ser la respuesta? ")
        self.database[user_input.lower()] = new_response
        self.save_database()
        return f"Gracias, he aprendido algo nuevo: '{user_input}' significa '{new_response}'."


def main():
    print("puro fokin chatbox")
    chatbot = Chatbot()

    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "exit"]:
            print("¡Hasta luego!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
