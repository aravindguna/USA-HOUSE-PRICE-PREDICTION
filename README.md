# USA-HOUSE-PRICE-PREDICTION
ML-Model-Flask-Deployment

This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API

Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model), Flask (for API) installed,A account in Heruko.

Project Structure
This project has four major parts :

model.py - This contains code fot our Machine Learning model to predict house price in USA based on trainig data in 'USA_Housing.csv' file.
app.py - This contains Flask APIs that receives house details through GUI or API calls and converts into polynomial form and then computes the precited value based on our model and returns it.
templates - This folder contains the HTML template to allow user to enter house detail and displays the price of the house.
Running the project

Ensure that you are in the project home directory. Create the machine learning model by running below command -
python model.py
This would create a serialized version of our model into a USA_Housing.sav

Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.

Navigate to URL http://localhost:5000
You should be able to view the homepage as below : alt text

Enter valid numerical values in all 5 input boxes and hit Predict.

If everything goes well, you should be able to see the predcited Price of the house on the HTML page! alt text

Other than running the model in local machine i also deployed the model in heruko website and created a unique URL to do the prediction which can be done in the following URL : https://usa-house-price-prediction.herokuapp.com/
