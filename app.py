from flask import Flask, render_template

app = Flask(__name__)

@app.route('/board_page')
def to_index():
    return render_template('index.html')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run()
