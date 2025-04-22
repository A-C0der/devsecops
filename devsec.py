from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "secret: 123hello private-key:hello_acoder"

if __name__ == '__main__':
    app.run(debug=True)

