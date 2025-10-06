from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(difficulty):
    if difficulty == 'easy':
        characters = string.ascii_lowercase
        length = 8
    elif difficulty == 'medium':
        characters = string.ascii_letters + string.digits
        length = 12
    else:
        characters = string.ascii_letters + string.digits + '!@#$%^&*№'
        length = 16

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    difficulty = request.form.get('difficulty', 'medium')
    password = generate_password(difficulty)
    return render_template('index.html', password=password, selected_difficulty=difficulty)

if __name__ == '__main__':
    app.run(debug=True)