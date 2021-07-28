import streamlit as st 
import pandas as pd 
import numpy as np
# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 
from bokeh.plotting import figure
import altair as alt

from numpy import asarray
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from matplotlib import pyplot
import seaborn as sns


@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df




def run_prediction():
	#st.subheader("Predicted Data")
	df = load_data("X_test_y_pred.csv")
	#st.dataframe(df)
	
	
	with st.beta_expander("Upload Data"):
	    data_file = st.file_uploader("Upload CSV",type=['csv'])
	    if st.button("Process"):
	        if data_file is not None:
	            file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
	            st.write(file_details)
	            df = pd.read_csv(data_file)
	            st.dataframe(df.head())

	            

	
	with st.beta_expander("Descriptive Summary"):
		st.dataframe(df.describe())


    
	with st.beta_expander("Pie Chart(New_Item_Type)"):
		st.title("Impact of Item_Type on Sale")
		st.text("0= Food")
		st.text("1= Non-Consumable")
		st.text("2= Drinks")
		fig = px.pie(df, values=df['Item_Outlet_Sales'], names=df['New_Item_Type'])
		st.plotly_chart(fig)


	with st.beta_expander("Pie Chart(Item_Outlet_Type)"):
		st.title("Impact of Outlet_Type on Sale")
		st.text("0= Supermarket Type 1")
		st.text("1= Supermarket Type 3")
		st.text("2= Grocery Store")
		st.text("3= Supermarket Type 2")
		fig = px.pie(df, values=df['Item_Outlet_Sales'],names=df['Outlet_Type'])
		st.plotly_chart(fig)


	
		

	with st.beta_expander("Chart (Outlet_Type,Item_Outlet_Sales)"):
		chart_data = pd.DataFrame(np.random.randn(20, 2),columns=['Outlet_Type', 'Item_Outlet_Sales'])
		st.line_chart(chart_data)


	with st.beta_expander("Chart (Item_Outlet_Sales, Item_MRP, Item visibility)"):
		chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['Item_MRP', 'Item_Outlet_Sales','item_visib_avg'])
		st.line_chart(chart_data)

	

	


