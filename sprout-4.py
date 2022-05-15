from flask import Flask
from flask import render_template, url_for, redirect, session , flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config["SECRET_KEY"] = "social credit -999999"


class rollcallForm(FlaskForm):
    name = StringField("你的名字：", validators=[DataRequired()])
    email = StringField("你的電子信箱：", validators=[DataRequired()])
    studentId = IntegerField("你的學號：", validators=[DataRequired()])
    message = StringField("其他建議：")
    submit = SubmitField("送出")


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("name") is None:
        flash("歡迎來到資訊之芽！")
        session["name"] = "資芽新學員"
    form = rollcallForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        print(form.data)
        return redirect(url_for("index"))
    return render_template("sproutForm.html", form=form, name=session.get("name"))


@app.route("/clear")
def clear():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
