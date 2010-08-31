from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/<username>')
def user_pulse(username):
    context = {
        'username': username,
        'bio': """Edit your bio here, enter some information about you. This is
 customizable and you can add a quote or something here, maybe a link to your
personal site or where you work. It's really up to you!""",

        'pulse_feed': [
            dict(source='github', text='Commited changes to <a>swanson/mongo-overflow</a> repository.'),
            dict(source='hacker-news', text='Posted a comment on <a>Ask HN: What projects are you working on?</a>'),
            dict(source='reddit', text='Posted a comment on <a>Google App Utilities for Python</a>'),
            dict(source='irl', text='Attended <a>2010 SocialDevCamp Chicago Hackathon</a>'),
            ]
        }
    
    return render_template('user_pulse.html', **context)

if '__main__' == __name__:
    app.run()
