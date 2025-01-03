from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

api_key = "AIzaSyCBZcIFlUoHfcOObHHYVzcizN2X7GPyYgE"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
MASTER_PROMPT = "generate a summary"

@app.route("/generate", methods=["POST"])
def generate():
    try:
        message = request.form.get("message", "")
        file = request.files.get("file")
        input_text = message if message else MASTER_PROMPT
        
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            print(f"File saved to: {file_path}")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    file_content = f.read()
            except UnicodeDecodeError:
                with open(file_path, "r", encoding="latin-1") as f:
                    file_content = f.read()

            input_text = f"{file_content} User Query: {message}" if message else f"{file_content} {MASTER_PROMPT}"
        
        try:
            response = model.generate_content(input_text)
            return jsonify({"response": response.text})
        except Exception as model_error:
            print(f"Model generation error: {model_error}")
            return jsonify({"error": str(model_error)}), 500

    except Exception as e:
        print(f"Unhandled exception: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
