from flask import Flask, render_template
app = Flask(__name__)

cout = '1000'

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Estimation')

if __name__ == '__main__':
    app.run(debug=True)