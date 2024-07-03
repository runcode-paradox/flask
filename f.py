from flask import Flask, render_template, request
from dgg import *
from fr import *
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def hello_world():
   if request.method=='GET':
        return render_template('index.html',o=s,f=d)

@app.route("/doctors.html", methods=['GET','POST'])
def doc():
     if request.method=='GET':
        return render_template('doctors.html',f=d)
     else:
       return render_template('doctors.html',f=d)
@app.route("/hospitals.html", methods=['GET','POST'])
def hos():
     if request.method=='GET':
        return render_template('hospitals.html',o=s)
     else:
       return render_template('hospitals.html',o=s)

if __name__ == "__main__":
    app.run(debug=True)
