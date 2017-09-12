from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "h.ufriywasdf3aq34hiucv"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    lastTime = request.form['getName']
    message = "Last name give was {}".format(lastTime) 
    session['listTime'] = message
    return redirect('/')

# @app.context_processor
# def inject_getName(name):
#     return dict(lastTime="The last name given is {}".format(name))

app.run(debug=True)
