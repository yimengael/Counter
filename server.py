from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsTheSecret'


@app.route('/')
def index():
    return render_template('index.html', times=0)


@app.route('/inc2Reset', methods=['POST'])
def inc2():
    try:
        if request.form['action'] == 'add2':
            session['times'] = session['times'] + 2
        elif request.form['action'] == 'reset':
            session['times'] = 0
    except Exception as e:
        raise
    return render_template('index.html', times=session['times'])


app.run(debug=True)
