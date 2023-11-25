from flask import Flask , request , render_template

import requests

app = Flask(__name__)

@app.route('/')
def displayWebPage():
    return render_template('index.html')

@app.route('/weatherroute',methods = ['POST'])
def fetchdata():
    city = request.form.get('city')
    unit = request.form.get('unit')
    appid = request.form.get('appid')

    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {'q':city,'unit':unit,'appid':appid}

    datas = requests.get(url,params=params)

    data = datas.json()

    cityname = data['name'] 

    return f'city  = {city}  , unit  = {unit} , appid  = {appid}  {data} city = {cityname}'

if __name__ == "__main__" :
    app.run(host="0.0.0.0")

