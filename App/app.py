# importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec
import streamlit as st
import pickle as pkl


# loading and reading the file
# Opening the file
model = pkl.load(open('Model/sentinelAI.pkl', 'rb'))

# Welcome Page and Page Configuration
st.set_page_config(
    page_title="SentinelAI",
    initial_sidebar_state="expanded",
)

st.title("SentinelAI - Credit Card Fraud Detector")
