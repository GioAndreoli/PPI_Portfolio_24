from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run()