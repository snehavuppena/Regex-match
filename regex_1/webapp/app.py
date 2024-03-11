from flask import  Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    form_data = {'regex': '', 'test_string': ''}
    matches=[]
    if request.method=="POST":
        regex_string=request.form["regex"]
        test_string=request.form["test_string"]
        matches = re.findall(regex_string, test_string)
        return  render_template("home.html",form_data={'regex': regex_string, 'test_string': test_string}, matched_strings=enumerate(matches, start=1))
    else:
        return render_template("home.html", form_data=form_data, matched_strings=matches) 


@app.route('/email', methods=["GET", "POST"])
def email_validation():
     if request.method=="POST":
        email_pattern = r'[\w.%+-]+@[\w.-]+[\w]+\.[\w]{2,}'
        email_input= request.form["email_input"]
        match_result= re.findall(email_pattern, email_input)
        return render_template("email_validation.html", match_result=match_result)
     return render_template("email_validation.html")

# r'[\w.%+-]+@[\w.-]+\.[\w]{2,}'
if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0") # running the app and adding a broadcasting IP