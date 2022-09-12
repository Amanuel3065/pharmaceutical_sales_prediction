from operator import mod
import sys
import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import pickle
from sklearn.preprocessing import StandardScaler


warnings.filterwarnings('ignore')

cwd = os.getcwd()
sys.path.append(f'{cwd}/scripts/')

from data_preProcessing import dataProcessor
from data_cleaning import dataCleaner
from ltsm_helper import ltsm_time

cwd = os.getcwd()
sys.path.append(f'{cwd}/scripts/')

preprocess = dataProcessor()
cleaner= dataCleaner()

cols = ['Store', 'Customers', 'Promo', 'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment','CompetitionDistance', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 'Promo2', 'Promos2SinceWeek', 'Promo2SinceYear','PromoInterval', 'Open','Date', 'DayOfWeek'  ]
    


def plot_predictions(date, sales):
    fig = plt.figure(figsize=(20, 7))
    ax = sns.lineplot(x=date, y=sales)
    ax.set_title("Predicted Sales", fontsize=24)
    ax.set_xlabel("Row index", fontsize=18)
    ax.set_ylabel("Sales", fontsize=18)
    
    # fig = plt.figure(figsize=(18, 5))
    

    return fig 




st.title("Rossmann Pharmaceuticals Sales Forecaster")

# @st.cache


input_data = pd.DataFrame(columns=cols)
submitted = False

df = None
file=True
data_added = False
uploaded_file = None
model = None


file=False
values = []

with st.form(key='inference', clear_on_submit=True):
        
    for feature in cols:
            
        values.append(st.text_input(feature,key=feature))

        submitted = st.form_submit_button("Show Prediction")
    

@st.cache
def load_model():
    model = pd.read_pickle(r'../../models/10-09-2022-01-13-01-52.92%.pkl')
    return model


if data_added:

    # model = load_model()
    model = pickle.load(open(f'{cwd}/models/10-09-2022-01-13-01-52.92%.pkl', 'rb'))
        
    prediction = model.predict(df)
    df["Date"]=pd.DatetimeIndex(df["Day"].astype(str)+'-' + df["Month"].astype(str)+'-' + df["Year"].astype(str))
        

   

    fig = plot_predictions(df['Date'], prediction)
    download=pd.DataFrame(index=df['Date'],columns=["Sales Prediction"],data=prediction).to_csv()
    st.pyplot(fig)

    st.download_button("Download CSV",data=download,file_name="Prediction.csv")