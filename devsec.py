from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "secrets: 123hello"

if __name__ == '__main__':
    app.run(debug=True)

