from flask import Flask, Response,render_template
import time
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('2.html')


@app.route('/sse1')
def sse1():
    def generate():
        for i in range(5):
            if i == 4 :
                data = 'hello world!' + ' '
                data = json.dumps(data)
                yield f'data: {data}\n\n'
                time.sleep(1)
            else:
                data = 'hello world!' + '\n'
                data = json.dumps(data)
                yield f'data: {data}\n\n'
                time.sleep(1)

    return Response(generate(), mimetype='text/event-stream')



if __name__ == '__main__':
    app.run(debug=True)