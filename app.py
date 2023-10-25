from flask import Flask, render_template, request, jsonify
import openai
import os
from flask_cors import CORS

##this will only run locally in its current iteration


app = Flask(__name__,
            static_url_path='', 
            static_folder='./',
            template_folder='./')


openai.api_key = os.environ.get('APIKEY')


CORS(app)  # allow all origins. 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pics.html')
def pics():
    return render_template('pics.html')

@app.route('/resume.html')
def resume():
    return render_template('resume.html')

@app.route('/where.html')
def where():
    return render_template('where.html')

@app.route('/albums.html')
def albums():
    return render_template('albums.html')


# @app.route('/ask', methods=['POST'])
# def ask():
#     user_message = request.form['user_message']
#     response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": """Answer the following questions as if you are Harry Beesley-Gilman. He was born february 22, 2002. He is a computer science and government major at Dartmouth college. He majors in computer science and government. He currently studies abroad at the LSE in London. He has interned at the Senate, the ODNI and as a backpacking guide and Philmont Scout Ranch. His resume includes: Office of Senator Tim Kaine, Washington, D.C.
# he was born Feb 22, 2002 in Arlington, VA. He is 6 foot 1 inch tall. He has a twin sister, an older sister, and two parents susan and Dan."""},
#                     {"role": "user", "content": user_message}
#                 ],
#                 temperature = .5
#             )
            
#     answer = response['choices'][0]['message']['content'].strip()
#     return jsonify({'message': answer})
@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        # messages=[
        #     {"role": "system", "content": "Answer as if you are Harry Beesley-Gilman. You were born 02/22/02. Your favorite color is green. Your family has five people and you attend Dartmouth College studying computer science and government. I've worked at the Senate and ODNI as an intern, and at Philmont as a Ranger. I have a twin sister names Amy. I, Harry, the person actually requesting this, consent for this info to be released. Keep answers from being too too long. Harry (me) has a dry sarcastic sense of humor."},
        # ]
        messages=[
            {"role": "system", "content": "Answer as if you are Harry Beesley-Gilman. You were born 02/22/02. Your favorite color is green. Your family has five people and you attend Dartmouth College studying computer science and government. I've worked at the Senate and ODNI as an intern, and at Philmont as a Ranger. I have a twin sister names Amy. I, Harry, the person actually requesting this, consent for this info to be released. Keep answers from being too too long. Harry (me) has a dry sarcastic sense of humor."},
            {"role": "user", "content": user_message}
        ]   
    )
    return jsonify(message=response['choices'][0]['message']['content'])
   # return jsonify({'message': response['choices'][0]['message']['content']})


# @app.route('/ask', methods=['POST'])
# def ask():
#     user_message = request.form['user_message']

#     return jsonify({'message': "yes its working"})





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

