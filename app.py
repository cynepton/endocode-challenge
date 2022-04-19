from flask import Flask

app = Flask(__name__)

@app.route('/helloworld')
def helloworld():
    return "Hello Stranger"