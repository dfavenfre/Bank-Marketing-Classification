import streamlit as st
import numpy as np
import joblib
import time
from datetime import datetime
from typing import Iterable
import pickle



def main():

    # SIDEBAR CONTENT
    st.sidebar.title("Bank Customer Term Deposit Predictor")
    st.sidebar.write(
        """
        Machine Learning implementations across various industries scope for achieving superior advantages over long-existing methods. 
        This app provides banking professionals a novel perspective for predicting customer tendency in subscribing to a term deposit. 
         
        
        """
    )
    
    # Social Hubs
    st.sidebar.markdown(

    """
    <div stlye="{}">
        <h3> Follow My Social Hubs For More Content </h3>
        <ul>
            <li><a href="https://medium.com/@bauglir">Medium</a></li>
            <li><a href="https://www.kaggle.com/dfavenfre">Kaggle</a></li>
            <li><a href="https://github.com/dfavenfre">GitHub</a></li>
            <li><a href="https://www.linkedin.com/in/tolga-%C5%9Fakar-575b86136">LinkedIn</a></li>
         </ul>  
    
    """, unsafe_allow_html=True

    )

    # MAIN PAGE CONTENT
    st.title("Predict Customer Tendency")
    st.write(
         """
    Trained Machine Learning Model Achieves An Accuracy Up to 95%.

    """)

    # Load Model
    try:
        # Load the model
        with open(r"Model/xgbclassifier.pkl", "rb") as f:
            xgbclassifier = pickle.load(f)
        if xgbclassifier is not None:
            load_message = st.empty()
            load_message.text("Model Loaded Successfully")
            time.sleep(1)
            load_message.empty()

    except FileNotFoundError:
        load_message = st.empty()
        load_message.text("Model Not Found, Please Control Path")
        time.sleep(1)
        load_message.empty()


    # MODEL CONTENT

    ## Age Feature 
    select_age = st.date_input(label="Select A Birth Date", 
                value=datetime.today().date(),
                min_value=datetime(1930, 1, 1).date(),
                max_value=datetime.today().date())

    if select_age:
        current_time = datetime.today().date()
        select_age = datetime.strptime(str(select_age), '%Y-%m-%d')
        age = current_time.year - select_age.year

    ## Job Feature
    occupation_values ={"Administrative": 0,"Blue-collar": 1,"Entrepreneur": 2,"Housemaid": 3,
                        "Management": 4,"Retired": 5,"Self-employed": 6,"Services": 7,
                        "Student": 8,"Technician": 9,"Unemployed": 10}
    
    select_job = st.selectbox("Select Occupation", list(occupation_values.keys()))
    if select_job:        
        selected_job = occupation_values[select_job]
        if selected_job:
            st.write(selected_job)


if __name__ == '__main__':
	main()

