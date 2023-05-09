from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return redirect("https://wa.me/+34611676727", code=302)

if __name__ == '__main__':
    app.run(debug=True)
