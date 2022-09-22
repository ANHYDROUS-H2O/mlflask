from flask import Flask , render_template , request
import marks as m




app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        hrs = request.form['hrs']
        if hrs=="":
            return render_template("index.html", txt="Please Enter a value")
        marks_pred = m.marks_prediction(hrs)
        mk = marks_pred
        return render_template("index.html", my_marks = mk)

    return render_template("index.html")

"""@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == "POST":
        name = request.form["username"]
    
    return render_template("sub.html", n = name)"""

if __name__ == "__main__":
    app.run(debug=True)