import twint
import csv
from flask import Flask, request, render_template

import numpy as np
import pickle
from keras.utils import pad_sequences




app = Flask(__name__,template_folder='templates', static_folder='static')
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Keyword = request.form['Keyword']
        From = request.form['From']
        Until = request.form['Until']
        result = my_python_function(Keyword, From, Until)
        return render_template('index.html', result=result)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')



def my_python_function(Keyword, From, Until):
    f = open('pee.csv', 'r+')
    f.truncate(0)

    print(Keyword+", "+ From+", "+ Until)

    # Configure
    c = twint.Config()
    c.Search = "lang:en " + Keyword
    c.Limit = 10
    c.Since = From
    c.Until = Until
    c.Store_csv = True
    c.Hide_output = True
    c.Output = 'pee.csv'
    c.Custom_csv = ["tweet"]

    # Run
    twint.run.Search(c)

    with open('pee.csv') as csvfile:

        # get number of columns
        for line in csvfile.readlines():
            array = line.split(',')
            #to_emotion(str(array[10]), tokenizer, model, max_words)

    return 0

if __name__ == '__main__':
    def to_emotion(user_input, tokenizer, model, max_words):
        x = tokenizer.texts_to_sequences([user_input])
        x = pad_sequences(x, maxlen=max_words)
        y = model.predict(x)
        y = np.argmax(y, axis=1)
        emotion_mapping = {0: "sadness", 1: "joy", 2: "love", 3: "anger", 4: "fear", 5: "surprise"}
        return emotion_mapping[y[0]]


    tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))

    user_input = "I am depressed"
    x = to_emotion(user_input, tokenizer, model, 200)
    print(x)

    app.run()

