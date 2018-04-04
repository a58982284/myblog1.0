



from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Hello World!</h1>'

from hello import app

if __name__ == '__main__':

    app.debug = True

    app.run()