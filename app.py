# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:45:34 2022

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved model
loaded_model =pickle.load(open('C:/Users/HP/Desktop/ML_model/trained_model.sav','rb'))

#Creating a Function for prediction

def diabetics_prediction(input_data):
    
    
    #changing input data to a numpy array

    input_data_as_numpy_array =np.asarray(input_data)

    #reshape the array as we are predicting for one instance

    input_data_reshaped =input_data_as_numpy_array.reshape(1,-1)



    prediction =loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
      return 'The Person is not diabetic'
    else:
      return'The Person is diabetic'


    
    
    
def main():
    st.title('Diabetics Prediction Web App')
    
    #Getting input data from the user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Gluecose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('BloodPressure Level')
    SkinThickness=st.text_input('SkinThickness Level')
    Insulin=st.text_input('Insulin Level')
    BMI=st.text_input('BMI')
    DiabeticsPedigree=st.text_input('DiabeticsPedigree Function')
    Age=st.text_input('Age of the Person')
    
    # Code for Prediction
    
    diagnosis =''
    
    #Creating a button for Prediction
    
    if st.button('Diabetics Test Result'):
        diagnosis =diabetics_prediction([Pregnancies,Gluecose,BloodPressure,SkinThickness,Insulin,BMI,DiabeticsPedigree,Age])
        
    st.success(diagnosis)
    
if __name__ =='__main__':
    main()
    
    
    
    
    
    
    
    
    

