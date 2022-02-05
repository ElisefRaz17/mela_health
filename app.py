# helloTest.py
# at the end point / call method hello which returns "hello world"
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template('homepage.html')


