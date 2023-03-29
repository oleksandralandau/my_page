# I haven't finished yet, just sending before the meeting
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/mypage/me")
def mypage():
    return render_template("1st_page.html")

@app.route("/mypage/contact")
def mypage2():
    return render_template("2nd_page.html")


@app.route('/message', methods=['POST'])
def message():
    print(request.form)
    return redirect("/message")

if __name__ == '__main__':
    app.run(debug=True)
