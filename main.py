from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс! | Vulp, εnδex!"


if __name__ == '__main__':
    app.run(port=8001, host='192.168.2.113')
