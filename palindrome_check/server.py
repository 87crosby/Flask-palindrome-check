from flask import Flask, render_template, request, redirect, session
from math import floor

app = Flask(__name__)
app.secret_key = "lol im a secret key"

@app.route('/')
def index():

    if not 'number_of_checks' in session:
        session['number_of_checks'] = 0

    return render_template('index.html')

@app.route('/is_palindrome', methods=['POST'])
def is_palindrome():

    input_string = request.form['palindrome_input']

    session['is_palindrome'] = True
    session['input_string'] = input_string

    for x in range(0, floor(len(input_string)/2)):
        if input_string[x] != input_string[-1 - x]:
            session['is_palindrome'] = False

    session['number_of_checks'] += 1

    return redirect('/results')

@app.route('/results')
def palindrome_results():

    if 'is_palindrome' not in session:
        return redirect('/')

    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug = True)