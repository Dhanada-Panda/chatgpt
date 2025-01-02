from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
api_key = "AIzaSyCBZcIFlUoHfcOObHHYVzcizN2X7GPyYgE" 
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/generate', methods=['POST'])
def generate():
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = model.generate_content(user_message)
        return jsonify({'response': response.text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
