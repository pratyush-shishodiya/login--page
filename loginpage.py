from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
#@app.route('/loginpage',methods=["GET"])
#def loginpage():
#	return ("welcome to the login page")
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Pratyush' or request.form['password'] != '12345':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
if __name__=="__main__":
	app.run(host="0.0.0.0",port=8080)
