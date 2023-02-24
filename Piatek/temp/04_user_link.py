from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

print(__name__)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/czas")
def czas():
    return render_template("data.html", czas=datetime.now())


@app.route("/demo2")
def hello_world2():
    return "<p>Hej - Tu ADAM <hr> W Wersji 2!</p>"

@app.route("/test_req")
def request_test():
    return render_template("req.html",
                           czas=datetime.now(),
                           headers=request.headers,
                           address=request.remote_addr,
                           user=request.remote_user)


@app.route("/test_danej/<value>")
def request_test_danej(value):
    return render_template("val.html",
                           czas=datetime.now(),
                           headers=request.headers,
                           address=request.remote_addr,
                           user_value=value)


# http://127.0.0.1:5000/test_req_args/?a=3&b=45&ip=192.168.10.1
@app.route("/test_req_args/")
def request_test_args():
    return render_template("val.html",
                           czas=datetime.now(),
                           headers=request.headers,
                           address=request.remote_addr,
                           user_value=request.args.to_dict())

# Domyślne wartości parametrów:
@app.route('/index/', defaults={'subject' : ... })
@app.route('/index/<subject>')
def subject(subject):
    if subject is Ellipsis:
        subject = datetime.now().strftime("%c")
    return f"<h3>Subject is {subject}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
