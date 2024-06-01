from flask import Flask, render_template, request
import os
import requests

app = Flask(_name_)

# Load Azure Cognitive Services Translator key and endpoint from.env file
translator_key = os.environ['TRANSLATOR_KEY']
translator_endpoint = os.environ['TRANSLATOR_ENDPOINT']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    language = request.form['language']

    # Call Azure Cognitive Services Translator API
    headers = {
        'Ocp-Apim-Subscription-Key': translator_key,
        'Content-Type': 'application/json'
    }
    body = [{
        'text': text
    }]
    response = requests.post(translator_endpoint, headers=headers, json=body)

    # Get translated text from response
    translated_text = response.json()[0]['translations'][0]['text']

    # Render results.html template with translated text
    return render_template('results.html', original_text=text, translated_text=translated_text, target_language=language)

if _name_ == '_main_':
    app.run(debug=True)