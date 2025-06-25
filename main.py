from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

def generate_random_string():
    """Generate a 20-character random key with letters and numbers"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(20))

@app.route('/')
def index():
    """Main page with the generator interface"""
    return render_template('index.html')

@app.route('/generate')
def generate():
    """API endpoint to generate a new random string"""
    random_string = generate_random_string()
    return jsonify({'random_string': random_string})

