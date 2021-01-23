from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
@app.route('/web',methods=['GET'])
def webpage():
        return render_template('page.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Pratyush' or request.form['password'] != '12345':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('webpage'))

    return render_template('login.html', error=error)


if __name__=="__main__":
        app.run(host="0.0.0.0",port=8080)

