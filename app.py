''' author @Indigo Parlin
    Black Wings Hacks 2022
'''

import requests
from flask import Flask,render_template,request

app = Flask(__name__)
 
@app.route('/doctor/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/doctor/form' to submit form"
    if request.method == 'POST':
        
        form_data = request.form
        zipcode = form_data['Zipcode']
        URL = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCaouVmtg_xngRJbOb_GjtZ__sSPuRfyME"
        PARAMS = {'address':zipcode}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        results = data['results']
        dic = results[0]
        geo = dic['geometry']
        loc = geo['location']
        latitude = loc['lat']
        longitude = loc['lng']

        return render_template('data.html',lati = latitude, long = longitude)
      
@app.route("/")
def home():
  return render_template('homepage.html') 

app.run(host='localhost', port=5000)




