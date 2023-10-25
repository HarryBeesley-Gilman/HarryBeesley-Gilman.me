from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, template_folder='DALI')

# Make sure you set your API key here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = "hi im harry"
    return jsonify({'message': response})






if __name__ == '__main__':
    app.run(debug=True, port = 7000)
