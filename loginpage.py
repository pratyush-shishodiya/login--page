from flask import Flask,render_template,redirect,url_for,request,g,session
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        session.pop("user",None)
        if request.form['password']=='password':
            session["user"]=request.form['username']
            return redirect(url_for("webpage"))
    return render_template("login.html")
@app.route("/page",methods=["GET"])
def webpage():
    if g.user:
        return render_template("home.html",user=session["user"])
    return redirect(url_for('index'))
@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user=session['user']
@app.route("/dropsession")
def dropsession():
    session.pop("user",None)
    return render_template("login.html")

if __name__=='__main__':
    app.run(debug=True)
