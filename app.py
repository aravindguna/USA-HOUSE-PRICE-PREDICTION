#!/usr/bin/env python
# coding: utf-8

# In[4]:



import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('usa_housing.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array([int_features])
    final_features = PolynomialFeatures(degree=4).fit_transform(final_features)
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The Price Should Be {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)


