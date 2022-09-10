import streamlit as st
import pandas as pd
import numpy as np
from numpy.core.records import array
from pickle import load

import os
import sys


def app():

    # Load Saved Results Data
    model = load(filename='models/10-09-2022-01-13-01-52.92%.pkl')

    st.title("Model Predicition")

    st.header("To predict sales, enter values below.")

    Store = st.number_input('Store_id', key='a')
    Date = st.number_input('Date', key='b')
    IsPromo = st.number_input('Is promoted, please use 1 or 0', key='c')

    if st.button('sales prediction'):
        array = [Store, Date, IsPromo]
        val = model.predict([array])
        sales = [i[0] for i in val][0]
        st.write(
            "The estimated sales is: {:.3f}".format(sales))
