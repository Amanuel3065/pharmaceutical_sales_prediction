
from numpy.core.records import array
import streamlit as st
import numpy as np
import sys
import pickle
from sklearn import *

def app():

    # Load Saved Results Data
    model = pickle.load(open('models/10-09-2022-01-13-01-52.92%.pkl', 'rb'))

    st.title("Prediction")

    st.header("To calculate a sales prediction, enter values below.")

    Open = st.number_input('Is open?', key='a')
    Promo = st.number_input('Promoted?', key='b')
    #total_data = st.number_input('Enter total data', key='c')
    #total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    #average_delay = st.number_input('Enter average delay', key='e')
    #total_throughput = st.number_input('Enter average throughput', key='f')

    if st.button('Sales prediction'):
        array = [Open, Promo]
        """, total_data,
                 total_retransmission, average_delay, total_throughput]"""
        val = model.predict([array])
        sales = [i[0] for i in val][0]
        st.write(
            "The predicted sales is: {:.3f}".format(sales))



