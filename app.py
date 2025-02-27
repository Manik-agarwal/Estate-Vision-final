from flask import Flask,render_template,request
import pandas as pd 


app=Flask(__name__)
data=pd.read_csv("ML model/cleaned.csv")

@app.route('/')
def index():

    locations=sorted(data['location'].unique())
    
    return render_template('index.html',locations=locations)

# @app.route('/')
def about():
    return render_template('about.html')

@app.route('/ai_prediction.html')
def contact():
    return render_template('ai_prediction.html')

@app.route('/gallery')
def services():
    return render_template('gallery.html')

if __name__=="__main__":
    app.run(debug=True,port=5001)





