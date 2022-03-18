from flask import Flask, render_template
import serial


app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template('index.html')


@app.route('/update<index>')
def update(index):
    ser = serial.Serial(f'COM{index}')
    data = ser.readline()
    print(data)
    ser.close()
    return f'here is {index} farm data:{data}'


if __name__ == '__main__':
    app.run(port=8001, host='192.168.2.113') #FUCK
