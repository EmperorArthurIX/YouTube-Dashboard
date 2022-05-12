import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime


# LOAD DATA
@st.cache
def load_data():
    df_agg = pd.read_csv('./data/Aggregated_Metrics_By_Video.csv').iloc[1:, :]          # First row not needed
    df_agg_sub = pd.read_csv('./data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
    df_comments = pd.read_csv('./data/All_Comments_Final.csv')
    df_time = pd.read_csv('./data/Video_Performance_Over_Time.csv')

    return df_agg, df_agg_sub, df_comments, df_time


df_agg, df_agg_sub, df_comments, df_time = load_data()

bar = st.sidebar.selectbox('Analysis Type', ('Aggregate Metrics', 'Individual Video Analysis'))