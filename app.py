from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'Date': '12-Oct',
        'Session': 'Morning',
        'Job': 'Bio Box'
    },
    {
        'id': 2,
        'Date': '12-Oct',
        'Session': 'Morning',
        'Job': 'Check In Desk'
    },
    {
        'id': 3,
        'Date': '12-Oct',
        'Session': 'Morning',
        'Job': 'Backstage'
    },
    {
        'id': 4,
        'Date': '12-Oct',
        'Session': 'Afternoon',
        'Job': 'Bio Box'
    },
    {
        'id': 5,
        'Date': '12-Oct',
        'Session': 'Afternoon',
        'Job': 'Check In Desk'
    },
    {
        'id': 6,
        'Date': '12-Oct',
        'Session': 'Afternoon',
        'Job': 'Backstage'
    },
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)