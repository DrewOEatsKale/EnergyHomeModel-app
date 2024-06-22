import streamlit as st 
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

from datetime import date, timedelta

from sklearn.model_selection import train_test_split, RepeatedKFold, cross_val_score, validation_curve
from sklearn.linear_model import *
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline, make_pipeline

st.markdown("# Home Energy Model")

st.write("Welcome! This model will predict my whole home energy use based on a few HVAC input parameters.")
st.write("The following is hourly home energy usage as well as the HVAC operation data associated with it. Please see the README for more information.")

df = pd.read_csv('combined_data.csv')
df["dateOnly"] = pd.to_datetime(df["dateOnly"],
               format='%Y-%m-%d')
# need to make the date and hour as the index datetime
fullTime = []
for i in range(len(df)):
    fullTime.append(df["dateOnly"].loc[i].replace(hour=df["hourIndex"].loc[i]))

df["fullTime"] = fullTime
# from lab notebook
df.set_index('fullTime', inplace=True)
df.sort_index(inplace=True)

# --- SIMPLE MODEL ---
simpleDataset = ["usage", "oat", "thermT"]
runningparams = ["coolStage1", "heatStage1", "auxStage1"]
#smalldf = df[smallDataset].dropna() #Do not do this yet.

simpledf = df[simpleDataset + runningparams]
#simpledf['runtime'] = df[runningparams].sum(axis=1)

pipe = make_pipeline(KNNImputer(n_neighbors=2, weights="uniform"), LinearRegression())

X = simpledf.drop(['usage'], axis=1)
y = simpledf.usage

pipe.fit(X, y)
# --- MODEL TRAINED ---

st.write(simpledf)
st.write("Edit the dataframe below to predict the energy usage."
         "oat and thermT are in degrees F."
         "coolStage1, heatStage1, and auxStage1 are all in seconds. Note that the seconds should not exceed 3600.")

d = {'oat': [55.0], 'thermT': [72.0], 'coolStage1': [0.0], 'heatStage1': [720.0], 'auxStage1': [0.0]}
indf = pd.DataFrame(data=d)

with st.form("my_form"):
    edited_df = st.data_editor(indf, num_rows="dynamic")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("Predicted Usage (kWh)")
    st.dataframe(pipe.predict(edited_df))