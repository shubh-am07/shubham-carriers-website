from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 20,00,000'
}, {
  'id': 3,
  'title': 'Data Engineer',
  'location': 'Mumbai, India'
}, {
  'id': 4,
  'title': 'BackEnd Engineer',
  'location': 'Indore, India',
  'salary': 'Rs. 12,00,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, comapay_name='shubham')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


#print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
