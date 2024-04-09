from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger) 
        flash(f'{form.username.data} 님 가입 완료!', 'success')
        return redirect(url_for('/ranking'))
    return render_template('register.html', form=form)


@app.route('/ranking')
def ranking():
    return render_template("ranking.html")

if __name__ == '__main__':
    app.run(debug=True)