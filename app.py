from flask import Flask, render_template, request
import openai
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# api_key =   # Replace with your actual API key
# # Replace with your actual API key
openai.api_key = api_key
model_name = 'gpt-3.5-turbo'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Retrieve form data
    prompt = request.form.get('prompt')
    language = request.form.get('language', 'Python')
    
    try:
        specific_prompt = f"Write a {language} function that {prompt}."
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "user", "content": specific_prompt}],
            max_tokens=200
        )
        generated_code = response['choices'][0]['message']['content']

        return render_template(
            'index.html', 
            prompt=prompt, 
            language=language, 
            responses=[generated_code]
        )
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return render_template('index.html', prompt=prompt, language=language, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
