from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login/')
def login():
    return "login page goes here"

def create_or_login():
    """login handler for OpenID, either let them make an account or redirect"""
    return "create an account or be redirected"

@app.route('/create/'):
def create_account():
    return "form to enter feeds, etc"

@app.route('/<username>/')
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


@app.template_filter()
def timesince(dt, default="just now"):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """
    now = datetime.now()
    diff = now - dt

    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )

    for period, singular, plural in periods:
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)
    return default


if '__main__' == __name__:
    app.run()
