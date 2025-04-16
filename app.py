from flask import Flask, render_template, request
from generator import generate_password

app = Flask(__name__)
history = []

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        use_digits = 'digits' in request.form
        use_specials = 'specials' in request.form
        password = generate_password(length, use_digits, use_specials)
        history.insert(0, password)
    return render_template("index.html", password=password, history=history[:5])

if __name__ == "__main__":
    app.run(debug=True)
