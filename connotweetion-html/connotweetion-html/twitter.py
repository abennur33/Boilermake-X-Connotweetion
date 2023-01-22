import twint
import csv
from flask import Flask, request, render_template
app = Flask(__name__,template_folder='templates', static_folder='static')

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
            user_input = str(array[10])
            #emotion_mapping = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}
            #prediction, all = to_emotion(user_input, tokenizer, model)
            print(user_input)#prediction)

    return 0

if __name__ == '__main__':
    app.run()

#user_input = "surprise"
#emotion_mapping = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}
#prediction, all = to_emotion(user_input, tokenizer, model)
#print(prediction)
#print(all)