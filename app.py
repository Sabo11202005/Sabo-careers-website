from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'North Carolina',
  'Salary': '$150,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'South Carolina',
  'Salary': '$130,000'
}, {
  'id': 3,
  'title': 'Front-End Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Back-End Engineer',
  'location': 'San Francisco',
  'Salary': '$250,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
