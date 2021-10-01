import streamlit as st
from model import predict_duration
import numpy as np

st.set_page_config(page_title="Seoul Bike Trip Duration Prediction App",
                   page_icon="🛴", layout="wide")


with st.form("prediction_form"):

    st.header("Enter the Deciding Factors:")

    Distance = st.number_input("Distance: ", value=0, format="%d")
    Haversine = st.number_input("Haversine: ")
    Phour = st.number_input("Pickup Hour: ", min_value=0, max_value=23, value=0,format="%d")
    Pmin = st.number_input("Pickup Minute: ", min_value=0, max_value=59, value=0,format="%d")
    Dhour = st.number_input("Dropoff Hour: ", min_value=0, max_value=23, value=0,format="%d")
    Dmin = st.number_input("Dropoff Minute: ", min_value=0, max_value=59, value=0,format="%d")
    Solar = st.number_input("Solar: ")
    GroundTemp = st.number_input("Temp: ")

    submit_val = st.form_submit_button("Predict Duration")

if submit_val:
    # If submit is pressed == True
    attribute = np.array([Distance, Haversine, Phour,
                        Pmin, Dhour,
                        Dmin,Solar, GroundTemp]).reshape(1,-1)


    if attribute.shape == (1,8):
        print("attrubutes valid")
        

        value = predict_duration(attributes= attribute)


        st.header("Here are the results:")
        st.success(f"The Duration predicted is {value} mins")