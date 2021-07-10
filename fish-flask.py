import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("Fish_LogisticRegression.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    if prediction[0] == 0:
        return render_template('index.html', prediction_text='The fish belong to species Bream ')
    elif prediction[0] == 1:
        return render_template('index.html', prediction_text='The fish belong to species Parkki')
    elif prediction[0] == 2:
        return render_template('index.html', prediction_text='The fish belong to species Perch')
    elif prediction[0] == 3:
        return render_template('index.html', prediction_text='The fish belong to species Pike')
    elif prediction[0] == 4:
        return render_template('index.html', prediction_text='The fish belong to species Roach')
    elif prediction[0] == 5:
        return render_template('index.html', prediction_text='The fish belong to species Smelt')
    else:
        return render_template('index.html', prediction_text='The fish belong to species Whitefish')
    

if __name__=='__main__':
    app.run()