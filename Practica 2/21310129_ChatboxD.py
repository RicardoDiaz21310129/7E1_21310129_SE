"""
Sistemas Expertos
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Edwin Ricardo Diaz Valenzuela
Registro: 21310129
Grupo: 7E1
"""

from flask import Flask, request, render_template

app = Flask(__name__)

# Respuestas precargadas
responses = {
    "Hola": "Que rollito primavera",
    "¿Cual linea de lol es mejor y por que TOP?": "Puro fokin top",
    "¿Cuales son tus mains": "Puro fokin Darius, Renekton y Yasuo. ¿main Yasuo?, q gay",
    "Juegas mid?": "Si, soy main Ahri y Orianna",
}

# Base de datos para almacenar nuevos conocimientos
knowledge_base = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = responses.get(user_input)

    if response is None:
        response = "Todo eso te lo dijo el arbol mi amor?"
        # Pregunta para agregar conocimiento nuevo
        knowledge_base.append(user_input)  # Aquí se almacena el nuevo conocimiento

    return response

if __name__ == '__main__':
    app.run(debug=True)
