import google.generativeai as genai
api_key = "AIzaSyCBZcIFlUoHfcOObHHYVzcizN2X7GPyYgE" 
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)