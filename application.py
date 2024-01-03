from flask import Flask,render_template,request
import pickle
import numpy as np
#Create a Flask Object
application=Flask(__name__)
#Decorator
'''
@application.route('/')
def hello():
    """Test Function"""
    return "Welcome to the Flask"

@application.route('/mohan',methods=['GET'])
def check():
    """New Function"""
    return "Abhinav is in KITS College"
'''
#First let's read the pickle file
with open("House_Price.pkl",'rb') as f:
    model=pickle.load(f)

@application.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    Rooms=int(request.form['bedrooms'])
    Bathrooms=int(request.form['bathrooms'])
    Place=int(request.form['location'])
    Area=int(request.form['area'])
    Status=int(request.form['status'])
    Facing=int(request.form['facing'])
    P_Type=int(request.form['type'])
    #now take the above form data and convert to array
    input_data=np.array([[Place,Area,Status,Rooms,Bathrooms,Facing,P_Type]])
    #By taking above data we will predict the House_Price
    prediction=model.predict(input_data)[0]
    #print(prediction)
    # Now we will pass the predicted data to the template
    return render_template('index.html',prediction=prediction)
if __name__ == "__main__":
    application.run()
