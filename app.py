from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        input = request.form['input']
        return input+" world"
    return render_template('index.html')



if __name__ == '__main__':
    app.run(port=8881)
