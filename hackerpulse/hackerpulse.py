from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/<username>')
def user_pulse(username):
    return render_template('user_pulse.html')

if '__main__' == __name__:
    app.run()
