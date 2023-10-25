from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__, template_folder='/Users/hbg/Desktop/DALI/HarryBeesley-Gilman.me')

# Make sure you set your API key here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = "hi"

    answer = response['choices'][0]['message']['content'].strip()
    return jsonify({'message': answer})




if __name__ == '__main__':
    app.run(debug=True, port = 7352)
