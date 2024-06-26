from flask import Flask, render_template_string, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# HTML Template as a string
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Translator</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            background: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            overflow: hidden;
            position: relative;
            background-color: #add8e6; /* Light blue background */
        }

        .container {
            width: 60%;
            margin: 0 auto;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.8); /* Transparent background */
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 50px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        h1 {
            text-align: center;
            color: #333;
            font-weight: 600;
            width: 100%;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            flex: 0 0 45%;
        }

        label {
            margin-top: 10px;
            font-weight: 400;
        }

        textarea, input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(255, 0, 0, 0);
            transition: box-shadow 0.3s ease-in-out;
        }

        textarea:focus, input[type="text"]:focus {
            box-shadow: 0 0 10px rgba(255, 0, 0, 1);
            outline: none;
        }

        button {
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
            font-weight: 600;
            align-self: flex-end;
        }

        button:hover {
            background-color: #0056b3;
        }

        h2 {
            color: #333;
            margin-top: 20px;
            font-weight: 600;
        }

        p {
            background-color: #e9ecef;
            padding: 10px;
            border-radius: 5px;
            font-weight: 300;
            flex: 0 0 45%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Text Translator</h1>
        <form method="POST">
            <label for="text">Enter the text to translate:</label>
            <textarea id="text" name="text" rows="4" cols="50" required></textarea>
            <label for="src_lang">Enter the source language code (e.g., 'en' for English):</label>
            <input type="text" id="src_lang" name="src_lang" required>
            <label for="dest_lang">Enter the destination language code (e.g., 'es' for Spanish):</label>
            <input type="text" id="dest_lang" name="dest_lang" required>
            <button type="submit">Translate</button>
        </form>
        {% if translated_text %}
            <div>
                <h2>Original text:</h2>
                <p>{{ request.form['text'] }}</p>
                <h2>Translated text:</h2>
                <p>{{ translated_text }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def translate():
    translated_text = ''
    if request.method == 'POST':
        text = request.form['text']
        src_lang = request.form['src_lang']
        dest_lang = request.form['dest_lang']
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        translated_text = translation.text
    return render_template_string(html_template, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
