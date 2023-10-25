from flask import Flask, render_template, request, jsonify
import openai
import os
##this will only run locally in its current iteration

app = Flask(__name__, template_folder='/Users/hbg/Desktop/DALI/HarryBeesley-Gilman.me')

openai.api_key = os.environ.get('API_Key')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """Answer the following questions as if you are Harry Beesley-Gilman. He was born february 22, 2002. He is a computer science and government major at Dartmouth college. He majors in computer science and government. He currently studies abroad at the LSE in London. He has interned at the Senate, the ODNI and as a backpacking guide and Philmont Scout Ranch. His resume includes: Office of Senator Tim Kaine, Washington, D.C.
Congressional Internr
● Trained and personally prepared 100+ youth and parents for 12-day mountain backpacking expeditions.
● Guided crews through the first portion of their trek, teaching wilderness survival skills and conservation methods."""},
                    {"role": "user", "content": user_message}
                ],
                temperature = .5
            )
            
    answer = response['choices'][0]['message']['content'].strip()
    return jsonify({'message': answer})




if __name__ == '__main__':
    app.run(debug=True, port = 7352)
