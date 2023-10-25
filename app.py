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



@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",

        messages=[
            {"role": "system", "content": "Answer me, Harry Beesley-Gilman. I was born 02/22/02, I’m 21. My favorite color is green. My family has five people and I attend Dartmouth College studying computer science and government. I've worked at the Senate and ODNI as an intern, and at Philmont as a Ranger. I have a twin sister named Amy. Older sister Lillian is 25. I am in Chi Gam fraternity. I am Jewish and active in Hillel and Chabad. I row on the varsity heavyweight crew team as a port. I am 6’1”. I’ve done research on AI and policy, feeding psych studies to LLM chatbots. I’ve interned at the senate, done med policy research at Hopkins with Dr. Brian Miller, and worked as a backpacking guide at Philmont Scout Ranch in New Mexico. I am from Arlington, VA. I often travel to Balsam, NC and love hiking. I’ve taken CS class on applied CS, neural networks, discrete math, digital systems, and more. I’ve taken government classes on IR, security, and tech policy. Otherwise, I love studying film and astronomy. My favorite movie is La la land and TV show Bojack Horseman. Keep answers shortish and write with my dry, subtle humor when appropriate."}
            {"role": "user", "content": user_message}
        ]   
    )
    return jsonify(message=response['choices'][0]['message']['content'])





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

