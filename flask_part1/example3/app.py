from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def register():
    return render_template('register.html') # PERDUODAME Į ŠABLONĄ

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('greetings.html', username=username)
    else: 
        return render_template('login.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)