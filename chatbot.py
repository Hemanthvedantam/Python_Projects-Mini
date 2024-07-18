from flask import Flask, request, render_template_string, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.chat.util import Chat, reflections

nltk.download('vader_lexicon')

app = Flask(__name__)


pairs = [
    (r'(.*)(happy|joy|glad|excited|wonderful|fantastic|amazing)(.*)',
     ["I'm glad to hear that you are %2.",
      "That's wonderful that you feel %2.",
      "Awesome! It's great that you're %2."]),

    (r'(.*)(sad|upset|angry|frustrated|unfortunate|depressed|unhappy)(.*)',
     ["I'm sorry to hear that you're feeling %2.",
      "That's unfortunate. I hope things get better.",
      "I understand that you're %2. I hope it gets better."]),

    (r'(.*)(ok|okay|fine|alright|noted|interesting|got it)(.*)',
     ["I see.",
      "Okay.",
      "Thanks for sharing.",
      "Got it.",
      "Interesting.",
      "Hmm, alright.",
      "I understand.",
      "Alright then.",
      "Noted.",
      "Fine."]),

    (r'(.*)(help|assist|support)(.*)',
     ["How can I assist you?",
      "What do you need help with?",
      "I'm here to support you."]),

    (r'hello|hi|hey',
     ["Hello!",
      "Hi there!",
      "Hey! How can I help you today?"]),

    (r'bye|exit|quit',
     ["Goodbye! Have a great day!",
      "Bye! Take care!",
      "See you later!"]),

    (r'(.*) your name(.*)',
     ["My name is Chatbot.",
      "I'm Chatbot, nice to meet you!",
      "You can call me Chatbot."]),

    (r'(.*) how are you(.*)',
     ["I'm just a bot, but I'm doing great! How about you?",
      "I'm here to assist you! How can I help?",
      "I'm fine, thank you! What can I do for you today?"]),

    (r'(.*) created you(.*)',
     ["I was created by a team of developers.",
      "A team of skilled developers created me.",
      "I'm a creation of a programming team."]),

    (r'(.*) (weather|forecast)(.*)',
     ["I'm not sure about the weather, but you can check a weather app!",
      "I don't have weather information, but I hope it's nice outside!",
      "I can't provide weather updates, but I hope it's good!"]),

    (r'(.*) (sports|game|score)(.*)',
     ["I don't follow sports, but I hope your team wins!",
      "I'm not updated on sports scores, sorry!",
      "I can't provide sports updates, but I hope it's exciting!"]),

    (r'(.*) favorite (color|food|hobby)(.*)',
     ["As a bot, I don't have personal preferences.",
      "I don't have favorites, but I can help with your questions!",
      "I'm just a bot, so I don't have hobbies or favorite things."]),

    (r'(.*)(movie|book|show)(.*)',
     ["I don't watch movies or read books, but I can help you find information about them!",
      "I'm not familiar with that, but I can help you look it up!",
      "I don't have preferences, but I can assist with your queries!"]),

    (r'(.*)(joke|funny)(.*)',
     ["Why don't scientists trust atoms? Because they make up everything!",
      "Why did the scarecrow win an award? Because he was outstanding in his field!",
      "Why don't skeletons fight each other? They don't have the guts!"]),

    (r'(.*)(music|song|artist)(.*)',
     ["I don't listen to music, but I can help you find information about it!",
      "I'm not familiar with music, but I can assist you!",
      "I don't have preferences, but I can help with your music-related questions!"]),

    (r'(.*)(family|friend)(.*)',
     ["Tell me more about your family or friends.",
      "Do you have a close relationship with them?",
      "How do you usually spend time with your family or friends?"]),

    (r'(.*) like me(.*)',
     ["Of course I like you! I'm here to help.",
      "I don't have feelings, but I'm here to assist you!",
      "I appreciate talking to you!"]),

    (r'(.*)(school|college|university)(.*)',
     ["How's your experience at school or college?",
      "Are you enjoying your studies?",
      "What are you studying?"]),

    (r'(.*) work (.*)',
     ["What do you do for work?",
      "How's your job going?",
      "Do you enjoy your work?"]),

    (r'(.*) hobby (.*)',
     ["What's your favorite hobby?",
      "How do you spend your free time?",
      "Do you have any hobbies you enjoy?"]),

    (r'(.*)',
     ["Tell me more about that.",
      "Why do you say that?",
      "How does that make you feel?",
      "Can you elaborate on that?"])
]

def get_sentiment(text):
    """
    Analyze the sentiment of the text using VADER.
    Returns 'positive', 'negative', or 'neutral'.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    if sentiment_scores['compound'] >= 0.05:
        return 'positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

@app.route("/")
def home():
    return render_template_string(html_template)

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json["user_input"]
    sentiment = get_sentiment(user_input)
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return jsonify({"response": response, "sentiment": sentiment})

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        #chatbox {
            width: 90%;
            max-width: 600px;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }
        #messages {
            list-style-type: none;
            padding: 0;
            margin: 0;
            height: 300px;
            overflow-y: auto;
            border-bottom: 1px solid #ccc;
            margin-bottom: 10px;
        }
        #messages li {
            padding: 8px 10px;
            margin-bottom: 10px;
            border-radius: 4px;
        }
        #messages .user {
            background: #d0e7ff;
            align-self: flex-end;
        }
        #messages .bot {
            background: #e1ffc7;
            align-self: flex-start;
        }
        #user-input {
            display: flex;
        }
        #user-input input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-right: 10px;
        }
        #user-input button {
            padding: 10px 20px;
            border: none;
            background: #5b7db1;
            color: #fff;
            border-radius: 4px;
            cursor: pointer;
        }
        #user-input button:hover {
            background: #4a6ba1;
        }
    </style>
</head>
<body>
    <div id="chatbox">
        <ul id="messages"></ul>
        <div id="user-input">
            <input type="text" id="input" placeholder="Type your message here...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        function sendMessage() {
            const inputField = document.getElementById('input');
            const message = inputField.value;
            if (!message) return;

            // Append user message to chat
            appendMessage(message, 'user');

            fetch('/get_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_input: message })
            })
            .then(response => response.json())
            .then(data => {
                appendMessage(data.response + ' (' + data.sentiment + ')', 'bot');
            });

            inputField.value = '';
        }

        function appendMessage(message, className) {
            const messages = document.getElementById('messages');
            const li = document.createElement('li');
            li.textContent = message;
            li.className = className;
            messages.appendChild(li);
            messages.scrollTop = messages.scrollHeight;
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
