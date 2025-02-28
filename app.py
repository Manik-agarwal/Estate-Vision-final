from flask import Flask,render_template,request
import pandas as pd
import pickle
import numpy as np


app=Flask(__name__)
data=pd.read_csv("ML model/cleaned.csv")
pipe=pickle.load(open("ML model/RidgeModel.pkl",'rb'))

@app.route('/')
def index():
    
    return render_template('index.html')



@app.route('/ai_prediction')
def contact():
    locations=sorted(data['location'].unique())
    return render_template('ai_prediction.html',locations=locations)

@app.route('/gallery')
def services():
    return render_template('gallery.html')

@app.route('/predict',methods=['POST'])
def predict():
    location=request.form.get('location')
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    sqft=request.form.get('total_sqft')

    input=pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=pipe.predict(input)[0]*1e5
    return str(np.round(prediction,2))

if __name__=="__main__":
    app.run(debug=True,port=5001)





