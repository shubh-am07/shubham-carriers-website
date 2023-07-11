from flask import Flask, render_template
from database import load_jobs_from_db
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs, comapay_name='shubham')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  serialized_jobs = json.dumps(jobs)  # Serialize jobs using json.dumps
  return serialized_jobs, 200, {'Content-Type': 'application/json'}


#print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
